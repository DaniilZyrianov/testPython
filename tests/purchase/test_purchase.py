import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_tests.locators.saucedemo_locators import SauceDemoInventoryPage

@allure.suite("Покупка")
class TestPurchase:
    @allure.title("Успешная покупка товара")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.label("layer", "UI")
    def test_successful_purchase(self, logged_in_driver):
        driver = logged_in_driver
        wait = WebDriverWait(driver, 10)

        with allure.step("Добавить товар в корзину"):
            wait.until(EC.element_to_be_clickable(SauceDemoInventoryPage.ADD_TO_CART_BACKPACK)).click()

        with allure.step("Перейти в корзину и начать оформление"):
            driver.find_element(*SauceDemoInventoryPage.SHOPPING_CART_LINK).click()
            wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

        with allure.step("Заполнить данные покупателя"):
            wait.until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys("Ivan")
            driver.find_element(By.ID, "last-name").send_keys("Ivanov")
            driver.find_element(By.ID, "postal-code").send_keys("123456")
            driver.find_element(By.ID, "continue").click()

        with allure.step("Завершить покупку"):
            wait.until(EC.element_to_be_clickable((By.ID, "finish"))).click()

        with allure.step("Проверить успешное завершение"):
            finish_header = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "complete-header")))
            assert "Thank you for your order" in finish_header.text