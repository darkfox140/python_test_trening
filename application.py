from selenium import webdriver
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


    def destroy(self):
        self.browser.quit()