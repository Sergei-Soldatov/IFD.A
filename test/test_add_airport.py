# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_airport_by_IATA(app):
    app.session.enter_login(username="test")
    app.session.enter_password(password="1245")
    app.open_form_add_airport()
    app.enter_IATA_code(iata_cod="LED")
    app.select_airport_by_IATA_code()
    app.session.logout()

