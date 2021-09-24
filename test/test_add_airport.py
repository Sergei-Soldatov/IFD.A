# -*- coding: utf-8 -*-
import pytest
import allure

# IFD.A-15 :: Версия: 1 :: Переход в расширенную форму "Добавить аэропорт", при выборе кода ИАТА
# def test_add_airport_by_IATA(app):
#     app.session.enter_login(username="test")
#     app.session.enter_password(password="1245")
#     app.airport.open_form_add_airport()
#     app.airport.enter_IATA_code(iata_cod="LED")
#     app.airport.select_airport_by_IATA_code()
#     app.session.logout()

def test_add_airport_by_IATA(app):
    with allure.step('Given login and password'):
        app.session.enter_login(username="test")
        app.session.enter_password(password="1245")
    with allure.step('When I opened the form to add an airport'):
        app.airport.open_form_add_airport()
    with allure.step('Then I entered a valid IATA code for the airport and the "Search" button was displayed. And when the checkbox is activated, the "Add" button'):
        app.airport.enter_IATA_code(iata_cod="LED")
        app.airport.select_airport_by_IATA_code()
        app.session.logout()
