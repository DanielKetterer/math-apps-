"""Regression tests for the project registry validator.

All test registries and fake app entry points are created in temporary folders;
tests never add projects or app files to the actual repository.
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[1]
VALIDATOR = REPO / "tools" / "validate_registry.py"
SCHEMA = REPO / "schemas" / "project-registry.schema.json"


class RegistryValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "tools").mkdir()
        (self.root / "schemas").mkdir()
        (self.root / "projects").mkdir()
        shutil.copy2(VALIDATOR, self.root / "tools" / "validate_registry.py")
        shutil.copy2(SCHEMA, self.root / "schemas" / "project-registry.schema.json")
        self.registry_path = self.root / "projects" / "registry.yaml"

    def tearDown(self) -> None:
        self.temp.cleanup()

    def project(self, **changes: object) -> dict:
        data = {
            "id": "slope-lab",
            "title": "Slope Lab",
            "status": "proposed",
            "summary": "A focused learning experience about slope.",
            "target_nodes": ["slope.between-two-points"],
            "audience": "Middle school learners",
            "learning_objectives": ["Explain why the slope is constant along a line"],
            "interaction_rationale": "Dragging points makes the invariant visible.",
            "assessment": ["Predict the slope after moving a point along the line."],
            "evidence": ["Test fixture only; not a claim about learner outcomes."],
            "scope": {
                "included": ["Compare rise and run"],
                "excluded": ["Accounts and data collection"],
            },
        }
        data.update(changes)
        return data

    def run_validator(self, registry: dict) -> subprocess.CompletedProcess:
        self.registry_path.write_text(
            yaml.safe_dump(registry, sort_keys=False), encoding="utf-8"
        )
        return subprocess.run(
            [sys.executable, str(self.root / "tools" / "validate_registry.py")],
            cwd=self.root,
            capture_output=True,
            text=True,
            check=False,
        )

    def test_empty_registry_is_valid(self) -> None:
        result = self.run_validator({"version": 1, "projects": []})
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Registry valid: 0 project(s).", result.stdout)

    def test_valid_proposal_is_accepted(self) -> None:
        result = self.run_validator({"version": 1, "projects": [self.project()]})
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_bad_project_id_is_rejected(self) -> None:
        result = self.run_validator({
            "version": 1, "projects": [self.project(id="Slope Lab!")]
        })
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("does not match", result.stderr)

    def test_missing_required_assessment_is_rejected(self) -> None:
        project = self.project()
        del project["assessment"]
        result = self.run_validator({"version": 1, "projects": [project]})
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("'assessment' is a required property", result.stderr)

    def test_duplicate_project_ids_are_rejected(self) -> None:
        result = self.run_validator({
            "version": 1,
            "projects": [self.project(), self.project(title="Second title")],
        })
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Duplicate project id: slope-lab", result.stderr)

    def test_nonexistent_app_entry_point_is_rejected(self) -> None:
        result = self.run_validator({
            "version": 1,
            "projects": [self.project(app_path="apps/missing/index.html")],
        })
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("app_path does not exist", result.stderr)

    def test_path_traversal_is_rejected(self) -> None:
        result = self.run_validator({
            "version": 1,
            "projects": [self.project(app_path="../../outside.html")],
        })
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("app_path must remain inside the repository", result.stderr)

    def test_published_project_needs_path_and_url(self) -> None:
        result = self.run_validator({
            "version": 1,
            "projects": [self.project(status="published")],
        })
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("published projects need app_path and app_url", result.stderr)

    def test_malformed_published_url_is_rejected(self) -> None:
        result = self.run_validator({
            "version": 1,
            "projects": [self.project(
                status="published",
                app_path="apps/slope-lab/index.html",
                app_url="not a url",
            )],
        })
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("is not a 'uri'", result.stderr)

    def test_published_project_with_existing_entry_and_url_is_valid(self) -> None:
        app = self.root / "apps" / "slope-lab" / "index.html"
        app.parent.mkdir(parents=True)
        app.write_text("<!doctype html><title>Test fixture</title>", encoding="utf-8")
        result = self.run_validator({
            "version": 1,
            "projects": [self.project(
                status="published",
                app_path="apps/slope-lab/index.html",
                app_url="https://danielketterer.github.io/math-apps-/apps/slope-lab/",
            )],
        })
        self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == "__main__":
    unittest.main()
