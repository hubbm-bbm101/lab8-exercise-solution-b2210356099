import sys

stdDict = {}

with open(sys.argv[1], "r+", encoding="utf-8") as f1:
    for line in f1:
        stdList = line.split(":")
        stdDict[stdList[0]] = stdList[1]

    inp = sys.argv[2].split(",")
    for i in inp:
        try:
            print("Name:{} , University:{}".format(i, stdDict[i]))
        except KeyError:
            print("No record of ‘{}’ was found!".format(i))