#!/usr/bin/python3
import time

'''
T(n) = 1 + n
    One constant assignment statement (min)
    One assignment in loop done n times
O(n)
'''
def minNumberLinear(n):
    min = n[0]
    for x in n:
        if x < min:
            min = x
    return min

'''
T(n) = 1 + n^2
    One constant assignment (min)
    One assignment in loop done n times nested in another loop iterating n
    times.
O(n^2)
'''
def minNumber(n):
    min = n[0]
    for x in n:
        smallest = True
        for i in n:
            if x > i:
                smallest = False
        if smallest:
            min = x 
    return min


start = time.time()
a = minNumberLinear(list(range(0, 10000)))
print(a)
end = time.time()

print(end-start)

startB = time.time()
b = minNumber(list(range(0, 10000)))
print(b)
endB = time.time()

print(endB-startB)