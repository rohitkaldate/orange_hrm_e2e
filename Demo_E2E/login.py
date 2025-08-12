from selenium.webdriver.common.by import By


class Login:
    def __init__(self,driver):
        self.driver = driver
        self.email_id = (By.ID, "email")
        self.submit_btn = (By.ID, "enterimg")
        self.text_msg = (By.TAG_NAME, "h1")

    def login_to_app(self,email_id):
        self.driver.find_element(*self.email_id).send_keys(email_id)
        self.driver.find_element(*self.submit_btn).click()
        msg_text = self.driver.find_element(*self.text_msg).text
        print(msg_text)
        assert msg_text == "Automation Demo Site"