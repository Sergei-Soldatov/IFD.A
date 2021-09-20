# -*- coding: utf-8 -*-

#IFD.A-4 :: Версия: 1 :: Выход из расширенной формы "Добавить аэропорт"
def test_exit_extended_form_add_airport(app):
    app.session.enter_login(username="test")
    app.session.enter_password(password="1245")
    app.airport.open_form_add_airport()
    app.airport.enter_IATA_code(iata_cod="LED")
    app.airport.search_airport_by_parameter()
    app.airport.activat_checkbox_for_airport()
    app.airport.exit_from_the_add_airport_form()
    app.session.logout()
