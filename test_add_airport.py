# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import unittest, time, re

class TestAddAirport(unittest.TestCase):
    def setUp(self):
#        self.wd = webdriver.Chrome()
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(5)

    def test_add_airport(self):
        wd = self.wd
        # Открытие домашней страницы и максимальное разворачивание окна
        wd.get("http://192.168.178.197/")
        wd.maximize_window()

        # Ввод логина
        wd.find_element_by_xpath("//form[@id='login-card']/div[2]/label/div/div/div/input").click()
        wd.find_element_by_xpath("//form[@id='login-card']/div[2]/label/div/div/div/input").clear()
        wd.find_element_by_xpath("//form[@id='login-card']/div[2]/label/div/div/div/input").send_keys("test")
        # Ввод пароля
        wd.find_element_by_xpath("//form[@id='login-card']/div[2]/label[2]/div/div/div/input").click()
        wd.find_element_by_xpath("//form[@id='login-card']/div[2]/label[2]/div/div/div/input").clear()
        wd.find_element_by_xpath("//form[@id='login-card']/div[2]/label[2]/div/div/div/input").send_keys("1245")
        # Валидация логина и пароля (кнопка "Войти")
        wd.find_element_by_xpath("//form[@id='login-card']/div[3]/button/span[2]/span/span").click()

        # Открытие сэндвич-меню выбора модулей
        wd.find_element_by_xpath("//div[@id='q-app']/div/header/div/button/span[2]/span/i").click()
        # Выбор модуля "Справочники/Аэропорты"
        wd.find_element_by_xpath("//div[@id='q-app']/div/div/aside/div/div[2]/div[3]/div[3]/span").click()
        # Открытие вкладки "Аэропорты"
        wd.find_element_by_xpath("//div[@id='q-app']/div/div[2]/div/div/div/div/div/div/div[2]").click()

        # Открытие формы "Добавить Аэропорт" (кнопка "+Добавить")
        wd.find_element_by_xpath("//div[@id='q-app']/div/div[2]/div/div[2]/div[2]/div/button/span[2]/span").click()

        # Ввод кода ИАТА
        wd.find_element_by_xpath("//div[4]/label/div/div/div/input").click()
        wd.find_element_by_xpath("//div[4]/label/div/div/div/input").send_keys("LED")

        # Поиск аэропорта по введенным параметрам (кнопка "Поиск")
        wd.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Код ИАТА'])[1]/following::span[4]").click()
        # Активация чекбокса найденного аэропорта (поле "Выберите аэропорт")
        wd.find_element_by_css_selector("svg.q-checkbox__svg.fit.absolute-full").click()
        # Добавление найденного аэропорта (кнопка "Добавить")
        wd.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Назад'])[1]/following::span[4]").click()

        # Выполнение logout (первый способ). В методе def setUp(self): "играем" со временем
        #element = wd.find_element_by_xpath("//div[@id='q-app']/div/header/div/div/div[2]/div[4]/button/span[2]/span/i")
        #wd.execute_script("arguments[0].click();", element)
        # Выполнение logout (второй способ). В методе def setUp(self): "играем" со временем
        #element = wd.find_element_by_xpath("//div[@id='q-app']/div/header/div/div/div[2]/div[4]/button/span[2]/span/i")
        #webdriver.ActionChains(wd).move_to_element(element).click(element).perform()

        # Выполнение logout (третий способ). В методе def setUp(self): "играем" со временем
        WebDriverWait(wd, 7).until(EC.invisibility_of_element((By.XPATH, "//div[@class='q-dialog__backdrop fixed-full q-transition--fade-leave-active q-transition--fade-leave-to']")))
        WebDriverWait(wd, 7).until(EC.element_to_be_clickable((By.XPATH, "//i[@class='mdi mdi-exit-to-app q-icon notranslate']"))).click()

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
