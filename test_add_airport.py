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
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)

    def test_add_airport(self):
        driver = self.driver
        driver.get("http://192.168.178.197/login")
        driver.find_element_by_id("f_c845c713-4f14-44d5-9e78-737feb46b176").click()
        driver.find_element_by_id("f_c845c713-4f14-44d5-9e78-737feb46b176").clear()
        driver.find_element_by_id("f_c845c713-4f14-44d5-9e78-737feb46b176").send_keys("test")
        driver.find_element_by_id("f_03342e34-3fbb-45da-a7b2-1e7c35463693").click()
        driver.find_element_by_id("f_03342e34-3fbb-45da-a7b2-1e7c35463693").clear()
        driver.find_element_by_id("f_03342e34-3fbb-45da-a7b2-1e7c35463693").send_keys("1245")
        driver.find_element_by_xpath("//form[@id='login-card']/div[3]/button/span[2]/span/span").click()
        driver.find_element_by_xpath("//div[@id='q-app']/div/header/div/button/span[2]/span/i").click()
        driver.find_element_by_xpath("//div[@id='q-app']/div/div/aside/div/div[2]/div[2]/div[3]/span").click()
        driver.find_element_by_xpath("//div[@id='q-app']/div/div[2]/div/div/div/div/div/div/div[2]").click()
        driver.find_element_by_xpath("//div[@id='q-app']/div/div[2]/div/div[2]/div[2]/div/button/span[2]/span").click()
        driver.find_element_by_id("f_7fc25f94-7cba-469d-a730-ac9eae672d42").click()
        driver.find_element_by_id("f_7fc25f94-7cba-469d-a730-ac9eae672d42").clear()
        driver.find_element_by_id("f_7fc25f94-7cba-469d-a730-ac9eae672d42").send_keys("LED")
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Код ИАТА'])[1]/following::span[2]").click()
        driver.find_element_by_css_selector("path.q-checkbox__truthy").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Назад'])[1]/following::span[4]").click()
        driver.find_element_by_xpath("//div[@id='q-app']/div/header/div/div/div[2]/div[4]/button/span[2]/span/i").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
