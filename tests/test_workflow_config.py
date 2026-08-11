import unittest
from pathlib import Path


class TestProductionWorkflow(unittest.TestCase):
    WORKFLOW = Path(__file__).parents[1] / ".github" / "workflows" / "production.yml"

    def test_default_branch_placeholder_is_replaced(self):
        """The $default-branch placeholder is invalid in a committed workflow."""
        content = self.WORKFLOW.read_text()
        self.assertNotIn("$default-branch", content,
                         "production.yml must use a real branch name, not the $default-branch placeholder")


