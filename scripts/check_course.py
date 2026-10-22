#!/usr/bin/env python3
"""Read-only checks for slide identity, notes coverage, links and course inventory.
Run from any directory with Python 3. No third-party dependencies required.
Editorial meaning and timing still require review alongside the matching notes.
"""
from pathlib import Path
from html.parser import HTMLParser
import json,re,zipfile,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parent.parent
NS={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
class Course(HTMLParser):
    def __init__(self):super().__init__();self.sid=None;self.slides=[];self.images=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='section' and a.get('class')=='session':self.sid=a['id'];self.number=0
        if tag=='div' and 'slide' in a.get('class','').split():
            self.number+=1
            self.slides.append({'session':self.sid,'slide':self.number,'id':a.get('id'),'title':a.get('data-title'),'notes':f'notes/session-{self.sid[1:]}-notes.docx'})
        if tag=='img':self.images.append(a)
    def handle_endtag(self,tag):
        if tag=='section':self.sid=None
course=Course();course.feed((ROOT/'index.html').read_text())
assert len(course.slides)==137,'Unexpected slide count: review notes and timeline before changing the baseline.'
assert len({x['id'] for x in course.slides})==137,'Missing or duplicate stable slide ID.'
assert course.slides==json.loads((ROOT/'slide-map.json').read_text()),'Slide order/title differs from slide-map.json. Review matching notes and update the map together.'
for img in course.images:
    assert img.get('src','').startswith('images/'),img
    assert (ROOT/img['src']).is_file(),img
    assert img.get('alt'),f'Missing image description: {img}'
for sid in sorted({x['session'] for x in course.slides}):
    rows=[x for x in course.slides if x['session']==sid]
    path=ROOT/rows[0]['notes']
    with zipfile.ZipFile(path) as z:root=ET.fromstring(z.read('word/document.xml'))
    seen=[]
    for p in root.findall('.//w:p',NS):
        text=''.join(t.text or '' for t in p.findall('.//w:t',NS))
        match=re.match(r'Slide (\d+)\b',text)
        if match:
            number=int(match[1]);assert 1<=number<=len(rows),(sid,number)
            expected=rows[number-1]['id'].replace('-','_')[:40]
            bookmarks=[b.get('{'+NS['w']+'}name') for b in p.findall('w:bookmarkStart',NS)]
            assert expected in bookmarks,f'{sid}, note {number}: stable slide bookmark does not match.'
            seen.append(number)
        if re.match(r'0:\d\d',text):
            for numbers in re.findall(r'slides? ([\d ,andthrough]+)',text,re.I):
                assert all(1<=int(n)<=len(rows) for n in re.findall(r'\d+',numbers)),(sid,text)
    # Title slides in sessions 2-11 use the welcome timeline instead of a separate talking point.
    expected=list(range(1 if sid=='s01' else 2,len(rows)+1))
    assert seen==expected,f'{sid}: note coverage/order mismatch: {seen}'
    print(f'{sid}: {len(rows)} slides, notes and permanent bookmarks aligned')
print('PASS: 137 slides, 11 notes documents, slide map and referenced slide images.')
