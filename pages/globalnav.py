from selenium.webdriver.common.by import By
from pages.base_page import Page

class Globalnav(Page):
    SEARCH_FILED = (By.CSS_SELECTOR, '#shopify-section-header > sticky-header > header > search-modal > details > div > div.page-width > div > predictive-search > form > div.field')
    SEARCH_ICON = (By.XPATH, "//div[contains(@id, 'shopify-section-header')]")

def search_cureskin(self, search_query):
    self.input_text(search_query, *self.SEARCH_FIELD)
    self.click(*self.SEARCH_ICON)

#def input_text(self, text):
    #self.input_text(text, *self.SEARCH_FIELD)
    #self.click(*self.SEARCH_FIELD)




