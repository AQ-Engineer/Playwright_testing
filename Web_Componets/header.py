import allure
from playwright.sync_api import Page
from Data.data import base_url


@allure.step("Кликаем на кнопку 'Войти'")
class Header:
    def __init__(self, page: Page):
        self.page = page

    def open_page(self):
        self.page.goto(base_url)

    def pause(self):
        self.page.pause()
