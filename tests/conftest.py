import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Импортируем локаторы из ПР6
from selenium_tests.locators.saucedemo_locators import SauceDemoLoginPage, SauceDemoInventoryPage

@pytest.fixture
def driver():
    """Фикстура для запуска и закрытия браузера."""
    # Если ChromeDriver не в PATH, укажите путь: webdriver.Chrome(executable_path='путь/к/chromedriver.exe')
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def logged_in_driver(driver):
    """Фикстура для авторизации на сайте."""
    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 10)
    
    wait.until(EC.presence_of_element_located(SauceDemoLoginPage.USERNAME_FIELD)).send_keys("standard_user")
    driver.find_element(*SauceDemoLoginPage.PASSWORD_FIELD).send_keys("secret_sauce")
    driver.find_element(*SauceDemoLoginPage.LOGIN_BUTTON).click()
    
    # Ждем загрузки страницы товаров
    wait.until(EC.presence_of_element_located(SauceDemoInventoryPage.PAGE_TITLE))
    return driver