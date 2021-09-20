# -*- coding: utf-8 -*-
from fixture.session import SessionHelper
from selenium import webdriver
from fixture.airport import AirportHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(2)
        self.session = SessionHelper(self)
        self.airport = AirportHelper(self)

    def open_sandwich_menu(self):
        wd = self.wd
        # Открытие сэндвич-меню выбора модулей
        wd.find_element_by_xpath("//div[@id='q-app']/div/header/div/button/span[2]/span/i").click()

    def open_home_page(self):
        wd = self.wd
        # Открытие домашней страницы и максимальное разворачивание окна
        wd.get("http://192.168.178.197/")
        wd.maximize_window()

    def open_mod_airport_page(self):
        wd = self.wd
        # Открытие страницы "Справочники | Аэропорты" и максимальное разворачивание окна
        wd.get("http://192.168.178.197/referenceBooks")
        wd.maximize_window()

    def destroy(self):
        self.wd.quit()