from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
waiter = WebDriverWait(driver, 16, 0.1)

driver.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')

waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#text'), 'Done!')
)

src = driver.find_element(By.CSS_SELECTOR, '[src="img/award.png"]').get_attribute('src')

print(src)

driver.quit()