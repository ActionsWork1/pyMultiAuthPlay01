# import json
# from faker import Faker
#
# fake = Faker()
#
#
# def resolve_value(value):
#
#     if isinstance(value, str) and value.startswith("fake."):
#         faker_method = value.replace("fake.", "")
#
#         if hasattr(fake, faker_method):
#             return getattr(fake, faker_method)()
#
#         raise Exception(f"Invalid faker method: {faker_method}")
#
#     return value
#
#
# def resolve_object(obj):
#
#     if isinstance(obj, dict):
#         return {k: resolve_object(v) for k, v in obj.items()}
#
#     if isinstance(obj, list):
#         return [resolve_object(i) for i in obj]
#
#     return resolve_value(obj)
#
#
# def load_test_data(path):
#
#     with open(path) as f:
#         data = json.load(f)
#
#     return [resolve_object(item) for item in data["testdata"]]


import pytest
from faker import Faker

from authworks01.tests.param_tests.python_data_helper import load_test_data

# D:\GitHubRepos\AutoSingh\pyAuthPlay01\testdata\data3.json
data1 = load_test_data("./testdata/data3.json")


@pytest.mark.parametrize("user", data1)
def test_customer_registration1(user):

    print(user)
    assert user["fname"]
    assert user["lname"]
    assert user["address"]["city"] == "New York"


data2 = load_test_data("./testdata/data3.json")

@pytest.mark.parametrize("user", data2)
def test_customer_registration2(user):

    print(user)
    assert user["fname"]
    assert user["lname"]
    assert user["address"]["city"] == "New York"