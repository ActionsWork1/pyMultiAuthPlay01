import time

import pytest
from playwright.sync_api import expect
from authworks01.pages.TourBookPage import TourBookPage
from authworks01.pages.dashboard_page import DashboardPage, BOOKINGTYPE


def test_tour_book_action(admin_page):


    admin_page.goto("https://phptravels.net/tours")
    admin_page.wait_for_load_state(state="networkidle", timeout=15000)
    # time.sleep(5)
    # assert "Dashboard" in admin_page.title()

    dp = DashboardPage(admin_page)
    tour= TourBookPage(admin_page)

    # dp.create_bookiing(BOOKINGTYPE.TOURBOOK)
    # time.sleep(5)
    tour.book_tour(tour_city='Dubai')
    # time.sleep(5)
    admin_page.wait_for_selector("div.md\\:flex-row",state="visible",timeout=15000)
    #expect(admin_page.locator("div.md\\:flex-row")).to_be_visible(visible=True,timeout=25000)

    # Select by supplier
    supplier_filter_layout = admin_page.locator("div[x-show='filtersOpen.suppliers']")
    ck_options = admin_page.locator("div[x-show='filtersOpen.suppliers'] div.checkbox-item div.checkbox-container") #input[x-model='filters.suppliers']")

    time.sleep(0.6)
    ck_options.nth(0).scroll_into_view_if_needed()
    # ck_options.nth(0).click()
    # pytest.set_trace()

    for ck_option in ck_options.all():
        print(f"Tours by: {ck_option.locator("input[x-model='filters.suppliers']").get_attribute('value')}")
        if ck_option.locator("input[x-model='filters.suppliers']").get_attribute('value') != "Tours".lower(): #ck_option.is_checked() and
            ck_option.scroll_into_view_if_needed()
            # admin_page.locator(admin_page.locator("div[x-show='filtersOpen.suppliers'] div.checkbox-item div.checkbox-container").click()
            ck_option.click()

    # pytest.set_trace()
    tour_cards = admin_page.locator("div.md\\:flex-row")
    tour_cards.nth(0).locator("div>div.gap-3>a").click()

    if admin_page.locator("span.justify-center.gap-2").nth(0).is_visible(timeout=25000):
        admin_page.locator("span.justify-center.gap-2").nth(0).click()
    time.sleep(5)






    # bookNow_BTN =admin_page.locator("span.justify-center.gap-2")
    # bookNow_BTN.click()