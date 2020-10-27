from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(30)

    def test_add_group(self):
        browser = self.browser
        self.open_home_page(browser)
        self.login(browser, username="admin", password="secret")
        self.open_groups_page(browser)
        self.create_group(browser, name="qwerty", header="qazxsw", footer="asdf")
        self.return_to_groups_page(browser)
        self.logout(browser)

    def test_add_empty_group(self):
        browser = self.browser
        self.open_home_page(browser)
        self.login(browser, username="admin", password="secret")
        self.open_groups_page(browser)
        self.create_group(browser, name="", header="", footer="")
        self.return_to_groups_page(browser)
        self.logout(browser)

    def logout(self, browser):
        browser.find_element(By.LINK_TEXT, "Logout").click()

    def return_to_groups_page(self, browser):
        browser.find_element(By.LINK_TEXT, "group page").click()

    def create_group(self, browser, name, header, footer):
        # init group creation
        browser.find_element(By.NAME, "new").click()
        # fill group form
        browser.find_element(By.NAME, "group_name").click()
        browser.find_element(By.NAME, "group_name").clear()
        browser.find_element(By.NAME, "group_name").send_keys(name)
        browser.find_element(By.NAME, "group_header").click()
        browser.find_element(By.NAME, "group_header").clear()
        browser.find_element(By.NAME, "group_header").send_keys(header)
        browser.find_element(By.NAME, "group_footer").click()
        browser.find_element(By.NAME, "group_footer").clear()
        browser.find_element(By.NAME, "group_footer").send_keys(footer)
        # submit group creation
        browser.find_element(By.NAME, "submit").click()

    def open_groups_page(self, browser):
        browser.find_element(By.LINK_TEXT, "groups").click()

    def login(self, browser, username, password):
        browser.find_element(By.NAME, "user").click()
        browser.find_element(By.NAME, "user").clear()
        browser.find_element(By.NAME, "user").send_keys(username)
        browser.find_element(By.NAME, "pass").clear()
        browser.find_element(By.NAME, "pass").send_keys(password)
        browser.find_element(By.XPATH, "//input[@value='Login']").click()

    def open_home_page(self, browser):
        browser.get("http://localhost/addressbook/index.php")

    def tearDown(self):
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()
