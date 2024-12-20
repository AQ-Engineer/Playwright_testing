from playwright.async_api import expect
from playwright.sync_api import Page
from playwright.sync_api import expect

from conftest import header


def test_opens_page1(header):
    header.open_page()
    # header.pause()

def test_opens_page2(page: Page):

    page.goto("http://tester:dslfjsdfblkhew%40122b1klbfw@testing.misleplav.ru/")
    expect(page.get_by_role("link", name="Войти")).to_be_visible()
    # page.pause()
    page.get_by_role("link", name="Найти репетитора").nth(1).click()
    base_page = "http://tester:dslfjsdfblkhew%40122b1klbfw@testing.misleplav.ru/listings/list/"
    """ сравнение, что текущая стр. не равна главной"""
    expect(page).not_to_have_url(base_page)
    assert page != base_page


def test_open_page_pom(header,login):
    header.open_page()
    header.click_sign_up()
    login.enter_login()
    login.enter_password()
    # header.pause()
    login.sign_up_click()











