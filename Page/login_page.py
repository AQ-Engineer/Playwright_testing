import allure
from playwright.sync_api import Page
from Data.data import valid_login, valid_password

class Login:
    def __init__(self, page: Page):
        self.page = page

    def enter_login(self):
        self.page.locator('[name="username"]').fill(valid_login)

    def enter_password(self):
        self.page.locator('[name="password"]').fill(valid_password)

    def sign_up_click(self):
        self.page.get_by_role("button", name="Войти").click()





