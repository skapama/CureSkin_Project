from behave import given, when, then


@given("Open Cureskin shop page")
def open_main_page(context):
    context.app.main_page.open_shop()

@when('Click on search icon')
def click_search(context):
    context.app.search_results.click_search_icon()

@when("Input text {text}")
def input_words(context, text):
    context.app.search_results.input_text(text)


@when("Select price high to low")
def filter_applied(context):
    context.app.search_results.select_price()


@then("verify filter applied")
def verify_price(context):
    context.app.search_results.verify_filter_applied()
