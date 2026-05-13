from playwright.sync_api import sync_playwright


def before_scenario(context, scenario):
    # Customer code calls `chromium.launch()` directly. The BrowserStack SDK
    # monkeypatches Playwright at runtime so this launch is routed to the
    # browser configured in the platform entry the SDK is currently driving
    # — works unchanged for chromium, firefox, and webkit platforms.
    context.pw = sync_playwright().start()
    context.browser = context.pw.chromium.launch()
    context.page = context.browser.new_page()


def after_scenario(context, scenario):
    try:
        context.browser.close()
    finally:
        context.pw.stop()
