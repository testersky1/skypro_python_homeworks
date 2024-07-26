from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert


driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get('http://uitestingplayground.com/textinput')

driver.find_element(By.CSS_SELECTOR, '#newButtonName').click()

driver.find_element(By.CSS_SELECTOR, '#newButtonName').send_keys('SkyPro')

driver.find_element(By.CSS_SELECTOR, '#updatingButton').click()

txt = driver.find_element(By.CSS_SELECTOR, '#updatingButton').text

print(txt)

driver.quit()