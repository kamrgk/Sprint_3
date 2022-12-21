import conftest as fixtures
import selenium_locators as locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time


def login(driver):
    session_account_email = fixtures.test_account_email

    # на главной - авторизуемся через Войти в аккаунт
    driver.get(fixtures.url_host)

    WebDriverWait(driver, fixtures.response_timeout_s).until(
        expected_conditions.element_to_be_clickable((By.XPATH, locators.into_account_button))
    )

    driver.find_element(By.XPATH, locators.into_account_button).click()

    WebDriverWait(driver, fixtures.response_timeout_s).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.login_header))
    )

    # вводим логин и пароль
    driver.find_element(By.XPATH, locators.registration_email_input).send_keys(session_account_email)
    driver.find_element(By.XPATH, locators.registration_password_input).send_keys(fixtures.test_account_password)

    driver.find_element(By.XPATH, locators.login_button).click()

    assert fixtures.url_host in driver.current_url

    WebDriverWait(driver, fixtures.response_timeout_s).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.profile_p))
    )


def test_transition(driver):
    login(driver)

    # ждем, что отобразятся ингридиенты
    WebDriverWait(driver, fixtures.response_timeout_s).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.burger_ingredient_a))
    )

    # тапем на Начинки и ждем, чтобы стал виден их тайтл
    driver.find_element(By.XPATH, locators.toppings_span).click()
    WebDriverWait(driver, fixtures.response_timeout_s).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.toppings_title))
    )

    # тапем на Соусы и ждем, чтобы стал виден их тайтл
    time.sleep(3)
    driver.find_element(By.XPATH, locators.sauces_span).click()
    WebDriverWait(driver, fixtures.response_timeout_s).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.sauces_title))
    )

    # тапем на Булки и ждем, чтобы стал виден их тайтл
    time.sleep(3)
    driver.find_element(By.XPATH, locators.rolls_span).click()
    WebDriverWait(driver, fixtures.response_timeout_s).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.rolls_title))
    )

    driver.quit()
