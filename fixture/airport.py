from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
#from fixture.application import Application


class AirportHelper:
    def __init__(self, app):
        self.app = app


    def waiting_before_closing_form(self):
        wd = self.app.wd
        # Ожидание перед закрытием формы "Добавить аэропорт"
        WebDriverWait(wd, 7).until(
            EC.invisibility_of_element((By.XPATH, "//div[@class='q-dialog__backdrop fixed-full']")))
        WebDriverWait(wd, 7).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='q-btn__content text-center col items-center q-anchor--skip justify-center row']"))).click()

    # def waiting_before_closing_form(self):
    #     # Ожидание перед закрытием формы "Добавить аэропорт"
    #     WebDriverWait(wd, 7).until(EC.invisibility_of_element((By.XPATH, "//span[@class='q-ripple']")))
    #     WebDriverWait(wd, 7).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='q-btn__content text-center col items-center q-anchor--skip justify-center row']"))).click()

    def exit_from_the_add_airport_form(self):
        wd = self.app.wd
        # Закрытие формы "Добавить аэропорт". Кнопка "Х"
        wd.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='очистить'])[1]/following::span[1]").click()

    def сlicking_the_сlear_button(self):
        wd = self.app.wd
        # Очистка заполненной формы "Добавить аэропорт" (кнопка "Очистить"). Переход в нерасширенную форму
        wd.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Добавить аэропорт'])[1]/following::span[3]").click()

    def activat_first_checkbox_to_select_airport(self):
        wd = self.app.wd
        # Выбор первого аэропорта из отобразившегося списка чекбоксов аэропортов
        wd.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Выберите аэропорт'])[1]/following::*[name()='svg'][1]").click()

    # def select_town_from_displayed_list(self):
    #     # Из отобразившегося выбрать значение "Санкт-Петербург"
    #     wd.find_element_by_xpath("//div[@id='qvs_22']/div/div[2]/div").click()

    def selection_town_for_form_adding_airport(self):
        wd = self.app.wd
        # Клик по полю "Город" и ввод значения "Санкт"
        wd.find_element_by_xpath("//div[3]/div[2]/div/div[2]/div/label/div/div/div/div/input").click()
        wd.find_element_by_xpath("//div[3]/div[2]/div/div[2]/div[2]/label/div/div/div/div/input").click()
        wd.find_element_by_xpath("//div[3]/div[2]/div/div[2]/div[2]/label/div/div/div/div/input").clear()
        wd.find_element_by_xpath("//div[3]/div[2]/div/div[2]/div[2]/label/div/div/div/div/input").send_keys(
            u"Санкт-петербург")
        # wd.find_element_by_xpath("//div[@id='qvs_36']/div[14]/div[2]/div").click()
        # wd.find_element_by_xpath(u"//*/text()[normalize-space(.)='санкт-петербург']/parent::*").click()
        # wd.find_element_by_xpath("//div[3]/div[2]/div/div[2]/div[2]/label/div/div/div/div/input").send_keys('\ue007')
        # wd.find_element_by_id("login-card").submit()

    # def select_country_from_displayed_list(self):
    #     wd = self.app.wd
    #     # Из отобразившегося списка выбрать значение "Российская Федерация"
    #     wd.find_element_by_xpath("//div[@id='qvs_21']/div/div[2]/div").click()

    def selection_country_for_form_adding_airport(self):
        wd = self.app.wd
        # Клик по полю "Страна" и ввод значения "Российская федерация"
        wd.find_element_by_xpath("//div[3]/div[2]/div/div[2]/div/label/div/div/div/div/input").click()
        wd.find_element_by_xpath("//div[3]/div[2]/div/div[2]/div/label/div/div/div/div/input").clear()
        wd.find_element_by_xpath("//div[3]/div[2]/div/div[2]/div/label/div/div/div/div/input").send_keys(
            u"Российская федерация")
        wd.find_element_by_xpath("//div[3]/div[2]/div/div[2]/div/label/div/div/div/div/input").send_keys('\ue007')
        # wd.find_element_by_id("login-card").submit()




    def adding_found_airport(self):
        wd = self.app.wd
        # Добавление найденного аэропорта (кнопка "Добавить")
        wd.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Назад'])[1]/following::span[4]").click()

    def activat_checkbox_for_airport(self):
        wd = self.app.wd
        # Активация чекбокса найденного аэропорта (поле "Выберите аэропорт")
        wd.find_element_by_css_selector("svg.q-checkbox__svg.fit.absolute-full").click()

    def search_airport_by_parameter(self):
        wd = self.app.wd
        # Поиск аэропорта по введенным параметрам (кнопка "Поиск")
        wd.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Код ИАТА'])[1]/following::span[4]").click()

    def select_airport_by_IATA_code(self):
        wd = self.app.wd
        self.search_airport_by_parameter()
        self.activat_checkbox_for_airport()
        self.adding_found_airport()

    def enter_IATA_code(self, iata_cod):
        wd = self.app.wd
        # Ввод кода ИАТА в поле "Код ИАТА" в форме "Добавить аэропорт"
        wd.find_element_by_xpath("//div[4]/label/div/div/div/input").click()
        wd.find_element_by_xpath("//div[4]/label/div/div/div/input").send_keys(iata_cod)

    def open_form_add_airport(self):
        wd = self.app.wd
        self.app.open_sandwich_menu()
        self.airport_module_selection()
        self.open_tab_airport()
        # Открытие формы "Добавить Аэропорт" (кнопка "+Добавить")
        wd.find_element_by_xpath("//div[@id='q-app']/div/div[2]/div/div[2]/div[2]/div/button/span[2]/span").click()

    def open_tab_airport(self):
        wd = self.app.wd
        # Открытие вкладки "Аэропорты"
        wd.find_element_by_xpath("//div[@id='q-app']/div/div[2]/div/div/div/div/div/div/div[2]").click()

    def airport_module_selection(self):
        wd = self.app.wd
        # Выбор модуля "Справочники/Аэропорты"
        wd.find_element_by_xpath("//div[@id='q-app']/div/div/aside/div/div[2]/div[3]/div[3]/span").click()
