from selenium.webdriver.common.by import By

class PersonalInfo:
    def __init__(self,driver):
        self.driver = driver
        self.fname = (By.XPATH, "//input[@placeholder='First Name']")
        self.lname = (By.XPATH, "//input[@placeholder='Last Name']")
        self.add = (By.XPATH, "//textarea[@ng-model='Adress']")
        self.email_id = (By.XPATH, "//input[@type='email']")
        self.phone = (By.XPATH, "//input[@type='tel']")
        self.gender = (By.XPATH, "//input[@value='Male']")
        self.chk1 = (By.XPATH, "//input[@id='checkbox1']")
        self.chk2 = (By.XPATH, "//input[@id='checkbox2']")
        self.chk3 = (By.XPATH, "//input[@id='checkbox3']")
        self.lang_box = (By.XPATH, "//div[@id='msdd']")
        self.languages = (By.XPATH,"//div/ul[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content ui-corner-all']/li")
        self.skill = (By.XPATH, "//select[@id='Skills']/option")
        self.search_country = (By.XPATH, "//span[@role='combobox']")
        self.country_name = (By.XPATH, "//input[@type='search']")
        self.click_country = (By.XPATH, "//li[@role='treeitem']")
        self.year = (By.XPATH, "//select[@id='yearbox']/option")
        self.month = (By.XPATH, "//select[@placeholder='Month']/option")
        self.date = (By.XPATH, "//select[@id='daybox']/option")
        self.pass1 = (By.XPATH, "//input[@id='firstpassword']")
        self.pass2 = (By.XPATH, "//input[@id='secondpassword']")
        self.submit = (By.XPATH, "//button[@id='submitbtn']")


    def personal_info(self,name,last_name,address,eid,mobile):
        self.driver.find_element(*self.fname).send_keys(name)
        self.driver.find_element(*self.lname).send_keys(last_name)
        self.driver.find_element(*self.add).send_keys(address)
        self.driver.find_element(*self.email_id ).send_keys(eid)
        self.driver.find_element(*self.phone).send_keys(mobile)
        self.driver.find_element(*self.gender).click()
        self.driver.find_element(*self.chk1).click()
        self.driver.find_element(*self.chk2).click()
        self.driver.find_element(*self.chk3).click()


    def select_language(self, language):
        ## Select language from the dropdown
        self.driver.find_element(*self.lang_box ).click()
        languages = self.driver.find_elements(*self.languages)
        for language in languages:
            if language.text == "Hindi":
                language.click()
                break

    def skills_and_country(self):
        ##Skip this step
        skills = self.driver.find_element(*self.skill)
        skills.click()
        print(skills.text)

        ##Search country and select it
        self.driver.find_element(*self.search_country ).click()
        self.driver.find_element(*self.country_name ).send_keys("Ind")
        self.driver.find_element(*self.click_country).click()


    def date_of_birth(self):
        ##Select Year from the dropdown
        years = self.driver.find_elements(*self.year)
        years.__getattribute__("__iter__")()
        for year in years:
            if year.text == "2001":
                year.click()
                break

        ##Select month from the dropdown
        months = self.driver.find_elements(*self.month)
        months.__getattribute__("__iter__")()
        for month in months:
            if month.text == "October":
                month.click()
                break
        ## Select date from the dropdown
        Dates = self.driver.find_elements(*self.date)
        Dates.__getattribute__("__iter__")()
        for date in Dates:
            if date.text == "11":
                date.click()
                break

    def add_password(self):
        ## Add the Password
        self.driver.find_element(*self.pass1 ).send_keys("Rohit@123")
        self.driver.find_element(*self.pass1 ).send_keys("Rohit@123")

        ## Click on the Submit button
        self.driver.find_element(*self.submit).click()