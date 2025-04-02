#!/usr/bin/env python3
import shutil
import subprocess
from pathlib import Path


def run_tests_for_notebook(notebook_path: str) -> bool:
    """Run tests for a specific notebook and return whether they passed."""
    try:
        # Run pytest for specific tests matching the notebook name
        # e.g., for fibonacci.py it will run test_fibonacci.py
        notebook_name = Path(notebook_path).stem
        result = subprocess.run(
            ["pytest", f"tests/test_{notebook_name}.py", "-v"],
            capture_output=True,
            text=True,
        )
        return result.returncode == 0
    except Exception as e:
        print(f"Error running tests for {notebook_path}: {e}")
        return False


def migrate_notebooks():
    """Migrate notebooks that pass their tests from notebooks/ to apps/."""
    notebooks_dir = Path("notebooks")
    apps_dir = Path("apps")

    # Ensure apps directory exists
    apps_dir.mkdir(exist_ok=True)

    # Get all .py files in notebooks directory
    notebook_files = list(notebooks_dir.glob("*.py"))

    if not notebook_files:
        print("No notebooks found to migrate.")
        return

    for notebook_path in notebook_files:
        print(f"\nProcessing {notebook_path}...")

        # Skip __init__.py and other special files
        if notebook_path.name.startswith("__"):
            continue

        # Run tests for the notebook
        if run_tests_for_notebook(str(notebook_path)):
            print(f"✅ Tests passed for {notebook_path}")

            # Move the notebook to apps directory
            target_path = apps_dir / notebook_path.name
            try:
                shutil.move(str(notebook_path), str(target_path))
                print(f"✨ Successfully moved {notebook_path.name} to apps/")

                # If there are associated assets in public/, move them too
                source_public = notebooks_dir / "public"
                if source_public.exists():
                    target_public = apps_dir / "public"
                    target_public.mkdir(exist_ok=True)

                    # Move any associated files that match the notebook name
                    for asset in source_public.glob(f"{notebook_path.stem}*"):
                        shutil.move(str(asset), str(target_public / asset.name))
                        print(f"📦 Moved associated asset: {asset.name}")

            except Exception as e:
                print(f"❌ Error moving {notebook_path}: {e}")
        else:
            print(f"❌ Tests failed for {notebook_path}")


if __name__ == "__main__":
    print("🚀 Starting notebook migration...")
    migrate_notebooks()
    print("\n✅ Migration complete!")
