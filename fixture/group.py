from selenium.webdriver.common.by import By
from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        browser = self.app.browser
        if not (browser.current_url.endswith("/group.php") and len(browser.find_elements(By.NAME, "new")) > 0):
            browser.find_element(By.LINK_TEXT, "groups").click()

    def create_group(self, group):
        browser = self.app.browser
        self.open_groups_page()
        # init group creation
        browser.find_element(By.NAME, "new").click()
        # fill group form
        self.fill_group_form(group)
        # submit group creation
        browser.find_element(By.NAME, "submit").click()
        self.return_to_groups_page()
        self.group_cashe = None

    def fill_group_form(self, group):
        browser = self.app.browser
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        browser = self.app.browser
        if text is not None:
            browser.find_element(By.NAME, field_name).clear()
            browser.find_element(By.NAME, field_name).send_keys(text)

    def delete_first_group(self):
        browser = self.app.browser
        self.open_groups_page()
        self.select_first_group()
        browser.find_element(By.NAME, "delete").click()
        self.return_to_groups_page()
        self.group_cashe = None

    def modification_first_group(self, new_group_date):
        browser = self.app.browser
        self.open_groups_page()
        self.select_first_group()
        # Open modification form
        browser.find_element(By.XPATH, "//form/input[3]").click()
        # fill group form
        self.fill_group_form(new_group_date)
        # Submit modification
        browser.find_element(By.XPATH, "//form/input[3]").click()
        self.return_to_groups_page()
        self.group_cashe = None

    def select_first_group(self):
        browser = self.app.browser
        browser.find_element(By.NAME, "selected[]").click()

    def return_to_groups_page(self):
        browser = self.app.browser
        browser.find_element(By.LINK_TEXT, "group page").click()

    def count(self):
        browser = self.app.browser
        self.open_groups_page()
        return len(browser.find_elements(By.NAME, "selected[]"))

    group_cashe = None

    def get_group_list(self):
        if self.group_cashe is None:
            browser = self.app.browser
            self.open_groups_page()
            self.group_cashe = []
            for element in browser.find_elements(By.CSS_SELECTOR, "span.group"):
                text = element.text
                id = element.find_element(By.NAME, "selected[]").get_attribute("value")
                self.group_cashe.append(Group(name=text, id=id))
        return list(self.group_cashe)
