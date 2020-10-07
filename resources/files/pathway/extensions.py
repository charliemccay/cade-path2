import random
import json
import os


# this is an example of a function that will return a random item from a file
# https://stackoverflow.com/questions/3540288/how-do-i-read-a-random-line-from-one-file
def random_line(file_name, file_path=None):
    current_dirname = os.path.dirname(__file__)
    if not file_path:
        file_path = os.path.join(current_dirname, "../", file_name)

    file = open(file_path, "r")
    line = next(file)
    for num, aline in enumerate(file, 2):
        if random.randrange(num):
            continue
        line = aline
    return line


def obs(quantity, unit, code, display):
    json_string = """
    {"quantity":"",
     "unit":"",
     "code": {"coding":[{
         "system": "http://snomed.info/sct",
         "code": "",
         "display": ""}]}
    }
    """
    # could be some validation and lookup logic here, but for now really simple...
    data = json.loads(json_string)
    data['quantity'] = quantity
    data['unit'] = unit
    data['code']['coding'][0]['code'] = code
    data['code']['coding'][0]['display'] = display
    return data


# functions to return delay for use in the pathway timer events
def mins(min, max):
    timing = {'quantity': random.randint(min, max), 'unit': 'minutes'}
    return timing


def hours(min, max):
    timing = {'quantity': random.randint(min, max), 'unit': 'hours'}
    return timing


# another function might return sequential items from a file
