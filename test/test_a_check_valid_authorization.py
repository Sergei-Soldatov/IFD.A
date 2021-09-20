# -*- coding: utf-8 -*-

# IFD.A-223 :: Версия: 1 :: Проверка входа в программу (невалидное значение пароля)
# def test_check_invalid_password(app):
#     app.session.enter_login(username="test")
#     app.session.enter_password(password="6789")
#     app.session.logout()


# IFD.A-221 :: Версия: 1 :: Проверка входа в программу (валидные значения логина и пароля)
def test_check_valid_authorization(app):
    app.session.enter_login(username="test")
    app.session.enter_password(password="1245")
    app.session.logout()


# IFD.A-222 :: Версия: 1 :: Проверка входа в программу (невалидное значение логина)
# def test_check_invalid_login(app):
#     app.session.enter_login(username="qwerty")
#     app.session.enter_password(password="1245")
#     app.session.logout()



