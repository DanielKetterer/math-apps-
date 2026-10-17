# Recordings for Count to Ten

Leave this folder empty and the app uses the browser's built-in voice. Add your own voice in either of two ways.

## Option A: one take (easiest)

Record yourself counting from one to ten in a single take, with about a second of quiet between numbers, and save it here as:

```
count.m4a      (or count.mp3)
```

The app finds the ten words by the quiet between them. If it cannot find exactly ten, it uses the built-in voice instead and leaves a note in the browser console. The usual causes are talking before or after the count, or numbers run together with no pause.

## Option B: ten files

One file per number, named by the digit:

```
1.m4a  2.m4a  3.m4a  4.m4a  5.m4a  6.m4a  7.m4a  8.m4a  9.m4a  10.m4a
```

`.mp3` works too, and the two can be mixed. File `1` must exist for the app to look for the rest. Any number that is missing falls back to the built-in voice. If both options are present, the ten files win.

## Recording tips

- A quiet room, phone about a foot from your mouth.
- Say each number the way you would say it to her: slow, warm, a little sing-song. Make "ten" the excited one.
- Loudness does not need to match between numbers; the app evens it out.
- iPhone Voice Memos: Share, then Save to Files, gives an `.m4a`. Rename it to `count.m4a` (or `1.m4a` and so on).

## Adding the files on GitHub

Open this folder on github.com, choose **Add file**, then **Upload files**, drop the recordings in, and commit. GitHub Pages picks them up within a minute or two; reload the app.
