import conftest as fixtures
import selenium_locators as locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def auth_on_login_screen(driver, session_account_email):
    assert fixtures.url_login_path in driver.current_url

    WebDriverWait(driver, fixtures.response_timeout_s).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.login_header))
    )

    driver.find_element(By.XPATH, locators.registration_email_input).send_keys(session_account_email)
    driver.find_element(By.XPATH, locators.registration_password_input).send_keys(fixtures.test_account_password)

    driver.find_element(By.XPATH, locators.login_button).click()

    assert fixtures.url_host in driver.current_url

    WebDriverWait(driver, fixtures.response_timeout_s).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.order_text_button))
    )


# вход по кнопке «Войти в аккаунт» на главной
def test_login_from_main_page(driver):
    driver.get(fixtures.url_host)

    WebDriverWait(driver, fixtures.response_timeout_s).until(
        expected_conditions.element_to_be_clickable((By.XPATH, locators.into_account_button))
    )

    driver.find_element(By.XPATH, locators.into_account_button).click()
    auth_on_login_screen(driver=driver,session_account_email=fixtures.test_account_email)

    driver.quit()


# вход через кнопку «Личный кабинет»
def test_login_from_profile(driver):
    driver.get(fixtures.url_host)

    WebDriverWait(driver, fixtures.response_timeout_s).until(
        expected_conditions.element_to_be_clickable((By.XPATH, locators.profile_p))
    )

    driver.find_element(By.XPATH, locators.profile_p).click()
    auth_on_login_screen(driver=driver, session_account_email=fixtures.test_account_email)

    driver.quit()


# вход через кнопку в форме регистрации
def test_from_registration_screen(driver):
    driver.get(fixtures.url_host + fixtures.url_registration_path)

    WebDriverWait(driver, fixtures.response_timeout_s).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.registration_link_login))
    )

    login_link = driver.find_element(By.XPATH, locators.registration_link_login)
    driver.execute_script("arguments[0].scrollIntoView();", login_link)
    login_link.click()

    auth_on_login_screen(driver=driver, session_account_email=fixtures.test_account_email)

    driver.quit()


# вход через кнопку в форме восстановления пароля.
def test_from_restore_password(driver):
    driver.get(fixtures.url_host + fixtures.url_forgot_password_path)

    WebDriverWait(driver, fixtures.response_timeout_s).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.registration_link_login))
    )

    driver.find_element(By.XPATH, locators.registration_link_login).click()
    auth_on_login_screen(driver=driver, session_account_email=fixtures.test_account_email)

    driver.quit()
