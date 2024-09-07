from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class CalculatorPage:
    
    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
        self._driver.implicitly_wait(4)

    def delay(self):
        delay_field = self._driver.find_element(By.CSS_SELECTOR, '#delay')
        delay_field.clear()
        delay_field.click()
        delay_field.send_keys(Keys.NUMPAD4, Keys.NUMPAD5 )

    def key_7(self):
        key_7_field = self._driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[1]')
        key_7_field.click()

    def key_plus(self):
        key_plus_field = self._driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[4]')
        key_plus_field.click()

    def key_8(self):
        key_8_field = self._driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[2]')
        key_8_field.click()

    def key_equality(self):
        key_equality_field = self._driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[15]')
        key_equality_field.click()

    def result_field(self):
        waiter = WebDriverWait(self._driver, 60)

        waiter.until(
            EC.text_to_be_present_in_element((By.XPATH, '//*[@id="calculator"]/div[1]/div'), '15')
        )
        result = self._driver.find_element(By.XPATH, '//*[@id="calculator"]/div[1]/div').text

        return result