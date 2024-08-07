import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.fill_form_page import FillFormPage
from pages.calculator_page import CalculatorPage
from pages.cartPage.auth_page import AuthorizationPage
from pages.cartPage.catalog_page import CatalogPage
from pages.cartPage.form_page import FormPage
from pages.cartPage.total_page import TotalPage

def test_fill_form():

    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    test_fill_form = FillFormPage(driver)
    
    test_fill_form.first_name('Данил')
    test_fill_form.last_name('Тарханов')
    test_fill_form.address_field('Ленина, 55-3')
    test_fill_form.email_field('test@skypro.com')
    test_fill_form.phone_field('+7985899998787')
    test_fill_form.city_field('Москва')
    test_fill_form.country_field('Россия')
    test_fill_form.job_position('QA')
    test_fill_form.company_field('SkyPro')
    test_fill_form.submit()
    color = test_fill_form.empty_zip_field()
    
    assert color == 'rgb(248, 215, 218)'

    #driver.quit()

    test_calculator = CalculatorPage(driver)

    test_calculator.delay()
    test_calculator.key_7()
    test_calculator.key_plus()
    test_calculator.key_8()
    test_calculator.key_equality()
    result = test_calculator.result_field()

    assert result == '15'

    test_auth = AuthorizationPage(driver)

    test_auth.username('standard_user')
    test_auth.password('secret_sauce')
    test_auth.login()

    test_catalog = CatalogPage(driver)

    test_catalog.backpack()
    test_catalog.t_shirt()
    test_catalog.onesie()
    test_catalog.cart()
    test_catalog.checkout()

    test_form = FormPage(driver)

    test_form.first_name("Danil")
    test_form.last_name('Tarkhanov')
    test_form.postal_code('618416')
    test_form.button_continue()

    test_total = TotalPage(driver)

    res = test_total.total()

    assert res == 'Total: $58.29'

    driver.quit()

