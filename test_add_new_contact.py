# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from contact import NewContact
import unittest


class TestAddNewContact(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(30)

    def test_add_new_contact(self):
        browser = self.browser
        self.open_home_page(browser)
        self.login(browser, "admin", "secret")
        self.create_new_contact(browser, NewContact(last_name="Andrey", middle_name="Ivan", first_name="Maltsev",
                                nick_name="Fox140", tittle="test", company="testcompany", address1="Moscow",
                                home_phone="8495*******", mobile_phone="89168******", work_phone="8499*******",
                                fax="No", email1="testemail1@facegmail.com", email2="testemail2@facegmail.com",
                                email3="testemail3@facegmail.com", homepage="testhomepage.ru", bday="14",
                                bmonth="August", byear="1987", aday="24", amonth="October", ayear="2014",
                                address2="Moscow, Lenina 2", phone2="Phone2test", notes="Test information"))
        self.return_home(browser)
        self.logout(browser)

    def logout(self, browser):
        browser.find_element_by_link_text("Logout").click()

    def return_home(self, browser):
        browser.find_element_by_link_text("home").click()

    def create_new_contact(self, browser, contact):
        # init new contact creation
        browser.find_element_by_link_text("add new").click()
        # fill new contact form
        browser.find_element_by_name("firstname").clear()
        browser.find_element_by_name("firstname").send_keys(contact.first_name)
        browser.find_element_by_name("middlename").clear()
        browser.find_element_by_name("middlename").send_keys(contact.middle_name)
        browser.find_element_by_name("lastname").clear()
        browser.find_element_by_name("lastname").send_keys(contact.last_name)
        browser.find_element_by_name("nickname").clear()
        browser.find_element_by_name("nickname").send_keys(contact.nick_name)
        browser.find_element_by_name("title").clear()
        browser.find_element_by_name("title").send_keys(contact.tittle)
        browser.find_element_by_name("company").clear()
        browser.find_element_by_name("company").send_keys(contact.company)
        browser.find_element_by_name("address").clear()
        browser.find_element_by_name("address").send_keys(contact.address1)
        # Telephone
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
        # Birthday
        Select(browser.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        browser.find_element_by_name("bday").click()
        Select(browser.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        browser.find_element_by_name("bmonth").click()
        browser.find_element_by_name("byear").clear()
        browser.find_element_by_name("byear").send_keys(contact.byear)
        # Anniversary
        Select(browser.find_element_by_name("aday")).select_by_visible_text(contact.aday)
        browser.find_element_by_name("aday").click()
        browser.find_element_by_name("amonth").click()
        Select(browser.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)
        browser.find_element_by_name("amonth").click()
        browser.find_element_by_name("ayear").clear()
        browser.find_element_by_name("ayear").send_keys(contact.ayear)
        # Secondary
        browser.find_element_by_name("address2").clear()
        browser.find_element_by_name("address2").send_keys(contact.address2)
        browser.find_element_by_name("phone2").clear()
        browser.find_element_by_name("phone2").send_keys(contact.phone2)
        browser.find_element_by_name("notes").clear()
        browser.find_element_by_name("notes").send_keys(contact.notes)
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