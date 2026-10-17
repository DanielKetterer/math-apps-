# Standalone apps

This directory is reserved for approved projects.

| App | Status |
|---|---|
| [count-to-ten](count-to-ten/) | approved |

## Directory convention

Each app should live at `apps/<project-id>/index.html`, where `<project-id>` matches a unique ID in `projects/registry.yaml`.

An app should be independently usable and deployable. Prefer plain HTML, CSS, and JavaScript unless a project has a specific, documented reason for a framework or build step. Shared assets may live inside that app; shared cross-app utilities belong in `shared/` only after multiple real apps demonstrate the need.

## Requirements

- One clear, observable learning objective.
- Interaction that serves the mathematics rather than decoration.
- Correct, transparent feedback for learner actions.
- A transfer or explanation task when appropriate—not only a score.
- Responsive layout, keyboard operation, visible focus, and readable contrast.
- Respect reduced-motion preferences; do not rely on color alone.
- No account or personal data collection for a basic interaction.
- No broken relative links when served from a GitHub Pages subpath.
- A short app README explaining objective, controls, prerequisites, limitations, and review status.

The public catalogue should list only published apps that have passed review. Ideas belong in the project registry, not as unfinished links on the public home page.
