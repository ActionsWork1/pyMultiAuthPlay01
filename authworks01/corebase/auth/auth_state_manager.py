from pathlib import Path

from authworks01.corebase.auth.settings import BASE_URL, USERS
from authworks01.pages.login_page import LoginPage


class AuthStateManager:

    STORAGE_DIR = Path("storage")

    @classmethod
    def get_storage_path(cls, role):
        cls.STORAGE_DIR.mkdir(exist_ok=True)
        return cls.STORAGE_DIR / f"{role}.json"

    @classmethod
    def login_and_save(cls, page, role):
        user = USERS[role]

        login = LoginPage(page)
        login.navigate()
        login.login(user["email"], user["password"])
        page.context.storage_state(path=cls.get_storage_path(role))

    # @classmethod
    # def ensure_auth_state(cls, browser_manager, role):
    #
    #     storage_path = cls.get_storage_path(role)
    #     # CASE 1: storage file exists
    #     if storage_path.exists():
    #
    #         context = browser_manager.new_context(storage=str(storage_path))
    #         page = context.new_page()
    #         page.goto(BASE_URL)
    #         login = LoginPage(page)
    #
    #         # if login page visible -> session expired
    #         if login.is_login_page():
    #             context.close()
    #             return cls.refresh_auth(browser_manager, role)
    #         return storage_path
    #
    #     # CASE 2: storage file not exist
    #     return cls.refresh_auth(browser_manager, role)


    # @classmethod
    # def refresh_auth(cls, browser_manager, role):
    #
    #     storage_path = cls.get_storage_path(role)
    #
    #     user = USERS[role]
    #
    #     context = browser_manager.new_context()
    #     page = context.new_page()
    #
    #     login = LoginPage(page)
    #     login.navigate()
    #
    #     login.login(user["email"], user["password"])
    #     page.context.storage_state(path=storage_path)
    #
    #     context.close()
    #
    #     return storage_path