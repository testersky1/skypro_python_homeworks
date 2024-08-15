from selenium.webdriver.common.by import By
class CatalogPage:

    def __init__(self, driver):

        self._driver = driver
        self._driver.get('https://www.saucedemo.com/inventory.html')
        self._driver.implicitly_wait(4)

    def backpack(self):
        backpack = self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack')
        backpack.click()

    def t_shirt(self):
        t_shirt = self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt')
        t_shirt.click()

    def onesie(self):
        onesie = self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie')
        onesie.click()

    def cart(self):
        cart = self._driver.find_element(By.CSS_SELECTOR, 'a.shopping_cart_link')
        cart.click()

    def checkout(self):
        checkout = self._driver.find_element(By.CSS_SELECTOR, '#checkout')
        checkout.click()