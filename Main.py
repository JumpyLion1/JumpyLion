from tkinter import *
import tkinter.messagebox
from tkinter.ttk import Combobox

# input of candidates # Marcin
file = open("candidates.txt", "r+")
candidates = file.readlines()
file.close()

# variable used to overwrite current votes during saving
votesoverride = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# breaking down candidates for 3 different variables c stands for candidate # Marcin
cposition = []
cfirstname = []
clastname = []
for c in candidates:
    position = c[0] + c[1]  # according to our convention first 2 letters stands for position # Marcin
    marker = 0
    firstname = ''
    lastname = ''
    for i in range(2, len(c)):
        if c[i] == ';':  # then everything until ';' is first name # Marcin
            marker = 1  # everything else is last name # Marcin
        elif marker == 0:
            firstname += c[i]
        else:
            lastname += c[i]
    cposition.append(position)
    cfirstname.append(firstname)
    clastname.append(lastname)


def update_resultspresident(): # Marcin
    votesoverride[0] = ppreference_1.get()
    votesoverride[1] = ppreference_2.get()
    votesoverride[2] = ppreference_3.get()
    votesoverride[3] = ppreference_4.get()


def vote_president():  # Adrian
    root2 = Toplevel(window)
    root2.title('Vote Candidates')
    root2.configure(background='white')
    root2.geometry('600x600+400+50')  # to size the window

    global ppreference_1
    global ppreference_2
    global ppreference_3
    global ppreference_4

    dataa = []
    temp = cfirstname[0] + ' ' + clastname[0]
    dataa.append(temp)
    temp = cfirstname[1] + ' ' + clastname[1]
    dataa.append(temp)
    temp = cfirstname[2] + ' ' + clastname[2]
    dataa.append(temp)
    temp = cfirstname[3] + ' ' + clastname[3]
    dataa.append(temp)

    ppreference_1 = StringVar()
    ppreference_2 = StringVar()
    ppreference_3 = StringVar()
    ppreference_4 = StringVar()

    ppreference_1.set('Select')
    ppreference_2.set('Select')
    ppreference_3.set('Select')
    ppreference_4.set('Select')

    Label(root2, text='Vote for your President by preference:', bg='white', fg='black', font='none 16 bold').pack()
    Label(root2, text='\nYour 1st Preference', bg='white', fg='black', font='none 16 bold').pack()
    Combobox(root2, values=dataa, textvariable=ppreference_1).pack()
    Label(root2, text='\nYour 2nd Preference', bg='white', fg='black', font='none 16 bold').pack()
    Combobox(root2, values=dataa, textvariable=ppreference_2).pack()
    Label(root2, text='\nYour 3rd Preference', bg='white', fg='black', font='none 16 bold').pack()
    Combobox(root2, values=dataa, textvariable=ppreference_3).pack()
    Label(root2, text='\nYour 4th Preference', bg='white', fg='black', font='none 16 bold').pack()
    Combobox(root2, values=dataa, textvariable=ppreference_4).pack()
    Button(root2, text='Submit', command=update_resultspresident).pack()
    Button(root2, text='Close', command=root2.destroy).pack(side=BOTTOM)

    root2.mainloop()


def update_resultsg1(): # Marcin
    votesoverride[4] = g1preference_1.get()
    votesoverride[5] = g1preference_2.get()
    votesoverride[6] = g1preference_3.get()
    votesoverride[7] = g1preference_4.get()

def vote_gsu1():  # Adrian
    root2 = Toplevel(window)
    root2.title('Vote Candidates')
    root2.configure(background='white')
    root2.geometry('600x600+400+50')  # to size the window

    global g1preference_1
    global g1preference_2
    global g1preference_3
    global g1preference_4

    dataa = []
    temp = cfirstname[4] + ' ' + clastname[4]
    dataa.append(temp)
    temp = cfirstname[5] + ' ' + clastname[5]
    dataa.append(temp)
    temp = cfirstname[6] + ' ' + clastname[6]
    dataa.append(temp)
    temp = cfirstname[7] + ' ' + clastname[7]
    dataa.append(temp)

    g1preference_1 = StringVar()
    g1preference_2 = StringVar()
    g1preference_3 = StringVar()
    g1preference_4 = StringVar()

    g1preference_1.set('Select')
    g1preference_2.set('Select')
    g1preference_3.set('Select')
    g1preference_4.set('Select')

    Label(root2, text='Vote for your President by preference:', bg='white', fg='black', font='none 16 bold').pack()
    Label(root2, text='\nYour 1st Preference', bg='white', fg='black', font='none 16 bold').pack()
    Combobox(root2, values=dataa, textvariable=g1preference_1).pack()
    Label(root2, text='\nYour 2nd Preference', bg='white', fg='black', font='none 16 bold').pack()
    Combobox(root2, values=dataa, textvariable=g1preference_2).pack()
    Label(root2, text='\nYour 3rd Preference', bg='white', fg='black', font='none 16 bold').pack()
    Combobox(root2, values=dataa, textvariable=g1preference_3).pack()
    Label(root2, text='\nYour 4th Preference', bg='white', fg='black', font='none 16 bold').pack()
    Combobox(root2, values=dataa, textvariable=g1preference_4).pack()
    Button(root2, text='Submit', command=update_resultsg1).pack()
    Button(root2, text='Close', command=root2.destroy).pack(side=BOTTOM)

    root2.mainloop()



def update_resultsg2():  # Marcin
    votesoverride[8] = g2preference_1.get()
    votesoverride[9] = g2preference_2.get()
    votesoverride[10] = g2preference_3.get()
    votesoverride[11] = g2preference_4.get()

