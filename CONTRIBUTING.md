# Contributing

The goal is a set of small, reliable learning tools—not a high count of generated pages.

## Before proposing an app
- Review the relevant nodes and prerequisite edges in [math-dag](https://github.com/DanielKetterer/math-dag).
- Fill out the project-spec template.
- State what is known versus hypothesized about learner difficulty.
- Explain why interaction is useful and how learning will be checked.
- Keep scope narrow enough to review properly.

## Before adding an app
- Ensure its project is approved and recorded in the registry.
- Add it under `apps/<project-id>/`.
- Include a short app-specific README and manual test notes.
- Test mathematics, edge cases, keyboard use, responsive layout, and relative paths.
- Request mathematical and instructional review; generated code is not its own verification.

## Changes to the registry
Run `python tools/validate_registry.py` and ensure the workflow passes. Use unique lowercase kebab-case IDs. Do not set a project to `published` until its review is complete and the URL is live.

## Keep the portfolio understandable
Prefer focused apps over broad platforms. Do not add shared infrastructure until actual projects establish the need for it.
