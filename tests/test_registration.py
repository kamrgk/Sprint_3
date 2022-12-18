from selenium import webdriver
import conftest as fixtures
import selenium_locators as locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class RegistrationAccountTest:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.session_account_email = fixtures.generate_test_email()

        self.registration_success()

    def registration_success(self):
        self.driver.get(fixtures.url_host + fixtures.url_registration_path)

        WebDriverWait(self.driver, fixtures.response_timeout_s).until(
            expected_conditions.element_to_be_clickable((By.XPATH, locators.registration_button))
        )

        self.driver.find_element(By.XPATH, locators.registration_name_input).send_keys(fixtures.test_account_name)
        self.driver.find_element(By.XPATH, locators.registration_email_input).send_keys(self.session_account_email)
        self.driver.find_element(By.XPATH, locators.registration_password_input).send_keys(
            fixtures.test_account_password)

        self.driver.find_element(By.XPATH, locators.registration_button).click()

        WebDriverWait(self.driver, fixtures.response_timeout_s).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locators.login_header))
        )

        assert fixtures.url_login_path in self.driver.current_url

        self.driver.quit()
