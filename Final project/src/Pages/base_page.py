from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.base_url = "https://pizzeria.skillbox.cc/"

    def open(self, url=""):
        self.browser.get(self.base_url + url)

    def find(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator))

    def hover_over(self, locator):
        element = self.find(locator)
        action = ActionChains(self.browser)
        action.move_to_element(element).perform()

    def click(self, locator, scroll=False):
        element = self.find(locator)

        if scroll:
            self.browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            import time
            time.sleep(0.5)

        try:
            element.click()
        except Exception:
            self.browser.execute_script("arguments[0].click();", element)

    def send_keys(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text