def vote_gsu2():  # Adrian
    root2 = Toplevel(window)
    root2.title('Vote Candidates')
    root2.configure(background='white')
    root2.geometry('600x600+400+50')  # to size the window

    global g2preference_1
    global g2preference_2
    global g2preference_3
    global g2preference_4

    dataa = []
    temp = cfirstname[8] + ' ' + clastname[8]
    dataa.append(temp)
    temp = cfirstname[9] + ' ' + clastname[9]
    dataa.append(temp)
    temp = cfirstname[10] + ' ' + clastname[10]
    dataa.append(temp)
    temp = cfirstname[11] + ' ' + clastname[11]
    dataa.append(temp)

    g2preference_1 = StringVar()
    g2preference_2 = StringVar()
    g2preference_3 = StringVar()
    g2preference_4 = StringVar()

    g2preference_1.set('Select')
    g2preference_2.set('Select')
    g2preference_3.set('Select')
    g2preference_4.set('Select')

    Label(root2, text='Vote for your President by preference:', bg='white', fg='black', font='none 16 bold').pack()
    Label(root2, text='\nYour 1st Preference', bg='white', fg='black', font='none 16 bold').pack()
    Combobox(root2, values=dataa, textvariable=g2preference_1).pack()
    Label(root2, text='\nYour 2nd Preference', bg='white', fg='black', font='none 16 bold').pack()
    Combobox(root2, values=dataa, textvariable=g2preference_2).pack()
    Label(root2, text='\nYour 3rd Preference', bg='white', fg='black', font='none 16 bold').pack()
    Combobox(root2, values=dataa, textvariable=g2preference_3).pack()
    Label(root2, text='\nYour 4th Preference', bg='white', fg='black', font='none 16 bold').pack()
    Combobox(root2, values=dataa, textvariable=g2preference_4).pack()
    Button(root2, text='Submit', command=update_resultsg2).pack()
    Button(root2, text='Close', command=root2.destroy).pack(side=BOTTOM)

    root2.mainloop()

def update_resultsg3(): # Marcin
    votesoverride[12] = g3preference_1.get()
    votesoverride[13] = g3preference_2.get()
    votesoverride[14] = g3preference_3.get()
    votesoverride[15] = g3preference_4.get()

def vote_gsu3():  # Adrian
    root2 = Toplevel(window)
    root2.title('Vote Candidates')
    root2.configure(background='white')
    root2.geometry('600x600+400+50')  # to size the window

    global g3preference_1
    global g3preference_2
    global g3preference_3
    global g3preference_4

    dataa = []
    temp = cfirstname[12] + ' ' + clastname[12]
    dataa.append(temp)
    temp = cfirstname[13] + ' ' + clastname[13]
    dataa.append(temp)
    temp = cfirstname[14] + ' ' + clastname[14]
    dataa.append(temp)
    temp = cfirstname[15] + ' ' + clastname[15]
    dataa.append(temp)

    g3preference_1 = StringVar()
    g3preference_2 = StringVar()
    g3preference_3 = StringVar()
    g3preference_4 = StringVar()

    g3preference_1.set('Select')
    g3preference_2.set('Select')
    g3preference_3.set('Select')
    g3preference_4.set('Select')

    Label(root2, text='Vote for your President by preference:', bg='white', fg='black', font='none 16 bold').pack()
    Label(root2, text='\nYour 1st Preference', bg='white', fg='black', font='none 16 bold').pack()
    Combobox(root2, values=dataa, textvariable=g3preference_1).pack()
    Label(root2, text='\nYour 2nd Preference', bg='white', fg='black', font='none 16 bold').pack()
    Combobox(root2, values=dataa, textvariable=g3preference_2).pack()
    Label(root2, text='\nYour 3rd Preference', bg='white', fg='black', font='none 16 bold').pack()
    Combobox(root2, values=dataa, textvariable=g3preference_3).pack()
    Label(root2, text='\nYour 4th Preference', bg='white', fg='black', font='none 16 bold').pack()
    Combobox(root2, values=dataa, textvariable=g3preference_4).pack()
    Button(root2, text='Submit', command=update_resultsg3).pack()
    Button(root2, text='Close', command=root2.destroy).pack(side=BOTTOM)

    root2.mainloop()


def update_resultsfaculty(): # Marcin
    votesoverride[16] = fpreference_1.get()
    votesoverride[17] = fpreference_2.get()
    votesoverride[18] = fpreference_3.get()
    votesoverride[19] = fpreference_4.get()

def vote_faculty():  # Adrian
    root2 = Toplevel(window)
    root2.title('Vote Candidates')
    root2.configure(background='white')
    root2.geometry('600x600+400+50')  # to size the window

    global fpreference_1
    global fpreference_2
    global fpreference_3
    global fpreference_4

    dataa = []
    temp = cfirstname[16] + ' ' + clastname[16]
    dataa.append(temp)
    temp = cfirstname[17] + ' ' + clastname[17]
    dataa.append(temp)
    temp = cfirstname[18] + ' ' + clastname[18]
    dataa.append(temp)
    temp = cfirstname[19] + ' ' + clastname[19]
    dataa.append(temp)

    fpreference_1 = StringVar()
    fpreference_2 = StringVar()
    fpreference_3 = StringVar()
    fpreference_4 = StringVar()

    fpreference_1.set('Select')
    fpreference_2.set('Select')
    fpreference_3.set('Select')
    fpreference_4.set('Select')

    Label(root2, text='Vote for your President by preference:', bg='white', fg='black', font='none 16 bold').pack()
    Label(root2, text='\nYour 1st Preference', bg='white', fg='black', font='none 16 bold').pack()
    Combobox(root2, values=dataa, textvariable=fpreference_1).pack()
    Label(root2, text='\nYour 2nd Preference', bg='white', fg='black', font='none 16 bold').pack()
    Combobox(root2, values=dataa, textvariable=fpreference_2).pack()
    Label(root2, text='\nYour 3rd Preference', bg='white', fg='black', font='none 16 bold').pack()
    Combobox(root2, values=dataa, textvariable=fpreference_3).pack()
    Label(root2, text='\nYour 4th Preference', bg='white', fg='black', font='none 16 bold').pack()
    Combobox(root2, values=dataa, textvariable=fpreference_4).pack()
    Button(root2, text='Submit', command=update_resultsfaculty()).pack()
    Button(root2, text='Close', command=root2.destroy).pack(side=BOTTOM)

    root2.mainloop()


