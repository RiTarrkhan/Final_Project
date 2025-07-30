from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest
import time

@pytest.mark.login
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "@fakemail.org"
        self.page = LoginPage(browser, link)
        self.page.open()
        self.page.register_new_user(email, password)
        self.page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    @pytest.mark.parametrize('link',
                             ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
    def test_user_can_add_product_to_basket(self, browser, link):
        promo_link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
        page = ProductPage(browser, promo_link)
        page.open()
        page.should_be_add_to_basket()
        page.solve_quiz_and_get_code()
        time.sleep(30)
        page.should_be_the_same_names()
        page.should_be_the_same_price()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
@pytest.mark.parametrize('link', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, link):
    promo_link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, promo_link)
    page.open()
    page.should_be_add_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(30)
    page.should_be_the_same_names()
    page.should_be_the_same_price()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.should_be_is_basket_empty()
    page.should_be_is_text_present()

def test_guest_cant_see_success_message(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    button = browser.find_element(*ProductPageLocators.BASKET_FORM)
    button.click()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    button = browser.find_element(*ProductPageLocators.BASKET_FORM)
    button.click()
    page.should_dissapear_of_success_message()



