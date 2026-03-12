from playwright._impl._page import Page


class LoginPage:


    # Page p;

    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://phptravels.net/login")

    def login(self, email, password):

        self.page.fill("input[name='email']", email)
        self.page.fill("input[name='password']", password)
        self.page.click("button[type='submit']")
        self.page.wait_for_load_state("networkidle",timeout=25000)


    def is_login_page(self):
        return self.page.locator("input[name='email']").is_visible()