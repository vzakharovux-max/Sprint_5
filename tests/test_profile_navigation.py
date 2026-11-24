from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data import ExistingUser
from locators import LoginPageLocators, MainPageLocators, ProfilePageLocators
from urls import Urls


class TestProfileNavigation:
    def _login(self, driver):
        driver.get(Urls.LOGIN_URL)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT))
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(ExistingUser.EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(ExistingUser.PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))

    def test_navigate_to_personal_account(self, driver):
        self._login(driver)
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(ProfilePageLocators.PROFILE_LINK))
        assert driver.current_url == Urls.PROFILE_URL

    def test_navigate_from_profile_to_constructor(self, driver):
        self._login(driver)
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(ProfilePageLocators.PROFILE_LINK))

        driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()
        order_btn = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        )
        assert order_btn.is_displayed()

    def test_navigate_from_profile_via_logo(self, driver):
        self._login(driver)
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(ProfilePageLocators.PROFILE_LINK))

        driver.find_element(*MainPageLocators.LOGO_BUTTON).click()
        order_btn = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        )
        assert order_btn.is_displayed()

    def test_logout_from_personal_account(self, driver):
        self._login(driver)
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        logout_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ProfilePageLocators.LOGOUT_BUTTON)
        )
        logout_btn.click()

        WebDriverWait(driver, 10).until(EC.url_to_be(Urls.LOGIN_URL))
        assert driver.current_url == Urls.LOGIN_URL




