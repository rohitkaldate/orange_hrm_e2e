class LaunchPage:
    def __init__(self, driver):
        self.driver = driver

    def launch_page(self):
        self.driver.get("https://www.demoblaze.com/")
        print(self.driver.title)
        print(self.driver.current_url)