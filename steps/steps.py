import time

from behave import *


@given('the main page is open')
def step_impl(context):
    context.browser.open_page('https://qarecruitment.egnyte.com/fl/ZlhEpCQ89o')


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


@then('Then the elemnts are sorted by "{data_order}}" name')
def step_impl(context, data_order):
    context.top_bar.sort_elements(data_order)


@when('I select current folder')
def step_impl(context):
    context.top_bar.select_all_checkbox.click()


@when('I click on submit download button')
def step_impl(context):
    context.top_bar.download_btn.click()
    time.sleep(5)


@then('the current folder is dwonloaded')
def step_impl(context):
    context.top_bar.confirm_download()
