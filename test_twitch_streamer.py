import pytest

from playwright.sync_api import Page
from pages.twitch_home import TwitchHomePage


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

    # page.get_by_role("searchbox", name="Search").click()
    # page.get_by_role("searchbox", name="Search").fill("starcraft ii")
    # page.get_by_role("searchbox", name="Search").press("Enter")
    # page.screenshot(path="1_before_scroll.png")
    # page.mouse.wheel(0, 200)
    # page.screenshot(path="2_after_scroll.png")
    # live_streamers = page.get_by_role("button", name="Live").all()
    # print(live_streamers)

    # live_streamers[0].click()
    # page.screenshot(path="3_streamer_page.png")
