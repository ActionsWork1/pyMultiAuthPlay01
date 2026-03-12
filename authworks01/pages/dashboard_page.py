import time
from enum import Enum, auto

from playwright._impl._page import Page


class DashboardPage:  #(Page):


    def __init__(self, page:Page):
        self.page = page
        self.toggle_menu = page.locator("nav>div.relative").nth(2)



    def handle_navigation(self):
        self.toggle_menu.hover()
        time.sleep(2)

    def create_bookiing(self,book_type:Enum):
        self.page.wait_for_load_state(state="domcontentloaded", timeout=25000)
        self.page.locator("div.relative.group").nth(0).hover(timeout=150)
        match book_type:
             case BOOKINGTYPE.FLIGHTBOOK:
                 self.page.locator("a>span:has-text('Flights Booking')").nth(0).click()

             case BOOKINGTYPE.HOTELBOOK:
                 self.page.locator("a>span:has-text('Stays Booking')").nth(0).click()

             case BOOKINGTYPE.VISABOOK:
                 self.page.locator("a>span:has-text('Visa Booking')").nth(0).click()

             case BOOKINGTYPE.TOURBOOK:
                 self.page.locator("a>span:has-text('Tours Booking')").nth(0).click()

        self.page.wait_for_load_state(state="domcontentloaded", timeout=25000)


class  BOOKINGTYPE(Enum):
       FLIGHTBOOK=auto()
       HOTELBOOK=auto()
       VISABOOK=auto()
       TOURBOOK=auto()
