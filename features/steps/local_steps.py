from behave import given, then


LOCAL_URL = "http://localhost:45454/"
EXPECTED_HEADING = "BrowserStack Local Sample"


@given("I visit the local sample page")
def visit_local(context):
    context.page.goto(LOCAL_URL)


@then("I should see the local sample heading")
def verify_local_heading(context):
    heading = context.page.locator("h1").text_content()
    assert heading == EXPECTED_HEADING, (
        f"expected {EXPECTED_HEADING!r}, got {heading!r}"
    )
