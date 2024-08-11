import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.color import Color

from pages.fill_form_page import FillFormPage


def test_fill_form():

    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    test_fill_form = FillFormPage(driver)
    
    test_fill_form.first_name('Данил')
    test_fill_form.last_name('Тарханов')
    test_fill_form.address_field('Ленина, 55-3')
    test_fill_form.email_field('test@skypro.com')
    test_fill_form.phone_field('+7985899998787')
    test_fill_form.zip_code('')
    test_fill_form.city_field('Москва')
    test_fill_form.country_field('Россия')
    test_fill_form.job_position('QA')
    test_fill_form.company_field('SkyPro')
    test_fill_form.submit()
    
    red = '#842029'  # '#FF0000'
    green = '#0f5132'  # '#008000'

    check_color_by_class(test_fill_form, "alert-danger", red)
    check_color_by_class(test_fill_form, "alert-success", green)


def check_color_by_class(page, class_name, expected_color):
    field = page.get_element_by_class(class_name)
    actual_color = Color.from_string(field.value_of_css_property('color')).hex
    print(f"Expected color {expected_color}, but got {actual_color}")
    assert actual_color == expected_color

def quit():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver = FillFormPage(driver)
    quit.quit()
