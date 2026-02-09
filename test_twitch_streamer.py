import pytest

from playwright.sync_api import Page


@pytest.mark.smoke
def test_twitch_streamer(page: Page):
    viewport_size = page.viewport_size
    assert viewport_size["width"] == 360  # S24 screen width

    page.goto("https://www.twitch.tv")

    page.get_by_role("button", name="Keep using web").click()
    page.get_by_role("button", name="Accept").click()

    page.get_by_role("link", name="Browse").click()
    page.get_by_role("searchbox", name="Search").click()
    page.get_by_role("searchbox", name="Search").fill("starcraft ii")
    page.get_by_role("searchbox", name="Search").press("Enter")
    page.screenshot(path="1_before_scroll.png")
    page.mouse.wheel(0, 200)
    page.screenshot(path="2_after_scroll.png")
    live_streamers = page.get_by_role("button", name="Live").all()
    print(live_streamers)

    live_streamers[0].click()
    page.screenshot(path="3_streamer_page.png")
