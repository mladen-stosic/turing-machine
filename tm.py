#!/usr/bin/python3
import os
import re
from state import State

states = []
currstate = 0
file = open("nuleujedan.txt", "r")

for i in range(1000):
    states.append(0)

#read program
for line in file:

    existingstate = False
    newln = re.split('[()=,\n]', line)

    if states[int(newln[1][1:], 10)] != 0:
        existingstate = True
    if not existingstate:
        states[int(newln[1][1:])] = State(newln[1])
    if newln[2] == 'b':
        states[int(newln[1][1:])].blank = [newln[5][1:], newln[6], newln[7]]
    elif newln[2] == '0':
        states[int(newln[1][1:])].zero = [newln[5][1:], newln[6], newln[7]]
    elif newln[2] == '1':
        states[int(newln[1][1:])].one = [newln[5][1:], newln[6], newln[7]]
    else:
        print("error")
        input("...error...")

    #test print
    # if states[0]!= 0:
    #     print(states[0].name)
    #     print(states[0].blank)
    #     print(states[0].zero)
    #     print(states[0].one)
file.close()


tape = 'b010001bb'
tapelist = []
#currchar = tapelist[1]

for c in tape:
    tapelist.append(c)
i=1
print(states[currstate].one[2])
while (i < len(tapelist)):


    if (tapelist[i] == 'b'):
        if states[currstate].blank[0] == '+':
            print("program ended succesfully")
            print(tapelist)
            input("...")
        else:
            currstate = int(states[currstate].blank[0])
            tapelist[i] = int(states[currstate].blank[1])
            i += int(states[currstate].blank[2])

    elif (tapelist[i] == '0'):
        if states[currstate].zero[0] == '+':
            print("program ended succesfully")
            print(tapelist)
            input("...")
        else:
            currstate = int(states[currstate].zero[0])
            tapelist[i] = int(states[currstate].zero[1])
            i += int(states[currstate].zero[2])

    elif (tapelist[i] == '1'):
        if states[currstate].one[0] == '+':
            print("program ended succesfully")
            print(tapelist)
            input("...")
        else:
            currstate = int(states[currstate].one[0])
            tapelist[i] = int(states[currstate].one[1])
            i += int(states[currstate].one[2])
