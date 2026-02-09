import logging

from playwright.sync_api import Page

logger = logging.getLogger(__name__)


class TwitchHomePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        self.page.goto("https://www.twitch.tv")
        logger.info("Home page opened")

    def accept_keep_using_web(self):
        self.page.get_by_role("button", name="Keep using web").click()
        logger.info("Web browser selected")

    def accept_cookies(self):
        self.page.get_by_role("button", name="Accept").click()
        logger.info("All cookies accepted")

    def click_browse(self):
        self.page.get_by_role("link", name="Browse").click()
        logger.info("Browse button clicked")
