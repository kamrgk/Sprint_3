from selenium import webdriver
import conftest as fixtures
import selenium_locators as locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class LoginTest:
    def prepare_driver(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.session_account_email = fixtures.test_account_email  # используем фиксированный аккаунт

    def do_after(self):
        self.driver.quit()

    # вход по кнопке «Войти в аккаунт» на главной
    def login_from_main_page(self):
        self.prepare_driver()

        self.driver.get(fixtures.url_host)

        WebDriverWait(self.driver, fixtures.response_timeout_s).until(
            expected_conditions.element_to_be_clickable((By.XPATH, locators.into_account_button))
        )

        self.driver.find_element(By.XPATH, locators.into_account_button).click()
        self.auth_on_login_screen()

        self.do_after()

    # вход через кнопку «Личный кабинет»
    def login_from_profile(self):
        self.prepare_driver()

        self.driver.get(fixtures.url_host)

        WebDriverWait(self.driver, fixtures.response_timeout_s).until(
            expected_conditions.element_to_be_clickable((By.XPATH, locators.profile_p))
        )

        self.driver.find_element(By.XPATH, locators.profile_p).click()
        self.auth_on_login_screen()

        self.do_after()

    # вход через кнопку в форме регистрации
    def from_registration_screen(self):
        self.prepare_driver()

        self.driver.get(fixtures.url_host + fixtures.url_registration_path)

        WebDriverWait(self.driver, fixtures.response_timeout_s).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locators.registration_link_login))
        )

        login_link = self.driver.find_element(By.XPATH, locators.registration_link_login)
        self.driver.execute_script("arguments[0].scrollIntoView();", login_link)
        login_link.click()

        self.auth_on_login_screen()

        self.do_after()

    # вход через кнопку в форме восстановления пароля.
    def from_restore_password(self):
        self.prepare_driver()

        self.driver.get(fixtures.url_host + fixtures.url_forgot_password_path)

        WebDriverWait(self.driver, fixtures.response_timeout_s).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locators.registration_link_login))
        )

        self.driver.find_element(By.XPATH, locators.registration_link_login).click()
        self.auth_on_login_screen()

        self.do_after()

    def auth_on_login_screen(self):
        assert fixtures.url_login_path in self.driver.current_url

        WebDriverWait(self.driver, fixtures.response_timeout_s).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locators.login_header))
        )

        self.driver.find_element(By.XPATH, locators.registration_email_input).send_keys(self.session_account_email)
        self.driver.find_element(By.XPATH, locators.registration_password_input).send_keys(
            fixtures.test_account_password)

        self.driver.find_element(By.XPATH, locators.login_button).click()

        assert fixtures.url_host in self.driver.current_url

        WebDriverWait(self.driver, fixtures.response_timeout_s).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locators.order_text_button))
        )
