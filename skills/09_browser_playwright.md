# Skill: Browser Automation (Playwright)

## When to use
- Sites that require login (LinkedIn, Notion, dashboards)
- JS-heavy pages where simple fetch fails
- Form filling, button clicking, file downloads
- Screenshots of specific pages
- Scraping paginated or dynamically loaded content
- When the built-in browser tool fails or says "Chrome not found"

## Playwright is installed — use it directly via terminal

### Basic page scrape
```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, args=["--no-sandbox", "--disable-dev-shm-usage"])
    page = browser.new_page()
    page.goto("https://example.com")
    content = page.content()
    text = page.inner_text("body")
    print(text[:3000])
    browser.close()
```

### Screenshot
```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, args=["--no-sandbox", "--disable-dev-shm-usage"])
    page = browser.new_page(viewport={"width": 1280, "height": 800})
    page.goto("https://example.com")
    page.screenshot(path="/tmp/screenshot.png", full_page=True)
    browser.close()
print("SAVED:/tmp/screenshot.png")
```

### Login + scrape
```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, args=["--no-sandbox", "--disable-dev-shm-usage"])
    page = browser.new_page()
    page.goto("https://site.com/login")
    page.fill("#username", "user@email.com")
    page.fill("#password", "password")
    page.click("button[type=submit]")
    page.wait_for_load_state("networkidle")
    content = page.inner_text("body")
    print(content[:3000])
    browser.close()
```

## Always use these Chromium flags (required in container):
`args=["--no-sandbox", "--disable-dev-shm-usage"]`

## Workflow
1. Write the Python script to /tmp/playwright_script.py
2. Run: `python3 /tmp/playwright_script.py`
3. Parse output or send screenshot file to user
