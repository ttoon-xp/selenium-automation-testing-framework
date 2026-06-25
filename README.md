# Selenium Automation Testing Framework

Automation Testing Project using Selenium WebDriver and Pytest.

## Tech Stack

- Python
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- Pytest HTML Report


## Test Cases

## Test Cases

| Test Case | Description |
|---|---|
| Login Test | Verify user can login successfully with valid email and password credentials |
| Register Test | Verify new user can create an account by filling registration information and completing account creation process |
| Search Product Test | Verify user can search products using keyword and system displays related product results correctly |
| Add Cart Test | Verify user can add a product to shopping cart and product information is displayed correctly in the cart |
| Remove Cart Test | Verify user can remove a product from shopping cart and cart status is updated to empty successfully |


## Project Structure

```text
selenium-testing

├── pages
│   ├── login_page.py
│   ├── product_page.py
│   ├── cart_page.py
│   └── register_page.py
│
├── tests
│   ├── test_login.py
│   ├── test_product.py
│   ├── test_cart.py
│   ├── test_register.py
│   └── test_remove_cart.py
│
├── conftest.py
├── test_data.py
├── requirements.txt
└── report.html
```

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run Test

Run all tests:

```bash
pytest
```

Generate HTML Report:

```bash
pytest --html=report.html
```

