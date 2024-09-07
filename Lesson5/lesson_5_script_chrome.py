from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert 

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#Скрипты для Google Chrome

#Клик по кнопке
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
search_element = driver.find_element(By.CSS_SELECTOR, "[onclick='addElement()']")
search_element.click()
search_element.click()
search_element.click()
search_element.click()
search_element.click()
delete = driver.find_elements(By.CSS_SELECTOR, '.added-manually')

print(len(delete))

sleep(5)

#Клик по кнопке без ID
driver.get("http://uitestingplayground.com/dynamicid/")
driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
driver.get("http://uitestingplayground.com/dynamicid/")
driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
driver.get("http://uitestingplayground.com/dynamicid/")
driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()

sleep(5)

#Клик по кнопке с CSS-классом
driver.get('http://uitestingplayground.com/classattr')
driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
alert = Alert(driver)
print(alert.text)
alert.accept()

driver.get('http://uitestingplayground.com/classattr')
driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
alert = Alert(driver)
print(alert.text)
alert.accept()

driver.get('http://uitestingplayground.com/classattr')
driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
alert = Alert(driver)
print(alert.text)
alert.accept()

sleep(5)

#Модальное окно
driver.get('http://the-internet.herokuapp.com/entry_ad')
sleep(5)
driver.find_element(By.CSS_SELECTOR, 'div.modal-footer').click()

sleep(5)

#Поле ввода
driver.get('http://the-internet.herokuapp.com/inputs')
driver.find_element(By.CSS_SELECTOR, 'input[type="number"]').click()
driver.find_element(By.CSS_SELECTOR, 'input[type="number"]').send_keys('1000')
driver.find_element(By.CSS_SELECTOR, 'input[type="number"]').clear()
driver.find_element(By.CSS_SELECTOR, 'input[type="number"]').send_keys('999')

sleep(5)

#форма авторизации
driver.get('http://the-internet.herokuapp.com/login')
driver.find_element(By.CSS_SELECTOR, 'input#username').click()
driver.find_element(By.CSS_SELECTOR, 'input#username').send_keys("tomsmith")
driver.find_element(By.CSS_SELECTOR, 'input#password').click()
driver.find_element(By.CSS_SELECTOR, 'input#password').send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, 'i').click()
sleep(5)
