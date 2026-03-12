import pytest

from authworks01.corebase.auth.auth_state_manager import AuthStateManager
from authworks01.corebase.auth.browser_manager import BrowserManager


def pytest_addoption(parser):

        parser.addoption(
            "--browser",
            action="store",
            default="chromium",
            help="Browser type: chromium | firefox | webkit"
        )

        parser.addoption(
            "--headed",
            action='store_true',
            # action="store_true",
            help="Run browser in headed mode"
        )

# browser_name = request.config.getoption("--browser")
# headed = request.config.getoption("--headed")

# @pytest.fixture(scope="session")
# def browser_manager():
#     manager = BrowserManager()
#     yield manager
#     manager.close()

@pytest.fixture(scope="session")
def browser_manager(request):

    browser_name = request.config.getoption("--browser")
    headed = request.config.getoption("--headed")

    manager = BrowserManager(browser_name=browser_name, headless=not headed)
    yield manager
    manager.close()





@pytest.fixture
def admin_page(browser_manager):

    storage = AuthStateManager.get_storage_path("admin")

    if storage.exists():
        context = browser_manager.new_context(storage)
    else:
        context = browser_manager.new_context()
    page = context.new_page()

    page.goto("https://phptravels.net/admin/dashboard",timeout=25000)

    # detect login page
    if page.locator("input[name='email']").is_visible():

        AuthStateManager.login_and_save(page, "admin")
        context.close()
        context = browser_manager.new_context(storage)
        page = context.new_page()
    yield page
    context.close()


@pytest.fixture
def user_page(browser_manager):

    storage = AuthStateManager.get_storage_path("user")

    if storage.exists():
        context = browser_manager.new_context(storage)
    else:
        context = browser_manager.new_context()
    page = context.new_page()

    page.goto("https://phptravels.net/dashboard",timeout=25000)

    # detect login page
    if page.locator("input[name='email']").is_visible():

        AuthStateManager.login_and_save(page, "user")
        context.close()
        context = browser_manager.new_context(storage)
        page = context.new_page()
    yield page
    context.close()


# @pytest.fixture
# def admin_page(browser_manager):
#     storage = AuthStateManager.ensure_auth_state(browser_manager, "admin")
#     context = browser_manager.new_context(storage)
#     page = context.new_page()
#     yield page
#     context.close()


# @pytest.fixture
# def user_page(browser_manager):
#     storage = AuthStateManager.ensure_auth_state(browser_manager, "user")
#     context = browser_manager.new_context(storage)
#     page = context.new_page()
#     yield page
#     context.close()