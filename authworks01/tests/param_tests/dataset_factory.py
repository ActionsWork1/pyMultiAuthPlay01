
import json
import copy
from faker import Faker

fake = Faker()


def resolve_value(value):

    if isinstance(value, str) and value.startswith("fake."):
        faker_method = value.replace("fake.", "")

        if hasattr(fake, faker_method):
            return getattr(fake, faker_method)()

        raise Exception(f"Invalid faker method: {faker_method}")

    return value


def resolve_object(obj):

    if isinstance(obj, dict):
        return {k: resolve_object(v) for k, v in obj.items()}

    if isinstance(obj, list):
        return [resolve_object(i) for i in obj]

    return resolve_value(obj)


def load_test_data_set(path, datasets=1):

    with open(path) as f:
        raw = json.load(f)["testdata"]

    results = []

    for template in raw:
        for _ in range(datasets):
            data_copy = copy.deepcopy(template)
            results.append(resolve_object(data_copy))

    return results