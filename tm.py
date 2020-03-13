#!/usr/bin/python3
import os
import re
from state import State

states = []
file = open("test.txt", "r")

for i in range(1000):
    states.append(0)

#read program
for line in file:
    #print(line)
    existingstate = False
    newln = re.split('[()=,\n]', line)
    print(newln)
    print(states[int(newln[1][1:])])

    if states[int(newln[1][1:], 10)] != 0:
        existingstate = True
    if not existingstate:
        states[int(newln[1][1:])] = State(newln[1])
    if newln[2] == 'b':
        states[int(newln[1][1:])].blank = [newln[5], newln[6], newln[7]]
    elif newln[2] == '0':
        states[int(newln[1][1:])].zero = [newln[5], newln[6], newln[7]]
    elif newln[2] == '1':
        states[int(newln[1][1:])].one = [newln[5], newln[6], newln[7]]
    else:
        print("error")
        input("...error...")

    #test print    
    if states[100]!= 0:
        print(states[100].name)
        print(states[100].blank)
        print(states[100].zero)
        print(states[100].one)
file.close()
input("...")
