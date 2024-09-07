import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from pages.calculator_page import CalculatorPage

def test_calculator():

    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    test_calculator = CalculatorPage(driver)

    test_calculator.delay()
    test_calculator.key_7()
    test_calculator.key_plus()
    test_calculator.key_8()
    test_calculator.key_equality()
    result = test_calculator.result_field()

    assert result == '15'

    driver.quit()