from pages.login_page import LoginPage


# TC-005
# Login with valid credentials


def test_login_success(driver):

    driver.get(
        "https://automationexercise.com/login"
    )

    driver.maximize_window()


    login = LoginPage(driver)


    login.enter_email("Test007@gmail.com")

    login.enter_password("1234567")

    login.click_login()


    login.verify_login_success()
