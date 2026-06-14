import time
from playwright.sync_api import sync_playwright

def run_bot():
    with sync_playwright() as p:
        # Launch a visible browser (headless=False means we can see it)
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Navigate to LinkedIn
        print("Opening LinkedIn...")
        page.goto("https://www.linkedin.com")
        
        # Keep it open for 5 seconds so we can see it worked
        time.sleep(5)
        
        # Clean up and close
        browser.close()
        print("Browser closed successfully!")

if __name__ == "__main__":
    run_bot()