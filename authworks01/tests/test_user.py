import time
from random import Random

import allure


@allure.title("Test Authentication")
@allure.description("This test attempts to log into the website using a login as User")
@allure.tag("NewUI", "Essentials", "Authentication")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "John Doe")
@allure.link("https://dev.example.com/", name="Website")
@allure.issue("AUTH-124")
@allure.testcase("TMS-455")
def test_admin_user_flow(user_page):

    # # Step1 Admin performs action
    # admin_page.goto("https://phptravels.net/admin/dashboard")
    # admin_page.reload()

    # Step2 User verifies
    user_page.goto("https://phptravels.net/dashboard")
    assert "Dashboard" in user_page.title()

    timeList = [3,6,8,10,12]
    r = Random()
    timelimit =r.randint(0,len(timeList))
    print(f"time limit : {timelimit}")
    time.sleep(timelimit)
