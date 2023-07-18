from selenium.webdriver.common.by import By
from pages.base_page import Page

class Header(Page):
    SEARCH_FIELD = (By.XPATH, "//div[contains(@id, 'shopify-section-header')]")
    SEARCH_ICON = (By.CSS_SELECTOR, '#shopify-section-header > sticky-header > header > search-modal')

    def search_amazon(self, search_query):
        self.input_text(search_query, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_ICON)