# preparations for calculating votes # Marcin
# president with id 1 votes on 1st pref, 2nd... 4th, president with id 2 votes on 1st pref, 2nd... # Marcin
presidentvotes = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
gsu1votes = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
gsu2votes = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
gsu3votes = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
fo1votes = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
fo2votes = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
fo3votes = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
fo4votes = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# and getting usernames and passwords for Adrian's login system at once # Marcin
usernamesforAdrian = []
passwordsforAdrian = []


def calculate():  # calculating votes # Marcin

    file = open("userlist.txt", "r+")
    inputstrings = file.readlines()
    file.close()

    # converting lines from .txt file to our convention # Marcin
    for line in inputstrings:
        counter = 0
        usernametemp = ''
        passwordtemp = ''
        for i in range(len(line)):
            if line[i] == ';':
                counter += 1
                if counter == 2:
                    p1 = line[i + 1]
                    i += 1
                elif counter == 3:
                    p2 = line[i + 1]
                    i += 1
                elif counter == 4:
                    p3 = line[i + 1]
                    i += 1
                elif counter == 5:
                    p4 = line[i + 1]
                    i += 1
                elif counter == 6:
                    gsu11 = line[i + 1]
                    i += 1
                elif counter == 7:
                    gsu12 = line[i + 1]
                    i += 1
                elif counter == 8:
                    gsu13 = line[i + 1]
                    i += 1
                elif counter == 9:
                    gsu14 = line[i + 1]
                    i += 1
                elif counter == 10:
                    gsu21 = line[i + 1]
                    i += 1
                elif counter == 11:
                    gsu22 = line[i + 1]
                    i += 1
                elif counter == 12:
                    gsu23 = line[i + 1]
                    i += 1
                elif counter == 13:
                    gsu24 = line[i + 1]
                    i += 1
                elif counter == 14:
                    gsu31 = line[i + 1]
                    i += 1
                elif counter == 15:
                    gsu32 = line[i + 1]
                    i += 1
                elif counter == 16:
                    gsu33 = line[i + 1]
                    i += 1
                elif counter == 17:
                    gsu34 = line[i + 1]
                    i += 1
                elif counter == 18:
                    fo1 = line[i + 1]
                    i += 1
                elif counter == 19:
                    fo2 = line[i + 1]
                    i += 1
                elif counter == 20:
                    fo3 = line[i + 1]
                    i += 1
                elif counter == 21:
                    fo4 = line[i + 1]
                    i += 1
                elif counter == 22:
                    faculty = line[i + 1]
                    break
            elif counter == 0:
                usernametemp += line[i]
            elif counter == 1:
                passwordtemp += line[i]
        usernamesforAdrian.append(usernametemp)
        passwordsforAdrian.append(passwordtemp)
        # input converted # Marcin

        # calculations; if everything is correct president with id p1 gets the vote as on first position and so on # Marcin
        if int(p1) != 0 and int(p1) < 5:
            presidentvotes[int(p1) - 1][0] += 1
        if int(p2) != 0 and int(p2) < 5:
            presidentvotes[int(p2) - 1][1] += 1
        if int(p3) != 0 and int(p3) < 5:
            presidentvotes[int(p3) - 1][2] += 1
        if int(p4) != 0 and int(p4) < 5:
            presidentvotes[int(p4) - 1][3] += 1
        if int(gsu11) != 0 and int(gsu11) < 5:
            gsu1votes[int(gsu11) - 1][0] += 1
        if int(gsu12) != 0 and int(gsu12) < 5:
            gsu1votes[int(gsu12) - 1][1] += 1
        if int(gsu13) != 0 and int(gsu13) < 5:
            gsu1votes[int(gsu13) - 1][2] += 1
        if int(gsu14) != 0 and int(gsu14) < 5:
            gsu1votes[int(gsu14) - 1][3] += 1
        if int(gsu21) != 0 and int(gsu21) < 5:
            gsu2votes[int(gsu21) - 1][0] += 1
        if int(gsu22) != 0 and int(gsu22) < 5:
            gsu2votes[int(gsu22) - 1][1] += 1
        if int(gsu23) != 0 and int(gsu23) < 5:
            gsu2votes[int(gsu23) - 1][2] += 1
        if int(gsu24) != 0 and int(gsu24) < 5:
            gsu2votes[int(gsu24) - 1][3] += 1
        if int(gsu31) != 0 and int(gsu31) < 5:
            gsu3votes[int(gsu31) - 1][0] += 1
        if int(gsu32) != 0 and int(gsu32) < 5:
            gsu3votes[int(gsu32) - 1][1] += 1
        if int(gsu33) != 0 and int(gsu33) < 5:
            gsu3votes[int(gsu33) - 1][2] += 1
        if int(gsu34) != 0 and int(gsu34) < 5:
            gsu3votes[int(gsu34) - 1][3] += 1
        if int(faculty) == 1:
            if int(fo1) != 0 and int(fo1) < 5:
                fo1votes[int(fo1) - 1][0] += 1
            if int(fo2) != 0 and int(fo2) < 5:
                fo1votes[int(fo2) - 1][1] += 1
            if int(fo3) != 0 and int(fo3) < 5:
                fo1votes[int(fo3) - 1][2] += 1
            if int(fo4) != 0 and int(fo4) < 5:
                fo1votes[int(fo4) - 1][3] += 1
        if int(faculty) == 2:
            if int(fo1) != 0 and int(fo1) < 5:
                fo2votes[int(fo1) - 1][0] += 1
            if int(fo2) != 0 and int(fo2) < 5:
                fo2votes[int(fo2) - 1][1] += 1
            if int(fo3) != 0 and int(fo3) < 5:
                fo2votes[int(fo3) - 1][2] += 1
            if int(fo4) != 0 and int(fo4) < 5:
                fo2votes[int(fo4) - 1][3] += 1
        if int(faculty) == 3:
            if int(fo1) != 0 and int(fo1) < 5:
                fo3votes[int(fo1) - 1][0] += 1
            if int(fo2) != 0 and int(fo2) < 5:
                fo3votes[int(fo2) - 1][1] += 1
            if int(fo3) != 0 and int(fo3) < 5:
                fo3votes[int(fo3) - 1][2] += 1
            if int(fo4) != 0 and int(fo4) < 5:
                fo3votes[int(fo4) - 1][3] += 1
        if int(faculty) == 4:
            if int(fo1) != 0 and int(fo1) < 5:
                fo4votes[int(fo1) - 1][0] += 1
            if int(fo2) != 0 and int(fo2) < 5:
                fo4votes[int(fo2) - 1][1] += 1
            if int(fo3) != 0 and int(fo3) < 5:
                fo4votes[int(fo3) - 1][2] += 1
            if int(fo4) != 0 and int(fo4) < 5:
                fo4votes[int(fo4) - 1][3] += 1





