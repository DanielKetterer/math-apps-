# Math Apps

A portfolio of small, standalone educational mathematics webapps, informed by the [math-dag knowledge map](https://github.com/DanielKetterer/math-dag).

**Current state:** repository structure and project workflow are being established. No learning apps have been built or published yet.

## Purpose

Use the mathematics knowledge graph to identify worthwhile learning opportunities, specify what an app should help a learner understand, build a focused interactive experience, and test it before publishing.

The intended products are small webapps that can be opened directly in a browser. Each app should have a clear learning objective and should remain usable without the rest of this repository running as an application.

## How the pieces fit together

1. **Discover.** Use `math-dag` to investigate concepts, prerequisite relationships, representations, curricula, and known misconceptions.
2. **Specify.** Write a project proposal with an audience, learning objectives, reason for interactivity, and assessment plan.
3. **Prioritize.** Compare educational value, evidence of learner need, interactive potential, reach, and feasibility.
4. **Build.** Once a project is approved, implement it as a standalone app under `apps/<project-id>/`.
5. **Review and publish.** Check mathematical correctness, instructional alignment, accessibility, and usability before making the app public.

The graph is a map and source of hypotheses, not proof that a teaching approach works. Proposed or disputed prerequisite links should be reviewed before an app relies on them.

## Repository structure

```text
.
├── index.html                       # Future public catalogue; currently an empty-state page
├── apps/
│   └── README.md                    # Rules for standalone app directories
├── projects/
│   ├── README.md                    # Project proposal and registry workflow
│   └── registry.yaml                # Machine-readable project catalogue; initially empty
├── schemas/
│   └── project-registry.schema.json # Shape of the project registry
├── templates/
│   └── project-spec.md              # Template for designing a proposed app
├── docs/
│   ├── lifecycle.md                 # From discovery to publication
│   └── selection.md                 # Project-ranking rubric
├── tools/
│   └── validate_registry.py         # Local validation for project metadata
├── .github/workflows/
│   └── validate-registry.yml        # Validate metadata on pushes and pull requests
├── requirements.txt
└── CONTRIBUTING.md
```

## Where to start

- Read [the lifecycle](docs/lifecycle.md) to understand the intended workflow.
- Use the [project-selection rubric](docs/selection.md) when comparing ideas.
- Draft a proposal from [the project specification template](templates/project-spec.md).
- Add accepted project metadata to [the registry](projects/registry.yaml).
- Read [the app conventions](apps/README.md) before building an app.

## Validate the registry locally

Requires Python 3.10 or newer.

```sh
python -m pip install -r requirements.txt
python tools/validate_registry.py
```

The validator checks the registry against its JSON Schema, catches duplicate project IDs, and verifies local app entry points when they are declared. It does not check whether referenced mathematics nodes exist in `math-dag`; that remains a separate review or future integration.

## Standalone app conventions

- Use `apps/<project-id>/index.html` as the app entry point.
- Prefer plain HTML, CSS, and JavaScript unless a project has a concrete reason to use a build tool.
- Keep each app independently deployable at a GitHub Pages subpath.
- Do not require a backend, account, or collection of personal data for a basic learning interaction.
- Avoid making one app depend on another app's internal files.
- Include a meaningful learning objective, feedback for learner actions, and a way to check understanding.
- Treat responsive layout, keyboard access, clear language, and reduced-motion preferences as part of the design—not optional polish.

## Publishing

When ready, configure GitHub Pages to deploy from the `main` branch and repository root. The catalogue can then live at the repository's Pages root, with apps under `/apps/<project-id>/`. The catalogue should list apps that have passed review and have a published URL, not merely every idea in the project registry.

See [AlexandraCode](https://github.com/DanielKetterer/AlexandraCode) for the established pattern of publishing small HTML experiences through GitHub Pages.
