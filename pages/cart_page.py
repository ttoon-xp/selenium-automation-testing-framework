from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:


    add_cart_button = (
        By.XPATH,
        "//a[contains(@class,'add-to-cart')]"
    )


    view_cart_button = (
        By.XPATH,
        "//div[@id='cartModal']//a[@href='/view_cart']"
    )


    remove_product_button = (
        By.XPATH,
        "//a[contains(@class,'cart_quantity_delete')]"
    )


    added_message = (
        By.XPATH,
        "//div[@id='cartModal']//h4"
    )


    def __init__(self, driver):
        self.driver = driver



    def click_add_to_cart(self):

        button = WebDriverWait(
            self.driver,
            10
        ).until(
            EC.element_to_be_clickable(
                self.add_cart_button
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )



    def click_view_cart(self):

        button = WebDriverWait(
            self.driver,
            10
        ).until(
            EC.visibility_of_element_located(
                self.view_cart_button
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )



    def remove_product(self):

        button = WebDriverWait(
            self.driver,
            10
        ).until(
            EC.element_to_be_clickable(
                self.remove_product_button
            )
        )

        button.click()


    def verify_cart_empty(self):

        WebDriverWait(
            self.driver,
            10
        ).until(
            EC.visibility_of_element_located(
                self.empty_cart_text
            )
        )

        assert "Cart is empty" in self.driver.page_source
    