from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class Applicatin:
    def __init__(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(30)

    def open_home_page(self):
        browser = self.browser
        browser.get("http://localhost/addressbook/index.php")

    def login(self, username, password):
        browser = self.browser
        self.open_home_page()
        browser.find_element(By.NAME, "user").clear()
        browser.find_element(By.NAME, "user").send_keys(username)
        browser.find_element(By.NAME, "pass").clear()
        browser.find_element(By.NAME, "pass").send_keys(password)
        browser.find_element(By.XPATH, "//input[@value='Login']").click()

    def open_groups_page(self):
        browser = self.browser
        browser.find_element(By.LINK_TEXT, "groups").click()

    def create_group(self, group):
        browser = self.browser
        self.open_groups_page()
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
        self.return_to_groups_page()

    def return_to_groups_page(self):
        browser = self.browser
        browser.find_element(By.LINK_TEXT, "group page").click()

    def logout(self):
        browser = self.browser
        browser.find_element(By.LINK_TEXT, "Logout").click()

    def create_new_contact(self, contact):
        browser = self.browser
        # init new contact creation
        browser.find_element(By.LINK_TEXT, "add new").click()
        # fill new contact form
        browser.find_element(By.NAME, "firstname").clear()
        browser.find_element(By.NAME, "firstname").send_keys(contact.first_name)
        browser.find_element(By.NAME, "middlename").clear()
        browser.find_element(By.NAME, "middlename").send_keys(contact.middle_name)
        browser.find_element(By.NAME, "lastname").clear()
        browser.find_element(By.NAME, "lastname").send_keys(contact.last_name)
        browser.find_element(By.NAME, "nickname").clear()
        browser.find_element(By.NAME, "nickname").send_keys(contact.nick_name)
        browser.find_element(By.NAME, "title").clear()
        browser.find_element(By.NAME, "title").send_keys(contact.tittle)
        browser.find_element(By.NAME, "company").clear()
        browser.find_element(By.NAME, "company").send_keys(contact.company)
        browser.find_element(By.NAME, "address").clear()
        browser.find_element(By.NAME, "address").send_keys(contact.address1)
        # Telephone
        browser.find_element(By.NAME, "home").clear()
        browser.find_element(By.NAME, "home").send_keys(contact.home_phone)
        browser.find_element(By.NAME, "mobile").clear()
        browser.find_element(By.NAME, "mobile").send_keys(contact.mobile_phone)
        browser.find_element(By.NAME, "work").clear()
        browser.find_element(By.NAME, "work").send_keys(contact.work_phone)
        browser.find_element(By.NAME, "fax").clear()
        browser.find_element(By.NAME, "fax").send_keys(contact.fax)
        browser.find_element(By.NAME, "email").clear()
        browser.find_element(By.NAME, "email").send_keys(contact.email1)
        browser.find_element(By.NAME, "email2").clear()
        browser.find_element(By.NAME, "email2").send_keys(contact.email2)
        browser.find_element(By.NAME, "email3").clear()
        browser.find_element(By.NAME, "email3").send_keys(contact.email3)
        browser.find_element(By.NAME, "homepage").clear()
        browser.find_element(By.NAME, "homepage").send_keys(contact.homepage)
        # Birthday
        Select(browser.find_element(By.NAME, "bday")).select_by_visible_text(contact.bday)
        browser.find_element(By.NAME, "bday").click()
        Select(browser.find_element(By.NAME, "bmonth")).select_by_visible_text(contact.bmonth)
        browser.find_element(By.NAME, "bmonth").click()
        browser.find_element(By.NAME, "byear").clear()
        browser.find_element(By.NAME, "byear").send_keys(contact.byear)
        # Anniversary
        Select(browser.find_element(By.NAME, "aday")).select_by_visible_text(contact.aday)
        browser.find_element(By.NAME, "aday").click()
        browser.find_element(By.NAME, "amonth").click()
        Select(browser.find_element(By.NAME, "amonth")).select_by_visible_text(contact.amonth)
        browser.find_element(By.NAME, "amonth").click()
        browser.find_element(By.NAME, "ayear").clear()
        browser.find_element(By.NAME, "ayear").send_keys(contact.ayear)
        # Secondary
        browser.find_element(By.NAME, "address2").clear()
        browser.find_element(By.NAME, "address2").send_keys(contact.address2)
        browser.find_element(By.NAME, "phone2").clear()
        browser.find_element(By.NAME, "phone2").send_keys(contact.phone2)
        browser.find_element(By.NAME, "notes").clear()
        browser.find_element(By.NAME, "notes").send_keys(contact.notes)
        browser.find_element(By.XPATH, "(//input[@name='submit'])[2]").click()
        self.return_home()

    def return_home(self):
        browser = self.browser
        browser.find_element(By.LINK_TEXT, "home").click()



    def destroy(self):
        self.browser.quit()
