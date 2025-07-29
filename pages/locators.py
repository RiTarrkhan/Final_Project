from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BASKET_FORM = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    NAME_BOOK_REAL = (By.CSS_SELECTOR, ".alertinner strong")
    NAME_BOOK_BASE = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    PRICE_REAL = (By.CSS_SELECTOR, ".alertinner p strong")
    PRICE_BASE = (By.CSS_SELECTOR, ".col-sm-6.product_main p")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner ")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class BasketPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > .btn:first-child")
    BASKET_EMPTY = (By.CSS_SELECTOR, ".col-sm-6.h3")
    BASKET_TEXT = (By.CSS_SELECTOR, "p")