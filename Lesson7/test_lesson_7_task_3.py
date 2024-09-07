import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from pages.cartPage.auth_page import AuthorizationPage
from pages.cartPage.catalog_page import CatalogPage
from pages.cartPage.form_page import FormPage
from pages.cartPage.total_page import TotalPage

def test_cart():

    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
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