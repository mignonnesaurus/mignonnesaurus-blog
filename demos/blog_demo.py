from seleniumbase import BaseCase
import os

MY_BLOG_USERNAME = os.getenv('MY_BLOG_USERNAME')
MY_BLOG_PASSWORD = os.getenv('MY_BLOG_PASSWORD')


class BlogDemo(BaseCase):
    def test_blog(self):
        self.open(self.start_page)
        self.maximize_window()

        home_page = self.get_current_url()
        self.open(f'{home_page}admin/')

        self.type('#id_username', MY_BLOG_USERNAME)
        self.type('#id_password', MY_BLOG_USERNAME)
        self.click('input[type="submit"]')

        self.click('link=VIEW SITE')

        self.click('.glyphicon-plus')
        self.type('#id_title', 'Your Favorite Star Wars Quotes')
        self.type('#id_text', 'What are your favorite Star Wars Quotes?')

        self.click('#save-post')

        self.click('#publish-post')
        self.open(home_page)

        self.click('link=Your Favorite Star Wars Quotes')
        self.click('.add-comment')
        self.type('#id_author', 'Han Solo')
        self.type('#id_text', '"Crazy thing is, it’s true. The Force, the Jedi — all of it. It’s all true."️')
        self.click('button[type="submit"].save')
        self.click('.glyphicon-ok')

        self.click('.add-comment')
        self.type('#id_author', 'Yoda')
        self.type('#id_text', '"Do. Or do not. There is no try."️')
        self.click('button[type="submit"].save')
        self.click('.glyphicon-ok')

        self.click('.add-comment')
        self.type('#id_author', 'Darth Vader')
        self.type('#id_text', '"I find your lack of faith disturbing."')
        self.click('button[type="submit"].save')
        self.click('.glyphicon-ok')

        self.click('.glyphicon-remove')

        self.click('link=Log out')
