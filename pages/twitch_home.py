from playwright.sync_api import Page


class TwitchHomePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        self.page.goto("https://www.twitch.tv")

    def accept_keep_using_web(self):
        self.page.get_by_role("button", name="Keep using web").click()

    def accept_cookies(self):
        self.page.get_by_role("button", name="Accept").click()

    def click_browse(self):
        self.page.get_by_role("link", name="Browse").click()
