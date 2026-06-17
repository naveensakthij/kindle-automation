import os
from pages.kindle_login_page import KindleLoginPage
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

def test_kindle_login(page):
    email = os.getenv("AMZN_EMAIL")
    password = os.getenv("AMZN_PASSWORD")
    
    if not email or not password:
        raise ValueError("Credentials not found! Set AMZN_EMAIL and AMZN_PASSWORD in .env")
    
    login_page = KindleLoginPage(page)
    
    # Execution flow
    login_page.navigate()
    login_page.click_signin()
    login_page.fill_email(email)
    login_page.click_continue()
    login_page.fill_password(password)
    login_page.click_signin_button()
    login_page.verify_login()
    
    print("Login verified successfully!")