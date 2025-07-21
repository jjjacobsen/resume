# Resume Repository

This repository contains my resume in Markdown format (`resume.md`). The primary purpose is to maintain the resume in an editable text format and generate a PDF version using Pandoc.

## Requirements

- [Pandoc](https://pandoc.org/) must be installed on your system. You can download it from the official website or install via package managers like Homebrew on macOS. To generate PDFs, you will also need a TeX distribution like BasicTeX installed.

```bash
brew install pandoc
brew install --cask basictex
```

## Generating the PDF

To convert the `resume.md` file to a PDF, open your terminal, navigate to the repository directory, and run the following command:

```bash
pandoc resume.md -o resume.pdf
```

This will create a `resume.pdf` file in the same directory.

### Customization

- For adding styles, you can use a CSS file with the `--css` option or templates. Refer to [Pandoc's documentation](https://pandoc.org/MANUAL.html#creating-a-pdf) for more advanced usage.
- If you want to include metadata or use a specific template, modify the command accordingly, e.g., `pandoc resume.md --template=template.tex -o resume.pdf`.

Feel free to edit `resume.md` to update the resume content and regenerate the PDF as needed.
