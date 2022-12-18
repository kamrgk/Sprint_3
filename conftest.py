import random
import string

url_host = 'https://stellarburgers.nomoreparties.site'
url_registration_path = '/register'
url_login_path = '/login'
url_forgot_password_path = '/forgot-password'
url_profile_path = '/profile'

response_timeout_s = 5

test_account_name = 'Камилла'
test_account_email = 'kamillarakhmatulina1000@yandex.ru'
test_account_password = '123456'

# генерирует рандомный email в формете имя_фамилия_номер когорты_любые 3 цифры@домен. Например, testtestov1999@yandex.ru
def generate_test_email():
    numbers_for_random = '0123456789'

    name = "kamilla"
    surname = "rakhmatulina"
    kogorta = "1"
    random_numbers = ''.join(random.choices(numbers_for_random, k=3))
    random_domen = ''.join(random.choices(string.ascii_lowercase, k=3))

    result = name + surname + kogorta + random_numbers + "@" + random_domen + ".ru"
    return result
