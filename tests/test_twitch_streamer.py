import pytest
import allure

from playwright.sync_api import Page
from pages.twitch_home import TwitchHomePage
from pages.categories_page import CategoriesPage


@pytest.mark.smoke
def test_twitch_streamer(page: Page):
    with allure.step("Check the viewport size"):
        viewport_size = page.viewport_size
        assert viewport_size["width"] == 360  # S24 screen width

    # home page interactions
    with allure.step("Open Twitch page"):
        home_page = TwitchHomePage(page)
        home_page.navigate()
        assert home_page.page.title() == "Twitch"

    with allure.step("Stay in browser and accept cookies"):
        home_page.accept_keep_using_web()
        home_page.accept_cookies()

    with allure.step("Open the Categories page"):
        home_page.click_browse()
        categories_page = CategoriesPage(page)

    with allure.step("Search for Starcrat II"):
        categories_page.search_for_game("starcraft ii")

    with allure.step("Scroll down"):
        categories_page.page.mouse.wheel(0, 200)

    with allure.step("Click on the first streamer"):
        streamers = categories_page.get_all_streamers()
        assert len(streamers) > 0
        streamers[0].click()

    with allure.step("Take screenshot"):
        categories_page.take_screenshot()
