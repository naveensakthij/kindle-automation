# Open conftest.py in Notepad and paste:
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Change to True for CI
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()