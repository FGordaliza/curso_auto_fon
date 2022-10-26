from behave import given, when, then
from src.homepage import HomePage
from src.contactpage import ContactPage


@given("a webpage '{url}'")
def step_impl(context, url):
    context.driver.get(url)
    context.homepage = HomePage(context.driver)


@when("Accept cookies")
def step_impl(context):
    context.homepage.accept_cookies()
    print(context.text)


@when("open contact page")
def step_impl(context):
    context.homepage.open_contact_page()
    context.contact_page = ContactPage(context.driver)
    for row in context.table:
        for cell in row:
            print(cell)


@then("Check we are here text is '{text}'")
def step_impl(context, text):
    text_from_web = context.contact_page.print_text_we_are_here()
    assert text_from_web == text