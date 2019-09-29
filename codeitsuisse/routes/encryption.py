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
        cleantext1 = ""
        cleantext2 = ""
        encrypted = ""
        text = text.upper()
        for x in text:
            if (x >="A" and x <= "Z") or (x >= "0" and x <= "9"):
                cleantext1 = cleantext1 + x
        if n == 0 or n == 1:
            for x in text:
                if (x >= "A" and x <= "Z") or (x >= "0" and x <= "9"):
                    cleantext2 = cleantext2 + x
            result.append(cleantext1)
        else:
            for j in range(n):
                for x in range(j, len(cleantext1), n):
                    encrypted = encrypted + cleantext1[x]
            for x in text:
                if (x >="A" and x <= "Z"):
                    cleantext2 = cleantext2 + x
            result.append(encrypted)

    return result
