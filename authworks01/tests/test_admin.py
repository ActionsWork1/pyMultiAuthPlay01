import base64
import time

import allure

from authworks01.pages.dashboard_page import DashboardPage, BOOKINGTYPE


@allure.title("Test Authentication")
@allure.description("This test attempts to log into the website using a login as Admin")
@allure.tag("NewUI", "Essentials", "Authentication")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "John Doe")
@allure.link("https://dev.example.com/", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
def test_admin_booking_action(admin_page):

    admin_page.goto("https://phptravels.net/admin/dashboard")
    time.sleep(5)
    assert "Dashboard" in admin_page.title()

    dp = DashboardPage(admin_page)

    png_bytes = admin_page.screenshot()
    screenshot_bytes = admin_page.screenshot()
    # base64_string = base64.b64encode(screenshot_bytes).decode('utf-8')
    allure.attach(admin_page.screenshot(),name="screenshot",attachment_type=allure.attachment_type.PNG,extension=png_bytes)

    dp.create_bookiing(BOOKINGTYPE.FLIGHTBOOK)
    time.sleep(3)

    dp.create_bookiing(BOOKINGTYPE.HOTELBOOK)
    time.sleep(3)

    dp.create_bookiing(BOOKINGTYPE.TOURBOOK)
    time.sleep(3)









