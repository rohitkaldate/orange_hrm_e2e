# File: launch.py
class Launch:
    def __init__(self, driver):
        self.driver = driver

    def launch_app(self):
        self.driver.get("https://demo.automationtesting.in/Index.html")
        print(self.driver.current_url)
        print(self.driver.title)