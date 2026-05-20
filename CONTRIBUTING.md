# Contributing

## Development setup

```bash
git clone https://github.com/okwn/PPT-Design-Prompt.git
cd PPT-Design-Prompt
python -m pip install -e .
```

## Running locally

```bash
# Put your local source DESIGN.md files under source/<brand>/DESIGN.md
# Then run the converter:
design-md-ppt convert
```

Review the generated files under `ppt-image/`.

## Running tests

```bash
# pytest
python -m pytest tests/ -v

# or unittest
python -m unittest discover -s tests -v
```

## Adding a test

1. Create a new test file under `tests/` or add a new test method to an existing test class.
2. Import the functions you need from `awesome_design_md_ppt_images.converter`:

```python
from awesome_design_md_ppt_images.converter import convert_all, generate_ppt_image_design
```

3. Use `REPO_ROOT = Path(__file__).resolve().parents[1]` to get the repo root for path references.
4. For tests that write files, use a temp directory under `.tmp-tests` (see `tests/test_converter.py` for the pattern).
5. Always clean up temp directories in a `finally` block:

```python
finally:
    shutil.rmtree(tmp_root, ignore_errors=True)
```

## Typical workflow

1. Create a branch for your change:
   ```bash
   git checkout -b contrib/your-feature-name
   ```
2. Make your changes and commit:
   ```bash
   git add .
   git commit -m "description of change"
   ```
3. Push to your fork:
   ```bash
   git push origin contrib/your-feature-name
   ```
4. Open a pull request targeting `okwn/PPT-Design-Prompt:main`.

## PR process

- Keep changes small and reviewable.
- Add or update tests when behavior changes.
- Prefer repository-authored fixtures and examples over redistributing third-party source files.
- Document new CLI flags and behavior in `README.md`.
- Ensure all tests pass before opening a PR.

## Please do

- keep changes small and reviewable
- add or update tests when behavior changes
- prefer repository-authored fixtures and examples over redistributing third-party
  source files
- document new CLI flags and behavior in `README.md`

## Please avoid

- committing `source/` unless you have verified redistribution rights
- adding machine-specific absolute paths to docs
- introducing unnecessary runtime dependencies

