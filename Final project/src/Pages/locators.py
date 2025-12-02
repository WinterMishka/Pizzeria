from selenium.webdriver.common.by import By


class MainLocators:
    PRODUCT_CARD = (By.XPATH, '//h3[contains(text(), "4 в 1")]/ancestor::li')
    PIZZA_BUTTON = (By.XPATH, '//h3[contains(text(), "4 в 1")]/ancestor::li//a[contains(@class, "add_to_cart_button")]')
    CART_BUTTON = (By.CSS_SELECTOR, '.cart-contents')


class CartLocators:
    COUPON_INPUT = (By.ID, 'coupon_code')
    APPLY_COUPON_BTN = (By.NAME, 'apply_coupon')
    CHECKOUT_BTN = (By.CSS_SELECTOR, '.checkout-button')
    TOTAL_PRICE = (By.CSS_SELECTOR, '.order-total .woocommerce-Price-amount bdi')
    REMOVE_ITEM = (By.CSS_SELECTOR, '.remove')
    ERROR_MESSAGE = (By.CSS_SELECTOR, '.woocommerce-error')


class CheckoutLocators:
    SHOW_LOGIN_LINK = (By.CSS_SELECTOR, '.showlogin')
    LOGIN_USERNAME = (By.ID, 'username')
    LOGIN_PASSWORD = (By.ID, 'password')
    LOGIN_BTN = (By.NAME, 'login')

    FIRST_NAME = (By.ID, 'billing_first_name')
    LAST_NAME = (By.ID, 'billing_last_name')
    ADDRESS = (By.ID, 'billing_address_1')
    CITY = (By.ID, 'billing_city')
    STATE = (By.ID, 'billing_state')
    POSTCODE = (By.ID, 'billing_postcode')
    PHONE = (By.ID, 'billing_phone')
    EMAIL = (By.ID, 'billing_email')

    DATE_PICKER = (By.ID, 'order_date')
    PAYMENT_CASH = (By.CSS_SELECTOR, 'label[for="payment_method_cod"]')
    TERMS_CHECKBOX = (By.ID, 'terms')
    PLACE_ORDER_BTN = (By.ID, 'place_order')
    ORDER_THANK_YOU = (By.CSS_SELECTOR, '.woocommerce-thankyou-order-received')
