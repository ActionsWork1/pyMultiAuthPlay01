from playwright.sync_api import sync_playwright

from authworks01.corebase.config.browser_config import BROWSER_CONFIG

class BrowserManager:

    def __init__(self, browser_name="chromium", headless=True):

        self.playwright = sync_playwright().start()
        if browser_name == "chromium":
            self.browser = self.playwright.chromium.launch(headless=headless)

        elif browser_name == "firefox":
            self.browser = self.playwright.firefox.launch(headless=headless)

        elif browser_name == "webkit":
            self.browser = self.playwright.webkit.launch(headless=headless)

        else:
            raise ValueError(f"Unsupported browser: {browser_name}")

    def new_context(self, storage=None, **context_options):

        if storage:
            context_options["storage_state"] = storage
        return self.browser.new_context(**context_options)


    def close(self):
        self.browser.close()
        self.playwright.stop()

# class BrowserManager:
#
#     def __init__(self):
#         self.playwright = sync_playwright().start()
#         browser_name = BROWSER_CONFIG["browser_name"]
#         headless = BROWSER_CONFIG["headless"]
#
#         print(f"Browser: {browser_name}")
#
#         if browser_name == "chromium":
#             self.browser = self.playwright.chromium.launch(headless=headless)
#
#         elif browser_name == "firefox":
#             self.browser = self.playwright.firefox.launch(headless=headless)
#
#         elif browser_name == "webkit":
#             self.browser = self.playwright.webkit.launch(headless=headless)
#
#         else:
#             raise Exception(f"Unsupported browser: {browser_name}")
#
#
#     def new_context(self, storage=None):
#         context_config = BROWSER_CONFIG["context"]
#         mode = BROWSER_CONFIG["mode"]
#         context_options = context_config.copy()
#
#         if storage:
#             context_options["storage_state"] = storage
#         # Device emulation
#         if mode == "device":
#             device_name = BROWSER_CONFIG["device"]
#             device = self.playwright.devices[device_name]
#             context_options.update(device)
#         return self.browser.new_context(**context_options)

#     def close(self):
#         self.browser.close()
#         self.playwright.stop()



## older version of class
# class BrowserManager:
#
#     def __init__(self):
#         self.playwright = sync_playwright().start()
#         self.browser = self.playwright.chromium.launch(headless=False)
#
#     def new_context(self, storage=None):
#         if storage:
#             return self.browser.new_context(storage_state=storage)
#         return self.browser.new_context()
#
#     def close(self):
#         self.browser.close()
#         self.playwright.stop()