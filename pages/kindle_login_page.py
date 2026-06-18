from playwright.sync_api import Page

class KindleLoginPage:
    def __init__(self, page: Page):
        self.page = page
        
    # Locators
    SIGN_IN_BTN = "#top-sign-in-btn"
    EMAIL_INPUT = "#ap_email"
    CONTINUE_BTN = "#continue"
    PASSWORD_INPUT = "input[name='password']"
    SIGNIN_BTN = "input[type=submit]"
    
    def navigate(self):
        self.page.goto("https://read.amazon.com")
    
    def click_signin(self):
        self.page.click(self.SIGN_IN_BTN)
    
    def fill_email(self, email: str):
        self.page.fill(self.EMAIL_INPUT, email)
    
    def click_continue(self):
        self.page.click(self.CONTINUE_BTN)
    
    def fill_password(self, password: str):
        self.page.fill(self.PASSWORD_INPUT, password)
    
    def click_signin_button(self):
        self.page.click(self.SIGNIN_BTN)
    
    def verify_login(self):
        # Wait for URL to stabilize
        self.page.wait_for_load_state("networkidle")
        
        # Explicitly wait for the Kindle library URL
        self.page.wait_for_url(
            lambda url: "kindle-library" in url,
            timeout=15000  # 15 seconds
        )
        
        # Final assertion
        assert "/kindle-library" in self.page.url, f"Expected Kindle library URL, got: {self.page.url}"