from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BASKET_FORM)
        button.click()

    def should_be_the_same_names(self):
        assert self.browser.find_element(*ProductPageLocators.NAME_BOOK_REAL).text == self.browser.find_element(
            *ProductPageLocators.NAME_BOOK_BASE).text, "Another names"

    def should_be_the_same_price(self):
        assert self.browser.find_element(*ProductPageLocators.PRICE_REAL).text == self.browser.find_element(
            *ProductPageLocators.PRICE_BASE).text, "Another prices"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Message is not disappear, it's wrong"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Message is presented, it's wrong"


