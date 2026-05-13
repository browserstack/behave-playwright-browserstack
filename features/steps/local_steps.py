from behave import given, then


@given("I visit local app website")
def visit_local_app(context):
    context.page.goto("http://bs-local.com:45454/")


@then('the page title should contain "{expected}"')
def verify_title_contains(context, expected):
    title = context.page.title()
    assert expected in title, (
        f"expected title to contain {expected!r}, got {title!r}"
    )
