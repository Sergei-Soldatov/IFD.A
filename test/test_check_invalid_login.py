# -*- coding: utf-8 -*-

def test_check_invalid_login(app):
    app.session.enter_login(username="qwerty")
    app.session.enter_password(password="1245")
    app.session.logout()
