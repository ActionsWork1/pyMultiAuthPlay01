import json
import os
from pathlib import Path

from faker import Faker

fake = Faker()

def resolve_value(value):
    if isinstance(value, str) and value.startswith("fake."):
        method = value.split("fake.")[1]

        if hasattr(fake, method):
            return getattr(fake, method)()

        raise ValueError(f"Faker method '{method}' not found")

    return value


def resolve_object(obj):

    if isinstance(obj, dict):
        return {k: resolve_object(v) for k, v in obj.items()}

    if isinstance(obj, list):
        return [resolve_object(i) for i in obj]

    return resolve_value(obj)


def load_test_data(path):

    p= Path(path).resolve()
    with open(p) as f:
        data = json.load(f)

    return [resolve_object(item) for item in data["testdata"]]