import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver =  webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

##Launch webpage
driver.get("https://www.demoblaze.com/")
print(driver.title)
print(driver.current_url)

##Login to the application
driver.find_element(By.XPATH,"//a[@id='login2']").click()
driver.find_element(By.XPATH,"//input[@id='loginusername']").send_keys("Pranil@123")
driver.find_element(By.XPATH,"//input[@id='loginpassword']").send_keys("Rohit@123")
driver.find_element(By.XPATH,"//button[contains(text(),'Log in')]").click()
time.sleep(2)

##Select products depends upon the categories
categories = driver.find_elements(By.XPATH,"//a[@id='itemc']")
for cat in categories:
    if cat.text == "Laptops":
        cat.click()
        break

##Choose a product to purchase
driver.find_element(By.XPATH,"//a[contains(text(),'MacBook Pro')]").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.TAG_NAME, "h2")))

## Add product to cart
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Add to cart')]")))
driver.find_element(By.XPATH, "//a[contains(text(),'Add to cart')]").click()
time.sleep(2)
alert = driver.switch_to.alert
print(alert.text)
alert.accept()

## Navigate to cart and place order
driver.find_element(By.LINK_TEXT,"Cart").click()
price = wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//div/h3[@id='totalp']")))
print(price.text)
driver.find_element(By.XPATH,"//button[contains(text(),'Place Order')]").click()

## Fill in the order details
driver.find_element(By.ID,"name").send_keys("Rohit")
driver.find_element(By.ID,"country").send_keys("India")
driver.find_element(By.ID,"city").send_keys("Bangalore")
driver.find_element(By.ID,"card").send_keys("1234567890123456")
driver.find_element(By.ID,"month").send_keys("12")
driver.find_element(By.ID,"year").send_keys("2025")

## Click on Purchase button
driver.find_element(By.XPATH,"//button[contains(text(),'Purchase')]").click()

## Verify the purchase confirmation message
msg = driver.find_element(By.XPATH,"//div/h2[contains(text(),'Thank you for your purchase!')]")
print(msg.text)

details = driver.find_element(By.CSS_SELECTOR,".lead.text-muted")
print(details.text)
driver.find_element(By.XPATH,"//button[@class='confirm btn btn-lg btn-primary']").click()

##Logout from the application
driver.find_element(By.XPATH,"//a[contains(text(),'Log out')]").click()
time.sleep(2)