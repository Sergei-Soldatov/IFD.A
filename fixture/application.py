# -*- coding: utf-8 -*-
from fixture.session import SessionHelper
from selenium import webdriver
from fixture.airport import AirportHelper
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(10)
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

    def destroy(self):
        self.wd.quit()