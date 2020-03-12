#!/usr/bin/python3
import os
import re
import state

file = open("test.txt", "r")

for line in file:
    #print(line)
    newln = re.split('[()=,\n]', line)
    print(newln)
    #current state
    print(newln[1])
    #symbol1
    print(newln[2])
    #next state
    print(newln[5])
    #new symbol
    print(newln[6])
    #move
    print(newln[7])
    # for chars in newln:
    #     chars.rsplit("(")
    #     print(chars)

input("...")
file.close()
