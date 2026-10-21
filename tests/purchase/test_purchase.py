from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_tests.locators.saucedemo_locators import SauceDemoInventoryPage

def test_successful_purchase(logged_in_driver):
    """Сценарий: Успешная покупка."""
    driver = logged_in_driver
    wait = WebDriverWait(driver, 10)

    # Добавляем товар
    wait.until(EC.element_to_be_clickable(SauceDemoInventoryPage.ADD_TO_CART_BACKPACK)).click()
    
    # Переходим в корзину
    driver.find_element(*SauceDemoInventoryPage.SHOPPING_CART_LINK).click()
    
    # Оформляем заказ
    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()
    
    # Заполняем форму
    wait.until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys("Ivan")
    driver.find_element(By.ID, "last-name").send_keys("Ivanov")
    driver.find_element(By.ID, "postal-code").send_keys("123456")
    driver.find_element(By.ID, "continue").click()
    
    # Завершаем
    wait.until(EC.element_to_be_clickable((By.ID, "finish"))).click()
    
    # Проверяем
    finish_header = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "complete-header")))
    assert "Thank you for your order" in finish_header.text