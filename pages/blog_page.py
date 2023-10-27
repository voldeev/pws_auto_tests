from playwright.sync_api import Page


def open(page: Page):
    page.goto("https://frontend.pws-stg.px-dev.com/blog/")
    page.wait_for_load_state('load')
    assert _is_page_ready(page), "Blog page is not ready to be used"


def _is_page_ready(page: Page):
    blog_page_title_locator = page.locator("h3.blog__title")
    return blog_page_title_locator.is_visible()


def select_education_category(page):
    education_category_locator = page.locator("//nav[@class='blog__navigation']//a[text()='Education']")
    education_category_locator.click()


def get_education_post_locator(page: Page):
    return page.locator("//span[contains(text(), 'Paid Advertising for Photographers')]")


def select_news_category(page):
    news_category_locator = page.locator("//nav[@class='blog__navigation']//a[text()='News']")
    news_category_locator.click()


def get_news_category_post_locator(page: Page):
    return page.locator("//span[contains(text(), 'Pixellu SmartAlbums: New Imageless Spreads and In-App Updates')]")


def select_stories_category(page):
    stories_category_locator = page.locator("//nav[@class='blog__navigation']//a[text()='Stories']")
    stories_category_locator.click()


def get_stories_categories_post_locator(page: Page):
    return page.locator("//span[contains(text(), 'The Wilkinsons \"Live the Best Life\"')]")