# function finding winners # Marcin
def winner(data):
    max = 0
    id = 0
    for i in range(4):
        if data[i][0] > max:
            max = data[i][0]
            id = i
        elif data[i][0] == max:
            for ii in range(1, 4):
                if data[i][ii] > data[id][ii]:
                    id = i
                    break
                elif data[i][ii] < data[id][ii]:
                    break
    return id


calculate()

p1 = ''
p2 = ''
p3 = ''
p4 = ''
gsu11 = ''
gsu12 = ''
gsu13 = ''
gsu14 = ''
gsu21 = ''
gsu22 = ''
gsu23 = ''
gsu24 = ''
gsu31 = ''
gsu32 = ''
gsu33 = ''
gsu34 = ''
fo1 = ''
fo2 = ''
fo3 = ''
fo4 = ''
faculty = ''

# winner order: president, gsu1, gsu2, gsu3, fo1, fo2, fo3, fo4 # Marcin
winners = [winner(presidentvotes), winner(gsu1votes), winner(gsu2votes), winner(gsu3votes), winner(fo1votes),
           winner(fo2votes), winner(fo3votes), winner(fo4votes)]


# Code by Romans Porubovs 001069564
# from tkinter import *


# inputs for the winner variable
# takes in the canidates first, last names and their scores for the votes
# saves them as variables to be referenced by the main class
def p001(firstname, lastname, first, second, third, fourth):
    global p01, fst, snd, trd, fth, total
    p01 = str(firstname) + " " + str(lastname)
    fst = first
    snd = second
    trd = third
    fth = fourth


# Inputs for the second place variable
def p002(firstname, lastname, first, second, third, fourth):
    global p02, fst2, snd2, trd2, fth2
    p02 = str(firstname) + " " + str(lastname)
    fst2 = first
    snd2 = second
    trd2 = third
    fth2 = fourth


# Inputs for the third place variable
def p003(firstname, lastname, first, second, third, fourth):
    global p03, fst3, snd3, trd3, fth3
    p03 = str(firstname) + " " + str(lastname)
    fst3 = first
    snd3 = second
    trd3 = third
    fth3 = fourth


# Inputs for the fourth place variable
def p004(firstname, lastname, first, second, third, fourth):
    global p04, fst4, snd4, trd4, fth4
    p04 = str(firstname) + " " + str(lastname)
    fst4 = first
    snd4 = second
    trd4 = third
    fth4 = fourth


def victorious(firstname, lastname):
    global p05
    p05 = str(firstname) + " " + str(lastname)


# Creates the Visu class which houses the main code
class Visu:
    def __init__(self, master):
        # links the canvas code with the main tkinter canvas
        frame = Frame(master)
        frame.grid()  # grid layout to add to the design

        # titles, to explain what the results represent
        self.Title = Label(frame, text="Results", bg="gray").grid(row=0, columnspan=5, pady=10)
        self.pp0 = Label(frame, text=" canidate name |").grid(row=1, column=0)
        self.p10 = Label(frame, text="| 1st choice |").grid(row=1, column=1)
        self.p20 = Label(frame, text="| 2nd choice |").grid(row=1, column=2)
        self.p30 = Label(frame, text="| 3rd choice |").grid(row=1, column=3)
        self.p40 = Label(frame, text="| 4th choice ").grid(row=1, column=4)

        # candidate 1
        # retrieves the inputs from the variables and stores in the labels
        self.pp = Label(frame, text=p01).grid(row=2, column=0)
        self.p1 = Label(frame, text=fst).grid(row=2, column=1)
        self.p2 = Label(frame, text=snd).grid(row=2, column=2)
        self.p3 = Label(frame, text=trd).grid(row=2, column=3)
        self.p4 = Label(frame, text=fth).grid(row=2, column=4)

        # candidate 2
        self.pp = Label(frame, text=p02).grid(row=3, column=0)
        self.p1 = Label(frame, text=fst2).grid(row=3, column=1)
        self.p2 = Label(frame, text=snd2).grid(row=3, column=2)
        self.p3 = Label(frame, text=trd2).grid(row=3, column=3)
        self.p4 = Label(frame, text=fth2).grid(row=3, column=4)

        # candidate 3
        self.pp = Label(frame, text=p03).grid(row=4, column=0)
        self.p1 = Label(frame, text=fst3).grid(row=4, column=1)
        self.p2 = Label(frame, text=snd3).grid(row=4, column=2)
        self.p3 = Label(frame, text=trd3).grid(row=4, column=3)
        self.p4 = Label(frame, text=fth3).grid(row=4, column=4)

        # candidate 4
        self.pp = Label(frame, text=p04).grid(row=5, column=0)
        self.p1 = Label(frame, text=fst4).grid(row=5, column=1)
        self.p2 = Label(frame, text=snd4).grid(row=5, column=2)
        self.p3 = Label(frame, text=trd4).grid(row=5, column=3)
        self.p4 = Label(frame, text=fth4).grid(row=5, column=4)

        # total amount of votes the winner received
        total = fst + fst2 + fst3 + fst4

        # winner
        self.wister = Label(frame, text="Winner").grid(row=6, columnspan=5, pady=10)
        self.winner = Label(frame, text=p05).grid(row=7)
        self.w1 = Label(frame, text="|  total votes: ").grid(row=7, column=1, columnspan=1)
        self.w2 = Label(frame, text=total).grid(row=7, column=2)

        # save button code, button that allows the user to save the results
        self.sve = Button(frame, text="save results", command=self.savestuff).grid(row=8, columnspan=5, ipady=5)

    # creates a new function linked to the save button
    def savestuff(self):
        # saves the results in a text file, using this format
        f = open("Results.txt", "w")  # creates a new file called 'results' and writes to it
        f.write(" Results")
        f.write("\n canidate name || 1st choice || 2nd choice || 3rd choice || 4th choice ")
        f.write("\n {}        {}             {}           {}           {}".format(p01, fst, snd, trd, fth))
        f.write("\n {}        {}             {}           {}           {}".format(p02, fst2, snd2, trd2, fth2))
        f.write("\n {}        {}             {}           {}           {}".format(p03, fst3, snd3, trd3, fth3))
        f.write("\n {}        {}             {}           {}           {}".format(p04, fst4, snd4, trd4, fth4))
        f.write("\n   ")
        f.write("\n Winner")
        f.write("\n {}   | Total votes: {}".format(p05, total))


