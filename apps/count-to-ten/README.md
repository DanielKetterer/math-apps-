# Count to Ten
https://danielketterer.github.io/math-apps-/apps/count-to-ten/
A tap-to-count toy for a toddler. Tap anywhere and the next number appears, one to ten, each in its own color. At ten there is a celebration (fanfare, confetti, ten numbered balloons she can pop), and the next tap starts again at one.

Built for Alexandra, 17 months old in October 2026, to be played **with** a grown-up.

## What each number looks, sounds, and feels like

| Channel | What happens on every tap |
|---|---|
| See | The numeral, the number word, and one more counter in a ten-frame (two rows of five, top row first) |
| Hear | The number word said aloud, plus a soft chime that climbs a scale (one is the lowest note, ten the highest) |
| Touch | The tap itself; on phones that support vibration, three short buzzes for three |
| Order | Each tap adds exactly one counter, and the empty boxes show how far it is to ten |

## Controls

- Tap or click anywhere: count one more.
- Space, Enter, Right arrow, or Up arrow: the same, for keyboards.
- Taps less than about 0.4 seconds apart only make a ripple, so each word gets heard when she mashes.
- During the celebration, taps pop balloons or throw confetti and do not advance the count.

## Voice

With no recordings, the browser's built-in voice says the numbers (slowed down a little and pitched a little higher). To use your own voice, add recordings to `sounds/` in this folder. See [sounds/README.md](sounds/README.md). No code change is needed; the app finds them on load.

## Learning objective (honest version)

At this age the goal is exposure and routine, not mastery. The app pairs each spoken number word with its numeral and a set of that many counters, at the moment the child acts, and it gives the sequence a predictable end. Things worth watching for during co-play:

- She joins the count: babbles, repeats, or attempts a number word with you.
- She anticipates ten: watches the frame fill and looks for the balloons before the tenth tap.

It does not teach what a number means (that the last word tells how many). Children usually reach that years later. See the [project spec](../../projects/count-to-ten.md) for the reasoning and sources.

## Requirements and limits

- Plain HTML, CSS, and JavaScript in one file. No build step, no accounts, no data collected.
- The chime and fanfare use Web Audio. On iPhone the ring/silent switch mutes them; flip it to ring.
- Recordings only load when the page is served (GitHub Pages or a local server), not when `index.html` is opened from disk.
- Until recordings exist, the browser console shows a few 404s for the optional sound files. That is expected.
- Respects reduced-motion settings: no confetti, balloons, or bouncing; colors and sounds stay.

## Review status

`review` in the project registry: built and tested, awaiting a hands-on check on Alexandra's actual device and a decision on recordings.

## Test notes

Checked in headless Chromium at 390x844, 360x640, 844x390 (phone sideways), 820x1180, and 1440x900:

- One tap shows 1 with one counter; ten taps fill the frame and start the celebration; the next tap after the celebration shows 1 with one counter.
- Two taps in quick succession count once; Space advances.
- Tapping a balloon removes it; taps during the celebration never change the count.
- Numeral and ten-frame never overlap or leave the screen; no horizontal scroll.
- Reduced motion: the celebration runs without balloons or particles.
- No console errors other than the expected 404s for missing optional recordings.
- Recordings: ten separate files load and decode, including the fallback from `.mp3` to `.m4a` for a single number; a single counting take is split into ten words. (Test audio was MP3, because headless Chromium cannot decode AAC. Real `.m4a` decoding in Safari and Chrome is untested here.)
- The word splitter was also tested offline on synthesized counting at gaps from 0.25 to 1 second, uneven loudness, background noise, and breaths between words: it found exactly ten words every time, never cut into a neighboring word, and kept each word to within 35 ms of its quiet edges. It correctly refuses silence and a three-word take.

Not yet checked: Safari on iPhone and Chrome on Android with real speech voices, and real recordings of Daniel's voice.
