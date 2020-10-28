# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest


class TestAddNewContact(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(30)

    def test_add_new_contact(self):
        browser = self.browser
        self.open_home_page(browser)
        self.login(browser, "admin", "secret")
        self.create_new_contact(browser, "Andrey", "Ivan", "Maltsev", "Fox140", "test", "testcompany", "Moscow",
                                "8495*******", "89168******", "8499*******", "No", "testemail1@facegmail.com",
                                "testemail2@facegmail.com", "testemail3@facegmail.com", "testhomepage.ru", "14",
                                "August", "1987", "24", "October", "2014", "Moscow, Lenina 2", "Phone2test",
                                "Test information")
        self.return_home(browser)
        self.logout(browser)

    def logout(self, browser):
        browser.find_element_by_link_text("Logout").click()

    def return_home(self, browser):
        browser.find_element_by_link_text("home").click()

    def create_new_contact(self, browser, first_name, middle_name, last_name, nick_name, tittle, company, address1,
                           home_phone, mobile_phone, work_phone, fax, email1, email2, email3, homepage, bday, bmonth,
                           byear, aday, amonth, ayear, address2, phone2, notest):
        # init new contact creation
        browser.find_element_by_link_text("add new").click()
        # fill new contact form
        browser.find_element_by_name("firstname").clear()
        browser.find_element_by_name("firstname").send_keys(first_name)
        browser.find_element_by_name("middlename").clear()
        browser.find_element_by_name("middlename").send_keys(middle_name)
        browser.find_element_by_name("lastname").clear()
        browser.find_element_by_name("lastname").send_keys(last_name)
        browser.find_element_by_name("nickname").clear()
        browser.find_element_by_name("nickname").send_keys(nick_name)
        browser.find_element_by_name("title").clear()
        browser.find_element_by_name("title").send_keys(tittle)
        browser.find_element_by_name("company").clear()
        browser.find_element_by_name("company").send_keys(company)
        browser.find_element_by_name("address").clear()
        browser.find_element_by_name("address").send_keys(address1)
        # Telephone
        browser.find_element_by_name("home").clear()
        browser.find_element_by_name("home").send_keys(home_phone)
        browser.find_element_by_name("mobile").clear()
        browser.find_element_by_name("mobile").send_keys(mobile_phone)
        browser.find_element_by_name("work").clear()
        browser.find_element_by_name("work").send_keys(work_phone)
        browser.find_element_by_name("fax").clear()
        browser.find_element_by_name("fax").send_keys(fax)
        browser.find_element_by_name("email").clear()
        browser.find_element_by_name("email").send_keys(email1)
        browser.find_element_by_name("email2").clear()
        browser.find_element_by_name("email2").send_keys(email2)
        browser.find_element_by_name("email3").clear()
        browser.find_element_by_name("email3").send_keys(email3)
        browser.find_element_by_name("homepage").clear()
        browser.find_element_by_name("homepage").send_keys(homepage)
        # Birthday
        Select(browser.find_element_by_name("bday")).select_by_visible_text(bday)
        browser.find_element_by_name("bday").click()
        Select(browser.find_element_by_name("bmonth")).select_by_visible_text(bmonth)
        browser.find_element_by_name("bmonth").click()
        browser.find_element_by_name("byear").clear()
        browser.find_element_by_name("byear").send_keys(byear)
        # Anniversary
        Select(browser.find_element_by_name("aday")).select_by_visible_text(aday)
        browser.find_element_by_name("aday").click()
        browser.find_element_by_name("amonth").click()
        Select(browser.find_element_by_name("amonth")).select_by_visible_text(amonth)
        browser.find_element_by_name("amonth").click()
        browser.find_element_by_name("ayear").clear()
        browser.find_element_by_name("ayear").send_keys(ayear)
        # Secondary
        browser.find_element_by_name("address2").clear()
        browser.find_element_by_name("address2").send_keys(address2)
        browser.find_element_by_name("phone2").clear()
        browser.find_element_by_name("phone2").send_keys(phone2)
        browser.find_element_by_name("notes").clear()
        browser.find_element_by_name("notes").send_keys(notest)
        browser.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def login(self, browser, user_name, password):
        browser.find_element_by_name("user").send_keys(user_name)
        browser.find_element_by_name("pass").clear()
        browser.find_element_by_name("pass").send_keys(password)
        browser.find_element_by_id("LoginForm").submit()

    def open_home_page(self, browser):
        browser.get("http://localhost/addressbook/index.php")

    def tearDown(self):
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()