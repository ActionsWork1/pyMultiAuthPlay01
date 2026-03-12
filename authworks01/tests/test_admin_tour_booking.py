import time
from playwright.sync_api import expect
from authworks01.pages.TourBookPage import TourBookPage
from authworks01.pages.dashboard_page import DashboardPage, BOOKINGTYPE


def test_tour_book_action(admin_page):


    admin_page.goto("https://phptravels.net/tours")
    time.sleep(5)


    dp = DashboardPage(admin_page)
    tour= TourBookPage(admin_page)

    time.sleep(5)
    tour.book_tour(tour_city='Dub')

    expect(admin_page.locator("div.md\\:flex-row").first()).to_be_visible(visible=True,timeout=25000)

    tour_cards = admin_page.locator("div.md\\:flex-row")
    tour_cards.nth(0).locator("div>div.gap-3>a").click()
    #time.sleep(7)


    if admin_page.locator("span.justify-center.gap-2").nth(0).is_visible(timeout=25000):
        admin_page.locator("span.justify-center.gap-2").nth(0).click()
    time.sleep(5)

    # bookNow_BTN =admin_page.locator("span.justify-center.gap-2")
    # bookNow_BTN.click()