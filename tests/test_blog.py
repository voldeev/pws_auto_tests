from playwright.sync_api import Page, expect
from pages import blog_page


def test_correct_posts_are_displayed_in_education_category(page: Page):
    blog_page.open(page)
    blog_page.select_education_category(page)
    education_category_post_locator = blog_page.get_education_post_locator(page)
    expect(education_category_post_locator).to_be_visible(), "Education post is not displayed in the Education category"
    news_post_locator = blog_page.get_news_category_post_locator(page)
    expect(news_post_locator).not_to_be_visible(), "Incorrect post is displayed in the category"


def test_correct_posts_are_displayed_in_news_category(page: Page):
    blog_page.open(page)
    blog_page.select_news_category(page)
    news_category_post_locator = blog_page.get_news_category_post_locator(page)
    expect(news_category_post_locator).to_be_visible(), "News post is not displayed in the News category"
    education_post_locator = blog_page.get_education_post_locator(page)
    expect(education_post_locator).not_to_be_visible(), "Incorrect post is displayed in the category"


def test_correct_posts_are_displayed_in_stories_category(page: Page):
    blog_page.open(page)
    blog_page.select_stories_category(page)
    stories_category_post_locator = blog_page.get_stories_categories_post_locator(page)
    expect(stories_category_post_locator).to_be_visible(), "Stories post is not displayed in the Stories category"
    news_post_locator = blog_page.get_news_category_post_locator(page)
    expect(news_post_locator), "Incorrect post is displayed in the category"
