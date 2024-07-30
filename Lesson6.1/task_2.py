import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_calculate():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    try:
        driver.get(' https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

        delay_field = driver.find_element(By.CSS_SELECTOR, '#delay')
        delay_field.clear()
        delay_field.click()
        delay_field.send_keys(Keys.NUMPAD4, Keys.NUMPAD5 )

        key_7_field = driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[1]')
        key_7_field.click()

        key_plus_field = driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[4]')
        key_plus_field.click()

        key_8_field = driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[2]')
        key_8_field.click()

        key_equality_field = driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[15]')
        key_equality_field.click()

        waiter = WebDriverWait(driver, 60)

        waiter.until(
            EC.text_to_be_present_in_element((By.XPATH, '//*[@id="calculator"]/div[1]/div'), '15')
        )
        result = driver.find_element(By.XPATH, '//*[@id="calculator"]/div[1]/div').text

        assert result == '15'

    finally:
        driver.quit()
