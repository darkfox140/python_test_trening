from selenium.webdriver.common.by import By


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        browser = self.app.browser
        self.app.open_home_page()
        browser.find_element(By.NAME, "user").clear()
        browser.find_element(By.NAME, "user").send_keys(username)
        browser.find_element(By.NAME, "pass").clear()
        browser.find_element(By.NAME, "pass").send_keys(password)
        browser.find_element(By.XPATH, "//input[@value='Login']").click()

    def logout(self):
        browser = self.app.browser
        browser.find_element(By.LINK_TEXT, "Logout").click()
        browser.find_element(By.NAME, "user")

    def ensure_logout(self):
        browser = self.app.browser
        if len(browser.find_elements(By.LINK_TEXT, "Logout")) > 0:
            self.logout()

    def ensure_login(self, username, password):
        browser = self.app.browser
        if len(browser.find_elements(By.LINK_TEXT, "Logout")) > 0:
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

    def is_logged_in_as(self, username):
        browser = self.app.browser
        return self.get_logged_user() == username

    def get_logged_user(self):
        browser = self.app.browser
        return browser.find_element(By.XPATH, "//form/b").text[1:-1]
