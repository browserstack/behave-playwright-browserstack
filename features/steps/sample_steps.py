from behave import given, when, then


@given("I visit bstackdemo website")
def visit_bstackdemo(context):
    context.page.goto("https://www.bstackdemo.com/")
    assert context.page.title() == "StackDemo"


@when("I add a product to the cart")
def add_product(context):
    product_locator = context.page.locator('xpath=//*[@id="1"]/p')
    context.product_on_page_text = product_locator.text_content()
    context.page.locator('xpath=//*[@id="1"]/div[4]').click()


@then("I should see same product in cart section")
def verify_cart(context):
    cart = context.page.locator('xpath=//*[@class="float-cart__content"]')
    cart.wait_for(state="visible")
    cart_product_locator = context.page.locator(
        'xpath=//*[@id="__next"]/div/div/div[2]/div[2]/div[2]/div/div[3]/p[1]'
    )
    product_on_cart_text = cart_product_locator.text_content()
    assert product_on_cart_text == context.product_on_page_text, (
        f"expected {context.product_on_page_text!r} in cart, got {product_on_cart_text!r}"
    )
