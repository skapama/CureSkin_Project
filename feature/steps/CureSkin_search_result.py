from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

RESULT_TEXT = (By.CSS_SELECTOR, '#ProductCount')
PRODUCT_APPLIED = (By.CSS_SELECTOR,'#product-grid > li:nth-child(1) > div > a' )
SORT_BTN = (By.CSS_SELECTOR, '#FacetFiltersForm > div > div > div > details > summary > span')
PRICE_SORT = (By.CSS_SELECTOR, '#Filter-price-descending-3')
SEARCH_FIELD = (By.XPATH, "//div[contains(@id, 'shopify-section-header')]")
SEARCH_ICON = (By.CSS_SELECTOR, '#shopify-section-header > sticky-header > header > search-modal')


@given('Open Cureskin main page')
def open_amazon(context):
     #context.driver.get('https://shop.cureskin.com/')
    context.app.main_page.open_main_page()

@when('Click on search icon')
def click_search(context):
    context.driver.find_element(*SEARCH_ICON).click()
    #context.app.globalnav.click_search()
    sleep(2)

@when('Input text {text}')
def input_text(context, text):
    #context.driver.find_element(*SEARCH_FILED).send_keys('cure')
    #context.app.globalnav.input_search_text(text)
    context.driver.find_element(*SEARCH_FIELD).send_keys('text')
    context.driver.find_element(*SEARCH_ICON).click()

@when('Click price sort button')
def price_sort_btn(context):
    context.driver.find_element(*SORT_BTN).click()
    #context.app.globalnav.click_sort()
    sleep(2)

@when('Click price high to low')
def price_sort(context):
    context.driver.find_element(*PRICE_SORT).click()
    #context.app.globalnav.click_price_sort()
    sleep(2)

@then('Verify filter applied')
def verify_filter_applied(context):
    all_products = context.driver.find_elements(*RESULT_TEXT)
    print(all_products)

    for product in all_products:
        product_name = product.find_element(*PRODUCT_APPLIED).text
        print(product_name)
        assert product_name, 'Product section should not be blank'
        assert product.find_element(*RESULT_TEXT).is_displayed(), 'Product not found'