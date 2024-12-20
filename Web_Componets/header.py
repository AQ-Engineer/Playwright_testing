from playwright.sync_api import Page

from Data.data import base_url


class Header:
    def __init__(self, page: Page):
        self.page = page

    def open_page(self):
        self.page.goto(base_url)

    def pause(self):
        self.page.pause()

    def click_sign_up(self):
        self.page.locator('//*[@class="btn btn-outline-light mb-2 me-2 ms-3"][text()="Войти"]').click()
