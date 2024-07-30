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

def test_fill_form():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    try:
        driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

        first_name_field = driver.find_element(By.NAME, 'first-name')
        first_name_field.click()
        first_name_field.send_keys('Иван')

        last_name_field = driver.find_element(By.NAME, 'last-name')
        last_name_field.click()
        last_name_field.send_keys('Петров')

        address_field = driver.find_element(By.NAME, 'address')
        address_field.click()
        address_field.send_keys('Ленина, 55-3')

        email_field = driver.find_element(By.NAME, 'e-mail')
        email_field.click()
        email_field.send_keys('test@skypro.com')

        phone_field = driver.find_element(By.NAME, 'phone')
        phone_field.click()
        phone_field.send_keys('+7985899998787')

        city_field = driver.find_element(By.NAME, 'city')
        city_field.click()
        city_field.send_keys('Москва')

        country_field = driver.find_element(By.NAME, 'country')
        country_field.click()
        country_field.send_keys('Россия')

        job_position_field = driver.find_element(By.NAME, 'job-position')
        job_position_field.click()
        job_position_field.send_keys('QA')

        company_field = driver.find_element(By.NAME, 'company')
        company_field.click()
        company_field.send_keys('SkyPro')

        submit_button = driver.find_element(By.CSS_SELECTOR, 'button[type=submit]')
        submit_button.click()
        
        sleep(3)  
        zip_code_field = driver.find_element(By.CSS_SELECTOR, '#zip-code')
        assert zip_code_field.value_of_css_property('background-color') == 'rgb(248, 215, 218)'

    finally:
        driver.quit()


