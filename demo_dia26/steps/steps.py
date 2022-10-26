from behave import given, when, then
from source.homepage import HomePage
import time


@given("url '{url}' opened")
def step_impl(context, url):
    context.driver.get(url)
    context.homepage = HomePage(context.driver)


@when("open signup link")
def step_impl(context):
    context.homepage.open_signup_form()


@when("open login link")
def step_impl(context):
    context.homepage.open_login_form()


@when("open laptop section")
def step_impl(context):
    context.homepage.open_laptop_section()


@when("open item '{item}'")
def step_impl(context, item):
    context.homepage.open_item(item)


@when("fill signup form with '{username}' and '{password}'")
def step_impl(context, username, password):
    time.sleep(1)
    context.signup_confirmation = context.homepage.fill_signup_form(user=username, password=password)


@when("fill login form with '{username}' and '{password}'")
def step_impl(context, username, password):
    time.sleep(2)
    context.signup_confirmation = context.homepage.fill_login_form(user=username, password=password)


@then("check signup confirmation")
def step_impl(context):
    assert context.signup_confirmation == "This user already exist."


@when("add item to cart")
def step_impl(context):
    context.homepage.add_to_cart()