import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_cart():

    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    waiter = WebDriverWait(driver, 16, 0.1)

    try:

        driver.get('https://www.saucedemo.com/')

        username_field = driver.find_element(By.CSS_SELECTOR, '#user-name')
        username_field.click()
        username_field.send_keys('standard_user')

        password_field = driver.find_element(By.CSS_SELECTOR, '#password')
        password_field.click()
        password_field.send_keys('secret_sauce')

        login_button = driver.find_element(By.CSS_SELECTOR, '#login-button')
        login_button.click()

        backpack = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack')
        backpack.click()

        t_shirt = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt')
        t_shirt.click()

        onesie = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie')
        onesie.click()

        cart = driver.find_element(By.CSS_SELECTOR, 'a.shopping_cart_link')
        cart.click()

        checkout = driver.find_element(By.CSS_SELECTOR, '#checkout')
        checkout.click()

        first_name = driver.find_element(By.CSS_SELECTOR, '#first-name')
        first_name.click()
        first_name.send_keys('Danil')

        last_name = driver.find_element(By.CSS_SELECTOR, '#last-name')
        last_name.click()
        last_name.send_keys('Tarkhanov')

        postal_code = driver.find_element(By.CSS_SELECTOR, '#postal-code')
        postal_code.click()
        postal_code.send_keys('618416')

        driver.find_element(By.CSS_SELECTOR, '#continue').click()

        total = driver.find_element(By.CSS_SELECTOR, 'div.summary_total_label').text
        assert total == 'Total: $58.29'

    finally:

        driver.quit()