from SeleniumConcepts.add_to_cart import PurchaseAndAddToCart
from SeleniumConcepts.confirmation_logout import ConfirmationLogout
from SeleniumConcepts.launch_page import LaunchPage
from SeleniumConcepts.login_credentials import LoginCredentials

def test_demoblaze_e2e(browserInstance):
    driver = browserInstance

    ##Launch
    launch = LaunchPage(driver)
    launch.launch_page()

    #Login infor
    login = LoginCredentials(driver)
    login.login_info("Pranil@123", "Rohit@123")
    # # Verify login success
    # login.verify_login_success()

    ##Choose product and add to cart
    product = PurchaseAndAddToCart(driver)
    product.choose_product()
    product.navigate_to_cart()

    ##Fill purchase details
    product.fill_purchase_details("Rohit", "India", "Bangalore", "1234567890123456", "12", "2025")
    product.final_purchase()

    ##Confirmation and Logout
    confirm = ConfirmationLogout(driver)
    confirm.confirmation()
    confirm.logout()