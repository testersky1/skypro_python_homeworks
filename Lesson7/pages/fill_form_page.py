from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
class FillFormPage:

    def __init__(self, driver):

        self._driver = driver
        self._driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
        self._driver.implicitly_wait(4)

    def first_name(self, name):
        self._driver.find_element(By.NAME, 'first-name').click()
        self._driver.find_element(By.NAME, 'first-name').send_keys(name)

    def last_name(self, surname):
        self._driver.find_element(By.NAME, 'last-name').click()
        self._driver.find_element(By.NAME, 'last-name').send_keys(surname)

    def address_field(self, address): 
        self._driver.find_element(By.NAME, 'address').click()
        self._driver.find_element(By.NAME, 'address').send_keys(address)

    def email_field(self, email):    
        self._driver.find_element(By.NAME, 'e-mail').click()
        self._driver.find_element(By.NAME, 'e-mail').send_keys(email)

    def phone_field(self, phone):
        self._driver.find_element(By.NAME, 'phone').click()
        self._driver.find_element(By.NAME, 'phone').send_keys(phone)

    def zip_code(self, zip):
        self._driver.find_element(By.NAME, 'zip-code').click()
        self._driver.find_element(By.NAME, 'zip-code').send_keys(zip)

    def city_field(self, city):
        self._driver.find_element(By.NAME, 'city').click()
        self._driver.find_element(By.NAME, 'city').send_keys(city)

    def country_field(self, country):
        self._driver.find_element(By.NAME, 'country').click()
        self._driver.find_element(By.NAME, 'country').send_keys(country)

    def job_position(self, job):
        self._driver.find_element(By.NAME, 'job-position').click()
        self._driver.find_element(By.NAME, 'job-position').send_keys(job)

    def company_field(self, company):
        self._driver.find_element(By.NAME, 'company').click()
        self._driver.find_element(By.NAME, 'company').send_keys(company)

    def submit(self):
        self._driver.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()
        
    def empty_zip_field(self):
        zip = self._driver.find_element(By.ID, 'zip-code')
        return zip.value_of_css_property('background-color')
    
    def get_element_by_class(self, class_name):
        element = WebDriverWait(self._driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, class_name))
        )
        return element
    
    def quit(self):
        self._driver.quit()