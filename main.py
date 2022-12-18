from tests.test_registration import RegistrationAccountTest
from tests.test_login import LoginTest
from tests.test_profile import ProfileTest
from tests.test_constructor import ConstructorTest

# тест успешной регистрации аккаунта
registrationAccountTest = RegistrationAccountTest()


# тесты успешной авторизации
loginTest = LoginTest()

loginTest.login_from_main_page()
loginTest.login_from_profile()
loginTest.from_registration_screen()
loginTest.from_restore_password()


# тесты Личного кабинета
profileTest = ProfileTest()

profileTest.login_and_open_profile()
profileTest.open_constructor_from_profile()
profileTest.open_constructor_by_logo()
profileTest.login_and_logout()


# переходы к разделам: Булки, Соусы,Начинки
constructorTest = ConstructorTest()
constructorTest.transitions_test()

