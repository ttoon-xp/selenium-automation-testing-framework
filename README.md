# Selenium Automation Testing Framework

Automation Testing Project using Selenium WebDriver and Pytest.

## Tech Stack

- Python
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- Pytest HTML Report


## Test Cases

| Test Case | Description | Result |
|---|---|---|
| Login Test | Login with valid credentials | Passed |
| Register Test | Register new user | Passed |
| Search Product Test | Search product by keyword | Passed |
| Add Cart Test | Add product to cart | Passed |
| Remove Cart Test | Remove product from cart | Passed |


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

Run Test

Run all tests: pytest