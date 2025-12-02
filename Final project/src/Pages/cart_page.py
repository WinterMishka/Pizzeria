from src.Pages.base_page import BasePage
from src.Pages.locators import CartLocators
import time


class CartPage(BasePage):
    def apply_coupon(self, code):
        self.send_keys(CartLocators.COUPON_INPUT, code)
        self.click(CartLocators.APPLY_COUPON_BTN)
        time.sleep(2)

    def get_total_price(self):
        price_text = self.get_text(CartLocators.TOTAL_PRICE)
        clean_price = price_text.replace('₽', '').replace(',', '.').strip()
        return float(clean_price)

    def go_to_checkout(self):
        self.click(CartLocators.CHECKOUT_BTN)

    def get_error_message(self):
        return self.get_text(CartLocators.ERROR_MESSAGE)
