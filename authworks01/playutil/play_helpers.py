import allure
from playwright.sync_api import Page


class PlayHelper:

    # def __init__(self,page:Page):
    #     self.page = page
    @staticmethod
    def attach_base64_to_allure(page:Page,file_name="screenshot"):
        png_bytes = page.screenshot()

        # allure.attach(page.screenshot(),
        #               name=file_name,
        #               attachment_type=allure.attachment_type.PNG,
        #               extension=png_bytes
        #               )

        allure.attach(body=page.screenshot(),
                      name=file_name,
                      attachment_type=allure.attachment_type.PNG
                      )