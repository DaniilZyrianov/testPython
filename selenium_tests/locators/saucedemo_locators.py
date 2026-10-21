from selenium.webdriver.common.by import By


class SauceDemoLoginPage:
    """Локаторы для страницы авторизации."""

    USERNAME_FIELD = (By.CSS_SELECTOR, "#user-name")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login-button")
    ERROR_MESSAGE = (By.XPATH, "//h3[@data-test='error']")


class SauceDemoInventoryPage:
    """Локаторы для страницы товаров (после успешного логина)."""

    PAGE_TITLE = (By.CSS_SELECTOR, ".title")
    INVENTORY_ITEM = (By.CSS_SELECTOR, ".inventory_item")
    INVENTORY_ITEM_NAME = (By.CSS_SELECTOR, ".inventory_item_name")
    ADD_TO_CART_BACKPACK = (
        By.XPATH,
        "//button[@data-test='add-to-cart-sauce-labs-backpack']"
    )
    SHOPPING_CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")