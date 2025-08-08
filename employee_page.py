import time

from selenium.webdriver.common.by import By

class Employee:
    def __init__(self,driver):
        self.driver = driver
        self.employees_to_add = [
            {"first_name": "Rohit", "last_name": "Sharma", "emp_id": "1234"},
            {"first_name": "Virat", "last_name": "Kohli", "emp_id": "1235"},
            {"first_name": "MS", "last_name": "Dhoni", "emp_id": "1236"},
            {"first_name": "Hardik", "last_name": "Pandya", "emp_id": "1237"}
        ]

        self.pim = (By.XPATH, "//ul/li/a/span[text()='PIM']")
        self.click_emp = (By.XPATH, "//a[contains(text(),'Add Employee')]")
        self.fname = (By.NAME, "firstName")
        self.lname = (By.NAME, "lastName")
        self.employee_id = (By.XPATH, "//div/div[2]/input[@class='oxd-input oxd-input--active']")
        self.save1 = (By.XPATH, "//button[@type='submit']")
        self.save2 = (By.XPATH, "//div[@class='orangehrm-custom-fields']/div/form/div[2]/button")
        self.click_emp_list = (By.XPATH, "//nav/ul/li[2]/a")
        self.find_row_elements = (By.XPATH, "//div/div/div[@role='rowgroup'][2]/div")
        self.click_next_btn = (By.XPATH, "//i[@class='oxd-icon bi-chevron-right']")

    ##Click PIM attribute from sidebar
    def click_pim(self):
        self.driver.find_element(*self.pim).click()

    ## Add employees one by one
    def add_employees(self):
        for emp in self.employees_to_add:
            self.driver.find_element(*self.click_emp).click()
            self.driver.find_element(*self.fname).send_keys(emp["first_name"])
            self.driver.find_element(*self.lname).send_keys(emp["last_name"])
            self.emp_id_field = self.driver.find_element(*self.employee_id)
            self.emp_id_field.clear()
            self.emp_id_field.send_keys(emp["emp_id"])

            self.driver.find_element(*self.save1).click()
            time.sleep(3)
            self.driver.find_element(*self.save2).click()

    ## Click to view employee list
    def emp_list(self):
        self.driver.find_element(*self.click_emp_list).click()


    ## Search the employee name in the table
    def list_emp_table(self):
        rows = self.driver.find_elements(*self.click_emp_list)
        print(len(rows))

        for emp in self.employees_to_add:
            found = False
            while not found:
                rows = self.driver.find_elements(*self.find_row_elements)
                try:
                    for row in rows:
                        if emp["first_name"] in row.text and emp["last_name"] in row.text:
                            print(f"{emp['first_name']} {emp['last_name']} - Name Verified")
                            found = True
                            break
                    if not found:
                        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                        self.driver.find_element(*self.click_next_btn).click()
                        time.sleep(2)
                except Exception as e:
                    print(f"{emp['first_name']} {emp['last_name']} - NOT FOUND")
                    break