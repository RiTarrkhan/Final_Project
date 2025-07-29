from .base_page import BasePage
from .locators import BasketPageLocators
import time

class BasketPage(BasePage):
    def go_to_basket(self):
        button = self.browser.find_element(*BasketPageLocators.BASKET_LINK)
        button.click()

    def should_be_is_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_EMPTY), "Basket is not empty"

    def should_be_is_text_present(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_TEXT), "Basket is full"

