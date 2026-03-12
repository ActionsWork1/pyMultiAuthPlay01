import os.path
import time

import pytest
from faker.proxy import Faker
from playwright.sync_api import expect

from authworks01.pages.dashboard_page import DashboardPage
from authworks01.playutil.play_helpers import PlayHelper
from authworks01.playutil.table_helpers import TableHelpers, TableHelpers1
from conftest import admin_page


@pytest.mark.wip
def test_create_newuser(admin_page):
    # admin_page.goto("https://phptravels.net/admin/dashboard")
    # admin_page.wait_for_load_state(state="networkidle", timeout=15000)
    #
    # dp =DashboardPage(admin_page)
    # dp.handle_navigation()
    #
    # admin_page.locator("span:text-is('Users')").click()
    # admin_page.locator("span:text-is('All Users')").click()
    #
    # admin_page.wait_for_selector("div#tableContainer",state="visible" ,timeout=15000)
    # user_table = TableHelpers(admin_page,"div#tableContainer")
    # cell = user_table.row("joe.matt@yopmail.com")
    #
    # # row = user_table.text("joe.matt@yopmail.com","Email")
    # col = user_table.column_index("EMAIL")
    # print(f'\ncol Index: {col} \n  cell data: {cell}')
    # time.sleep(5)
    # # pytest.set_trace()
    # createnew_btn = admin_page.locator("a:has-text('Create New')")
    # createnew_btn.click()

    admin_page.goto("https://phptravels.net/admin/users/add")

    # Add New User
    roleTyp = admin_page.locator("select#role")
    admin_page.wait_for_selector("select#role",state="visible",timeout=15000)
    roleTyp.select_option("Supplier")

    fake = Faker(locale='en_US')
    fname = fake.first_name()
    lname = fake.last_name()
    email = f'{fname}.{lname}@yopmail.com'


    FirstNameTXT = admin_page.locator("input#first_name")
    LastNameTXT = admin_page.locator("input#last_name")
    EmailTXT = admin_page.locator("input#email")
    Country_SELECT = country_code_Select = admin_page.locator("select[name='phone_country_code']")
    PhoneTXT =admin_page.locator("input#phone")
    PasswordTXT = admin_page.locator("input#password")
    CreateUserBTN= admin_page.locator("button:has-text('Create User')")
    SucessMessageSelector = "div.alert-success.mb-4>span:nth-child(2)"
    BackBTN = admin_page.locator("div.gap-4.mb-6>div.gap-5>a")
    TableSelectorString = "div#tableContainer"

    FirstNameTXT.fill(fname)
    LastNameTXT.fill(lname)
    EmailTXT.fill(email)
    Country_SELECT.select_option("US +1")

    PhoneTXT.fill("7979123456")
    time.sleep(2)
    PasswordTXT.click()
    PasswordTXT.fill("demoadmin")
    time.sleep(2)
    CreateUserBTN.click()
    admin_page.wait_for_selector(SucessMessageSelector,state="visible",timeout=15000)

    # time.sleep(6)
    create_success_msg = admin_page.locator(SucessMessageSelector).text_content()
    assert create_success_msg == "User created successfully"
    time.sleep(7)
    PlayHelper.attach_base64_to_allure(admin_page)

    # playHelper = PlayHelper()
    # playHelper.attach_base64_to_allure(admin_page)

    BackBTN.click()
    admin_page.wait_for_selector(TableSelectorString, state="visible", timeout=15000)


    user_table1  = TableHelpers(admin_page,TableSelectorString)
    # pytest.set_trace()


    # str(user_table1.text("Alan.Johnson@yopmail.com","EMAIL"))
    # user_table1.cell("Alan.Johnson@yopmail.com","EMAIL")
    # user_table1.row("Alan.Johnson@yopmail.com")
    # user_table1.row('admin@phptravels.com')
    user_table1.rows()
    # pytest.set_trace()

    user_table2 = TableHelpers1(admin_page, TableSelectorString)
    assert user_table2.is_row_present(email)
    user_table2.click_action(email,"edit")
    time.sleep(7)
    # playHelper.attach_base64_to_allure(admin_page)
    PlayHelper.attach_base64_to_allure(admin_page)
    # pytest.set_trace()




    # admin_page.wait_for_selector("div.relative>div.mb-6>div.gap-2>div:nth-child(2)",timeout=15000,state="visible")
    # newuser_wallet_badge = admin_page.locator("div.relative>div.mb-6>div.gap-2>div:nth-child(2)").inner_text()
    # print(newuser_wallet_badge)
    #
    # admin_page.wait_for_selector("a>span:nth-child(2):text-is('Manage Funds')",state="visible",timeout=15000)
    #
    # #expect(admin_page.locator("a>span:nth-child(2):text-is('Manage Funds')")).to_be_visible(state="visible",timeout=15000)
    #
    # ## Add Funder for user
    # if f"{fname} {lname}" in newuser_wallet_badge:
    #     assert True
    #     admin_page.locator("a>span:nth-child(2):text-is('Manage Funds')").click()
    #
    # admin_page.locator("input#amount").wait_for(timeout=15000,state="visible")
    # admin_page.locator("input#amount").fill('2000')
    # payment_method= admin_page.locator("select#payment_gateway")
    # transaction_type= admin_page.locator("select#transaction_type")
    # payment_method.select_option("Stripe")
    # transaction_type.select_option("Credit (Add Funds)")
    #
    # ref_file = os.path.abspath('./testdata/flight_invoice.pdf')
    # admin_page.set_input_files("input#attachments",ref_file,timeout=15000)
    #
    # # admin_page.locator("button>span>span:has-text('Submit Fund')").click()
    # #
    # # for x in range(1,50):
    # #     if admin_page.locator("button>span>span:has-text('Processing...')").is_visible():
    # #         time.sleep(0.2 * x)
    # #         print(f'still processing after {0.2*x} secs')
    # #     else:
    # #         assert True
    # #         break




