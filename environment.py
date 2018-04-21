from browser import Browser

from pages import pages


def before_all(context):
    context.browser = Browser()
    context.login_page = pages.Login()
    context.top_bar = pages.TopBar()


def after_scenario(context, scenario):
    context.browser.delete_cookies()


def after_step(context, step):
    if step.status == 'failed':
        step_str = context.scenario.name + " " + step.name
        context.browser.screen_shot(step_str)


def after_all(context):
    context.browser.quit()
