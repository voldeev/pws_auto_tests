from playwright.sync_api import expect, Page

from pages import psf_pricing_page, sa_pricing_page, pss_pricing_page


def test_user_should_be_able_to_use_faq_on_psf_pricing_page(page: Page):
    psf_pricing_page.open(page)
    psf_pricing_page_title_locator = psf_pricing_page.get_psf_pricing_page_locator(page)
    expect(psf_pricing_page_title_locator).to_be_visible(), "FAQ titles is not displayed on PSF Pricing page"
    abb_question_locator = psf_pricing_page.get_abb_question_locator(page)
    expect(abb_question_locator).to_be_visible(), "FAQ can`t be opened on PSF Pricing page"


def test_user_shoudl_be_able_to_use_faq_in_sa_pricing_page(page: Page):
    sa_pricing_page.open(page)
    sa_pricing_page_title_locator = sa_pricing_page.get_sa_pricing_page_locator(page)
    expect(sa_pricing_page_title_locator).to_be_visible(), "FAQ titles is not displayed on SA Pricing page"
    abb_question_locator = sa_pricing_page.get_abb_question_locator(page)
    expect(abb_question_locator).to_be_visible(), "FAQ can`t be opened on SA Pricing page"


def test_user_should_be_able_to_use_faq_on_pss_pricing_page(page: Page):
    pss_pricing_page.open(page)
    pss_pricing_page_title_locator = pss_pricing_page.get_pss_pricing_page_locator(page)
    expect(pss_pricing_page_title_locator).to_be_visible(), "FAQ titles is not displayed on PSS Pricing page"
    abb_question_locator = pss_pricing_page.get_abb_question_locator(page)
    expect(abb_question_locator).to_be_visible(), "FAQ can`t be opened on PSS Pricing page"
