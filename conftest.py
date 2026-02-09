import logging

import pytest

logger = logging.getLogger(__name__)


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright):
    logger.info("Setting device to Galaxy S24")
    return {
        **browser_context_args,
        **playwright.devices["Galaxy S24"],
    }
