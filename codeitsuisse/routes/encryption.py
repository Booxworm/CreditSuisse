import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/encryption', methods=['POST'])
def evaluateEncryption():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    inputValue = data.get("input")
    result = secretMessage(inputValue)
    logging.info("My result :{}".format(result))
    return json.dumps(result)

def secretMessage(arr):
    result = []
    for item in arr:
        n = item.get("n")
        text = item.get("text")
        cleantext = ""
        encrypted = ""
        text.upper()
        for x in text:
            if x >"A" and x < "Z":
                cleantext = cleantext + x
        for j in range(n):
            for x in range(j, len(cleantext), n):
                encrypted = encrypted + cleantext[x]
        result.append(encrypted)

    return result
