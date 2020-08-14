from selenium.webdriver.common.by import By


class AdminLoginPage:
    USERNAME_INPUT = '#id_username'
    PASSWORD_INPUT = '#id_password'
    SUBMIT_BUTTON = 'input[type="submit"]'

    def __init__(self, driver, start_page):
        self.driver = driver
        self.start_page = start_page

    def load(self):
        self.driver.get(f'{self.start_page}/admin/')
        self.driver.maximize_window()

    def login(self, username, password):
        self.driver.find_element(by=By.CSS_SELECTOR, value=self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(by=By.CSS_SELECTOR, value=self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(by=By.CSS_SELECTOR, value=self.SUBMIT_BUTTON).click()
