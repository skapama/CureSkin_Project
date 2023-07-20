from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class SearchResultsPage(Page):
    SEARCH_BUTTON = (By.CSS_SELECTOR, "#predictive-search-option-search-keywords > button")
    SEARCH_BOX = (By.ID, "Search-In-Template")
    SORT = (By.CSS_SELECTOR, "#FacetFiltersForm > div > div > div > details > summary")
    SORT_BY_PRICE_DESCENDING = (
    By.CSS_SELECTOR, "#FacetFiltersForm > div > div > div > details > div > ul > li:nth-child(3)")
    LAST_PAGE = (By.CSS_SELECTOR, 'a.pagination__item[aria-label="Page 3"]')

    def open_search_page(self):
         self.open_url('https://shop.cureskin.com/search')

    def search_cureskin(self, product):
         self.input_text(product, *self.SEARCH_BOX)
         sleep(4)
         self.click(*self.SEARCH_BUTTON)
         sleep(4)

    def select_filter_price_descending(self):
         self.click(*self.SORT)
         sleep(2)
         self.click(*self.SORT_BY_PRICE_DESCENDING)
         sleep(4)

    def verify_sort_descending(self):
         price_elements_first_page = self.find_elements(By.CLASS_NAME, 'price__sale')
         first_price_text = price_elements_first_page[0].text.split('\n')[-1].strip('Rs.').replace(',', '')
         first_price = float(first_price_text)
         self.click(*self.LAST_PAGE)
         sleep(2)
         price_elements_last_page = self.find_elements(By.CLASS_NAME, 'price__sale')
         last_price_text = price_elements_last_page[-1].text.split('\n')[-1].strip('Rs.').replace(',', '')
         last_price = float(last_price_text)
         print(f"The highest prise is: {first_price}, the lowest price is: {last_price}")
         assert first_price > last_price, "Filter is not applied correctly"