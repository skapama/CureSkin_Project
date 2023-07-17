from pages.globalnav import Globalnav
from pages.main_page import MainPage
from pages.search_results import SearchResultsPage


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.globalnav = Globalnav(self.driver)
        self.main_page = MainPage(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)