# Resume Repository 📝

This repository contains my resume in Markdown format (`resume.md`). The primary purpose is to maintain the resume in an editable text format and generate a PDF version using Pandoc.

## Requirements ⚙️

To generate the PDF, [Pandoc](https://pandoc.org/) must be installed on your system. You can download it from the official website or install it via package managers like Homebrew on macOS. Additionally, to create PDFs, you'll need a TeX distribution such as BasicTeX.

```bash
brew install pandoc pipx
brew install --cask basictex

# Install invoke for task automation
pipx install invoke
```

## Development Setup 🚀

This project uses pre-commit hooks for code quality. To set up:

1. **Install Pre-commit** 🛠️
   ```bash
   # Install pre-commit globally using pipx
   pipx install pre-commit
   ```

2. **Set Up Pre-commit Hooks** ✅
   ```bash
   # Install pre-commit hooks
   pre-commit install

   # Verify the setup by running pre-commit on all files
   pre-commit run --all-files
   ```

## Generating the PDF 📄

### Using Invoke Tasks (Recommended) 🚀

This project includes invoke tasks for streamlined resume management:

```bash
# Build the PDF from Markdown
inv build

# Deploy the PDF to iCloud and website locations
inv deploy

# Build and deploy in one command
inv all
```

The `deploy` task copies the resume to:
- `~/Library/Mobile Documents/com~apple~CloudDocs/job/resume/Jonah_Jacobsen_Resume.pdf` (iCloud)
- `~/Projects/website/public/jonah_jacobsen_resume.pdf` (website)

### Manual PDF Generation 📝

Alternatively, you can manually convert `resume.md` to a PDF:

```bash
pandoc resume.md -o resume.pdf
```

This command will generate `resume.pdf` in the same directory.

### Customization 🎨

- For styling, refer to [Pandoc's documentation](https://pandoc.org/MANUAL.html#creating-a-pdf).
- To include metadata or use a custom template, adjust the command, e.g., `pandoc resume.md --template=template.tex -o resume.pdf`.

Feel free to edit `resume.md` to update the content and regenerate the PDF as needed.

## Ensuring ATS Compatibility 🤖

Applicant Tracking Systems (ATS) parse resumes automatically, so it's important to ensure your PDF is readable by these systems. The PDF generated from Markdown via Pandoc is generally simple and ATS-friendly, but here's how to verify:

1. **Use Online ATS Checkers** 🔍
   Upload your `resume.pdf` to free tools like:
   - [Jobscan](https://www.jobscan.co)
   - [Resume Worded](https://resumeworded.com)
   - [VMock](https://www.vmock.com/)

   These tools simulate ATS parsing and provide feedback on readability, keywords, and formatting issues.

2. **Manual Text Extraction Test** 📋
   Convert the PDF to plain text and check if the content flows logically without garbled text:
   ```bash
   # Install pdf2txt if needed (via pip or brew install poppler)
   pdftotext resume.pdf resume.txt

   # Then open resume.txt in a text editor to review
   ```

   Ensure sections, bullet points, and details are preserved without visual elements disrupting the text.

3. **Best Practices for ATS-Friendly Resumes** 💡
   - Use standard fonts (e.g., Arial, Times New Roman) – customize via Pandoc if needed.
   - Avoid tables, images, headers/footers, or complex layouts in `resume.md`.
   - Include relevant keywords from job descriptions naturally.
   - Stick to standard sections (e.g., Experience, Education).

If issues are found, simplify the Markdown content and regenerate the PDF.

## General Resume Tips 💡

Here are some tips to make your resume more effective:

- **Quantify accomplishments**: Use specific numbers to demonstrate impact, e.g., "Increased sales by 20%" instead of just "Increased sales".
- **Use action verbs**: Start each bullet point with strong verbs like "Led", "Developed", "Managed", or "Optimized".
- **Tailor to the job**: Customize your resume to match the job description by highlighting relevant skills and experiences.
- **Keep it concise**: Aim for one page if possible, focusing on the most important information.
- **Proofread carefully**: Check for spelling, grammar, and formatting errors multiple times.
- **Include keywords**: Incorporate terms from the job posting to pass ATS filters.
