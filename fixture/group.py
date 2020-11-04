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
        browser.find_element(By.NAME, "group_name").clear()
        browser.find_element(By.NAME, "group_name").send_keys(group.name)
        browser.find_element(By.NAME, "group_header").clear()
        browser.find_element(By.NAME, "group_header").send_keys(group.header)
        browser.find_element(By.NAME, "group_footer").clear()
        browser.find_element(By.NAME, "group_footer").send_keys(group.footer)
        # submit group creation
        browser.find_element(By.NAME, "submit").click()
        self.return_to_groups_page()

    def delete_all_group(self):
        browser = self.app.browser
        self.open_groups_page()
        elements = browser.find_elements(By.CSS_SELECTOR, "input[type=checkbox]")
        for element in elements:
            element.click()
        browser.find_element(By.NAME, "delete").click()
        self.return_to_groups_page()

    def modification_empty_group(self, group):
        browser = self.app.browser
        self.open_groups_page()
        browser.find_element(By.NAME, "selected[]").click()
        browser.find_element(By.XPATH, "//form/input[3]").click()
        browser.find_element(By.NAME, "group_name").clear()
        browser.find_element(By.NAME, "group_name").send_keys(group.name)
        browser.find_element(By.NAME, "group_header").clear()
        browser.find_element(By.NAME, "group_header").send_keys(group.header)
        browser.find_element(By.NAME, "group_footer").clear()
        browser.find_element(By.NAME, "group_footer").send_keys(group.footer)
        browser.find_element(By.XPATH, "//form/input[3]").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        browser = self.app.browser
        browser.find_element(By.LINK_TEXT, "group page").click()

