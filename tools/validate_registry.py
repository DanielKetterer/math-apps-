#!/usr/bin/env python3
"""Validate project registry shape and internal consistency."""
from pathlib import Path
import sys

import json
import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "projects" / "registry.yaml"
SCHEMA = ROOT / "schemas" / "project-registry.schema.json"


def main() -> int:
    try:
        data = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError, yaml.YAMLError) as exc:
        print(f"Could not load registry or schema: {exc}", file=sys.stderr)
        return 2

    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(data), key=lambda e: list(map(str, e.absolute_path)))
    if errors:
        for error in errors:
            location = ".".join(map(str, error.absolute_path)) or "<root>"
            print(f"{location}: {error.message}", file=sys.stderr)
        return 1

    projects = data["projects"]
    seen = set()
    failed = False
    for project in projects:
        project_id = project["id"]
        if project_id in seen:
            print(f"Duplicate project id: {project_id}", file=sys.stderr)
            failed = True
        seen.add(project_id)

        app_path = project.get("app_path")
        if app_path:
            candidate = (ROOT / app_path).resolve()
            if ROOT.resolve() not in candidate.parents:
                print(f"{project_id}: app_path must remain inside the repository", file=sys.stderr)
                failed = True
            elif not candidate.is_file():
                print(f"{project_id}: app_path does not exist: {app_path}", file=sys.stderr)
                failed = True

        if project["status"] == "published":
            if not project.get("app_path") or not project.get("app_url"):
                print(f"{project_id}: published projects need app_path and app_url", file=sys.stderr)
                failed = True

    if failed:
        return 1
    print(f"Registry valid: {len(projects)} project(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
