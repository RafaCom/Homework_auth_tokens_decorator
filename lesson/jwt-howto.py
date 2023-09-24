import calendar
import datetime

import jwt  # pip3 install pyjwt

secret = 's3cR$eT'
algo = 'HS256'


# Создание токена
def generate_token(data):
    # Время жизни токена
    min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    # сохраняем время жизни токена в информацию, которую будем кодировать
    data["exp"] = calendar.timegm(min30.timetuple())  # формат: кол-во секунд с 70-ого года

    return jwt.encode(data, secret, algorithm=algo)


# Проверка токена
def check_token(token):
    try:
        jwt.decode(token, secret, algorithms=[algo])
        return True
    except Exception as e:
        print(e)
        return False


if __name__ == '__main__':
    data_user = {
        'username': 'myname',
        'role': 'user'
    }
    token_user = generate_token(data_user)
    is_ok = check_token(token_user)

    print(token_user)
    print(is_ok)
