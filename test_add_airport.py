# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestAddAirport(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_airport(self):
        wd = self.wd
        wd.get("http://192.168.178.197/login")
        wd.find_element_by_id("f_c845c713-4f14-44d5-9e78-737feb46b176").click()
        wd.find_element_by_id("f_c845c713-4f14-44d5-9e78-737feb46b176").clear()
        wd.find_element_by_id("f_c845c713-4f14-44d5-9e78-737feb46b176").send_keys("test")
        wd.find_element_by_id("f_03342e34-3fbb-45da-a7b2-1e7c35463693").click()
        wd.find_element_by_id("f_03342e34-3fbb-45da-a7b2-1e7c35463693").clear()
        wd.find_element_by_id("f_03342e34-3fbb-45da-a7b2-1e7c35463693").send_keys("1245")
        wd.find_element_by_xpath("//form[@id='login-card']/div[3]/button/span[2]/span/span").click()
        wd.find_element_by_xpath("//div[@id='q-app']/div/header/div/button/span[2]/span/i").click()
        wd.find_element_by_xpath("//div[@id='q-app']/div/div/aside/div/div[2]/div[2]/div[3]/span").click()
        wd.find_element_by_xpath("//div[@id='q-app']/div/div[2]/div/div/div/div/div/div/div[2]").click()
        wd.find_element_by_xpath("//div[@id='q-app']/div/div[2]/div/div[2]/div[2]/div/button/span[2]/span").click()
        wd.find_element_by_id("f_7fc25f94-7cba-469d-a730-ac9eae672d42").click()
        wd.find_element_by_id("f_7fc25f94-7cba-469d-a730-ac9eae672d42").clear()
        wd.find_element_by_id("f_7fc25f94-7cba-469d-a730-ac9eae672d42").send_keys("LED")
        wd.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Код ИАТА'])[1]/following::span[2]").click()
        wd.find_element_by_css_selector("path.q-checkbox__truthy").click()
        wd.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Назад'])[1]/following::span[4]").click()
        wd.find_element_by_xpath("//div[@id='q-app']/div/header/div/div/div[2]/div[4]/button/span[2]/span/i").click()
    
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
