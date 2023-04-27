#!/usr/bin/python3
import random
quote = "methinks it is like a weasel"

def generate(target, attempt):
    charset = "abcdefghijklmnopqrstuvwxyz "
    output = attempt

    if len(target) != len(attempt) : 
        raise RuntimeError("Target & Prev Attempt strings not equal!")
    else:
        for x in range(len(target)):
            if output[x] != target[x]:
                if target[x] not in charset: 
                    raise ValueError("Character %c not present in charset" 
                                     % (target[x]))
                else:
                    output[x] = charset[random.randint(0,len(charset)-1)]

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
    bestAttempt = [None] * len(target)

    while not done:
        count += 1
        output = generate(target, bestAttempt)
        thisScore = score(target, output)
        if thisScore > highScore:
            highScore = thisScore
            bestAttempt = output
        if thisScore == len(target):
            done = True
            print("Done on attempt: %i" % (count) )
        if count % 1000 == 0:
            print("Attempt %i: Best Score - %i\nBest Attempt: %s"
             % (count, highScore, ''.join(bestAttempt)))

do(quote)