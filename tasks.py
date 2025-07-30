"""
Invoke tasks for resume management.

This module provides tasks for building and deploying resume PDFs.
"""

from pathlib import Path

from invoke import task


@task
def build(c):
    """Build the resume PDF from Markdown using Pandoc."""
    print("Building resume.pdf from resume.md...")
    c.run("pandoc resume.md -o resume.pdf")
    print("✅ Resume PDF built successfully!")


@task
def deploy(c):
    """Copy resume.pdf to iCloud and website locations."""
    source = Path("resume.pdf")

    if not source.exists():
        print("❌ resume.pdf not found! Run 'invoke build' first.")
        return

    # Define destination paths
    icloud_path = (
        Path.home()
        / "Library/Mobile Documents/com~apple~CloudDocs/job/resume/"
        / "Jonah_Jacobsen_Resume.pdf"
    )
    website_path = Path.home() / "Projects/website/public/jonah_jacobsen_resume.pdf"

    destinations = [("iCloud", icloud_path), ("website", website_path)]

    for name, dest_path in destinations:
        try:
            # Create parent directory if it doesn't exist
            dest_path.parent.mkdir(parents=True, exist_ok=True)

            # Copy the file
            c.run(f"cp '{source}' '{dest_path}'")
            print(f"✅ Copied resume to {name}: {dest_path}")

        except Exception as e:
            print(f"❌ Failed to copy to {name}: {e}")


@task
def all(c):
    """Build and deploy the resume in one command."""
    build(c)
    deploy(c)
