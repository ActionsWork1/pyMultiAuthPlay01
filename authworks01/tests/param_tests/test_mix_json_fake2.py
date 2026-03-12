from pathlib import Path

import pytest
from authworks01.tests.param_tests.dataset_factory import load_test_data_set


data1 = load_test_data_set("./testdata/data3.json",datasets=2)


@pytest.mark.parametrize("user", data1)
def test_customer_registration1(user):

    p = Path('./testdata/data3.json').resolve()
    print(p)

    print(user)
    assert user["fname"]
    assert user["lname"]
    assert user["address"]["city"] == "New York"
