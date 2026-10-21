import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_tests.locators.saucedemo_locators import SauceDemoLoginPage, SauceDemoInventoryPage

@pytest.fixture(scope="function")
def driver():
    """Фикстура для запуска и закрытия браузера."""
    options = Options()
    # options.add_argument("--headless")  # Раскомментируйте, если хотите запускать без окна
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    
    # Неявное ожидание: если элемент не найден сразу, Selenium подождет до 10 секунд
    driver.implicitly_wait(10) 
    
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def logged_in_driver(driver):
    """Фикстура для авторизации. Использует уже созданный driver."""
    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 10)
    
    # Ждем, пока поле логина станет кликабельным, и только потом вводим текст
    wait.until(EC.element_to_be_clickable(SauceDemoLoginPage.USERNAME_FIELD)).send_keys("standard_user")
    wait.until(EC.element_to_be_clickable(SauceDemoLoginPage.PASSWORD_FIELD)).send_keys("secret_sauce")
    wait.until(EC.element_to_be_clickable(SauceDemoLoginPage.LOGIN_BUTTON)).click()
    
    # Ждем загрузки страницы товаров (появления заголовка)
    wait.until(EC.presence_of_element_located(SauceDemoInventoryPage.PAGE_TITLE))
    return driver