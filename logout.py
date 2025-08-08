import time
from ast import Bytes

from selenium.webdriver.common.by import By


class Logout:
    def __init__(self,driver):
        self.driver = driver
        self.click_logout_menu = (By.XPATH,"//li[@class='oxd-userdropdown']")
        self.logout_btn = (By.XPATH,"//a[contains(text(),'Logout')]")

    def logout_page(self):
        self.driver.find_element(*self.click_logout_menu).click()
        self.driver.find_element(*self.logout_btn).click()
        time.sleep(2)