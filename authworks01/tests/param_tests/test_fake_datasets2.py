import pytest
import json
from faker import Faker

"""
The Hybrid Approach:
We will create a helper that loads your "Contractual" JSON data 
and appends "Synthetic" Faker data to the list.
"""

fake = Faker()

def get_combined_data(num_fakes=5):
    # 1. Load the "Must-Pass" cases from JSON
    with open('./testdata/data2.json', 'r') as f:
        data = json.load(f)['testdata']

    # 2. Generate the "Stress-Test" cases from Faker
    for _ in range(num_fakes):
        data.append({
            "fname": fake.first_name(),
            "lname": fake.last_name(),
            "address": {
                "street": fake.street_address(),
                "building": f"Apt {fake.random_int(1, 100)}",
                "city": fake.city(),
                "zip": fake.zipcode()
            },
            "source": "faker"  # Flag to identify origin
        })
    return data


@pytest.mark.parametrize("user", get_combined_data(num_fakes=4))
def test_user_persistence1(user):
    # This test runs for both your JSON entries AND 10 random users
    print("")
    print(f"Testing {user['fname']} from {user.get('source', 'json')}")
    assert len(user['fname']) > 0
    assert "city" in user['address']


@pytest.mark.parametrize("user", get_combined_data(num_fakes=4))
def test_user_persistence2(user):
    # This test runs for both your JSON entries AND 10 random users
    print("")
    print(f"Testing {user['fname']} from {user.get('source')}")
    assert len(user['fname']) > 0
    assert "city" in user['address']