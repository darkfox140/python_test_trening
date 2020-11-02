from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Applicatin:

    def __init__(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.cotact = ContactHelper(self)

    def open_home_page(self):
        browser = self.browser
        browser.get("http://localhost/addressbook/index.php")

    def destroy(self):
        self.browser.quit()
