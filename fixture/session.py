# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class SessionHelper:
    def __init__(self, app):
        self.app = app

    def enter_login(self, username):
        wd = self.app.wd
        self.app.open_home_page()
        # Ввод логина
        wd.find_element_by_xpath("//form[@id='login-card']/div[2]/label/div/div/div/input").click()
        wd.find_element_by_xpath("//form[@id='login-card']/div[2]/label/div/div/div/input").clear()
        wd.find_element_by_xpath("//form[@id='login-card']/div[2]/label/div/div/div/input").send_keys(username)

    def enter_password(self, password):
        wd = self.app.wd
        # Ввод пароля
        wd.find_element_by_xpath("//form[@id='login-card']/div[2]/label[2]/div/div/div/input").click()
        wd.find_element_by_xpath("//form[@id='login-card']/div[2]/label[2]/div/div/div/input").clear()
        wd.find_element_by_xpath("//form[@id='login-card']/div[2]/label[2]/div/div/div/input").send_keys(password)
        self.confurm_login_and_password()

    def confurm_login_and_password(self):
        wd = self.app.wd
        # Валидация логина и пароля (кнопка "Войти")
        wd.find_element_by_xpath("//form[@id='login-card']/div[3]/button/span[2]/span/span").click()


    def logout(self):
        wd = self.app.wd
        WebDriverWait(wd, 2).until(EC.invisibility_of_element((By.XPATH, "//div[@class='q-dialog__backdrop fixed-full q-transition--fade-leave-active q-transition--fade-leave-to']")))
        WebDriverWait(wd, 2).until(
            EC.element_to_be_clickable((By.XPATH, "//i[@class='mdi mdi-exit-to-app q-icon notranslate']"))).click()

