from playwright.sync_api import Page


def open(page: Page):
    page.goto("https://frontend.pws-stg.px-dev.com/smartslides/pricing/")
    page.wait_for_load_state('load')
    assert _is_page_ready(page), "SA pricing page is not ready to be used"


def _is_page_ready(page: Page):
    pss_pricing_page_title_locator = page.locator("section.pricing-container")
    return pss_pricing_page_title_locator.is_visible()


def get_pss_pricing_page_locator(page: Page):
    return page.locator("section.pricing-container")


def get_abb_question_locator(page: Page):
    return page.locator("span >> text='What is included in the All Apps Bundle?'")
