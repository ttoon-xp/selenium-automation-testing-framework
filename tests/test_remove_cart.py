from pages.cart_page import CartPage


# Test Case: TC-019
# Remove product from cart


def test_remove_product_from_cart(driver):


    driver.get(
        "https://automationexercise.com/products"
    )

    driver.maximize_window()


    cart = CartPage(driver)


    # Add product first
    cart.click_add_to_cart()


    # Go to cart
    cart.click_view_cart()


    # Remove product
    cart.remove_product()


    # Verify cart empty
    assert "Cart is empty!" in driver.page_source
