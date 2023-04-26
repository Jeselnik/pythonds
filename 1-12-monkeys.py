#!/usr/bin/python3
import random
quote = "methinks it is like a weasel"

def generate(target):
    values = "abcdefghijklmnopqrstuvwxyz "
    output = ""
    for x in target:
        output += values[random.randint(0,len(values)-1)]
    return output


def score(target, comparison):
    score = 0
    for x in range(len(target)):
        if target[x] == comparison[x]: score += 1
    return score

def do(target):
    done = False
    count = 0
    highScore = 0
    bestAttempt = ""
    while not done:
        count += 1
        output = generate(target)
        thisScore = score(target, output)
        if thisScore > highScore:
            highScore = thisScore
            bestAttempt = output
        if thisScore == len(target):
            done = True
            print("Done on attempt: " + count)
        if count % 1000 == 0:
            print(highScore)
            print(bestAttempt)

do(quote)