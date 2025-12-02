import allure
import time
from src.Pages.main_page import MainPage
from src.Pages.cart_page import CartPage
from src.Pages.checkout_page import CheckoutPage

@allure.story("Пользовательский сценарий покупки")
class TestE2E:

    @allure.title("Заказ пиццы: Полный путь клиента (E2E)")
    def test_buy_pizza_e2e(self, browser):
        main_page = MainPage(browser)
        cart_page = CartPage(browser)
        checkout_page = CheckoutPage(browser)

        with allure.step("Открыть главную страницу"):
            main_page.open()

        with allure.step("Добавить пиццу в корзину"):
            main_page.add_pizza_to_cart()
            time.sleep(1)

        with allure.step("Перейти в корзину"):
            main_page.go_to_cart()

        with allure.step("Перейти к оформлению"):
            cart_page.go_to_checkout()

        with allure.step("Авторизация перед заказом"):
            checkout_page.login("Artyom", "123456")

        with allure.step("Заполнить данные заказа"):
            checkout_page.fill_billing_details(
                name="Александр",
                last_name="Тестовый",
                address="Улица Пушкина, дом Колотушкина",
                city="Москва",
                phone="+79991234567",
                email="test@mail.ru"
            )
            checkout_page.select_payment_and_date()

        with allure.step("Подтвердить заказ"):
            checkout_page.place_order()

        with allure.step("Проверка успешного оформления"):
            assert checkout_page.is_order_received(), "Сообщение об успешном заказе не найдено!"
