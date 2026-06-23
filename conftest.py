import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():

    options = Options()

    # ปิด Chrome password save popup
    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        }
    )


    driver = webdriver.Chrome(
        options=options
    )


    driver.maximize_window()


    yield driver


    driver.quit()