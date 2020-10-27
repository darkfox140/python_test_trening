# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(30)

    def test_add_group(self):
        browser = self.browser
        browser.get("http://localhost/addressbook/index.php")
        browser.find_element(By.NAME, "user").click()
        browser.find_element(By.NAME, "user").clear()
        browser.find_element(By.NAME, "user").send_keys("admin")
        browser.find_element(By.NAME, "pass").clear()
        browser.find_element(By.NAME, "pass").send_keys("secret")
        browser.find_element(By.XPATH, "//input[@value='Login']").click()
        browser.find_element(By.LINK_TEXT, "groups").click()
        browser.find_element(By.NAME, "new").click()
        browser.find_element(By.NAME, "group_name").click()
        browser.find_element(By.NAME, "group_name").clear()
        browser.find_element(By.NAME, "group_name").send_keys("qwerty")
        browser.find_element(By.NAME, "group_header").click()
        browser.find_element(By.NAME, "group_header").clear()
        browser.find_element(By.NAME, "group_header").send_keys("qazxsw")
        browser.find_element(By.NAME, "group_footer").click()
        browser.find_element(By.NAME, "group_footer").clear()
        browser.find_element(By.NAME, "group_footer").send_keys("asdf")
        browser.find_element(By.NAME, "submit").click()
        browser.find_element(By.LINK_TEXT, "group page").click()
        browser.find_element(By.LINK_TEXT, "Logout").click()

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.browser.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def tearDown(self):
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()
