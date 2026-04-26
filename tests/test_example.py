from playwright.sync_api import Page


def test_google_title(page: Page):
    page.goto("https://www.google.com")
    assert "Google_1" in page.title()
