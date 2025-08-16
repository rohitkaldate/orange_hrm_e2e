import time

from selenium.webdriver.common.by import By


class ConfirmationLogout:
    """
    This class handles the confirmation logout process.
    It provides methods to confirm the logout action.
    """

    def __init__(self, driver):
        self.driver = driver
        self.thanks_msg = (By.XPATH, "//div/h2[contains(text(),'Thank you for your purchase!')]")
        self.order_details = (By.CSS_SELECTOR, ".lead.text-muted")
        self.click_ok = (By.XPATH, "//button[@class='confirm btn btn-lg btn-primary']")
        self.logoutbtn = (By.XPATH, "//a[contains(text(),'Log out')]")

    def confirmation(self):
        ## Verify the purchase confirmation message
        msg = self.driver.find_element(*self.thanks_msg)
        print(msg.text)

        details = self.driver.find_element(*self.order_details)
        print(details.text)
        self.driver.find_element(*self.click_ok ).click()
        time.sleep(2)

    def logout(self):
        """
        This method logs out the user from the application.
        """
        self.driver.find_element(*self.logoutbtn).click()
        time.sleep(2)
        print("User logged out successfully.")