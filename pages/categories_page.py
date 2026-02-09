from playwright.sync_api import Page


class CategoriesPage:
    def __init__(self, page: Page):
        self.page = page

    def search_for_game(self, game_name: str):
        searchbox = self.page.get_by_role("searchbox", name="Search")
        searchbox.click()
        searchbox.fill(game_name)
        searchbox.press("Enter")

    def get_all_streamers(self) -> list:
        # get all the locators for the live streamers
        return self.page.get_by_role("button", name="live").all()
