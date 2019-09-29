import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/exponents', methods=['POST'])
def evaluateExponents():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    result = exponents(data.get("n"), data.get("p"))
    logging.info("My result :{}".format(result))
    return json.dumps(result)

def counting_length(value_name):
    count = 0
    while (value_name != 0):
        count += 1
        value_name = value_name // 10
    return count


def last_value(total_length, value):
    orig = value
    no_of_divisions = total_length - 1
    while (no_of_divisions != 0):
        orig = orig // 10
        no_of_divisions -= 1
    return orig


def exponents (number, power):

    value = number**power

    tail = value % 10 #getting the first value

    length = counting_length(value)

    head = last_value(length, value)

    result_list = []

    result_list.extend([head])
    result_list.extend([length])
    result_list.extend([tail])

    return result_list
