from selenium import webdriver
import conftest as fixtures
import selenium_locators as locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ProfileTest:
    def prepare_driver(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.session_account_email = fixtures.test_account_email  # используем фиксированный аккаунт

    def do_after(self):
        self.driver.quit()

    # авторизация и переход по клику на «Личный кабинет»
    def login_and_open_profile(self):
        self.prepare_driver()
        self.open_profile()
        self.do_after()

    # авторизация, переход по клику на «Личный кабинет» и переход в конструктор по тапу на Конструктор
    def open_constructor_from_profile(self):
        self.prepare_driver()
        self.open_profile()

        # клик по Конструктор
        self.driver.find_element(By.XPATH, locators.constructor_p).click()

        # открыт конструктор
        WebDriverWait(self.driver, fixtures.response_timeout_s).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locators.create_burger_h1))
        )

        self.do_after()

    # авторизация, переход по клику на «Личный кабинет» и переход в конструктор по тапу на Лого
    def open_constructor_by_logo(self):
        self.prepare_driver()
        self.open_profile()

        # клик по лого
        self.driver.find_element(By.XPATH, locators.logo_div).click()

        # открыт конструктор
        WebDriverWait(self.driver, fixtures.response_timeout_s).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locators.create_burger_h1))
        )

        self.do_after()

    # авторизация и выход из аккаунта в личном кабинете
    def login_and_logout(self):
        self.prepare_driver()
        self.open_profile()

        self.driver.find_element(By.XPATH, locators.exit_button).click()

        WebDriverWait(self.driver, fixtures.response_timeout_s).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locators.login_header))
        )

        self.do_after()

    def open_profile(self):
        # на главной - авторизуемся через Войти в аккаунт
        self.driver.get(fixtures.url_host)

        WebDriverWait(self.driver, fixtures.response_timeout_s).until(
            expected_conditions.element_to_be_clickable((By.XPATH, locators.into_account_button))
        )

        self.driver.find_element(By.XPATH, locators.into_account_button).click()

        WebDriverWait(self.driver, fixtures.response_timeout_s).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locators.login_header))
        )

        # вводим логин и пароль
        self.driver.find_element(By.XPATH, locators.registration_email_input).send_keys(self.session_account_email)
        self.driver.find_element(By.XPATH, locators.registration_password_input).send_keys(
            fixtures.test_account_password)

        self.driver.find_element(By.XPATH, locators.login_button).click()

        assert fixtures.url_host in self.driver.current_url

        WebDriverWait(self.driver, fixtures.response_timeout_s).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locators.profile_p))
        )

        # кликаем на профиль
        self.driver.find_element(By.XPATH, locators.profile_p).click()

        WebDriverWait(self.driver, fixtures.response_timeout_s).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locators.profile_link))
        )

        assert fixtures.url_profile_path in self.driver.current_url
