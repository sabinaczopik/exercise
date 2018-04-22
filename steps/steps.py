import time

from behave import *
from data import UserData


@given('the main page is open')
def step_impl(context):
    user = UserData()
    context.browser.open_page(user.shered_link)


@when('I enter "{variety}" password')
def step_impl(context, variety):
    context.login_page.enter_password(variety)


@when('I submit it')
def step_impl(context):
    context.login_page.primary_btn.click()


@then('I\'m logged in user')
def step_impl(context):
    assert context.top_bar.folder_link_top_bar


@then('the validation mesage appers')
def step_impl(context):
    assert context.login_page.error_msg


@given('I\'m logged in user')
def step_impl(context):
    context.login_page.login_to_service()


@when('I choose sort by "{data_sort}" data')
def step_impl(context, data_sort):
    context.top_bar.choose_data_sort(data_sort)


@when('I choose "{data_order}" order')
def step_impl(context, data_order):
    context.top_bar.choose_data_order(data_order)


@then('the elements are sorted by "{data_order}" name')
def step_impl(context, data_order):
    context.top_bar.sort_elements(data_order)


@when('I choose preview selected files')
def step_impl(context):
    context.folder_item.preview_icon.click()


@then('the I see preview')
def step_impl(context):
    context.folder_item.files_preview
