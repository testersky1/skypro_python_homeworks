from selenium.webdriver.common.by import By
class FormPage:

    def __init__(self, driver):

        self._driver = driver
        self._driver.get('https://www.saucedemo.com/checkout-step-one.html')
        self._driver.implicitly_wait(4)

    def first_name(self, name):
        first_name = self._driver.find_element(By.CSS_SELECTOR, '#first-name')
        first_name.click()
        first_name.send_keys(name)

    def last_name(self, surname):
        last_name = self._driver.find_element(By.CSS_SELECTOR, '#last-name')
        last_name.click()
        last_name.send_keys(surname)

    def postal_code(self, code):
        postal_code = self._driver.find_element(By.CSS_SELECTOR, '#postal-code')
        postal_code.click()
        postal_code.send_keys(code)

    def button_continue(self):
        self._driver.find_element(By.CSS_SELECTOR, '#continue').click()