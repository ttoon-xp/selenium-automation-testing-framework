from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:


    email_input = (
        By.NAME,
        "email"
    )


    password_input = (
        By.NAME,
        "password"
    )


    login_button = (
        By.XPATH,
        "//button[contains(text(),'Login')]"
    )


    logged_in_text = (
        By.XPATH,
        "//a[contains(text(),'Logged in as')]"
    )


    def __init__(self, driver):
        self.driver = driver



    def enter_email(self, email):

        WebDriverWait(
            self.driver,
            10
        ).until(
            EC.visibility_of_element_located(
                self.email_input
            )
        ).send_keys(email)



    def enter_password(self, password):

        WebDriverWait(
            self.driver,
            10
        ).until(
            EC.visibility_of_element_located(
                self.password_input
            )
        ).send_keys(password)



    def click_login(self):

        WebDriverWait(
            self.driver,
            10
        ).until(
            EC.element_to_be_clickable(
                self.login_button
            )
        ).click()



    def verify_login_success(self):

        WebDriverWait(
            self.driver,
            10
        ).until(
            EC.visibility_of_element_located(
                self.logged_in_text
            )
        )