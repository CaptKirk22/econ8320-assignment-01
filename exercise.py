tacos = [i for i in range(1, 6)]

print(tacos)

print(tacos[0])

print(tacos[-1])

tacos[2] = 7

tacos.sort()

for i in tacos:
    print(i)

tacos.append(6)

tacos.reverse()

print(tacos)

tacos.pop()

tacos[1] = "two"

print(tacos)

taco3 = tacos*2 + tacos

print(taco3)

print(len(tacos))

tacos2 = [[1,2,3],[4,5,6]]

print(len(tacos2))

longList = [i for i in range(0,10100101)]

# like a list but immutable
oneTuple = [1]

test_dictionary = {"first": "Kirk", "last": "B"}

# this below will error out bc zero index doesn't exist, the keys are indexes
#print(test_dictionary[0])

print(test_dictionary["first"])

test_dictionary["favorite food"] = "pizza"

print(test_dictionary.keys())

for i in test_dictionary:
    print(i)

for i in test_dictionary:
    print(test_dictionary[i])

import numpy as np

help(np.random)