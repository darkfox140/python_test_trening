# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from contact import Contact
import unittest


class TestAddNewContact(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(30)

    def test_add_new_contact(self):
        browser = self.browser
        self.open_home_page(browser)
        self.login(browser, username="admin", password="secret")
        self.create_group(browser, Contact(first_name="Andrey", middle_name="Ivan", last_name="Maltsev",
                                           nick_name="Fox140", title="test", company="testCompany", address="Moscov",
                                           home_phone="8495*******", mobile_phone="89168******",
                                           work_phone="8499*******", fax="no", email1="testemail1@facegmail.com",
                                           email2="testemail2@facegmail.com", email3="testemail3@facegmail.com",
                                           homepage="testhomepage.ru", bday="14", bmoth="August",byears="1987",
                                           aday="24", amonth="October", ayear="2014",
                                           address2="St. Peterburg, Lenina 2", phone2="Phone2test",
                                           notes=u"Сдесь могла быть ваша рекламма"))
        self.return_to_home(browser)
        self.logout(browser)

    def test_add_empty_new_contact(self):
        browser = self.browser
        self.open_home_page(browser)
        self.login(browser, username="admin", password="secret")
        self.create_group(browser, Contact(first_name="", middle_name="", last_name="",
                                           nick_name="", title="", company="", address="",
                                           home_phone="", mobile_phone="",
                                           work_phone="", fax="", email1="",
                                           email2="", email3="",
                                           homepage="", bday="", bmoth="",byears="",
                                           aday="", amonth="", ayear="",
                                           address2="", phone2="",
                                           notes=""))
        self.return_to_home(browser)
        self.logout(browser)

    def logout(self, browser):
        browser.find_element_by_link_text("Logout").click()

    def return_to_home(self, browser):
        browser.find_element_by_link_text("home").click()

    def create_group(self, browser, contact):
        # init contact creation
        browser.find_element_by_link_text("add new").click()
        # fill contact form
        browser.find_element_by_name("firstname").clear()
        browser.find_element_by_name("firstname").send_keys(contact.first_name)
        browser.find_element_by_name("middlename").click()
        browser.find_element_by_name("middlename").clear()
        browser.find_element_by_name("middlename").send_keys(contact.middle_name)
        browser.find_element_by_name("lastname").click()
        browser.find_element_by_name("lastname").clear()
        browser.find_element_by_name("lastname").send_keys(contact.last_name)
        browser.find_element_by_name("nickname").clear()
        browser.find_element_by_name("nickname").send_keys(contact.nick_name)
        browser.find_element_by_name("title").click()
        browser.find_element_by_name("title").clear()
        browser.find_element_by_name("title").send_keys(contact.title)
        browser.find_element_by_name("company").click()
        browser.find_element_by_name("company").clear()
        browser.find_element_by_name("company").send_keys(contact.company)
        browser.find_element_by_name("address").click()
        browser.find_element_by_name("address").clear()
        browser.find_element_by_name("address").send_keys(contact.address)
        browser.find_element_by_name("home").clear()
        browser.find_element_by_name("home").send_keys(contact.home_phone)
        browser.find_element_by_name("mobile").clear()
        browser.find_element_by_name("mobile").send_keys(contact.mobile_phone)
        browser.find_element_by_name("work").clear()
        browser.find_element_by_name("work").send_keys(contact.work_phone)
        browser.find_element_by_name("fax").clear()
        browser.find_element_by_name("fax").send_keys(contact.fax)
        browser.find_element_by_name("email").clear()
        browser.find_element_by_name("email").send_keys(contact.email1)
        browser.find_element_by_name("email2").clear()
        browser.find_element_by_name("email2").send_keys(contact.email2)
        browser.find_element_by_name("email3").clear()
        browser.find_element_by_name("email3").send_keys(contact.email3)
        browser.find_element_by_name("homepage").clear()
        browser.find_element_by_name("homepage").send_keys(contact.homepage)
        Select(browser.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        browser.find_element_by_name("bday").click()
        Select(browser.find_element_by_name("bmonth")).select_by_visible_text(contact.bmoth)
        browser.find_element_by_name("bmonth").click()
        browser.find_element_by_name("byear").click()
        browser.find_element_by_name("byear").clear()
        browser.find_element_by_name("byear").send_keys(contact.byears)
        Select(browser.find_element_by_name("aday")).select_by_visible_text(contact.aday)
        browser.find_element_by_name("aday").click()
        browser.find_element_by_name("amonth").click()
        Select(browser.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)
        browser.find_element_by_name("amonth").click()
        browser.find_element_by_name("ayear").click()
        browser.find_element_by_name("ayear").clear()
        browser.find_element_by_name("ayear").send_keys(contact.ayear)
        browser.find_element_by_name("address2").click()
        browser.find_element_by_name("address2").clear()
        browser.find_element_by_name("address2").send_keys(contact.address2)
        browser.find_element_by_name("phone2").clear()
        browser.find_element_by_name("phone2").send_keys(contact.phone2)
        browser.find_element_by_name("notes").clear()
        browser.find_element_by_name("notes").send_keys(contact.notes)
        browser.find_element_by_xpath("(//input[@name='submit'])[2]").click()

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
