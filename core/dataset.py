import json
import urllib.request

from config import url


def database():
    with urllib.request.urlopen(url) as response:
        source = response.read()
        _json_ = json.loads(source)
        return _json_


def dataset(name):
    data = database()[f"{name}"]
    return data


def dataset_all():
    data = database()
    return data


def dataset_keys():
    data = database().keys()
    return data


def dataset_values():
    data = database().values()
    return data
