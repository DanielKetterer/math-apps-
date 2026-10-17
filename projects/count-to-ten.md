# Project specification: Count to Ten

> Status: review. Built at a parent's request for one child; see the registry entry `count-to-ten`.

## 1. Summary
A tap-to-count toy for a toddler. Each tap shows the next number from one to ten as a numeral, a word, one more counter in a ten-frame, and a color, while the number word is said aloud. Ten ends in a celebration, and the next tap starts over at one. The point is to give the count sequence a physical rhythm the child controls, with an adult counting alongside.

## 2. Learner and context
- **Intended audience:** one toddler, 17 months at build time (October 2026). Usable by any child who is starting to hear number words.
- **Prior knowledge assumed:** none. She can tap a screen and attend to sound and color.
- **Likely learning context:** short co-play sessions with a parent, who counts aloud with the app.
- **Accessibility and device considerations:** whole screen is one target, so motor precision does not matter. Works on a phone held either way, a tablet, or a computer. Keyboard operable. Respects reduced motion. Color is never the only signal: the numeral, word, counters, and voice carry the number.

## 3. Mathematical target
- **math-dag node IDs:** `counting.sequence.recite` (primary), `counting.successor`, `numeral.match-quantity`.
- **Prerequisite links that matter:** none are assumed. `counting.sequence.recite` is a root node in the map.
- **Uncertain or disputed links requiring review:** none introduced. The app does not rely on `cardinality.small-number-words` or `subitizing.*`, and should not be read as evidence about them.
- **Learning objectives (observable, age-appropriate):**
  - Joins the count: babbles, repeats, or attempts a number word with the adult or the app.
  - Anticipates ten: watches the ten-frame fill and looks for the celebration before the tenth tap.

Neither objective is mastery of any node above. At this age they are precursors: familiarity with the sound and order of the words, paired with quantity and numeral.

## 4. Why an app?
The child's own tap is the pacing. Each action produces exactly one more counter and exactly the next word, at the same moment, through sight, sound, and touch. A picture book shows the pairing but cannot let a one-year-old drive it one step at a time or make the end of the sequence an event.

## 5. Learning experience
- **Start:** an empty ten-frame and a pulsing pointing hand.
- **Each tap:** the numeral pops in, in that number's color; the word appears under it; one counter drops into the next box; the number word is spoken; a chime plays a note that climbs a scale; supported phones buzz once per unit (three buzzes for three).
- **Ten:** the word "ten", then a short fanfare, confetti, the ten counters hop in order, and ten balloons numbered one to ten rise in order. Tapping a balloon pops it.
- **After ten:** the full frame stays until the next tap, which clears it and shows one.
- **Mashing:** taps closer than about 0.4 seconds ripple but do not advance, so words are not cut off.
- **Voice:** the browser voice by default. A parent can drop in recordings (ten files or one counting take) with no code change.

## 6. Misconceptions and feedback
| Misconception or error | How the app will detect or expose it | Feedback / next step |
|---|---|---|
| (Expected at this age, not an error) Number words heard as a single rote string, "onetwothree" | Not detected; the app separates the words with a tap and a visual change for each | The adult's live counting is the feedback; the app only paces and pairs |
| (Hypothesis) Reading the app as teaching how many | Not applicable to the learner; a risk for the adult's interpretation | The README and this spec state the limit explicitly |

## 7. Assessment
- **Initial diagnostic:** none. Note whether she says or attempts any number word before first use.
- **In-app checks:** none. A toddler app with a test would be the wrong design.
- **Observation during co-play:** does she attempt a number word; does she anticipate ten.
- **Transfer question:** later, does she say "one, two..." while climbing stairs or handling objects, away from the screen.
- **Success criteria:** any attempt at a number word in the counting context, or clear anticipation of the celebration.
- **What this assessment cannot establish:** that the app caused any of it. A parent who counts with her is the more likely cause, and that is the intended use.

## 8. Scope
### Included
- Counting one to ten by tapping, with numeral, word, ten-frame counters, color, voice, chime, and vibration.
- A celebration at ten and a restart at one.
- Optional parent recordings.

### Explicitly excluded
- Counting backward, beyond ten, or skipping.
- Questions, scores, levels, streaks, or any assessment inside the app.
- Accounts, data collection, or analytics.
- Autoplay of any kind: nothing happens without a tap.

## 9. Acceptance tests
- [x] Mathematical sequence is correct: one to ten, one counter per tap, restart at one after ten.
- [x] Interaction states have defined feedback: idle, counting, mash, celebration, after celebration.
- [ ] Assessment tests the stated objective: by observation only, as described above.
- [x] Works at narrow and wide viewport sizes, including a phone held sideways.
- [x] Usable with keyboard; focus is visible; a status region announces each number.
- [x] No console errors other than the expected 404s for optional recordings.
- [x] Can be deployed at a GitHub Pages subpath (all paths are relative).
- [ ] Checked on Alexandra's actual device with real speech voices and real recordings.

## 10. Prioritization
Built at the parent's request for one child, so it was not ranked against the portfolio rubric. Main uncertainty: whether a toddler gains anything beyond what an adult counting with her would give without the screen.

## 11. Implementation and publication
- **ID:** `count-to-ten`
- **App entry point:** `apps/count-to-ten/index.html`
- **Dependencies / build step:** none.
- **Reviewers / review status:** Daniel Ketterer; awaiting a hands-on check.
- **Target publication URL:** `https://danielketterer.github.io/math-apps-/apps/count-to-ten/` once GitHub Pages is on for this repository.

## Sources and notes
- Children usually learn the exact meaning of "one" around two and a half, and the cardinal principle (the last word tells how many) around three and a half to four. Wynn, K. (1990), Children's understanding of counting, *Cognition* 36; Sarnecka, B. W. and Carey, S. (2008), How counting represents number, *Cognition* 108.
- American Academy of Pediatrics guidance recommends minimizing screen media before 18 months, with an adult using media together with the child from 18 to 24 months. The design follows from that: short, tap-driven, no autoplay, made for co-play.
