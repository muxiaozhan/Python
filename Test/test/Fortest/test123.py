#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from time import sleep


''' '''
class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.set_window_size(400, 800)
        self.driver.get("http://10.66.30.85:59999/home")
        self.driver.find_element_by_link_text("我的").click()
        self.driver.find_element_by_link_text("点击登录").click()

    def login(self,phone,password):
        self.driver.find_element_by_xpath("//input[@type='tel']").clear()
        self.driver.find_element_by_xpath("//input[@type='tel']").send_keys(phone)
        self.driver.find_element_by_xpath("//input[@type='password']").clear()
        self.driver.find_element_by_xpath("//input[@type='password']").send_keys(password)
        self.driver.find_element_by_xpath("//button[@class='gz-btn']").click()
        sleep(3)

    def is_login_sucess(self):
        try:
            test=self.driver.find_element_by_xpath("//div[@class='user-name']").text
            return True
        except:
            return False

    def test_login(self):
        self.login("15705963365","zhang12345")
        result=self.is_login_sucess()
        self.assertTrue(result)

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":

    unittest.main()

