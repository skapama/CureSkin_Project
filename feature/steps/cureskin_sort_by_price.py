from behave import given, when, then


@given("Opens cureskin Search page")
def open_browser(context):
    context.app.search_results.open_search_page()


@when("Searches for the {product}")
def search(context, product):
    context.app.search_results.search_cureskin(product)


@when("Selects sort by price, high to low")
def select_sort_high_to_low(context):
    context.app.search_results.select_filter_price_descending()


@then('Verifies filter applied')
def verify_sort_high_to_low(context):
    context.app.search_results.verify_sort_descending()