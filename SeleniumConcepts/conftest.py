import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browserInstance():
    print("Launching the  browser instance")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    print("Closing the browser instance")
    driver.close()  # it will run after the test execution