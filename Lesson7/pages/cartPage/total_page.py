from selenium.webdriver.common.by import By
class TotalPage:

    def __init__(self, driver):

        self._driver = driver
        self._driver.get('https://www.saucedemo.com/checkout-step-two.html')
        self._driver.implicitly_wait(4)

    def total(self):
        total = self._driver.find_element(By.CSS_SELECTOR, 'div.summary_total_label').text

        return total
        