# Skill: Document & PDF Creation

## When to use
Resumes, CVs, reports, proposals, memos, structured documents sent as files.

## CRITICAL: Use this exact approach — do not deviate

### Step 1: Write HTML to /tmp/document.html
Generate clean HTML with inline CSS. Use this command in terminal:
```
python3 -c "
content = '''<!DOCTYPE html>...'''
open('/tmp/document.html', 'w').write(content)
print('written')
"
```

### Step 2: Convert to PDF
```
wkhtmltopdf --page-size A4 --margin-top 15mm --margin-bottom 15mm --margin-left 15mm --margin-right 15mm /tmp/document.html /tmp/document.pdf
```

### Step 3: Send the file
Send /tmp/document.pdf as a Telegram file attachment.

## If wkhtmltopdf fails, use Python fpdf2 directly:
```python
from fpdf import FPDF
pdf = FPDF()
pdf.add_page()
pdf.set_font('Helvetica', size=12)
pdf.cell(0, 10, 'Content here')
pdf.output('/tmp/document.pdf')
```

## DO NOT:
- Use pptxgenjs for PDFs
- Use soffice (not installed)
- Use npm packages for PDF generation
- Plan without executing — run the terminal commands immediately

## Resume HTML Template for Oui
```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  body { font-family: Arial, sans-serif; font-size: 11px; margin: 0; color: #212121; }
  .header { background: #1a2332; color: white; padding: 20px; }
  .header h1 { margin: 0; font-size: 24px; }
  .header .subtitle { color: #90b4d4; font-size: 12px; margin-top: 4px; }
  .header .contact { font-size: 10px; margin-top: 8px; color: #ccc; }
  .section { padding: 12px 20px 4px; border-bottom: 1px solid #eee; }
  .section h2 { color: #028090; font-size: 13px; margin: 0 0 8px; text-transform: uppercase; letter-spacing: 1px; }
  .job { margin-bottom: 10px; }
  .job-title { font-weight: bold; font-size: 11px; }
  .job-company { color: #555; }
  .job-dates { float: right; color: #888; font-size: 10px; }
  ul { margin: 4px 0 0 16px; padding: 0; }
  li { margin-bottom: 2px; }
  .skills { display: flex; flex-wrap: wrap; gap: 4px; }
  .skill-tag { background: #e8f4f8; padding: 2px 8px; border-radius: 10px; font-size: 9px; color: #028090; }
</style>
</head>
<body>
<!-- Fill in Oui's content here -->
</body>
</html>
```

## Oui's Default Info
- **Name:** Wutcharin (Oui) Thatan
- **Title:** Head of FinTech Data & Automation | AI, Analytics & Automation
- **Company:** Agoda, Bangkok, Thailand
- **Email:** wutcharin.th@gmail.com
- **LinkedIn:** https://linkedin.com/in/wutcharin
- **GitHub:** https://github.com/wutcharinth
- **Website:** https://wutcharin.com
