from playwright.sync_api import sync_playwright
import os

def login_to_instagram(page, username, password):
    print("Navigating to Instagram login page...")
    page.goto("https://www.instagram.com/accounts/login/")
    page.fill('input[name="username"]', username)
    page.fill('input[name="password"]', password)
    print("Logging in...")
    page.click('button[type="submit"]')
    page.wait_for_load_state('networkidle')
    print("Login successful. Waiting for the page to load completely...")

    # Handling "Save Your Login Info?" pop-up
    page.wait_for_timeout(3000)  # Wait for 3 seconds
    try:
        page.click('button:has-text("Not Now")')
        print("Clicked 'Not Now' on save login info.")
    except:
        print("No 'Not Now' for save login info.")

    # Handling "Turn on Notifications" pop-up
    page.wait_for_timeout(3000)  # Wait for 3 seconds
    try:
        page.click('button:has-text("Not Now")')
        print("Clicked 'Not Now' on notifications.")
    except:
        print("No 'Not Now' for notifications.")

def capture_profile(page):
    print("Navigating to Instagram home page...")
    page.goto("https://www.instagram.com/")
    print("Waiting for home page to load...")
    page.wait_for_timeout(5000)  # Wait for 5 seconds to ensure the page is fully loaded
    print("Navigating to profile...")
    page.click('a[href="/{}/"]'.format(username))  # Click on the profile icon to go to your profile
    page.wait_for_timeout(5000)  # Wait for 5 seconds to ensure the profile page is fully loaded

    # Save screenshot to a specific folder
    screenshot_folder = os.path.join(os.path.expanduser("~"), "Desktop", "MyScreenshots")
    if not os.path.exists(screenshot_folder):
        os.makedirs(screenshot_folder)  # Create the folder if it doesn't exist

    screenshot_path = os.path.join(screenshot_folder, "instagram_profile.png")
    print(f"Taking screenshot and saving to {screenshot_path}...")
    page.screenshot(path=screenshot_path)
    print("Screenshot taken and saved.")

def main():
    global username  # Define username globally to use in the profile URL
    username = "oreo_thecowmeow"  # Replace with your Instagram username
    password = "jellyintuna"  # Replace with your Instagram password

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login_to_instagram(page, username, password)
        capture_profile(page)

        browser.close()
        print("Browser closed.")

if __name__ == "__main__":
    main()
