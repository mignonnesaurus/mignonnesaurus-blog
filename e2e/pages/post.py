from selenium.webdriver.common.by import By


class PostPage:
    ADD_COMMENT_BUTTON = '#add-comment'
    APPROVE_COMMENT_BUTTON = '#approve-comment'
    DELETE_POST_BUTTON = '#delete-post'

    def __init__(self, driver):
        self.driver = driver

    def new_comment(self):
        self.driver.find_element(by=By.CSS_SELECTOR, value=self.ADD_COMMENT_BUTTON).click()

    def approve_comment(self):
        self.driver.find_element(by=By.CSS_SELECTOR, value=self.APPROVE_COMMENT_BUTTON).click()

    def delete_post(self):
        self.driver.find_element(by=By.CSS_SELECTOR, value=self.DELETE_POST_BUTTON).click()
