# Project proposals and registry

The registry is the catalogue of candidate and active projects. It is not a list of every mathematical node and it is not the app gallery.

## Workflow

1. Copy `../templates/project-spec.md` and fill in the learning case before writing implementation code.
2. Check the target nodes and prerequisite rationale in [math-dag](https://github.com/DanielKetterer/math-dag). Mark uncertain edges for review; do not quietly treat proposed edges as established facts.
3. Score the idea using [the selection rubric](../docs/selection.md).
4. Review the scope, evidence, assessment, and acceptance tests with a human reviewer.
5. Once approved, add a corresponding record to `registry.yaml`.
6. Only create `apps/<id>/` when the project is approved for implementation.

## Status meanings

- `proposed`: an idea has been recorded, not endorsed.
- `researching`: learning need, mathematics, or prerequisite claims are being checked.
- `specified`: scope, interaction, and assessment are drafted.
- `approved`: accepted for implementation.
- `building`: implementation is in progress.
- `review`: awaiting mathematical, instructional, accessibility, or technical review.
- `published`: passed review and has a live URL.
- `paused`: intentionally on hold.
- `rejected`: reviewed and not selected; preserve the record to avoid repeating the same evaluation.

Keep `registry.yaml` valid against `schemas/project-registry.schema.json`. Keep the initial registry empty until there are actual proposals.
