from selenium.webdriver.common.by import By
from pages.base_page import Page

class SearchResultsPage(Page):
    RESULT_TEXT = (By.CSS_SELECTOR, '#ProductCount')
    PRODUCT_APPLIED = (By.CSS_SELECTOR, '#product-grid > li:nth-child(1) > div > a')


def verify_search_results(self, expected_result):
    self.verify_element_text(expected_result, *self.RESULT_TEXT)

def verify_search_results(self, expected_result):
    self.verify_element_text(expected_result, *self.PRODUCT_APPLIED)

        ### Class example (we didn't have verify_element_text() in base Page):
        # actual_result = self.driver.find_element(*self.RESULT_TEXT).text
        # assert expected_result == actual_result, \
        #     f'Error! Expected {expected_result} bot got actual {actual_result}'