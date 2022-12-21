import conftest as fixtures
import selenium_locators as locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def open_profile(driver, session_account_email):
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

    # кликаем на профиль
    driver.find_element(By.XPATH, locators.profile_p).click()

    WebDriverWait(driver, fixtures.response_timeout_s).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.profile_link))
    )

    assert fixtures.url_profile_path in driver.current_url


# авторизация и переход по клику на «Личный кабинет»
def test_login_and_open_profile(driver):
    open_profile(driver=driver, session_account_email=fixtures.test_account_email)
    driver.quit()


# авторизация, переход по клику на «Личный кабинет» и переход в конструктор по тапу на Конструктор
def test_open_constructor_from_profile(driver):
    open_profile(driver=driver, session_account_email=fixtures.test_account_email)

    # клик по Конструктор
    driver.find_element(By.XPATH, locators.constructor_p).click()

    # открыт конструктор
    WebDriverWait(driver, fixtures.response_timeout_s).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.create_burger_h1))
    )

    driver.quit()


# авторизация, переход по клику на «Личный кабинет» и переход в конструктор по тапу на Лого
def test_open_constructor_by_logo(driver):
    open_profile(driver=driver, session_account_email=fixtures.test_account_email)

    # клик по лого
    driver.find_element(By.XPATH, locators.logo_div).click()

    # открыт конструктор
    WebDriverWait(driver, fixtures.response_timeout_s).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.create_burger_h1))
    )

    driver.quit()


 # авторизация и выход из аккаунта в личном кабинете
def test_login_and_logout(driver):
    open_profile(driver=driver, session_account_email=fixtures.test_account_email)

    driver.find_element(By.XPATH, locators.exit_button).click()

    WebDriverWait(driver, fixtures.response_timeout_s).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.login_header))
    )

    driver.quit()
