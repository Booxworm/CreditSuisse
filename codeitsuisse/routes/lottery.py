import logging
import json
import random

from flask import request, jsonify
from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/lottery', methods=['GET'])
def evaluateLottery():
    result = lottery()
    logging.info("My result :{}".format(result))
    return json.dumps(result)

def lottery():

    set_guessing = []

    for i in range(10):
        set_guessing.extend([random.randint(1,100)]) #generating the set of winning numbers for the lottery

    return set_guessing