# commands and test values
# p001(10, 10, 10, 10, 10, 10)
# p002(10, 10, 10, 10, 9, 10)
# p003(1, 12, 10, 10, 10, 10)
# p004(10, 10, 10, 4, 1, 0)

# starting tkinter and calling the class
# root = Tk()
# root.title("Visualisation")
# b = Visu(root)
# root.mainloop()

# merging Visu # Marcin
# results of president elections # Marcin
def showresultsforpresident():
    p001(cfirstname[0], clastname[0], presidentvotes[0][0], presidentvotes[0][1], presidentvotes[0][2],
         presidentvotes[0][3])
    p002(cfirstname[1], clastname[1], presidentvotes[1][0], presidentvotes[1][1], presidentvotes[1][2],
         presidentvotes[1][3])
    p003(cfirstname[2], clastname[2], presidentvotes[2][0], presidentvotes[2][1], presidentvotes[2][2],
         presidentvotes[2][3])
    p004(cfirstname[3], clastname[3], presidentvotes[3][0], presidentvotes[3][1], presidentvotes[3][2],
         presidentvotes[3][3])
    victorious(cfirstname[winners[0]], clastname[winners[0]])
    root = Tk()
    root.title("President results")
    Visu(root)
    root.mainloop()


# results for first gsu elections # Marcin
def showresultsforgsu1():
    p001(cfirstname[4], clastname[4], gsu1votes[0][0], gsu1votes[0][1], gsu1votes[0][2], gsu1votes[0][3])
    p002(cfirstname[5], clastname[5], gsu1votes[1][0], gsu1votes[1][1], gsu1votes[1][2], gsu1votes[1][3])
    p003(cfirstname[6], clastname[6], gsu1votes[2][0], gsu1votes[2][1], gsu1votes[2][2], gsu1votes[2][3])
    p004(cfirstname[7], clastname[7], gsu1votes[3][0], gsu1votes[3][1], gsu1votes[3][2], gsu1votes[3][3])
    victorious(cfirstname[winners[1] + 4], clastname[winners[1] + 4])
    root = Tk()
    root.title("Gsu officer number 1 results")
    Visu(root)
    root.mainloop()


# results for second gsu elections # Marcin
def showresultsforgsu2():
    p001(cfirstname[8], clastname[8], gsu2votes[0][0], gsu2votes[0][1], gsu2votes[0][2], gsu2votes[0][3])
    p002(cfirstname[9], clastname[9], gsu2votes[1][0], gsu2votes[1][1], gsu2votes[1][2], gsu2votes[1][3])
    p003(cfirstname[10], clastname[10], gsu2votes[2][0], gsu2votes[2][1], gsu2votes[2][2], gsu2votes[2][3])
    p004(cfirstname[11], clastname[11], gsu2votes[3][0], gsu2votes[3][1], gsu2votes[3][2], gsu2votes[3][3])
    victorious(cfirstname[winners[2] + 8], clastname[winners[2] + 8])
    root = Tk()
    root.title("Gsu officer number 2 results")
    Visu(root)
    root.mainloop()


# results for third gsu elections # Marcin
def showresultsforgsu3():
    p001(cfirstname[12], clastname[12], gsu3votes[0][0], gsu3votes[0][1], gsu3votes[0][2], gsu3votes[0][3])
    p002(cfirstname[13], clastname[13], gsu3votes[1][0], gsu3votes[1][1], gsu3votes[1][2], gsu3votes[1][3])
    p003(cfirstname[14], clastname[14], gsu3votes[2][0], gsu3votes[2][1], gsu3votes[2][2], gsu3votes[2][3])
    p004(cfirstname[15], clastname[15], gsu3votes[3][0], gsu3votes[3][1], gsu3votes[3][2], gsu3votes[3][3])
    victorious(cfirstname[winners[3] + 12], clastname[winners[3] + 12])
    root = Tk()
    root.title("Gsu officer number 3 results")
    Visu(root)
    root.mainloop()


