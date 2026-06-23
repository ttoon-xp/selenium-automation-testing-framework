from pages.cart_page import CartPage


# TC016 Add product to cart


def test_add_product_to_cart(driver):


    driver.get(
        "https://automationexercise.com/products"
    )

    driver.maximize_window()


    cart = CartPage(driver)


    cart.click_add_to_cart()

    cart.verify_product_added()
