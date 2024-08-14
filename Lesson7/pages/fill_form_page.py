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
        
    def success_first_name(self):
        first = self._driver.find_element(By.ID, 'first-name')
        return first.value_of_css_property('background-color')
    def success_last_name(self):
        last = self._driver.find_element(By.ID, 'last-name')
        return last.value_of_css_property('background-color')
    def success_address(self):
        address = self._driver.find_element(By.ID, 'address')
        return address.value_of_css_property('background-color')
    def success_e_mail(self):
        e_mail_id = self._driver.find_element(By.ID, 'e-mail')
        return e_mail_id.value_of_css_property('background-color')
    def success_phone(self):
        phone = self._driver.find_element(By.ID, 'phone')
        return phone.value_of_css_property('background-color')
    def success_city(self):
        city = self._driver.find_element(By.ID, 'city')
        return city.value_of_css_property('background-color')
    def success_country(self):
        country = self._driver.find_element(By.ID, 'country')
        return country.value_of_css_property('background-color')
    def success_job_position(self):
        job_position = self._driver.find_element(By.ID, 'job-position')
        return job_position.value_of_css_property('background-color')
    def success_company(self):
        company = self._driver.find_element(By.ID, 'company')
        return company.value_of_css_property('background-color')
    

    def empty_zip_field(self):
        zip = self._driver.find_element(By.ID, 'zip-code')
        return zip.value_of_css_property('background-color')
    
    