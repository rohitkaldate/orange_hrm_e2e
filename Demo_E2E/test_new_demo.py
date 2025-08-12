from Demo_E2E.launch import Launch
from Demo_E2E.login import Login
from Demo_E2E.personal_info import PersonalInfo


def test_e2e_demo(browserInstance):
    driver = browserInstance
    # Launch the application
    launch_page = Launch(driver)
    launch_page.launch_app()

    # Perform login
    login_step = Login(driver)
    login_step.login_to_app("test@gmail.com")

    ##Personal_information
    info = PersonalInfo(driver)
    info.personal_info("rohit", "sharma", "Mumbai,Maharashtra, India", "rohit@gmail.com", "9665191918")
    info.select_language("Hindi")
    info.skills_and_country()
    info.date_of_birth()
    info.add_password()





