from pages.register_page import RegisterPage
from test_data import REGISTER_DATA


def test_register_user(driver):


    driver.get(
        "https://automationexercise.com/login"
    )


    register = RegisterPage(driver)


    # Signup
    register.enter_name(
        REGISTER_DATA["name"]
    )


    register.enter_email(
        REGISTER_DATA["email"]
    )


    register.click_signup()



    # Create Account

    register.enter_password(
        REGISTER_DATA["password"]
    )


    register.enter_first_name(
        REGISTER_DATA["first_name"]
    )


    register.enter_last_name(
        REGISTER_DATA["last_name"]
    )


    register.enter_address(
        REGISTER_DATA["address"]
    )


    register.enter_state(
        REGISTER_DATA["state"]
    )


    register.enter_city(
        REGISTER_DATA["city"]
    )


    register.enter_zipcode(
        REGISTER_DATA["zipcode"]
    )


    register.enter_mobile(
        REGISTER_DATA["mobile"]
    )


    register.click_create_account()



    register.verify_account_created()