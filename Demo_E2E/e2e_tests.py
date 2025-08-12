import time
from os import times

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

## Launch the application
driver.get("https://demo.automationtesting.in/Index.html")
print(driver.current_url)
print(driver.title)

# Click on the "Login" button
driver.find_element(By.ID,"email").send_keys("test@gmail.com")
driver.find_element(By.ID,"enterimg").click()
msg_text = driver.find_element(By.TAG_NAME,"h1").text
print(msg_text)
assert msg_text == "Automation Demo Site"

## Enter Personal Details
driver.find_element(By.XPATH,"//input[@placeholder='First Name']").send_keys("Rohit")
driver.find_element(By.XPATH,"//input[@placeholder='Last Name']").send_keys("Sharma")
driver.find_element(By.XPATH,"//textarea[@ng-model='Adress']").send_keys("Mumbai,Maharashtra, India")
driver.find_element(By.XPATH,"//input[@type='email']").send_keys("rohitsharma@gmail.com")
driver.find_element(By.XPATH,"//input[@type='tel']").send_keys("9665191918")

#Select radio button
driver.find_element(By.XPATH,"//input[@value='Male']").click()

## Select the checkboxes for hobbies
driver.find_element(By.XPATH,"//input[@id='checkbox1']").click()
driver.find_element(By.XPATH,"//input[@id='checkbox2']").click()
driver.find_element(By.XPATH,"//input[@id='checkbox3']").click()


## Select language from the dropdown
driver.find_element(By.XPATH, "//div[@id='msdd']").click()
languages = driver.find_elements(By.XPATH,"//div/ul[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content ui-corner-all']/li")
for language in languages:
    if language.text == "Hindi":
        language.click()
        break

##Skip this step
skills = driver.find_element(By.XPATH,"//select[@id='Skills']/option")
skills.click()
print(skills.text)

##Search country and select it
driver.find_element(By.XPATH,"//span[@role='combobox']").click()
driver.find_element(By.XPATH,"//input[@type='search']").send_keys("Ind")
driver.find_element(By.XPATH,"//li[@role='treeitem']").click()

##Select Year from the dropdown
years = driver.find_elements(By.XPATH,"//select[@id='yearbox']/option")
years.__getattribute__("__iter__")()
for year in years:
    if year.text == "2001":
        year.click()
        break

##Select month from the dropdown
months = driver.find_elements(By.XPATH,"//select[@placeholder='Month']/option")
months.__getattribute__("__iter__")()
for month in months:
    if month.text == "October":
        month.click()
        break
## Select date from the dropdown
Dates = driver.find_elements(By.XPATH,"//select[@id='daybox']/option")
Dates.__getattribute__("__iter__")()
for date in Dates:
    if date.text == "11":
        date.click()
        break
## Add the Password
driver.find_element(By.XPATH,"//input[@id='firstpassword']").send_keys("Rohit@123")
driver.find_element(By.XPATH,"//input[@id='secondpassword']").send_keys("Rohit@123")

## Click on the Submit button
driver.find_element(By.XPATH,"//button[@id='submitbtn']").click()
time.sleep(2)


