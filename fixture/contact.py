from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from model.contact import NewContact
import re


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
        self.contact_cashe = None

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

    def modification_first_contact(self):
        self.modification_contact_by_index(0)

    def modification_contact_by_index(self, index, new_contact_form):
        browser = self.app.browser
        self.open_home()
        self.open_contact_to_edit_by_index(index)
        self.fill_contact_form(new_contact_form)
        self.button_update_click()
        self.open_home()
        self.contact_cashe = None

    def modification_contact_by_id(self, id, new_contact_form):
        browser = self.app.browser
        self.open_home()
        self.open_contact_to_edit_by_id(id)
        self.fill_contact_form(new_contact_form)
        self.button_update_click()
        self.open_home()
        self.contact_cashe = None

    def button_update_click(self):
        browser = self.app.browser
        browser.find_element(By.XPATH, "//form[1]/input[22]").click()

    def open_contact_to_edit_by_index(self, index):
        browser = self.app.browser
        self.open_home()
        contact_elem = browser.find_elements(By.NAME, "entry")[index]
        cells = contact_elem.find_elements(By.TAG_NAME, "td")[7]
        cells.find_element(By.TAG_NAME, "a").click()

    def open_contact_to_edit_by_id(self, id):
        browser = self.app.browser
        self.open_home()
        browser.find_element(By.CSS_SELECTOR, "input[value='%s']" % id)
        cells = browser.find_elements(By.TAG_NAME, "td")[7]
        cells.find_element(By.TAG_NAME, "a").click()

    def open_contact_view_index(self, index):
        browser = self.app.browser
        self.open_home()
        contact_elem = browser.find_elements(By.NAME, "entry")[index]
        cells = contact_elem.find_elements(By.TAG_NAME, "td")[6]
        cells.find_element(By.CSS_SELECTOR, "#maintable a img").click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        browser = self.app.browser
        self.open_home()
        self.select_contact_by_index(index)
        self.button_delete_click()
        browser.switch_to_alert().accept()
        browser.find_element(By.CSS_SELECTOR, "div.msgbox")
        self.open_home()
        self.contact_cashe = None

    def button_delete_click(self):
        browser = self.app.browser
        browser.find_element(By.XPATH, "//input[@value='Delete']").click()

    def delete_contact_by_id(self, id):
        browser = self.app.browser
        self.open_home()
        self.select_contact_by_id(id)
        self.button_delete_click()
        browser.switch_to_alert().accept()
        browser.find_element(By.CSS_SELECTOR, "div.msgbox")
        self.open_home()
        self.contact_cashe = None

    def select_contact_by_index(self, index):
        browser = self.app.browser
        browser.find_elements(By.NAME, "selected[]")[index].click()

    def select_contact_by_id(self, id):
        browser = self.app.browser
        browser.find_element(By.CSS_SELECTOR, "input[value='%s']" % id).click()

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

    contact_cashe = None # Кеширование списка контактов, сбрасывается после добавления\удаления\модификации

    def get_contact_list(self):
        if self.contact_cashe is None:
            browser = self.app.browser
            self.open_home()
            self.contact_cashe = []
            for elements in browser.find_elements(By.NAME, "entry"):
                cells = elements.find_elements(By.TAG_NAME, "td") # Данная точка найтёт текст
                id = cells[0].find_element(By.TAG_NAME, "input").get_attribute("value")
                last_text = cells[1].text
                first_text = cells[2].text
                address = cells[3].text
                all_email = cells[4].text
                all_phones = cells[5].text
                self.contact_cashe.append(NewContact(last_name=last_text, first_name=first_text, address1=address,
                                                     all_phones_from_home_page=all_phones,
                                                     all_email_from_home_page=all_email, id=id, ))
        return list(self.contact_cashe)

    def get_contact_info_from_edit_page(self, index):
        browser = self.app.browser
        self.open_contact_to_edit_by_index(index)
        firstname = browser.find_element(By.NAME, "firstname").get_attribute("value")
        lastname = browser.find_element(By.NAME, "lastname").get_attribute("value")
        address = browser.find_element(By.NAME, "address").text
        email1 = browser.find_element(By.NAME, "email").get_attribute("value")
        email2 = browser.find_element(By.NAME, "email2").get_attribute("value")
        email3 = browser.find_element(By.NAME, "email3").get_attribute("value")
        homephone = browser.find_element(By.NAME, "home").get_attribute("value")
        mobilephone = browser.find_element(By.NAME, "mobile").get_attribute("value")
        workphone = browser.find_element(By.NAME, "work").get_attribute("value")
        secondaryphone = browser.find_element(By.NAME, "phone2").get_attribute("value")
        id = browser.find_element(By.NAME, "id").get_attribute("value")
        return NewContact(first_name=firstname, last_name=lastname, address1=address, email1=email1, email2=email2,
                          email3=email3, home_phone=homephone, mobile_phone=mobilephone, work_phone=workphone,
                          phone2=secondaryphone, id=id)

    def get_contact_from_view_page(self, index):
        browser = self.app.browser
        self.open_contact_view_index(index)
        text = browser.find_element(By.ID, "content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return NewContact(home_phone=homephone, mobile_phone=mobilephone, work_phone=workphone,
                          phone2=secondaryphone, id=id)

    def add_contact_to_group_by_id(self, contact_id, group_id, group_name):
        browser = self.app.browser
        self.open_home()
        self.select_contact_by_id(contact_id)
        browser.find_element(By.NAME, "to_group").click()
        browser.find_element(By.XPATH, "(//option[@value=%s])[2]" % group_id).click()
        browser.find_element(By.NAME, "add").click()
        browser.find_element(By.LINK_TEXT, 'group page "%s"' % group_name).click()

    def delete_contact_from_group(self, group_id, contact_id):
        browser = self.app.browser
        self.open_home()
        browser.find_element(By.NAME, "group").click()
        browser.find_element(By.XPATH, "//option[@value=%s]" % group_id).click()
        self.select_contact_by_id(contact_id)
        browser.find_element(By.NAME, "remove").click()
        browser.find_element(By.CSS_SELECTOR, "div.msgbox")