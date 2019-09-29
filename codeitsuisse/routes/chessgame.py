import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/chessgame', methods=['POST'])
def evaluate():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    inputValue = data.get("input")
    result = chessGame(inputValue)
    logging.info("My result :{}".format(result))
    return json.dumps(result)

def chessGame(board):
    size = len(arr)

    flag = False
    for i in range(size):
        for j in range (size):
            if board[i][j] == "K":
                queenRow = i
                queenColumn = j
                flag = True
                break
        if flag == True:
            break
    # board = [[0 for x in range(size)] for y in range(size)]
    #
    # #Get Queen position
    # queenRow = int(input("Enter row for Queen: ")) - 1
    # queenColumn = int(input("Enter column for Queen: ")) - 1
    # board[queenRow][queenColumn] = 1
    #
    # #Get Obstacle position
    # obstacleCount = int(input("How many obstacles: "))
    # for i in range(obstacleCount):
    #     obstacleRow = int(input("Enter row for obstacle " + str(i+1) + " : ")) - 1
    #     obstacleColumn = int(input("Enter column for obstacle " + str(i + 1) + " : ")) - 1
    #     board[obstacleRow][obstacleColumn] = 2

    #Count Horizontal squares
    horizontalCount = 0

    checkRow = queenRow
    checkColumn = queenColumn - 1
    while checkColumn >= 0:
        if board[checkRow][checkColumn] == "X":
            break
        horizontalCount += 1
        checkColumn -= 1

    checkRow = queenRow
    checkColumn = queenColumn + 1
    while checkColumn < size:
        if board[checkRow][checkColumn] == "X":
            break
        horizontalCount += 1
        checkColumn += 1

    #Count Vertical squares
    verticalCount = 0

    checkRow = queenRow - 1
    checkColumn = queenColumn
    while checkRow >= 0:
        if board[checkRow][checkColumn] == "X":
            break
        verticalCount += 1
        checkRow -= 1

    checkRow = queenRow + 1
    checkColumn = queenColumn
    while checkRow < size:
        if board[checkRow][checkColumn] == "X":
            break
        verticalCount += 1
        checkRow += 1

    #Count Diagonal squares
    diagonalCount = 0

    checkRow = queenRow - 1
    checkColumn = queenColumn - 1
    while (checkRow >= 0) and (checkColumn >= 0):
        if board[checkRow][checkColumn] == "X":
            break
        diagonalCount += 1
        checkRow -= 1
        checkColumn -= 1

    checkRow = queenRow + 1
    checkColumn = queenColumn + 1
    while (checkRow < size) and (checkColumn < size):
        if board[checkRow][checkColumn] == "X":
            break
        diagonalCount += 1
        checkRow += 1
        checkColumn += 1

    checkRow = queenRow - 1
    checkColumn = queenColumn + 1
    while (checkRow >= 0) and (checkColumn < size):
        if board[checkRow][checkColumn] == "X":
            break
        diagonalCount += 1
        checkRow -= 1
        checkColumn += 1

    checkRow = queenRow + 1
    checkColumn = queenColumn - 1
    while (checkRow < size) and (checkColumn >= 0):
        if board[checkRow][checkColumn] == "X":
            break
        diagonalCount += 1
        checkRow += 1
        checkColumn -= 1

    return (verticalCount + horizontalCount + diagonalCount)

