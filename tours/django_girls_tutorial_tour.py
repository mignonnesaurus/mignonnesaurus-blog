from seleniumbase import BaseCase


class DjangoGirlsTutorialTour(BaseCase):
    def test_django_girl_tutorial(self):
        self.open('https://tutorial.djangogirls.org/en/')
        self.maximize_window()

        self.wait_for_element('input[type="text"]')

        self.create_bootstrap_tour()
        self.add_tour_step('Welcome to the Django Girls Tutorial!', title='Django Girls Tutorial Tour')
        self.add_tour_step("You can look for content here :)", 'input[type="text"]')
        self.play_tour()

        self.highlight_update_text('input[type="text"]', 'Installation')

        self.create_bootstrap_tour()
        self.add_tour_step("And find your results here", '.search-results')
        self.play_tour()

        self.create_bootstrap_tour()
        self.add_tour_step("Start with the installation :)", '.search-results-item')
        self.play_tour()

        self.click("link=Installation")

        self.create_bootstrap_tour()
        self.add_tour_step("Doing the tutorial at home?", '#if-youre-doing-the-tutorial-at-home')
        self.add_tour_step("At the installation party?", '#if-youre-attending-a-workshop')
        self.play_tour()

        self.create_bootstrap_tour()
        self.add_tour_step("At the installation party?", '#if-youre-attending-a-workshop')
        self.play_tour()

        self.create_bootstrap_tour()
        self.add_tour_step("Now, let's read how the Internet works :)", 'input[type="text"]')
        self.play_tour()

        self.highlight_update_text('input[type="text"]', 'How the Internet works')

        self.create_bootstrap_tour()
        self.add_tour_step("Here we are!", '.search-results-item')
        self.play_tour()

        self.click("link=How the Internet works")

        self.create_bootstrap_tour()
        self.add_tour_step("Yay! Have fun! 💛", '#how-the-internet-works')
        self.play_tour()
