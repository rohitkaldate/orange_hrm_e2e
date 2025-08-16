import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class PurchaseAndAddToCart:
    def __init__(self, driver):
        self.driver = driver
        self.categories = (By.XPATH, "//a[@id='itemc']")
        self.product = (By.XPATH, "//a[contains(text(),'MacBook Pro')]")
        self.add_cart = (By.XPATH, "//a[contains(text(),'Add to cart')]")
        self.go_to_cart = (By.LINK_TEXT, "Cart")
        self.total_price = (By.XPATH, "//div/h3[@id='totalp']")
        self.place_order = (By.XPATH, "//button[contains(text(),'Place Order')]")
        self.name = (By.ID, "name")
        self.country = (By.ID, "country")
        self.city = (By.ID, "city")
        self.credit = (By.ID, "card")
        self.month = (By.ID, "month")
        self.year = (By.ID, "year")
        self.confirm_purchase = (By.XPATH, "//button[contains(text(),'Purchase')]")


    def choose_product(self):
        categories = self.driver.find_elements(*self.categories)
        for cat in categories:
            if cat.text == "Laptops":
                cat.click()
                break
        self.driver.find_element(*self.product).click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.visibility_of_element_located((By.TAG_NAME, "h2")))
        wait.until(expected_conditions.visibility_of_element_located((self.add_cart)))
        self.driver.find_element(*self.add_cart).click()
        time.sleep(2)
        alert = self.driver.switch_to.alert
        print(alert.text)
        alert.accept()

    def navigate_to_cart(self):
        self.driver.find_element(*self.go_to_cart).click()
        wait = WebDriverWait(self.driver, 10)
        price = wait.until(expected_conditions.visibility_of_element_located((self.total_price)))
        print(price.text)
        self.driver.find_element(*self.place_order).click()

    def fill_purchase_details(self,name, country, city, credit_card, month, year):
        self.driver.find_element(*self.name).send_keys(name)
        self.driver.find_element(*self.country).send_keys(country)
        self.driver.find_element(*self.city).send_keys(city)
        self.driver.find_element(*self.credit).send_keys(credit_card)
        self.driver.find_element(*self.month).send_keys(month)
        self.driver.find_element(*self.year).send_keys(year)

    def final_purchase(self):
        ## Click on Purchase button
        self.driver.find_element(*self.confirm_purchase).click()
        time.sleep(2)
