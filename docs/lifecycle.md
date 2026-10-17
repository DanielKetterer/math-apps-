# Project lifecycle

## Discover
Use the knowledge graph to find plausible learning opportunities: high-leverage prerequisites, transitions between representations, recurrent misconceptions, and difficult explanations or justifications. Graph structure generates candidates; it does not by itself prove learner need.

## Verify
Check the mathematics and relevant prerequisite chains. Look for evidence of learner difficulty where possible. Record whether each claim is established, inferred from the graph, or a hypothesis.

## Specify
Write a project spec before coding. Define a target learner, observable objective, interaction rationale, assessment, scope exclusions, and acceptance tests.

## Prioritize
Use the rubric in [selection.md](selection.md). Scores are decision aids, not objective measurements; record the reasoning and uncertainties alongside them.

## Approve
A human review should confirm that the project is appropriately scoped, mathematically grounded, and worth building. Avoid generating apps from unreviewed graph nodes at scale.

## Build
Implement a focused standalone app. Keep the app independent of other apps and make the GitHub Pages subpath work. Add tests for calculations and important interaction states.

## Review
Review separately for:
- mathematical correctness and edge cases;
- whether the interaction teaches the stated objective;
- whether assessment actually measures that objective;
- clarity, accessibility, and responsive behavior;
- technical reliability and deployment.

## Publish and learn
Update the registry with status, app path, URL, and review date. The gallery lists only published apps. Where feasible, gather privacy-respecting evidence about usability and learning; a correct app is not automatically an effective intervention.

## Improve the graph
If building or reviewing an app reveals a missing concept, unclear node, or questionable prerequisite, propose a change to [math-dag](https://github.com/DanielKetterer/math-dag) separately. Do not silently rewrite the knowledge graph to fit one app.
