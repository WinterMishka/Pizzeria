from src.Pages.base_page import BasePage
from src.Pages.locators import MainLocators
import time


class MainPage(BasePage):
    def add_pizza_to_cart(self):
        self.hover_over(MainLocators.PRODUCT_CARD)

        time.sleep(1)

        self.click(MainLocators.PIZZA_BUTTON)

    def go_to_cart(self):
        self.click(MainLocators.CART_BUTTON)
