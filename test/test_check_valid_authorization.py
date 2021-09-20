# -*- coding: utf-8 -*-


def test_check_invalid_password(app):
    app.session.enter_login(username="test")
    app.session.enter_password(password="6789")
    app.session.logout()


def test_check_valid_authorization(app):
    app.session.enter_login(username="test")
    app.session.enter_password(password="1245")
    app.session.logout()


def test_check_invalid_login(app):
    app.session.enter_login(username="qwerty")
    app.session.enter_password(password="1245")
    app.session.logout()



