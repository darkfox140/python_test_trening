from selenium.webdriver.common.by import By


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        browser = self.app.browser
        browser.find_element(By.LINK_TEXT, "groups").click()

    def create(self, group):
        browser = self.app.browser
        self.open_groups_page()
        # init group creation
        browser.find_element(By.NAME, "new").click()
        # fill group form
        self.fill_group_form(group)
        # submit group creation
        browser.find_element(By.NAME, "submit").click()
        self.return_to_groups_page()

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

    def select_first_group(self):
        browser = self.app.browser
        browser.find_element(By.NAME, "selected[]").click()

    def return_to_groups_page(self):
        browser = self.app.browser
        browser.find_element(By.LINK_TEXT, "group page").click()

