from .pages.product_page import PageObject
from .pages.locators import ProductPageLocators
import pytest
import time

@pytest.mark.parametrize('link', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, link):
    promo_link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = PageObject(browser, promo_link)
    page.open()
    page.should_be_add_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(30)
    page.should_be_the_same_names()
    page.should_be_the_same_price()


