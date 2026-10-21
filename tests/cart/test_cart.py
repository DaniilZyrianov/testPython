from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_tests.locators.saucedemo_locators import SauceDemoInventoryPage

def test_cart_cleanup(logged_in_driver):
    """Сценарий: Очистка корзины."""
    driver = logged_in_driver
    wait = WebDriverWait(driver, 10)

    # Добавляем товар
    wait.until(EC.element_to_be_clickable(SauceDemoInventoryPage.ADD_TO_CART_BACKPACK)).click()
    
    # Переходим в корзину
    driver.find_element(*SauceDemoInventoryPage.SHOPPING_CART_LINK).click()
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart_list")))

    # Удаляем товар
    driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
    
    # Проверяем, что корзина пуста
    assert len(driver.find_elements(By.CLASS_NAME, "cart_item")) == 0