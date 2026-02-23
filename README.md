# Selenium UI Test Suite 🔬

Automated UI test suite for web applications using **Python**, **Selenium WebDriver**, and **pytest**, following the **Page Object Model (POM)** design pattern.

## 🧪 What's Being Tested

Target site: [SauceDemo](https://www.saucedemo.com) — a purpose-built QA practice application.

Test coverage includes:
- ✅ User login (valid and invalid credentials)
- ✅ Product search and filtering
- ✅ Add to cart / remove from cart
- ✅ Checkout flow (complete purchase)
- ✅ Logout functionality
- ✅ Error message validation
- ✅ UI element visibility checks

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.x | Programming language |
| Selenium WebDriver | Browser automation |
| pytest | Test framework |
| pytest-html | HTML test reports |
| webdriver-manager | Auto-manage ChromeDriver |

## 📁 Project Structure

```
selenium-ui-test-suite/
│
├── pages/                  # Page Object Model classes
│   ├── __init__.py
│   ├── base_page.py        # Base class with common methods
│   ├── login_page.py       # Login page interactions
│   ├── home_page.py        # Home/inventory page
│   └── checkout_page.py    # Checkout flow
│
├── tests/                  # Test files
│   ├── __init__.py
│   ├── test_login.py       # Login test cases
│   ├── test_cart.py        # Shopping cart tests
│   └── test_checkout.py    # End-to-end checkout tests
│
├── reports/                # Auto-generated HTML test reports
├── conftest.py             # pytest fixtures (browser setup/teardown)
├── requirements.txt        # Project dependencies
└── README.md
```

## ⚙️ Setup & Run

### 1. Clone the repo
```bash
git clone https://github.com/kavyah44/selenium-ui-test-suite.git
cd selenium-ui-test-suite
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run all tests
```bash
pytest tests/ -v
```

### 4. Run with HTML report
```bash
pytest tests/ -v --html=reports/report.html
```

## 📸 Sample Test Output

```
tests/test_login.py::test_valid_login PASSED
tests/test_login.py::test_invalid_password PASSED
tests/test_login.py::test_locked_out_user PASSED
tests/test_cart.py::test_add_item_to_cart PASSED
tests/test_cart.py::test_remove_item_from_cart PASSED
tests/test_checkout.py::test_complete_purchase PASSED
```

## 📌 Key Concepts Demonstrated

- **Page Object Model (POM)** — separates test logic from page interactions
- **Fixtures** — reusable browser setup/teardown via conftest.py
- **Explicit Waits** — reliable element interaction with WebDriverWait
- **Parametrize** — data-driven test cases with @pytest.mark.parametrize
