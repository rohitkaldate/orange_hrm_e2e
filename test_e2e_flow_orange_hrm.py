from employee_page import Employee
from login_page import Launch
import os
import sys

import pytest

from logout import Logout

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

def test_orange_hrm(browserInstance):
    driver = browserInstance

    ##Launch and Login to app
    launch_login = Launch(driver)
    launch_login.launch_page()
    launch_login.login_app()

    ##Click PIM and add the employees
    employee =  Employee(driver)
    employee.click_pim()
    employee.add_employees()
    employee.emp_list()
    employee.list_emp_table()

    ## Logout Page
    logout =  Logout(driver)
    logout.logout_page()