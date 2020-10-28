# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import unittest


class TestAddNewContact(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(30)


    def test_add_new_contact(self):
        browser = self.browser
        self.open_home_page(browser)
        self.login(browser, username="admin", password="secret")
        # init contact creation
        browser.find_element_by_link_text("add new").click()
        # fill contact form
        browser.find_element_by_name("firstname").clear()
        browser.find_element_by_name("firstname").send_keys("Andrey")
        browser.find_element_by_name("middlename").click()
        browser.find_element_by_name("middlename").clear()
        browser.find_element_by_name("middlename").send_keys("Andrey11")
        browser.find_element_by_name("lastname").click()
        browser.find_element_by_name("lastname").clear()
        browser.find_element_by_name("lastname").send_keys("Maltsev")
        browser.find_element_by_name("nickname").clear()
        browser.find_element_by_name("nickname").send_keys("Fox140")
        browser.find_element_by_name("title").click()
        browser.find_element_by_name("title").clear()
        browser.find_element_by_name("title").send_keys("test")
        browser.find_element_by_name("company").click()
        browser.find_element_by_name("company").clear()
        browser.find_element_by_name("company").send_keys("testCompany")
        browser.find_element_by_name("address").click()
        browser.find_element_by_name("address").clear()
        browser.find_element_by_name("address").send_keys("Moscov")
        browser.find_element_by_name("home").clear()
        browser.find_element_by_name("home").send_keys("8495*******")
        browser.find_element_by_name("mobile").clear()
        browser.find_element_by_name("mobile").send_keys("89168******")
        browser.find_element_by_name("work").clear()
        browser.find_element_by_name("work").send_keys("8499*******")
        browser.find_element_by_name("fax").clear()
        browser.find_element_by_name("fax").send_keys("no")
        browser.find_element_by_name("email").clear()
        browser.find_element_by_name("email").send_keys("testemail1@facegmail.com")
        browser.find_element_by_name("email2").clear()
        browser.find_element_by_name("email2").send_keys("testemail2@facegmail.com")
        browser.find_element_by_name("email3").clear()
        browser.find_element_by_name("email3").send_keys("testemail3@facegmail.com")
        browser.find_element_by_name("homepage").clear()
        browser.find_element_by_name("homepage").send_keys("testhomepage.ru")
        Select(browser.find_element_by_name("bday")).select_by_visible_text("14")
        browser.find_element_by_name("bday").click()
        Select(browser.find_element_by_name("bmonth")).select_by_visible_text("August")
        browser.find_element_by_name("bmonth").click()
        browser.find_element_by_name("byear").click()
        browser.find_element_by_name("byear").clear()
        browser.find_element_by_name("byear").send_keys("1987")
        Select(browser.find_element_by_name("aday")).select_by_visible_text("24")
        browser.find_element_by_name("aday").click()
        browser.find_element_by_name("amonth").click()
        Select(browser.find_element_by_name("amonth")).select_by_visible_text("October")
        browser.find_element_by_name("amonth").click()
        browser.find_element_by_name("ayear").click()
        browser.find_element_by_name("ayear").clear()
        browser.find_element_by_name("ayear").send_keys("2014")
        browser.find_element_by_name("address2").click()
        browser.find_element_by_name("address2").clear()
        browser.find_element_by_name("address2").send_keys("St. Peterburg, Lenina 2")
        browser.find_element_by_name("phone2").clear()
        browser.find_element_by_name("phone2").send_keys("Phone2test")
        browser.find_element_by_name("notes").clear()
        browser.find_element_by_name("notes").send_keys(u"Сдесь могла быть ваша рекламма")
        browser.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        # return to home
        browser.find_element_by_link_text("home").click()
        # logout
        browser.find_element_by_link_text("Logout").click()

    def login(self, browser, username, password):
        browser.find_element_by_name("user").send_keys(username)
        browser.find_element_by_name("pass").clear()
        browser.find_element_by_name("pass").send_keys(password)
        browser.find_element_by_id("LoginForm").submit()

    def open_home_page(self, browser):
        browser.get("http://localhost/addressbook/index.php")

    def tearDown(self):
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()
