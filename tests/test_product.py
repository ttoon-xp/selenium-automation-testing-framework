from pages.product_page import ProductPage


# Test Case: TC-014
# Search product by keyword


def test_search_product(driver):


    driver.get(
        "https://automationexercise.com/products"
    )

    driver.maximize_window()


    product = ProductPage(driver)


    product.enter_search("dress")

    product.click_search()


    product.verify_search_result()
