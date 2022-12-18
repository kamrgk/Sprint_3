from selenium import webdriver
import conftest as fixtures
import selenium_locators as locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time


class ConstructorTest:
    def prepare_driver(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.session_account_email = fixtures.test_account_email  # используем фиксированный аккаунт

    def do_after(self):
        self.driver.quit()

    # переходы к разделам: Булки, Соусы,Начинки
    def transitions_test(self):
        self.prepare_driver()
        self.login()

        # ждем, что отобразятся ингридиенты
        WebDriverWait(self.driver, fixtures.response_timeout_s).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locators.burger_ingredient_a))
        )

        # тапем на Начинки и ждем, чтобы стал виден их тайтл
        self.driver.find_element(By.XPATH, locators.toppings_span).click()
        WebDriverWait(self.driver, fixtures.response_timeout_s).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locators.toppings_title))
        )

        # тапем на Соусы и ждем, чтобы стал виден их тайтл
        time.sleep(3)
        self.driver.find_element(By.XPATH, locators.sauces_span).click()
        WebDriverWait(self.driver, fixtures.response_timeout_s).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locators.sauces_title))
        )

        # тапем на Булки и ждем, чтобы стал виден их тайтл
        time.sleep(3)
        self.driver.find_element(By.XPATH, locators.rolls_span).click()
        WebDriverWait(self.driver, fixtures.response_timeout_s).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locators.rolls_title))
        )

        self.do_after()

    def login(self):
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
