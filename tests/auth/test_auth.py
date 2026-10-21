from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_tests.locators.saucedemo_locators import SauceDemoLoginPage

def test_negative_login(driver):
    """Сценарий: Неуспешная авторизация."""
    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 10)

    driver.find_element(*SauceDemoLoginPage.USERNAME_FIELD).send_keys("wrong_user")
    driver.find_element(*SauceDemoLoginPage.PASSWORD_FIELD).send_keys("wrong_pass")
    driver.find_element(*SauceDemoLoginPage.LOGIN_BUTTON).click()

    error_message = wait.until(EC.presence_of_element_located(SauceDemoLoginPage.ERROR_MESSAGE))
    assert "Username and password do not match" in error_message.text