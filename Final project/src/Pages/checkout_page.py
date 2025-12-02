from src.Pages.base_page import BasePage
from src.Pages.locators import CheckoutLocators
import time


class CheckoutPage(BasePage):
    def login(self, username, password):
        try:
            self.click(CheckoutLocators.SHOW_LOGIN_LINK)
            time.sleep(1)
        except Exception:
            print("Ссылка 'Авторизуйтесь' не найдена или уже нажата")

        self.send_keys(CheckoutLocators.LOGIN_USERNAME, username)
        self.send_keys(CheckoutLocators.LOGIN_PASSWORD, password)
        self.click(CheckoutLocators.LOGIN_BTN)
        time.sleep(2)

    def fill_billing_details(self, name, last_name, address, city, phone, email, post="100000"):
        self.send_keys(CheckoutLocators.FIRST_NAME, name)
        self.send_keys(CheckoutLocators.LAST_NAME, last_name)
        self.send_keys(CheckoutLocators.ADDRESS, address)
        self.send_keys(CheckoutLocators.CITY, city)
        self.send_keys(CheckoutLocators.POSTCODE, post)
        self.send_keys(CheckoutLocators.PHONE, phone)
        self.send_keys(CheckoutLocators.EMAIL, email)

    def select_payment_and_date(self):
        self.send_keys(CheckoutLocators.DATE_PICKER, "25.12.2025")

        try:
            self.click(CheckoutLocators.PAYMENT_CASH, scroll=True)
        except Exception:
            pass

        self.click(CheckoutLocators.TERMS_CHECKBOX, scroll=True)

    def place_order(self):
        self.click(CheckoutLocators.PLACE_ORDER_BTN, scroll=True)
        time.sleep(3)

    def is_order_received(self):
        text = self.get_text(CheckoutLocators.ORDER_THANK_YOU)
        return "Спасибо! Ваш заказ был получен." in text
