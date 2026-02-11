"""Tests for app logic."""

import unittest

from app import completion_message, normalize_text


class NormalizeTextTests(unittest.TestCase):
    def test_trims_and_collapses_spaces(self) -> None:
        self.assertEqual(normalize_text("   hello    world   "), "hello world")

    def test_empty_string(self) -> None:
        self.assertEqual(normalize_text("   \t \n "), "")


class CompletionMessageTests(unittest.TestCase):
    def test_with_project_name(self) -> None:
        self.assertEqual(completion_message("   My   Project  "), "Project 'My Project' is complete.")

    def test_without_project_name(self) -> None:
        self.assertEqual(completion_message(""), "Your project is complete.")


if __name__ == "__main__":
    unittest.main()
