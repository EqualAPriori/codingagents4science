# Course authoring scaffold

This directory is a small Quarto website project. Python metadata and the
locked environment live beside the Quarto source so a lesson can later add
checkable or executable support without changing the repository layout.

Run the local smoke check from the repository root:

```bash
uv run --directory course python verify.py
```

If Quarto is installed, render the project with:

```bash
quarto render course
```

`uv` can manage the Python environment, but the Quarto CLI is an external
prerequisite and is not installed by this repository. Install Quarto using the
[official instructions](https://quarto.org/docs/get-started/) for your
operating system before running the render command.

## Publishing

The workflow at `.github/workflows/publish-course.yml` renders this project and
publishes `course/_site` to GitHub Pages when changes land on `main`. It also
checks the uv lockfile and smoke test before rendering. In the repository's
Pages settings, select **GitHub Actions** as the build and deployment source.
