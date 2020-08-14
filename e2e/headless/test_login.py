from django.test import LiveServerTestCase
from selenium.webdriver.firefox import options
from selenium.webdriver.firefox.webdriver import WebDriver
from django.contrib.auth import get_user_model

from e2e.pages.admin import AdminLoginPage


class LoginTestCase(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        firefoxOptions = options.Options()
        firefoxOptions.headless = True
        cls.webdriver = WebDriver(options=firefoxOptions)
        cls.webdriver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.webdriver.find_element_by_xpath("//a[@href='/admin/logout/']").click()
        cls.webdriver.quit()
        super().tearDownClass()

    def test_admin_can_login(self):
        get_user_model().objects.create_superuser('admin', 'admin@example.com', 'password')

        admin_login_page = AdminLoginPage(self.webdriver)
        admin_login_page.load(self.live_server_url)
        admin_login_page.login("admin", "password")

        self.webdriver.find_element_by_xpath('//*[contains(text(), "Site administration")]')

        self.assertTrue(self.webdriver.title.startswith('Site administration'))
