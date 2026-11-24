from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from helpers import generate_registration_data
from locators import LoginPageLocators, RegisterPageLocators
from urls import Urls


class TestRegistration:
    def test_successful_registration(self, driver):
        name, email, password = generate_registration_data()
        driver.get(Urls.REGISTER_URL)

        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(name)
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginPageLocators.LOGIN_HEADER))
        assert driver.current_url == Urls.LOGIN_URL

    def test_registration_short_password_error(self, driver):
        name, email, _ = generate_registration_data()
        driver.get(Urls.REGISTER_URL)

        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(name)
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys("12345")
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

        error_element = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(RegisterPageLocators.PASSWORD_ERROR_TEXT)
        )
        assert error_element.text == "Некорректный пароль"
