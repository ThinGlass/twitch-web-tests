import pytest

from playwright.sync_api import Page
from pages.twitch_home import TwitchHomePage
from pages.categories_page import CategoriesPage


@pytest.mark.debug
def test_twitch_streamer(page: Page):
    viewport_size = page.viewport_size
    assert viewport_size["width"] == 360  # S24 screen width

    # home page interactions
    home_page = TwitchHomePage(page)
    home_page.navigate()
    home_page.accept_keep_using_web()
    home_page.accept_cookies()
    home_page.click_browse()

    # categories page interactions
    categories_page = CategoriesPage(page)
    categories_page.search_for_game("starcraft ii")
    categories_page.page.mouse.wheel(0, 200)
    streamers = categories_page.get_all_streamers()
    streamers[0].click()
    categories_page.page.screenshot(path="output.png")
