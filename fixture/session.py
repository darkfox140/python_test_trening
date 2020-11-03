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

