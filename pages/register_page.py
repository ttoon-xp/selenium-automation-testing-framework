from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegisterPage:


    name_input = (
        By.NAME,
        "name"
    )


    email_input = (
        By.XPATH,
        "//input[@data-qa='signup-email']"
    )


    signup_button = (
        By.XPATH,
        "//button[@data-qa='signup-button']"
    )


    password_input = (
        By.XPATH,
        "//input[@data-qa='password']"
    )


    first_name_input = (
        By.XPATH,
        "//input[@data-qa='first_name']"
    )


    last_name_input = (
        By.XPATH,
        "//input[@data-qa='last_name']"
    )


    address_input = (
        By.XPATH,
        "//input[@data-qa='address']"
    )


    state_input = (
        By.XPATH,
        "//input[@data-qa='state']"
    )


    city_input = (
        By.XPATH,
        "//input[@data-qa='city']"
    )


    zipcode_input = (
        By.XPATH,
        "//input[@data-qa='zipcode']"
    )


    mobile_input = (
        By.XPATH,
        "//input[@data-qa='mobile_number']"
    )


    create_account_button = (
        By.XPATH,
        "//button[@data-qa='create-account']"
    )


    def __init__(self, driver):

        self.driver = driver



    def enter_name(self, name):

        WebDriverWait(
            self.driver,
            10
        ).until(
            EC.visibility_of_element_located(
                self.name_input
            )
        ).send_keys(name)



    def enter_email(self, email):

        WebDriverWait(
            self.driver,
            10
        ).until(
            EC.visibility_of_element_located(
                self.email_input
            )
        ).send_keys(email)



    def click_signup(self):

        WebDriverWait(
            self.driver,
            10
        ).until(
            EC.element_to_be_clickable(
                self.signup_button
            )
        ).click()



    def enter_password(self, password):

        WebDriverWait(
            self.driver,
            10
        ).until(
            EC.visibility_of_element_located(
                self.password_input
            )
        ).send_keys(password)



    def enter_first_name(self, first_name):

        WebDriverWait(
            self.driver,
            10
        ).until(
            EC.visibility_of_element_located(
                self.first_name_input
            )
        ).send_keys(first_name)



    def enter_last_name(self, last_name):

        WebDriverWait(
            self.driver,
            10
        ).until(
            EC.visibility_of_element_located(
                self.last_name_input
            )
        ).send_keys(last_name)



    def enter_address(self, address):

        WebDriverWait(
            self.driver,
            10
        ).until(
            EC.visibility_of_element_located(
                self.address_input
            )
        ).send_keys(address)



    def enter_state(self, state):

        WebDriverWait(
            self.driver,
            10
        ).until(
            EC.visibility_of_element_located(
                self.state_input
            )
        ).send_keys(state)



    def enter_city(self, city):

        WebDriverWait(
            self.driver,
            10
        ).until(
            EC.visibility_of_element_located(
                self.city_input
            )
        ).send_keys(city)



    def enter_zipcode(self, zipcode):

        WebDriverWait(
            self.driver,
            10
        ).until(
            EC.visibility_of_element_located(
                self.zipcode_input
            )
        ).send_keys(zipcode)



    def enter_mobile(self, mobile):

        WebDriverWait(
            self.driver,
            10
        ).until(
            EC.visibility_of_element_located(
                self.mobile_input
            )
        ).send_keys(mobile)



    def click_create_account(self):

        WebDriverWait(
            self.driver,
            10
        ).until(
            EC.element_to_be_clickable(
                self.create_account_button
            )
        ).click()



    def verify_account_created(self):

        WebDriverWait(
            self.driver,
            10
        ).until(
            lambda driver: "Account Created!" in driver.page_source
        )
            