from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from model.contact import NewContact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_add_new(self):
        browser = self.app.browser
        browser.find_element(By.LINK_TEXT, "add new").click()

    def create_new_contact(self, contact):
        browser = self.app.browser
        self.open_add_new()
        self.fill_contact_form(contact)
        self.submit_enter()
        self.open_home()

    def create_empty_contact(self):
        self.open_add_new()
        self.submit_enter()
        self.open_home()

    def submit_enter(self):
        browser = self.app.browser
        browser.find_element(By.XPATH, "//form/input[21]").click()

    def fill_contact_form(self, contact):
        browser = self.app.browser
        self.change_field_contact_value("firstname", contact.first_name)
        self.change_field_contact_value("middlename", contact.middle_name)
        self.change_field_contact_value("lastname", contact.last_name)
        self.change_field_contact_value("nickname", contact.nick_name)
        self.change_field_contact_value("title", contact.tittle)
        self.change_field_contact_value("company", contact.company)
        self.change_field_contact_value("address", contact.address1)
        # Telephone
        self.change_field_contact_value("home", contact.home_phone)
        self.change_field_contact_value("mobile", contact.mobile_phone)
        self.change_field_contact_value("work", contact.work_phone)
        self.change_field_contact_value("fax", contact.fax)
        # Email and homepage
        self.change_field_contact_value("email", contact.email1)
        self.change_field_contact_value("email2", contact.email2)
        self.change_field_contact_value("email3", contact.email3)
        self.change_field_contact_value("homepage", contact.homepage)
        # Birthday
        self.select_day("bday", contact.bday)
        self.select_month("bmonth", contact.bmonth)
        self.change_field_contact_value("byear", contact.byear)
        # Anniversary
        self.select_day("aday", contact.aday)
        self.select_month("amonth", contact.amonth)
        self.change_field_contact_value("ayear", contact.ayear)
        # Secondary
        self.change_field_contact_value("address2", contact.address2)
        self.change_field_contact_value("phone2", contact.phone2)
        self.change_field_contact_value("notes", contact.notes)

    def select_month(self, insert_month, month):
        browser = self.app.browser
        if month is not None:
            Select(browser.find_element(By.NAME, insert_month)).select_by_visible_text(month)
            browser.find_element(By.NAME, insert_month).click()

    def select_day(self, insert_the_day, number):
        browser = self.app.browser
        if number is not None:
            Select(browser.find_element(By.NAME, insert_the_day)).select_by_visible_text(number)
            browser.find_element(By.NAME, insert_the_day).click()

    def change_field_contact_value(self, field_name, text):
        browser = self.app.browser
        if text is not None:
            browser.find_element(By.NAME, field_name).clear()
            browser.find_element(By.NAME, field_name).send_keys(text)

    def modification_first_contact(self, new_contact_form):
        browser = self.app.browser
        self.open_home()
        self.select_first_contact()
        browser.find_element(By.XPATH, "//tbody/tr[2]/td[8]/a").click()
        self.fill_contact_form(new_contact_form)
        browser.find_element(By.XPATH, "//form[1]/input[22]").click()
        self.open_home()

    def delete_first_contact(self,):
        browser = self.app.browser
        self.open_home()
        self.select_first_contact()
        browser.find_element(By.XPATH, "//input[@value='Delete']").click()
        browser.switch_to_alert().accept()
        browser.find_element(By.CSS_SELECTOR, "div.msgbox")
        self.open_home()

    def select_first_contact(self):
        browser = self.app.browser
        browser.find_element(By.NAME, "selected[]").click()

    def open_home(self):
        browser = self.app.browser
        if not (browser.current_url.endswith("/index.php") and
                len(browser.find_elements(By.XPATH, "//form[2]/div[1]/input")) > 0):
            browser.find_element(By.LINK_TEXT, "home").click()

    def count(self):
        browser = self.app.browser
        self.open_home()
        return len(browser.find_elements(By.NAME, "selected[]"))

    def get_contact_list(self):
        browser = self.app.browser
        self.open_home()
        contacts = []
        table = browser.find_element(By.ID, "maintable")
        line = table.find_elements(By.NAME, "entry")
        for element in line.find_elements(By.NAME, "entry"):
            lastname = element.find_elements(By.XPATH, "//tbody/tr/td[2]")
            lastname_text = lastname.text
            id = element.find_elements(By.NAME, "selected[]").get_attribute("value")
            firstname = element.find_element(By.XPATH, "//tbody/tr/td[3]")
            firstname_text = firstname.text
            contacts.append(NewContact(last_name=lastname_text, first_name=firstname_text, id=id))
        return contacts