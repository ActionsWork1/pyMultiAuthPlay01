import pytest


def pytest_generate_tests(metafunc):
    """
    Implementation:
    Since @pytest.mark.parametrize is evaluated at "Collection Time" (before fixtures exist),
    you use the pytest_generate_tests hook to inject Faker data dynamically.
    :param metafunc:
    :return:
    """

    # Check if 'dynamic_user' is a parameter in the test function
    if "dynamic_user" in metafunc.fixturenames:
        from faker import Faker
        fake = Faker(locale="en_US")

        # Create 10 unique, complex user objects
        data = [
            {
                "fname": fake.first_name(),
                "lname": fake.last_name(),
                "address": {
                             "city": fake.city(),
                             "zip": fake.zipcode(),
                             "state": fake.state(),
                }
            } for _ in range(3)
        ]
        metafunc.parametrize("dynamic_user", data)


def test_complex_faker_flow(dynamic_user):
    print("")
    assert "city" in dynamic_user["address"]
    print(f"Verified user: {dynamic_user['fname']}")
    print(f"Verified Address: {dynamic_user["address"]["city"]}, {dynamic_user['address']['zip']}, {dynamic_user['address']['state']}")
