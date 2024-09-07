import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.color import Color
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from pages.fill_form_page import FillFormPage

@pytest.fixture(scope="function")  
def driver():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    yield driver 
    driver.quit()  

def test_fill_form(driver):

    test_fill_form = FillFormPage(driver)
    
    test_fill_form.first_name('Данил')
    test_fill_form.last_name('Тарханов')
    test_fill_form.address_field('Ленина, 55-3')
    test_fill_form.email_field('test@skypro.com')
    #test_fill_form.email_field('')
    test_fill_form.phone_field('+7985899998787')
    test_fill_form.zip_code('')
    test_fill_form.city_field('Москва')
    test_fill_form.country_field('Россия')
    test_fill_form.job_position('QA')
    test_fill_form.company_field('SkyPro')
    test_fill_form.submit()
    
    assert test_fill_form.success_first_name() == 'rgb(209, 231, 221)'
    assert test_fill_form.success_last_name() == 'rgb(209, 231, 221)'
    assert test_fill_form.success_address() == 'rgb(209, 231, 221)'
    assert test_fill_form.empty_zip_field() == 'rgb(248, 215, 218)'
    assert test_fill_form.success_e_mail() == 'rgb(209, 231, 221)'
    assert test_fill_form.success_phone() == 'rgb(209, 231, 221)'
    assert test_fill_form.success_city() == 'rgb(209, 231, 221)'
    assert test_fill_form.success_country() == 'rgb(209, 231, 221)'
    assert test_fill_form.success_job_position() == 'rgb(209, 231, 221)'
    assert test_fill_form.success_company() == 'rgb(209, 231, 221)'
    