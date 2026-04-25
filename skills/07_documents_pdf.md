# Skill: Document & PDF Creation

## When to use
Resumes, CVs, reports, proposals, memos, contracts templates, structured documents that need to be sent as files.

## PDF Generation Tools Available
- `fpdf2` — Python library, fast, good for structured docs
- `reportlab` — Python library, powerful for complex layouts
- `wkhtmltopdf` — converts HTML to PDF, best for styled documents

## Preferred Approach: HTML → PDF via wkhtmltopdf
1. Generate clean HTML with inline CSS (professional styling)
2. Convert with: `wkhtmltopdf --page-size A4 input.html output.pdf`
3. Save to /tmp/document.pdf
4. Send as Telegram file attachment

## Resume/CV Template for Oui
When building Oui's resume, use these defaults:
- **Name:** Wutcharin (Oui) Thatan
- **Role:** Head of FinTech Data & Automation | AI, Analytics & Automation Leader
- **Company:** Agoda
- **Location:** Bangkok, Thailand
- **Style:** Clean, modern, single or two-page, ATS-friendly
- **Sections:** Summary → Experience → Skills → Education → Certifications

## Document Design Standards
- A4 page size
- Clean sans-serif font (Arial, Helvetica, or Inter)
- Professional color: dark navy or charcoal headers, white background
- Adequate whitespace — never cramped
- Page numbers for multi-page documents

## Workflow
1. Collect content (ask if not provided)
2. Generate HTML template with proper styling
3. Convert to PDF using wkhtmltopdf
4. Send file via Telegram
5. Offer to adjust layout, content, or style

## Examples
- "Build my resume as a PDF"
- "Create a project proposal document for the AI automation initiative"
- "Write a one-pager on our Q1 analytics results and export as PDF"
