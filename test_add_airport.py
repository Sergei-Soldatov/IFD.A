# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest, time, re

class TestAddAirport(unittest.TestCase):
    def setUp(self):
#        self.wd = webdriver.Chrome()
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_airport(self):
        wd = self.wd
        wd.get("http://192.168.178.197/")
        wd.maximize_window()
        wd.find_element_by_xpath("//form[@id='login-card']/div[2]/label/div/div/div/input").click()
        wd.find_element_by_xpath("//form[@id='login-card']/div[2]/label/div/div/div/input").clear()
        wd.find_element_by_xpath("//form[@id='login-card']/div[2]/label/div/div/div/input").send_keys("test")
        wd.find_element_by_xpath("//form[@id='login-card']/div[2]/label[2]/div/div/div/input").click()
        wd.find_element_by_xpath("//form[@id='login-card']/div[2]/label[2]/div/div/div/input").clear()
        wd.find_element_by_xpath("//form[@id='login-card']/div[2]/label[2]/div/div/div/input").send_keys("1245")
        wd.find_element_by_xpath("//form[@id='login-card']/div[3]/button/span[2]/span/span").click()
        wd.find_element_by_xpath("//div[@id='q-app']/div/header/div/button/span[2]/span/i").click()
        wd.find_element_by_xpath("//div[@id='q-app']/div/div/aside/div/div[2]/div[3]/div[3]/span").click()
        wd.find_element_by_xpath("//div[@id='q-app']/div/div[2]/div/div/div/div/div/div/div[2]").click()
        wd.find_element_by_xpath("//div[@id='q-app']/div/div[2]/div/div[2]/div[2]/div/button/span[2]/span").click()
        wd.find_element_by_xpath("//div[4]/label/div/div/div/input").click()
        wd.find_element_by_xpath("//div[4]/label/div/div/div/input").clear()
        wd.find_element_by_xpath("//div[4]/label/div/div/div/input").send_keys("LED")

        wd.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Код ИАТА'])[1]/following::span[4]").click()
        wd.find_element_by_css_selector("svg.q-checkbox__svg.fit.absolute-full").click()
        wd.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Назад'])[1]/following::span[4]").click()

        wd.implicitly_wait(30)
        wd.quit()
        #wd.find_element_by_xpath("//div[4]/button/span[2]/span/i").click()
        #wd.find_element_by_xpath("//div[@id='q-app']/div/header/div/button/span[2]/span/i").click()
        #wd.find_element_by_xpath("//div[@id='q-app']/div/header/div/button/span[2]/span/i").click()
        #wd.find_element_by_xpath("//div[@id='q-app']/div/header/div/div/div[2]/div[4]/button/span[2]/span/i").click()

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
