from .base_page import BasePage
from .locators import ProductPageLocators

class PageObject(BasePage):
    def should_be_add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BASKET_FORM)
        button.click()

    def should_be_the_same_names(self):
        assert self.browser.find_element(*ProductPageLocators.NAME_BOOK_REAL).text == self.browser.find_element(
            *ProductPageLocators.NAME_BOOK_BASE).text, "Another names"

    def should_be_the_same_price(self):
        assert self.browser.find_element(*ProductPageLocators.PRICE_REAL).text == self.browser.find_element(
            *ProductPageLocators.PRICE_BASE).text, "Another prices"