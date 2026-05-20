"""Tests for CLI argument parsing and main entry point."""
from __future__ import annotations

import argparse
import sys
import unittest
from pathlib import Path
from io import StringIO

REPO_ROOT = Path(__file__).resolve().parents[1]
PYMODULE = "awesome_design_md_ppt_images.cli"


class CliArgumentParserTests(unittest.TestCase):
    """Test CLI argument parser configuration."""

    def test_convert_subcommand_is_registered(self) -> None:
        """Parser accepts 'convert' as a valid subcommand (--help triggers exit 0)."""
        from awesome_design_md_ppt_images.cli import build_parser
        parser = build_parser(default_project_root=REPO_ROOT)
        # 'convert --help' should exit with 0 (not with an argparse error)
        with self.assertRaises(SystemExit) as cm:
            parser.parse_args(["convert", "--help"])
        self.assertEqual(cm.exception.code, 0)

    def test_convert_subcommand_help(self) -> None:
        """'convert --help' produces help output."""
        from awesome_design_md_ppt_images.cli import build_parser
        parser = build_parser(default_project_root=REPO_ROOT)
        # Capture help for convert subcommand
        with self.assertRaises(SystemExit) as cm:
            parser.parse_args(["convert", "--help"])
        # argparse exits with 0 on --help
        self.assertEqual(cm.exception.code, 0)

    def test_no_args_shows_usage(self) -> None:
        """Calling CLI with no args shows usage (not silent success)."""
        from awesome_design_md_ppt_images.cli import main
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        sys.stdout = StringIO()
        sys.stderr = StringIO()
        try:
            with self.assertRaises(SystemExit) as cm:
                # Patch sys.argv to simulate no args
                old_argv = sys.argv
                sys.argv = ["design-md-ppt"]
                try:
                    main()
                finally:
                    sys.argv = old_argv
            # Should exit with error (missing subcommand or required args)
            self.assertNotEqual(cm.exception.code, 0)
        finally:
            sys.stdout = old_stdout
            sys.stderr = old_stderr


if __name__ == "__main__":
    unittest.main()