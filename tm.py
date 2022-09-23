#!/usr/bin/python3
import glob
from tkinter import *
from tkinter.ttk import *

run = True

newfile = []
printFile=[]

# Pronalazi imena svih fajlova u folderu primeri i smesta ih u listu
files = glob.glob("primeri/*.txt")

# Razdvaja ime fajla od BIN, UN1, UN0 i .txt
for file in files:
    printFile.append(file[8:-4])
    newfile.append(file[12:-4])

# Inicijalizacija tkintera
window = Tk()
window.title("Tjuringova mašina")
window.geometry('300x800')
window.resizable(0,0)

# Inicijalizacija promenljivih
var = IntVar()
v = StringVar()
v2 = StringVar()



class State():
    """
    name = string
    blank, zero, one = [next state, substitution char(0, 1 or b), head move(+1 or -1)]
    """
    def __init__(self, name, blank = 0, zero = 0, one = 0):
      self.name = name
      self.blank = blank
      self.zero = zero
      self.one = one

def initializeStates(n):
    """
    Popunjava listu stanja nulama
    U listu se posle upisuju stanja tako da se i-to stanje nalazi na lista[i]
    """
    states = []
    for i in range(n):
        states.append(0)
    return states

def readProgram(string):
    """
    :param string:
    Ulazni parametar je string u kome se nalazi glavni program

    Funkcija readProgram() uzima ulazni string i razdvaja ga
    na listu ciji je svaki clan jedan red programa, nakon
    razdvajanja funkcija prolazi kroz listu i za svako novo
    stanje pravi novi objekat State
    """
    global states

    # Pravi listu od ulaznog stringa
    # Svaki clan liste je jedan red programa
    newln = re.split('[\n]', string)

    # Ako postoji clan u listi koji je prazan string
    # brise takav clan
    for ln in newln:
        if ln == '':
            newln.remove('')

    # Prolazi kroz listu i popunjava stanja
    for line in newln:
        existingstate = False
        line = re.split('[()=,]', line)

        if states[int(line[1][1:])] != 0:
            existingstate = True
        if not existingstate:
            states[int(line[1][1:])] = State(line[1])
        if line[2] == 'b':
            states[int(line[1][1:])].blank = [line[5][1:], line[6], line[7]]
        elif line[2] == '0':
            states[int(line[1][1:])].zero = [line[5][1:], line[6], line[7]]
        elif line[2] == '1':
            states[int(line[1][1:])].one = [line[5][1:], line[6], line[7]]
        else:
            print("error")
            input("...error...")

def tapeToList(tape):
    """
    Inicijalizuje traku i pravi listu od stringa
    Dodaje 'b' ispred i iza unete vrednosti trake
    """
    tapelist = []
    if tape[0] != 'b' and tape[1] != 'b':
        tape = 'bbbb' + tape
    for i in range(5):
        tape = tape + 'b'
    for c in tape:
        tapelist.append(c)
    return tapelist

def maincont(tapelist):
    """
    Glavni program, ako korisnik izabere da se
    program izvrsi odjednom
    """
    global programStatus, states, run, currState

    # Nalazi pocetak ulazne trake (vrednosti '0' ili '1')
    for j in range(len(tapelist)):
        if tapelist[j] != 'b':
            i = j
            break

    # Inicijalizacija pocetnih vrednosti
    run = True
    currState = 0

    # Glavna petlja
    while (i < len(tapelist)) and run:

        if (tapelist[i] == 'b'):
            tapelist[i] = states[currState].blank[1]
            i += int(states[currState].blank[2])

            if states[currState].blank[0] == '+':
                programStatus = "Program uspešno izvršen!"
                run = False

            elif states[currState].blank[0] == '-':
                programStatus = "Program neuspešno izvršen!"
                run = False

            else:
                currState = int(states[currState].blank[0])

        elif (tapelist[i] == '0'):
            tapelist[i] = states[currState].zero[1]
            i += int(states[currState].zero[2])

            if states[currState].zero[0] == '+':
                programStatus = "Program uspešno izvršen!"
                run = False

            elif states[currState].zero[0] == '-':
                programStatus = "Program neuspešno izvršen!"
                run = False

            else:
                currState = int(states[currState].zero[0])

        elif (tapelist[i] == '1'):
            tapelist[i] = states[currState].one[1]
            i += int(states[currState].one[2])

            if states[currState].one[0] == '+':
                programStatus = "Program uspešno izvršen!"
                run = False

            elif states[currState].one[0] == '-':
                programStatus = "Program neuspešno izvršen!"
                run = False

            else:
                currState = int(states[currState].one[0])

