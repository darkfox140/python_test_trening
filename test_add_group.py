# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from group import Group


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(30)

    def test_add_group(self):
        browser = self.browser
        self.login(browser, username="admin", password="secret")
        self.create_group(browser, Group(name="qwerty", header="qazxsw", footer="asdf"))
        self.logout(browser)

    def test_add_empty_group(self):
        browser = self.browser
        self.login(browser, username="admin", password="secret")
        self.create_group(browser, Group(name="", header="", footer=""))
        self.logout(browser)

    def logout(self, browser):
        browser.find_element(By.LINK_TEXT, "Logout").click()

    def return_to_groups_page(self, browser,):
        browser.find_element(By.LINK_TEXT, "group page").click()

    def create_group(self, browser, group):
        self.open_groups_page(browser)
        # init group creation
        browser.find_element(By.NAME, "new").click()
        # fill group form
        browser.find_element(By.NAME, "group_name").clear()
        browser.find_element(By.NAME, "group_name").send_keys(group.name)
        browser.find_element(By.NAME, "group_header").clear()
        browser.find_element(By.NAME, "group_header").send_keys(group.header)
        browser.find_element(By.NAME, "group_footer").clear()
        browser.find_element(By.NAME, "group_footer").send_keys(group.footer)
        # submit group creation
        browser.find_element(By.NAME, "submit").click()
        self.return_to_groups_page(browser)

    def open_groups_page(self, browser):
        browser.find_element(By.LINK_TEXT, "groups").click()

    def login(self, browser, username, password):
        self.open_home_page(browser)
        browser.find_element(By.NAME, "user").clear()
        browser.find_element(By.NAME, "user").send_keys(username)
        browser.find_element(By.NAME, "pass").clear()
        browser.find_element(By.NAME, "pass").send_keys(password)
        browser.find_element(By.XPATH, "//input[@value='Login']").click()

    def open_home_page(self, browser):
        browser.get("http://localhost/addressbook/index.php")

    def tearDown(self):
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()
