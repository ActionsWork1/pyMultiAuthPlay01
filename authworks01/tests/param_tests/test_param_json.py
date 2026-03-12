import json

import pytest

from authworks01.tests.param_tests.python_pojo import User


def load_simple_test_data():
    """
    reading a simple json test data file
    :return:
    """
    with open('./testdata/data1.json', 'r') as f:
        return json.load(f)


pytest.mark.parametrize("data", load_simple_test_data())
def param_test1(data):
    result = data['input_a'] + data['input_b']
    assert result == data['expected']



def load_complex_data():
    """
    reading a complex json test data file with pojo class
    data with fixed data values
    :return:
    """
    with open('./testdata/data2.json', 'r') as f:
        return json.load(f)

@pytest.mark.parametrize("user_data", load_complex_data())
def test_with_model(user_data):
    # This validates the JSON structure immediately
    user = User(**user_data)
    assert user.address.city == "New York"
    assert user.fname == "fake.name1"