# results for first faculty elections # Marcin
def showresultsforfo1():
    p001(cfirstname[16], clastname[16], fo1votes[0][0], fo1votes[0][1], fo1votes[0][2], fo1votes[0][3])
    p002(cfirstname[17], clastname[17], fo1votes[1][0], fo1votes[1][1], fo1votes[1][2], fo1votes[1][3])
    p003(cfirstname[18], clastname[18], fo1votes[2][0], fo1votes[2][1], fo1votes[2][2], fo1votes[2][3])
    p004(cfirstname[19], clastname[19], fo1votes[3][0], fo1votes[3][1], fo1votes[3][2], fo1votes[3][3])
    victorious(cfirstname[winners[4] + 16], clastname[winners[4] + 16])
    root = Tk()
    root.title("First faculty officer results")
    Visu(root)
    root.mainloop()


# results for second faculty elections # Marcin
def showresultsforfo2():
    p001(cfirstname[20], clastname[20], fo2votes[0][0], fo2votes[0][1], fo2votes[0][2], fo2votes[0][3])
    p002(cfirstname[21], clastname[21], fo2votes[1][0], fo2votes[1][1], fo2votes[1][2], fo2votes[1][3])
    p003(cfirstname[22], clastname[22], fo2votes[2][0], fo2votes[2][1], fo2votes[2][2], fo2votes[2][3])
    p004(cfirstname[23], clastname[23], fo2votes[3][0], fo2votes[3][1], fo2votes[3][2], fo2votes[3][3])
    victorious(cfirstname[winners[5] + 20], clastname[winners[5] + 20])
    root = Tk()
    root.title("Second faculty officer results")
    Visu(root)
    root.mainloop()


# results for third faculty elections # Marcin
def showresultsforfo3():
    p001(cfirstname[24], clastname[24], fo3votes[0][0], fo3votes[0][1], fo3votes[0][2], fo3votes[0][3])
    p002(cfirstname[25], clastname[25], fo3votes[1][0], fo3votes[1][1], fo3votes[1][2], fo3votes[1][3])
    p003(cfirstname[26], clastname[26], fo3votes[2][0], fo3votes[2][1], fo3votes[2][2], fo3votes[2][3])
    p004(cfirstname[27], clastname[27], fo3votes[3][0], fo3votes[3][1], fo3votes[3][2], fo3votes[3][3])
    victorious(cfirstname[winners[6] + 24], clastname[winners[6] + 24])
    root = Tk()
    root.title("Third faculty officer results")
    Visu(root)
    root.mainloop()


# results for forth faculty elections # Marcin
def showresultsforfo4():
    p001(cfirstname[28], clastname[28], fo4votes[0][0], fo4votes[0][1], fo4votes[0][2], fo4votes[0][3])
    p002(cfirstname[29], clastname[29], fo4votes[1][0], fo4votes[1][1], fo4votes[1][2], fo4votes[1][3])
    p003(cfirstname[30], clastname[30], fo4votes[2][0], fo4votes[2][1], fo4votes[2][2], fo4votes[2][3])
    p004(cfirstname[31], clastname[31], fo4votes[3][0], fo4votes[3][1], fo4votes[3][2], fo4votes[3][3])
    victorious(cfirstname[winners[7] + 28], clastname[winners[7] + 28])
    root = Tk()
    root.title("Forth faculty officer results")
    Visu(root)
    root.mainloop()


def vote_candidates():  # Adrian
    global root1
    root1 = Toplevel(root)
    root1.title('GSU Candidates')
    root1.configure(background='white')
    root1.geometry('600x600+400+50')  # to size the window
    photo = PhotoImage(file='UniversityLogo.png')
    Label(root1, image=photo, bg='white').pack()
    Label(root1, text="Students' Union", bg='white', fg='black', font='none 20 bold').pack()
    Label(root1, text='Vote for:\n\nPresident', bg='white', fg='black', font='none 16 bold').pack()
    Button(root1, text='ENTER', relief='solid', bg='black', fg='white', font='none 12 bold',
           command=vote_president).pack()
    Label(root1, text='\nGSU Officer 1', bg='white', fg='black', font='none 16 bold').pack()
    Button(root1, text='ENTER', relief='solid', bg='black', fg='white', font='none 12 bold',
           command=vote_gsu1).pack()
    Label(root1, text='\nGSU Officer 2', bg='white', fg='black', font='none 16 bold').pack()
    Button(root1, text='ENTER', relief='solid', bg='black', fg='white', font='none 12 bold',
           command=vote_gsu2).pack()
    Label(root1, text='\nGSU Officer 3', bg='white', fg='black', font='none 16 bold').pack()
    Button(root1, text='ENTER', relief='solid', bg='black', fg='white', font='none 12 bold',
           command=vote_gsu3).pack()
    Label(root1, text='\nFaculty Officer', bg='white', fg='black', font='none 16 bold').pack()
    Button(root1, text='ENTER', relief='solid', bg='black', fg='white', font='none 12 bold',
           command=vote_faculty).pack()
    root1.mainloop()


def check_login():  # Adrian
    username_info = usernameinput.get()
    password_info = passwordinput.get()
    username_entry.delete(0, END)
    password_entry.delete(0, END)

    if username_info in usernamesforAdrian and password_info in passwordsforAdrian:
        if usernamesforAdrian.index(username_info) == passwordsforAdrian.index(password_info):
            global intline  # getting the line of user string that just logged in # Marcin
            intline = usernamesforAdrian.index(username_info)
            vote_candidates()
        else:
            tkinter.messagebox.showinfo('Login', 'Invalid user name or password')


def login_win():  # Adrian
    global root
    root = Toplevel(window)
    root.title('Log In Area')
    root.configure(background='white')
    root.geometry('600x600+400+50')  # to size the window
    global usernameinput
    global passwordinput
    global username_entry
    global password_entry

    usernameinput = StringVar()
    passwordinput = StringVar()

    photo = PhotoImage(file='UniversityLogo.png')
    Label(root, image=photo, bg='white').pack()
    Label(root, text="Students' Union", bg='white', fg='black', font='none 20 bold').pack()
    Label(root, text='Username:', bg='white', fg='black', font='none 16 bold').pack()
    username_entry = Entry(root, textvariable=usernameinput)
    username_entry.pack()
    Label(root, text='Password:', bg='white', fg='black', font='none 16 bold').pack()
    password_entry = Entry(root, textvariable=passwordinput, show='*')
    password_entry.pack()
    Button(root, text='Submit', relief='solid', bg='black', fg='white', font='none 12 bold',
           command=check_login).pack()
    root.mainloop()


