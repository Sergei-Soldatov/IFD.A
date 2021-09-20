# -*- coding: utf-8 -*-

# IFD.A-1 :: Версия: 1 :: Открытие формы "Добавить аэропорт" (русская локаль)
# IFD.A-2 :: Версия: 1 :: Закрытие формы "Добавить аэропорт"
def test_add_airport_form_rus(app):
    app.session.enter_login(username="test")
    app.session.enter_password(password="1245")
    app.airport.open_form_add_airport()
    app.airport.exit_from_the_add_airport_form()
    app.session.logout()