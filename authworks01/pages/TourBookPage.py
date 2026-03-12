import time
from datetime import datetime
from xml.sax.xmlreader import Locator

import pytest
from playwright._impl._page import Page
from playwright.sync_api import expect


class TourBookPage: #(Page):
    def __init__(self, page:Page):
        self.page = page
        self.dest_clear_btn = self.page.locator("button[x-show='destinationSelected && !destinationLoading']")
        self.dest_txt = self.page.locator('input[x-ref="destinationInput"]')
        self.duration_dropdown =self.page.locator('div.input-dropdown>div').nth(0)
        self.duration_option_layout = self.page.locator('div.input-dropdown>div').nth(1)
        self.duration_options = self.page.locator("div.input-dropdown-content.show>div.gap-2")
        self.search_BTN = self.page.locator("button[type='submit']")

        # self.desti_options_layout = self.page.locator(
        #     "div[x-show='destinationShouldShowDropdown || destinationShowNoResults']")
        # self.desti_options = self.page.locator("div.p-3>div.gap-3")

    def book_tour(self,tour_city='London'):

        if self.dest_clear_btn.is_visible(timeout=15000):
           self.dest_clear_btn.click()

        self.dest_txt.press_sequentially(tour_city) #,delay=500,timeout=3000) #,timeout=2000)
        self.page.wait_for_selector("div[x-show='destinationShouldShowDropdown || destinationShowNoResults']",state="attached",timeout=15000)
        # time.sleep(0.2)
        _destilayout = self.page.locator("div[x-show='destinationShouldShowDropdown || destinationShowNoResults']")
        desti_options =  _destilayout.locator("div.flex.items-center.gap-3 div.items-center.gap-2>span:nth-child(1)")
        # pytest.set_trace()

        expect(_destilayout).to_be_visible(visible=True, timeout=10000)
        self.choose_destination_from_list(_destilayout, desti_options)

        # select day in current month
        d1 = today_month_day()
        d = int(d1)+2
        self.page.locator("input[name='start_date']").click()
        time.sleep(0.3)
        self.page.locator(f"td.p-0>div:has-text('{d}')").click()
        time.sleep(0.2)

        # select duration of vacation
        self.duration_dropdown.click()
        time.sleep(0.3)
        if self.duration_option_layout.is_visible(timeout=15000):
            self.duration_options.nth(2).click()

        self.search_BTN.click()
        time.sleep(0.2)
        for x in range(1,100):
            if self.page.locator("span:has-text('Suppliers...')").first.is_visible():
                time.sleep(0.1*x)
            else:
                print(f"search completed in {0.1*x} secs")
                break

        self.page.wait_for_selector("div.mb-4>div.justify-between.gap-3>h2>span",state="attached",timeout=15000)
        search_result_text = self.page.locator("div.mb-4>div.justify-between.gap-3>h2>span").nth(1)
        if search_result_text.is_visible(timeout=25000):
           print(search_result_text.text_content())


    def choose_destination_from_list(self,_destilayout,_destioptions):
       """
       :description: choose a destination from a list of destination layout
       :param self:
       :param _destilayout:
       :param _destioptions:
       :return:
       """
       # desti_options_layout = self.page.locator("div[x-show='destinationShouldShowDropdown || destinationShowNoResults']")
       # desti_options = self.page.locator("div.p-3>div.gap-3")
       print(" ")
       print("choose layout...")
       if _destilayout.is_visible(timeout=15000):
           desti_options = _destioptions.all()

           for options in desti_options:
               options.scroll_into_view_if_needed()
               options.hover()
               time.sleep(0.2)
               print(f'options:{options.text_content()}')

           desti_options[0].click()
           time.sleep(0.3)


def today_month_day():
        dt = datetime.now()
        formatted_string = dt.strftime("%d")
        print(f"Formatted String: {formatted_string}")
        return formatted_string