from seleniumbase import BaseCase
import os

MY_BLOG_USERNAME = os.getenv('MY_BLOG_USERNAME')
MY_BLOG_PASSWORD = os.getenv('MY_BLOG_PASSWORD')


class BlogDemo(BaseCase):
    def test_blog(self):
        self.open(self.start_page)

        home_page = self.get_current_url()
        self.open(f'{home_page}admin/')

        self.type('#id_username', MY_BLOG_USERNAME)
        self.type('#id_password', MY_BLOG_USERNAME)
        self.save_screenshot('login_page.png', folder='demos/screenshots')
        self.click('input[type="submit"]')
        self.save_screenshot('admin_page.png', folder='demos/screenshots')

        self.click('link=VIEW SITE')

        self.click('.glyphicon-plus')
        self.save_screenshot('add_new_post.png', folder='demos/screenshots')
        self.type('#id_title', 'Star Wars IX: The Rise of Skywalker')
        self.type('#id_text', 'Star Wars IX: The Rise of Skywalker will be released on December 18, 2019. ')

        self.click('button[type="submit"].save')

        self.click('.publish')
        self.open(home_page)
        self.save_screenshot('posts_list.png', folder='demos/screenshots')

        self.click('link=Star Wars IX: The Rise of Skywalker')
        self.click('.add-comment')
        self.save_screenshot('add_comment.png', folder='demos/screenshots')
        self.type('#id_author', 'Yoda')
        self.type('#id_text', 'Happy I am ❤️')
        self.click('button[type="submit"].save')

        self.click('.add-comment')
        self.type('#id_author', 'Han Solo')
        self.type('#id_text', 'Am I invited? 💔')
        self.click('button[type="submit"].save')

        self.save_screenshot('posts_list_with_comments.png', folder='demos/screenshots')

        self.click('.glyphicon-remove')

        self.click('link=Log out')
