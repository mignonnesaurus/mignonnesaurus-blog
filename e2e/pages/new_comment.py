from selenium.webdriver.common.by import By


class NewCommentPage:
    SAVE_COMMENT_BUTTON = '#save-comment'

    def __init__(self, driver):
        self.driver = driver

    def add_comment(self, author, text):
        self.driver.find_element(by=By.CSS_SELECTOR, value='#id_author').send_keys(author)
        self.driver.find_element(by=By.CSS_SELECTOR, value='#id_text').send_keys(text)
        self.driver.find_element(by=By.CSS_SELECTOR, value=self.SAVE_COMMENT_BUTTON).click()
