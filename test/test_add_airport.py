# -*- coding: utf-8 -*-


def test_add_airport_by_IATA(app):
    app.session.enter_login(username="test")
    app.session.enter_password(password="1245")
    app.airport.open_form_add_airport()
    app.airport.enter_IATA_code(iata_cod="LED")
    app.airport.select_airport_by_IATA_code()
    app.session.logout()

