from selenium.webdriver.common.by import By


class HomePage:
    ADD_LINK = '.glyphicon-plus'
    LOGOUT_LINK_TEXT = 'Log out'
    VIEW_SITE_LINK_TEXT = 'VIEW SITE'

    def __init__(self, driver, start_page):
        self.driver = driver
        self.start_page = start_page

    def load(self):
        self.driver.get(self.start_page)

    def new_post(self):
        self.driver.find_element(by=By.CSS_SELECTOR, value=self.ADD_LINK).click()

    def view_post(self, title):
        self.driver.find_element(by=By.LINK_TEXT, value=title).click()

    def logout(self):
        self.driver.find_element(by=By.LINK_TEXT, value=self.LOGOUT_LINK_TEXT).click()
