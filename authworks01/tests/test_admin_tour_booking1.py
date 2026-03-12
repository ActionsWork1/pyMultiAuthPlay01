from playwright._impl._page import Page
from playwright.sync_api import expect


# def test_example(page: Page) -> None:
#
#     # page.goto("https://phptravels.net/login")
#     # expect(page.get_by_role("link", name="PHPTARVELS")).to_be_visible()
#     #
#     # page.get_by_role("textbox", name="Email Address").click()
#     # page.get_by_role("textbox", name="Email Address").fill("admin@phptravels.com")
#     # page.get_by_role("textbox", name="Password").click()
#     # page.get_by_role("textbox", name="Password").fill("demoadmin")
#     # page.get_by_role("button", name="login Sign In to your account").click()
#     # expect(page.get_by_role("link", name="event Total Bookings")).to_be_visible()
#     #
#     # page.get_by_role("link", name="tour Tours Manage Tours").click()
#     # expect(page.get_by_role("row", name="1 Tour Circle Istanbul (")).to_be_visible()
#
#     # #create new tours
#     page.get_by_role("link", name="add Create New").click()
#     expect(page.get_by_role("application", name="Rich Text Editor")).to_be_visible()
#
#     page.get_by_role("textbox", name="Search by name or email...").click()
#     page.get_by_role("textbox", name="Search by name or email...").fill("joehanks01@yopmail.com")
#
#     page.get_by_role("textbox", name="Enter Tour Name").click()
#     page.get_by_role("textbox", name="Enter Tour Name").fill("Chikala")
#     page.locator("select[name=\"tour_type_id\"]").select_option("3")
#     page.locator("select[name=\"stars\"]").select_option("3")
#     page.locator("input[name=\"days\"]").click()
#     page.locator("input[name=\"days\"]").click()
#     page.locator("input[name=\"days\"]").fill("5")
#
#     page.locator("input[name=\"nights\"]").clear()
#     page.locator("input[name=\"nights\"]").fill("4")
#
#     page.locator("input[name=\"discount_percentage\"]").clear()
#     # page.locator("input[name=\"discount_percentage\"]").fill("010")
#     # page.locator("input[name=\"discount_percentage\"]").press("ArrowLeft")
#     # page.locator("input[name=\"discount_percentage\"]").press("ArrowLeft")
#     page.locator("input[name=\"discount_percentage\"]").fill("10")
#
#     page.get_by_role("application", name="Rich Text Editor").get_by_role("paragraph").click()
#     expect(page.get_by_role("button", name="Back to top")).to_be_visible()
#
#     # page.get_by_role("textbox", name="contact@example.com").click()
#     # page.get_by_role("textbox", name="contact@example.com").fill("joehanks")
#     # page.get_by_role("textbox", name="contact@example.com").click()
#     page.get_by_role("textbox", name="contact@example.com").fill("joehanks@yopmail.com")
#
#     page.get_by_role("textbox", name="+1 (555) 123-").click()
#     page.get_by_role("textbox", name="+1 (555) 123-").fill("+18889991234")
#
#     page.get_by_role("textbox", name="https://example.com").click()
#     page.get_by_role("textbox", name="Enter cancellation policy").click()
#     page.get_by_role("textbox", name="Enter cancellation policy").fill("dfgdfgfgfgfffffff")
#     page.get_by_role("textbox", name="Enter terms and conditions").click()
#     page.get_by_role("textbox", name="Enter terms and conditions").fill("ttttttttttttttttttttttttttt &&&&&&&&&&&& CCCCCCCCCCCCCCCCCCCC")
#
#     page.get_by_role("button", name="save Submit").click()
#     expect(page.get_by_role("heading", name="location_on Location")).to_be_visible()
#
#     # page.get_by_role("textbox", name="Search city or country").click()
#     page.get_by_role("textbox", name="Search city or country").click()
#     page.get_by_role("textbox", name="Search city or country").fill("United ")
#     expect(page.get_by_role("button", name="Back to top")).to_be_visible()
#
#     page.get_by_text("Allentown, United States").click()
#     page.get_by_role("textbox", name="Full address").click()
#     page.get_by_role("textbox", name="Full address").fill("Bilvd1 Tower1")
#     page.get_by_role("button", name="save Submit").click()
#
#     page.goto("https://phptravels.net/admin/tours/add#location")
#     expect(page.get_by_role("link", name="PHPTARVELS")).to_be_visible()
#
#     page.get_by_role("button", name="calendar_month Itinerary").click()
#     expect(page.get_by_role("heading", name="calendar_month Tour Itinerary")).to_be_visible()
#
#     page.get_by_role("button", name="checklist Inclusions &").click()
#     expect(page.get_by_role("heading", name="check_circle Inclusions (10)")).to_be_visible()
#
#     page.get_by_role("button", name="photo_library Gallery").click()
#     expect(page.get_by_role("heading", name="photo_library Tour Gallery")).to_be_visible()
#
#     page.get_by_role("link", name="arrow_back").click()
#     expect(page.get_by_role("row", name="1 Tour Circle Istanbul (")).to_be_visible()
#
#     page.get_by_role("link", name="chevron_right Tours Booking").click()
#     expect(page.get_by_role("link", name="PHPTARVELS")).to_be_visible()
#
#     page.get_by_role("textbox", name="Search By City").click()
#     page.get_by_role("textbox", name="Search By City").fill("Circ")
#     page.locator(".flex-1 > .flex.items-center.gap-2").first.click()
#     expect(page.get_by_role("button", name="close")).to_be_visible()
#
#     page.get_by_text("Any Type expand_more").click()
#     page.get_by_text("category Any Type").click()
#     page.get_by_role("button", name="search Search Tours").click()
#     expect(page.get_by_role("link", name="PHPTARVELS")).to_be_visible()
#
#     page.locator("div:nth-child(37) > .card > .flex.flex-col.md\\:flex-row > .md\\:w-2\\/3 > .mt-3 > .btn").click()
#     expect(page.get_by_role("link", name="PHPTARVELS")).to_be_visible()
#
#     page.get_by_text("Book Now Processing...").click()
#     expect(page.get_by_role("link", name="logo", exact=True)).to_be_visible()
#
#     page.locator("div:nth-child(3) > .w-full > .flex.items-center.justify-between > .flex.items-center.flex-1 > .radio-container > .radio-custom").click()
#     page.get_by_text("check", exact=True).nth(5).click()
#     page.get_by_role("button", name="lock Confirm Booking").click()
#     page.goto("https://phptravels.net/invoice/tours/60A56278")
#     expect(page.get_by_role("link", name="PHPTARVELS")).to_be_visible()
#
#     page.get_by_role("button", name="payment Make Payment").click()
#     expect(page.get_by_role("heading", name="Proceed to Payment")).to_be_visible()
#
#     page.get_by_role("button", name="Proceed to Payment").click()
#     expect(page.get_by_role("group", name="Choose a currency:")).to_be_visible()
#
#     page.get_by_test_id("sms-code-input-0").click()
#     page.get_by_test_id("sms-code-input-0").fill("0")
#     page.get_by_test_id("sms-code-input-1").fill("0")
#     page.get_by_test_id("sms-code-input-2").fill("0")
#     page.get_by_test_id("sms-code-input-3").fill("0")
#     page.get_by_test_id("sms-code-input-4").fill("0")
#     page.get_by_test_id("sms-code-input-5").fill("0")
#     page.get_by_test_id("hosted-payment-submit-button").click()
#     page.goto("https://phptravels.net/invoice/tours/60A56278")
#     expect(page.get_by_role("link", name="PHPTARVELS")).to_be_visible()
#
#     page.get_by_text("Tour Invoice #60A56278 has").click()
#     page.get_by_text("Payment Successful").click()
#     page.get_by_text("check_circle Payment Successful Tour Invoice #60A56278 has been paid").click()
