from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# Скрипты для Mozilla Firefox

# Клик по кнопке
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
search_element = driver.find_element(By.XPATH, "//button[text()='Add Element']")
for _ in range(5):  
    search_element.click()

delete = driver.find_elements(By.CSS_SELECTOR, '.added-manually')
print(len(delete))

sleep(5)

# Клик по кнопке без ID
driver.get("http://uitestingplayground.com/dynamicid/")
driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
for _ in range(2):  
    driver.get("http://uitestingplayground.com/dynamicid/")
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()

sleep(5)

# Клик по кнопке с CSS-классом
driver.get('http://uitestingplayground.com/classattr')
driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
alert = Alert(driver)
print(alert.text)
alert.accept()

for _ in range(2):
    driver.get('http://uitestingplayground.com/classattr')
    driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    alert = Alert(driver)
    print(alert.text)
    alert.accept()

sleep(5)

# Модальное окно
driver.get('http://the-internet.herokuapp.com/entry_ad')
sleep(5)
driver.find_element(By.CSS_SELECTOR, '.modal-footer').click()

sleep(5)

# Поле ввода
driver.get('http://the-internet.herokuapp.com/inputs')
number_field = driver.find_element(By.CSS_SELECTOR, 'input[type="number"]')
number_field.click()
number_field.send_keys('1000')
number_field.clear()
number_field.send_keys('999')

sleep(5)

# форма авторизации
driver.get('http://the-internet.herokuapp.com/login')
username_field = driver.find_element(By.ID, 'username')
username_field.click()
username_field.send_keys("tomsmith")

password_field = driver.find_element(By.ID, 'password')
password_field.click()
password_field.send_keys("SuperSecretPassword!")

driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()  # Click login button

sleep(5)

driver.quit()
