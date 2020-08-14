from selenium.webdriver.common.by import By


class NewPostPage:
    SAVE_POST_BUTTON = '#save-post'
    PUBLISH_POST_BUTTON = '#publish-post'
    TEXT_INPUT = '#id_text'
    TITLE_INPUT = '#id_title'

    def __init__(self, driver):
        self.driver = driver

    def add_post(self, title, text):
        self.driver.find_element(by=By.CSS_SELECTOR, value=self.TITLE_INPUT).send_keys(title)
        self.driver.find_element(by=By.CSS_SELECTOR, value=self.TEXT_INPUT).send_keys(text)
        self.driver.find_element(by=By.CSS_SELECTOR, value=self.SAVE_POST_BUTTON).click()

    def publish_post(self):
        self.driver.find_element(by=By.CSS_SELECTOR, value=self.PUBLISH_POST_BUTTON).click()
