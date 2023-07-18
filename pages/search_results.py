from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep



class SearchResults(Page):
    RESULT_TEXT = (By.CSS_SELECTOR, '#ProductCount')
    PRODUCT_APPLIED = (By.CSS_SELECTOR, '#product-grid > li:nth-child(1) > div > a')
    SORT_BTN = (By.CSS_SELECTOR, '#FacetFiltersForm > div > div > div > details > summary > span')
    PRICE_SORT = (By.CSS_SELECTOR, '#Filter-price-descending-3')
    SEARCH_FIELD = (By.XPATH, "//div[contains(@id, 'shopify-section-header')]")
    SEARCH_ICON = (By.CSS_SELECTOR, '#shopify-section-header > sticky-header > header > search-modal')

def open_shop(self):
    self.open_url('https://shop.cureskin.com/search')

def click_search_icon(self):
    self.search(self, *self.SEARCH_ICON)
    sleep(4)
    self.click(*self.SEARCH_FIELD)
    sleep(4)

def input_text(self, text):
    self.input_text(text, *self.SEARCH_FIELD)
    sleep(4)
    self.click(*self.SEARCH_ICON)
    sleep(4)

def select_price(self):
    self.click(*self.SORT_BTN)
    sleep(2)
    self.click(*self.PRICE_SORT)
    sleep(4)


def verify_filter_applied(context):
    all_filter = context.driver.find_elements(*self.RESULT_TEXT)
    print(all_filter)

    for product in all_filter:
        product_name = product.find_element(*self.PRODUCT_APPLIED).text
        print(product_name)
        assert product_name, 'Filter should select high to low'
        assert product.find_element(*self.RESULT_TEXT).is_displayed(), 'Filter not applied'