from selenium import webdriver
from selenium.webdriver.common.by import By


class Launch:
    def __init__(self,driver):
        self.driver=driver
        self.username = (By.NAME, "username")
        self.password = (By.NAME, "password")
        self.login_btn =  (By.XPATH, "//button[@type='submit']")

    def launch_page(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        print(self.driver.title)
        print(self.driver.current_url)

    def login_app(self):
        self.driver.find_element(*self.username).send_keys("Admin")
        self.driver.find_element(*self.password).send_keys("admin123")
        self.driver.find_element(*self.login_btn).click()