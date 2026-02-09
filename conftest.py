import pytest


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright):
    return {
        **browser_context_args,
        **playwright.devices["Galaxy S24"],
    }
