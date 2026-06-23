from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:


    search_input = (
        By.ID,
        "search_product"
    )


    search_button = (
        By.ID,
        "submit_search"
    )


    searched_products_title = (
        By.XPATH,
        "//h2[contains(text(),'Searched Products')]"
    )


    def __init__(self, driver):
        self.driver = driver


    def enter_search(self, keyword):

        WebDriverWait(
            self.driver,
            10
        ).until(
            EC.visibility_of_element_located(
                self.search_input
            )
        ).send_keys(keyword)



    def click_search(self):

        WebDriverWait(
            self.driver,
            10
        ).until(
            EC.element_to_be_clickable(
                self.search_button
            )
        ).click()



    def verify_search_result(self):

        WebDriverWait(
            self.driver,
            10
        ).until(
            EC.visibility_of_element_located(
                self.searched_products_title
            )
        )