def enter_voting_poll():  # Adrian
    from datetime import date
    today = date.today()
    start_date = date(2020, 1, 20)
    end_date = date(2020, 2, 10)
    if start_date <= today <= end_date:
        login_win()
    elif today < start_date:
        tkinter.messagebox.showinfo('Voting Poll Message', f'Voting opens on {start_date} and closes on {end_date}')
    elif end_date < today:
        tkinter.messagebox.showinfo('Voting Poll Message', f'Voting closed on {end_date}')


def first_window():  # Adrian
    global window
    window = Tk()
    window.title('University of Greenwich')
    window.configure(background='white')
    window.geometry('600x600+400+50')  # to size the window

    # add frames
    topFrame = Frame(window, bg='white')
    topFrame.pack()
    bottomFrame = Frame(window, bg='white')
    bottomFrame.pack(side=BOTTOM)

    # add photo
    photo = PhotoImage(file='UniversityLogo.png')
    # Label(window, image = photo, bg='white').grid(row=0,column=0,sticky=E)
    Label(topFrame, image=photo, bg='white').pack()

    # add label
    Label(topFrame, text="Students' Union", bg='white', fg='black', font='none 20 bold').pack()
    Label(bottomFrame, text="Officer Team Elections", bg='white', fg='black', font='none 20 bold').pack()
    Label(bottomFrame, text="press", bg='white', fg='black', font='none 15 bold').pack()

    # add button
    EnterButton = Button(bottomFrame, text='ENTER', bg='black', fg='white', font='none 16 bold',
                         command=enter_voting_poll).pack()
    window.mainloop()


first_window()
# so first we should pass which line from userlist.txt logged in # Marcin
file = open("userlist.txt", "r+")
temp = file.readlines()
file.close()
loggedinstring = temp[intline]  # not the best efficient way to get that string... # Marcin TODO: optimalize
del temp
# p -> votes for president gsu -> votes for gsu officer fo -> votes for faculty officer # Marcin


# updating votes after user saved votes # Marcin
def updatevote():
    file = open("userlist.txt", "r+")
    temp = file.readlines()
    file.seek(0)  # resetting pointer # Marcin
    for i in temp:
        if i != loggedinstring:  # TODO: OPTIMALIZEEEEEEEEE # Marcin
            file.write(i)
        else:
            file.write(username)
            file.write(';')
            file.write(password)
            file.write(';')
            file.write(str(p1))
            file.write(';')
            file.write(str(p2))
            file.write(';')
            file.write(str(p3))
            file.write(';')
            file.write(str(p4))
            file.write(';')
            file.write(str(gsu11))
            file.write(';')
            file.write(str(gsu12))
            file.write(';')
            file.write(str(gsu13))
            file.write(';')
            file.write(str(gsu14))
            file.write(';')
            file.write(str(gsu21))
            file.write(';')
            file.write(str(gsu22))
            file.write(';')
            file.write(str(gsu23))
            file.write(';')
            file.write(str(gsu24))
            file.write(';')
            file.write(str(gsu31))
            file.write(';')
            file.write(str(gsu32))
            file.write(';')
            file.write(str(gsu33))
            file.write(';')
            file.write(str(gsu34))
            file.write(';')
            file.write(str(fo1))
            file.write(';')
            file.write(str(fo2))
            file.write(';')
            file.write(str(fo3))
            file.write(';')
            file.write(str(fo4))
            file.write(';')
            file.write(str(faculty))
            file.write('\r')
    file.truncate()


# extracting votes of our logged in user # Marcin
counter = 0
username = ''
password = ''


for i in range(len(loggedinstring)):
    if loggedinstring[i] == ';':
        counter += 1
        if counter == 2:
            p1 = loggedinstring[i + 1]
            i += 1
        elif counter == 3:
            p2 = loggedinstring[i + 1]
            i += 1
        elif counter == 4:
            p3 = loggedinstring[i + 1]
            i += 1
        elif counter == 5:
            p4 = loggedinstring[i + 1]
            i += 1
        elif counter == 6:
            gsu11 = loggedinstring[i + 1]
            i += 1
        elif counter == 7:
            gsu12 = loggedinstring[i + 1]
            i += 1
        elif counter == 8:
            gsu13 = loggedinstring[i + 1]
            i += 1
        elif counter == 9:
            gsu14 = loggedinstring[i + 1]
            i += 1
        elif counter == 10:
            gsu21 = loggedinstring[i + 1]
            i += 1
        elif counter == 11:
            gsu22 = loggedinstring[i + 1]
            i += 1
        elif counter == 12:
            gsu23 = loggedinstring[i + 1]
            i += 1
        elif counter == 13:
            gsu24 = loggedinstring[i + 1]
            i += 1
        elif counter == 14:
            gsu31 = loggedinstring[i + 1]
            i += 1
        elif counter == 15:
            gsu32 = loggedinstring[i + 1]
            i += 1
        elif counter == 16:
            gsu33 = loggedinstring[i + 1]
            i += 1
        elif counter == 17:
            gsu34 = loggedinstring[i + 1]
            i += 1
        elif counter == 18:
            fo1 = loggedinstring[i + 1]
            i += 1
        elif counter == 19:
            fo2 = loggedinstring[i + 1]
            i += 1
        elif counter == 20:
            fo3 = loggedinstring[i + 1]
            i += 1
        elif counter == 21:
            fo4 = loggedinstring[i + 1]
            i += 1
        elif counter == 22:
            faculty = loggedinstring[i + 1]
            break
    elif counter == 0:
        username += loggedinstring[i]
    elif counter == 1:
        password += loggedinstring[i]

