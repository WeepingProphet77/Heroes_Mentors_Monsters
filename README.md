# Heroes, Mentors, and Monsters

A church class for older teens and adults on the structure of reality, the stories that endure, and the Logos who stands behind both. Grounded in Scripture, with illustrations from enduring stories and literary insights from C.S. Lewis and J.R.R. Tolkien.

## What's here

- `GUIDANCE.md` governs all work on this project. Read it first.
- `index.html` is the entire course presentation. Open it in any browser; it works offline. Arrow keys or spacebar advance slides, Escape returns to the menu.
- `images/` holds all artwork. `images/MANIFEST.md` lists every needed image with art direction; Codex generates and verifies images against those exact filenames.
- `notes/` holds the teacher notes, one Word document per session.

## Project ownership

Jason Davis owns the project and retains final editorial and theological authority. As of 21 October 2026, **Codex (ChatGPT) is the sole active agent for all project work**, including course content, presentation code, teacher notes, imagery, documentation, verification, and GitHub maintenance. Claude is inactive unless Jason explicitly instructs otherwise. See `AGENTS.md` and `GUIDANCE.md` section 7.

Repository: [WeepingProphet77/Heroes_Mentors_Monsters](https://github.com/WeepingProphet77/Heroes_Mentors_Monsters).

## Status

**Complete.** All eleven sessions are built: 137 slides, 71 images, and eleven teacher notes documents. Every image in the manifest has been delivered and placed.

## The eleven sessions

1. The World Has a Shape (Genesis 1; John 1:1-5)
2. Why Stories Ring True (Ecclesiastes 3:11; Acts 17)
3. The Call of the Hero (Genesis 12; Exodus 3; 1 Samuel 16)
4. The Mentor (1 Samuel 3; 2 Timothy 1)
5. The Monster Outside (1 Samuel 17; Job 41)
6. The Monster Within (Genesis 4:7; Romans 7)
7. Into the Belly of the Beast (Jonah 1-2; Matthew 12:39-40)
8. The Life Laid Down (Isaiah 53; John 10:11-18; John 15:13)
9. The Least Likely One (1 Samuel 16:7; 1 Corinthians 1:26-29)
10. The Return of the King (Isaiah 9:6-7; Revelation 21)
11. Living Inside the Story (Hebrews 12:1-2; Ephesians 2:10)

## Teaching it

Open `index.html` and press a session tile. Arrow keys, spacebar, or click advance slides; Escape returns to the menu. The address bar tracks your position (for example `#s03/5`), so you can bookmark a slide or resume after a refresh. Hash indexes begin at zero; the example opens displayed slide 6. Each session's notes document includes preparation, a minute-by-minute timeline, talking points keyed to slide numbers, Scripture in full, two tiers of discussion questions, background reading, and pastoral notes.

## Presentation controls

The home screen includes **Resume teaching** (when this browser has a saved position) and a Word notes link for every session. Inside a session, select **Tools** (or press T) to reveal the teaching controls. They close when you change slides or tap the artwork. Use **Slides** to jump to any slide, **Notes** for its matching document, **Fullscreen**, or **Blank** to turn attention back to the room. The **?** button explains the controls.

- Right arrow, Space, or Page Down: next item or slide.
- Left arrow or Page Up: previous item or slide.
- S: slide overview. A: show all questions or recap sentences.
- F: fullscreen when the browser supports it. B: blank or restore the screen.
- Escape: close an open panel, restore a blank screen, or return to the menu.

Discussion questions and Session 11's ten-sentence recap appear one at a time within their original numbered slides. **Show all** displays the full set; **Show one** restores focused teaching. Small screens can scroll longer slides. Notes open in a separate tab or download according to the browser; keep private notes on a separate device or display.

The interface and Word notes use the same one-based slide numbers. Existing zero-based hash bookmarks remain compatible: `#s03/5` opens displayed slide 6. An optional third segment remembers the question or recap item. Resume is saved locally in this browser, not shared between devices, and may be unavailable where browser storage is restricted.

## Keeping slides and notes aligned

Each slide has a permanent HTML ID, recorded with its current number and title in `slide-map.json`. Its matching Word talking point contains a corresponding invisible bookmark. Preserve these IDs when changing a title or moving a slide.

Run `python3 scripts/check_course.py` before committing. It checks the 137-slide inventory, map, talking-point coverage, note bookmarks, timeline number ranges, and slide image paths. It cannot judge the meaning of a note or its timing: review those alongside any content change. Update the slide map, affected Word notes, and timelines in the same commit when changing the sequence. The October interface refresh retains the existing sequence and time budgets.
