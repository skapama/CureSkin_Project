from pages.base_page import Page

class MainPage(Page):

    def open_shop(self):
        self.open_url('https://shop.cureskin.com/')

