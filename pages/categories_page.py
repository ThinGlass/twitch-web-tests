import logging

from playwright.sync_api import Page

logger = logging.getLogger(__name__)


class CategoriesPage:
    def __init__(self, page: Page):
        self.page = page

    def search_for_game(self, game_name: str):
        searchbox = self.page.get_by_role("searchbox", name="Search")
        searchbox.click()
        logger.info("Searchbox clicked")
        searchbox.fill(game_name)
        logger.info(f"Game name entered: {game_name}")
        searchbox.press("Enter")
        logger.info("Enter button pressed")

    def get_all_streamers(self) -> list:
        # get all the locators for the live streamers
        all_locators = self.page.get_by_role("button", name="live").all()
        logger.info("Locators for live streamers collected")
        logger.debug(f"Locators list: {all_locators}")
        return all_locators