# so we have saved votes from file # Marcin

# place for GUI allowing to select particular vote and for voting GUIs changing values # Marcin

# Emergency display # Marcin # When am I gonna get admin GUI, guys?
# showresultsforpresident()
# showresultsforgsu1()
# showresultsforgsu2()
# showresultsforgsu3()
showresultsforfo1()
showresultsforfo2()
showresultsforfo3()
showresultsforfo4()


# saving votes # Marcin

if votesoverride[0] != 'Select' and votesoverride[0] != 0:
    string = votesoverride[0]
    x = string.split()
    for j in range(4):
        if x[0] == cfirstname[j] and x[1] + "\n" == clastname[j]:
            p1 = j + 1

if votesoverride[1] != 'Select' and votesoverride[1] != 0:
    string = votesoverride[1]
    x = string.split()
    for j in range(4):
        if x[0] == cfirstname[j] and x[1] + "\n" == clastname[j]:
            p2 = j + 1

if votesoverride[2] != 'Select' and votesoverride[2] != 0:
    string = votesoverride[2]
    x = string.split()
    for j in range(4):
        if x[0] == cfirstname[j] and x[1] + "\n" == clastname[j]:
            p3 = j + 1

if votesoverride[3] != 'Select' and votesoverride[3] != 0:
    string = votesoverride[3]
    x = string.split()
    for j in range(4):
        if x[0] == cfirstname[j] and x[1] + "\n" == clastname[j]:
            p4 = j + 1

if votesoverride[4] != 'Select' and votesoverride[4] != 0:
    string = votesoverride[4]
    x = string.split()
    for j in range(4):
        if x[0] == cfirstname[j+4] and x[1] + "\n" == clastname[j+4]:
            gsu11 = j + 1

if votesoverride[5] != 'Select' and votesoverride[5] != 0:
    string = votesoverride[5]
    x = string.split()
    for j in range(4):
        if x[0] == cfirstname[j+4] and x[1] + "\n" == clastname[j+4]:
            gsu12 = j + 1

if votesoverride[6] != 'Select' and votesoverride[6] != 0:
    string = votesoverride[6]
    x = string.split()
    for j in range(4):
        if x[0] == cfirstname[j+4] and x[1] + "\n" == clastname[j+4]:
            gsu13 = j + 1

if votesoverride[7] != 'Select' and votesoverride[7] != 0:
    string = votesoverride[7]
    x = string.split()
    for j in range(4):
        if x[0] == cfirstname[j+4] and x[1] + "\n" == clastname[j+4]:
            gsu14 = j + 1

if votesoverride[8] != 'Select' and votesoverride[8] != 0:
    string = votesoverride[8]
    x = string.split()
    for j in range(4):
        if x[0] == cfirstname[j+8] and x[1] + "\n" == clastname[j+8]:
            gsu21 = j + 1

if votesoverride[9] != 'Select' and votesoverride[9] != 0:
    string = votesoverride[9]
    x = string.split()
    for j in range(4):
        if x[0] == cfirstname[j+8] and x[1] + "\n" == clastname[j+8]:
            gsu22 = j + 1

if votesoverride[10] != 'Select' and votesoverride[10] != 0:
    string = votesoverride[10]
    x = string.split()
    for j in range(4):
        if x[0] == cfirstname[j+8] and x[1] + "\n" == clastname[j+8]:
            gsu23 = j + 1

if votesoverride[11] != 'Select' and votesoverride[11] != 0:
    string = votesoverride[11]
    x = string.split()
    for j in range(4):
        if x[0] == cfirstname[j+8] and x[1] + "\n" == clastname[j+8]:
            gsu24 = j + 1

if votesoverride[12] != 'Select' and votesoverride[12] != 0:
    string = votesoverride[12]
    x = string.split()
    for j in range(4):
        if x[0] == cfirstname[j+12] and x[1] + "\n" == clastname[j+12]:
            gsu31 = j + 1

if votesoverride[13] != 'Select' and votesoverride[13] != 0:
    string = votesoverride[13]
    x = string.split()
    for j in range(4):
        if x[0] == cfirstname[j+12] and x[1] + "\n" == clastname[j+12]:
            gsu32 = j + 1

if votesoverride[14] != 'Select' and votesoverride[14] != 0:
    string = votesoverride[14]
    x = string.split()
    for j in range(4):
        if x[0] == cfirstname[j+12] and x[1] + "\n" == clastname[j+12]:
            gsu33 = j + 1

if votesoverride[15] != 'Select' and votesoverride[15] != 0:
    string = votesoverride[15]
    x = string.split()
    for j in range(4):
        if x[0] == cfirstname[j+12] and x[1] + "\n" == clastname[j+12]:
            gsu34 = j + 1

if votesoverride[16] != 'Select' and votesoverride[16] != 0:
    string = votesoverride[16]
    x = string.split()
    for j in range(4):
        if x[0] == cfirstname[j] and x[1] + "\n" == clastname[j]:
            fo1 = j + 1

if votesoverride[17] != 'Select' and votesoverride[17] != 0:
    string = votesoverride[17]
    x = string.split()
    for j in range(4):
        if x[0] == cfirstname[j] and x[1] + "\n" == clastname[j]:
            fo2 = j + 1

if votesoverride[18] != 'Select' and votesoverride[18] != 0:
    string = votesoverride[18]
    x = string.split()
    for j in range(4):
        if x[0] == cfirstname[j] and x[1] + "\n" == clastname[j]:
            fo3 = j + 1

if votesoverride[19] != 'Select' and votesoverride[19] != 0:
    string = votesoverride[19]
    x = string.split()
    for j in range(4):
        if x[0] == cfirstname[j] and x[1] + "\n" == clastname[j]:
            fo4 = j + 1

updatevote()
