import conftest as fixtures
import selenium_locators as locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_registration_success(driver):
    session_account_email = fixtures.generate_test_email()
    driver.get(fixtures.url_host + fixtures.url_registration_path)

    WebDriverWait(driver, fixtures.response_timeout_s).until(
        expected_conditions.element_to_be_clickable((By.XPATH, locators.registration_button))
    )

    driver.find_element(By.XPATH, locators.registration_name_input).send_keys(fixtures.test_account_name)
    driver.find_element(By.XPATH, locators.registration_email_input).send_keys(session_account_email)
    driver.find_element(By.XPATH, locators.registration_password_input).send_keys(
        fixtures.test_account_password)

    driver.find_element(By.XPATH, locators.registration_button).click()

    WebDriverWait(driver, fixtures.response_timeout_s).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locators.login_header))
    )

    assert fixtures.url_login_path in driver.current_url

    driver.quit()
