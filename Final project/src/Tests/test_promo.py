import time
import allure
import pytest
from src.Pages.main_page import MainPage
from src.Pages.cart_page import CartPage


@allure.story("Проверка работы промокодов")
class TestPromoCode:

    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.main_page = MainPage(browser)
        self.cart_page = CartPage(browser)

        with allure.step("Предусловие: Добавить пиццу и перейти в корзину"):
            self.main_page.open()
            self.main_page.add_pizza_to_cart()

            time.sleep(1)
            self.main_page.go_to_cart()

    @allure.title("Сценарий №1: Применение валидного купона (GIVEMEHALYAVA)")
    def test_valid_promo(self, browser):
        price_before = self.cart_page.get_total_price()

        with allure.step("Применить купон GIVEMEHALYAVA"):
            self.cart_page.apply_coupon("GIVEMEHALYAVA")

        with allure.step("Проверить скидку 10%"):
            time.sleep(2)
            price_after = self.cart_page.get_total_price()

            expected_price = price_before * 0.9

            assert abs(price_after - expected_price) < 1.0, \
                f"Цена не снизилась на 10%! Было: {price_before}, Стало: {price_after}"

    @allure.title("Сценарий №2: Невалидный купон (DC120)")
    def test_invalid_promo(self, browser):
        price_before = self.cart_page.get_total_price()

        with allure.step("Применить неверный купон"):
            self.cart_page.apply_coupon("DC120")

        with allure.step("Проверить отсутствие скидки и ошибку"):
            time.sleep(2)
            price_after = self.cart_page.get_total_price()

            assert price_before == price_after, "Цена изменилась от невалидного купона!"

            error_msg = self.cart_page.get_error_message()
            assert "неверный" in error_msg.lower() or "does not exist" in error_msg.lower(), \
                f"Нет сообщения об ошибке! Текст: {error_msg}"

    @allure.title("Сценарий №3: Ошибка сервера 500 (Перехват запроса)")
    def test_promo_server_error(self, browser):
        price_before = self.cart_page.get_total_price()

        def interceptor(request):
            if 'apply_coupon' in request.url or 'coupon_code' in request.body.decode('utf-8', errors='ignore'):
                request.create_response(
                    status_code=500,
                    headers={'Content-Type': 'application/json'},
                    body='{"error": "Internal Server Error"}'
                )

        browser.request_interceptor = interceptor

        with allure.step("Применить купон с ошибкой сервера"):
            self.cart_page.apply_coupon("GIVEMEHALYAVA")
            time.sleep(2)

        with allure.step("Проверить, что сайт не упал и скидки нет"):
            price_after = self.cart_page.get_total_price()
            assert price_before == price_after, "Цена изменилась, хотя сервер вернул 500!"

        del browser.request_interceptor
