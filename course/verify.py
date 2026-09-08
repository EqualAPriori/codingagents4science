"""Check the minimal course-authoring scaffold without external packages."""

from pathlib import Path
from typing import Optional


ROOT = Path(__file__).resolve().parent


def require(path: Path, text: Optional[str] = None) -> None:
    if not path.is_file():
        raise SystemExit(f"missing required file: {path.relative_to(ROOT)}")
    if text is not None and text not in path.read_text(encoding="utf-8"):
        raise SystemExit(f"missing {text!r} in {path.relative_to(ROOT)}")


def main() -> None:
    require(ROOT / "_quarto.yml", "type: website")
    require(ROOT / "index.qmd", "title: \"Quarto + uv smoke test\"")
    require(ROOT / "pyproject.toml", 'name = "codingagents4science-course"')
    require(ROOT / "pyproject.toml", 'requires-python = ">=3.9"')
    require(ROOT / "uv.lock", 'name = "codingagents4science-course"')
    print("course scaffold OK")


if __name__ == "__main__":
    main()
