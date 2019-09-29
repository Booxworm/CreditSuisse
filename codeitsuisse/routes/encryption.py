import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/encryption', methods=['POST'])
def evaluateEncryption():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    result = secretMessage(data)
    logging.info("My result :{}".format(result))
    return json.dumps(result)

def secretMessage(arr):
    result = []
    for item in arr:
        n = item.get("n")
        text = str(item.get("text"))
        cleantext = ""
        encrypted = ""
        text = text.upper()
        for x in text:
            if x >="A" and x <= "Z":
                cleantext = cleantext + x
        if n == 0 or n == 1:
            result.append(cleantext)
        else:
            for j in range(n):
                for x in range(j, len(cleantext), n):
                    encrypted = encrypted + cleantext[x]
            result.append(encrypted)

    return result
