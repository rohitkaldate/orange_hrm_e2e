import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class LoginCredentials:
    """
    Class to store login credentials for a website.
    """
    def __init__(self, driver):
        self.driver = driver
        self.login_option = (By.XPATH, "//a[@id='login2']")
        self.username = (By.XPATH, "//input[@id='loginusername']")
        self.password = (By.XPATH, "//input[@id='loginpassword']")
        self.click_login_btn = (By.XPATH, "//button[contains(text(),'Log in')]")
        self.verify_user = (By.XPATH,"//a[@id='nameofuser']")

    def login_info(self,username,password):
        """
        It is the login information of the user.
        """
        self.driver.find_element(*self.login_option).click()
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.click_login_btn).click()
        time.sleep(2)

    # def verify_login_success(self):
    #     """
    #     Verify if login was successful by checking the presence of a logout button.
    #     """
    #     wait = WebDriverWait(self.driver, 10)
    #     wait.until(expected_conditions.presence_of_element_located((self.verify_user)))
    #     user = self.driver.find_element(*self.verify_user )
    #     print(user.text)