def mainStep(tapelist):
    """
    Izvrsavanje programa korak po korak
    Svaki put kada je dugme2 pritisnuto poziva se funkcija
    click3 koja poziva funkciju mainStep i izvrsava se jedan
    korak tj. jedno pomeranje glave
    """
    global currState, run, stepCount, first, programStatus

    i = stepCount + first
    if run:
        if (tapelist[i] == 'b'):
            tapelist[i] = states[currState].blank[1]
            stepCount += int(states[currState].blank[2])

            if states[currState].blank[0] == '+':
                programStatus = "Program uspešno izvršen!"
                run = False

            elif states[currState].blank[0] == '-':
                programStatus = "Program neuspešno izvršen!"
                run = False

            else:
                currState = int(states[currState].blank[0])

        elif (tapelist[i] == '0'):
            tapelist[i] = states[currState].zero[1]
            stepCount += int(states[currState].zero[2])

            if states[currState].zero[0] == '+':
                programStatus = "Program uspešno izvršen!"
                run = False

            elif states[currState].zero[0] == '-':
                programStatus = "Program neuspešno izvršen!"
                run = False

            else:
                currState = int(states[currState].zero[0])

        elif (tapelist[i] == '1'):
            tapelist[i] = states[currState].one[1]
            stepCount += int(states[currState].one[2])

            if states[currState].one[0] == '+':
                programStatus = "Program uspešno izvršen!"
                run = False

            elif states[currState].one[0] == '-':
                programStatus = "Program neuspešno izvršen!"
                run = False

            else:
                currState = int(states[currState].one[0])

def click1():
    """
    Definise sta se desava kada je dugme1 pritisnuto
    """
    global choice, stepCount, firstRun, tapelist
    # Resetuje broj koraka
    stepCount = 0
    firstRun = True

    # Prazni textbox
    input.delete("1.0", END)

    program = []
    choice = var.get()
    filename = "primeri/" + printFile[choice] + ".txt"
    file = open(filename, 'r')

    # Ako nije uneta vrednost za traku automatski unosi vrednosti
    if e1.get() == '':
        if choice < 7:
            tape = '00011000'
        elif choice <10:
            tape = '11101111'
        else:
            tape = '11111'
        e1.insert(END, tape)
        tapelist = tapeToList(tape)

    # Iz textboxa ucitava program u listu
    for line in file:
        program.append(line)

    # Od liste programa pravi string
    newprog = ''
    for line in program:
        newprog = newprog + line

    # Ispisuje program u textbox
    input.insert(END, newprog)
    file.close()

def click2():
    """
    Definise sta se desava kada je dugme2 pritisnuto
    """
    global tapelist, programStatus, states, run, choice, v, v2, firstRun

    # Inicijalizuje vrednosti, resetuje promenljivu firstRun
    firstRun = True
    run = True

    # Inicijalizuje stanja
    states = initializeStates(1000)

    # Ucitava glavni program iz textboxa
    mainprogram = input.get("1.0",END)
    readProgram(mainprogram)

    # Proverava da li je polje traka prazno i pokrece glavni program
    if e1.get() != '':
        tapelist = tapeToList(e1.get())
        maincont(tapelist)
    else:
        if choice < 7:
            tape = '00011000'
        elif choice <10:
            tape = '11101111'
        else:
            tape = '11111'
        e1.insert(END, tape)
        tapelist = tapeToList(tape)
        maincont(tapelist)

    # Konvertuje traku u string
    tape = ''
    for str in tapelist:
        tape = tape + str
    if e2.get() != '':
        e2.delete(0, END)
    e2.insert(END,tape)
    v.set(programStatus)
    v2.set('')

