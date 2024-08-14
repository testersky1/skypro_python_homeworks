from selenium.webdriver.common.by import By
class AuthorizationPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://www.saucedemo.com/')
        self._driver.implicitly_wait(4)

    def username(self, name):
        username_field = self._driver.find_element(By.CSS_SELECTOR, '#user-name')
        username_field.click()
        username_field.send_keys(name)

    def password(self, password):
        password_field = self._driver.find_element(By.CSS_SELECTOR, '#password')
        password_field.click()
        password_field.send_keys(password)

    def login(self):
        login_button = self._driver.find_element(By.CSS_SELECTOR, '#login-button')
        login_button.click() 

        #https://www.saucedemo.com/inventory.html