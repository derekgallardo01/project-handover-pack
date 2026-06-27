import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)

import validate  # noqa: E402


def _abs(rel):
    return os.path.join(ROOT, rel)


def test_examples_have_no_unfilled_placeholders():
    for name in ("examples/handover-greenfield-logistics.md",
                 "examples/runbook-greenfield-logistics.md",
                 "examples/loom-script-greenfield-logistics.md"):
        issues = validate.lint(_abs(name))
        assert issues == [], f"{name} still has placeholders: {issues[:3]}"


def test_bare_templates_still_look_like_templates():
    for name in ("handover-guide-template.md", "runbook-template.md", "loom-script.md"):
        issues = validate.lint(_abs(name))
        assert len(issues) >= 3, f"{name} has too few placeholders to look like a template"