def click3():
    """
    Definise sta se desava kada je dugme3 pritisnuto
    """
    global tapelist, programStatus, states, run, choice, v, first, currState, firstRun


    if run:
        programStatus = ''
    states = initializeStates(1000)
    mainprogram = input.get("1.0", END)
    readProgram(mainprogram)

    # Ako je prvi korak, resetuje sve promenljive
    if firstRun:
        run = True
        currState = 0
        if e1.get() != '':
            tapelist = tapeToList(e1.get())
        else:
            if choice < 5:
                tape = '00011000'
            else:
                tape = '11111111'
            e1.insert(END, tape)
            tapelist = tapeToList(tape)
        for i in range(len(tapelist)):
            if tapelist[i] != 'b':
                first = i
                break
        firstRun = False

    mainStep(tapelist)
    tape = ''
    for str in tapelist:
        tape = tape + str
    if e2.get() != '':
        e2.delete(0, END)\

    # Iscrtava poziciju glave
    headPositionList = []
    headPosition = ''
    for t in range(len(tapelist)):
        headPositionList.append('  ')
    headPositionList[first + stepCount] = '^'
    for k in headPositionList:
        headPosition = headPosition + k

    e2.insert(END,tape)
    v.set(programStatus)
    v2.set(headPosition)


# Inicijalizacija elemenata prozora (Widgeta)
input = Text(window, width=40, height=10, wrap='none')

l1 = Label(window, text = "Unesite početnu traku:")
l2 = Label(window, textvariable = v)
l3 = Label(window, text ="Test programi:")
l4 = Label(window, text = "Unesite vaš program:")
l5 = Label(window, text = "Trenutno stanje trake:")
l6 = Label(window, textvariable = v2)
l7 = Label(window, text = "Binarni S={0,1,b}:")

button1 = Button(window, text = "Izaberi", width = 10, command = click1)
button2 = Button(window, text = "Izvrši", width = 10, command = click2)
button3 = Button(window, text = "Korak", width = 10, command = click3)

e1 = Entry(window)
e2 = Entry(window)

# Iscrtavanje elemenata prozora
l1.grid(row = 0, column = 0)
e1.grid(row = 1, column = 0)
l3.grid(row = 2, column = 0)
l7.grid(row = 3, column = 0, sticky = W)

buttons = []
for i in range(7):
    buttons.append(Radiobutton(window, variable=var, text=newfile[i], value=i).grid(row=i + 4, column=0, sticky=W))
Label(window, text="Unarni S={0,1,b}:").grid(row = 11, column = 0, sticky = W)
for i in range(7, len(newfile) - 5):
    buttons.append(Radiobutton(window, variable=var, text=newfile[i], value=i).grid(row=i + 5, column=0, sticky=W))
Label(window, text="Unarni S={1,b}:").grid(row = 15, column = 0, sticky = W)
for i in range(len(newfile) - 5, len(newfile)):
    buttons.append(Radiobutton(window, variable=var, text=newfile[i], value=i).grid(row=i + 7, column=0, sticky=W))
    
button1.grid(row = len(newfile) + 7, column = 0, sticky = W)
l4.grid(row = len(newfile) + 8, column = 0)
input.grid(column = 0, columnspan = 500, row = len(newfile) + 9)
button2.grid(row = len(newfile) + 10, column = 0, sticky = W)
button3.grid(row = len(newfile) + 10, column = 2, sticky = W)
l5.grid(row = len(newfile) + 11, column = 0)
e2.grid(row = len(newfile) + 12, column = 0, sticky = W)
l6.grid(row = len(newfile) + 13, column = 0, sticky = W)
l2.grid(row = len(newfile) + 14, column = 0)


window.mainloop()