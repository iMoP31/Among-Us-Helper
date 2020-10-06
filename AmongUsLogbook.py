import tkinter as tk
from PIL import Image, ImageTk
root= tk.Tk()
canvas1 = tk.Canvas(root, width = 115, height = 400,  relief = 'raised',bg='#141414')
canvas1.pack()
target='null'
temp=''


suspects = tk.Label(root, text= "No Sus", anchor="n", wraplength=110 ,bg='#141414', fg='#FFFFFF', justify='left',font=("Arial", 8))
canvas1.create_window(60, 225, window=suspects)

b = tk.Label(root, text= "", anchor="n", wraplength=110 ,bg='#141414', fg='#FFFFFF', justify='left',font=("Arial", 8))
canvas1.create_window(60, 100, window=b)


b.lower()


sus = []
clear = []
dead = []
nouse = []
score = []
score.insert(0, int("0"))
score.insert(1, int("0"))
score.insert(2, int("0"))



def editB():
    wonL.lift()
    lostL.lift()
    minusW.lift()
    minusL.lift()
    plusW.lift()
    plusL.lift()
    backB.lift()
    blackD.lower()
    blueD.lower()
    brownD.lower()
    cyanD.lower()
    greenD.lower()
    limeD.lower()
    orangeD.lower()
    pinkD.lower()
    purpleD.lower()
    redD.lower()
    whiteD.lower()
    yellowD.lower()
    suspectREM.lower()
    suspectADD.lower()
    clearedADD.lower()
    clearedREM.lower()
    killedADD.lower()
    killedREM.lower()
    storeE.lower()
    entrye.lower()
    suspects.lower()
    infoB.lower()
    editO.lower()
    scoreL.lower()
    resetS.lift()

def wonAdd():
    global score
    global won
    score.insert(1, int(score[1]) + 1)
    wonL.config(text= "W: " + str(score[1]))
    scoreL.config(text= "W: " + str(score[1]) + " L: " + str(score[2]))

def wonRem():
    global score
    global won
    if score[1] == 0:
        pass
    else:
        score.insert(1, int(score[1]) - 1)
        wonL.config(text= "W: " + str(score[1]))
        scoreL.config(text= "W: " + str(score[1]) + " L: " + str(score[2]))

def lostAdd():
    global score
    global lost
    score.insert(2, int(score[2]) + 1)
    lostL.config(text= "L: " + str(score[2]))
    scoreL.config(text= "W: " + str(score[1]) + " L: " + str(score[2]))

def lostRem():
    global score
    global lost
    if score[2] == 0:
        pass
    else:
        score.insert(2, int(score[2]) - 1)
        lostL.config(text= "L: " + str(score[2]))
        scoreL.config(text= "W: " + str(score[1]) + " L: " + str(score[2]))
    
                


def clearInfo():
    black.clear()
    blue.clear()
    brown.clear()
    cyan.clear()
    green.clear()
    lime.clear()
    orange.clear()
    pink.clear()
    purple.clear()
    red.clear()
    white.clear()
    yellow.clear()
    sus.clear()
    dead.clear()
    clear.clear()
    suspects.config(text="No Sus")
    blackD.config(bg="SystemButtonFace")
    blueD.config(bg="SystemButtonFace")
    brownD.config(bg="SystemButtonFace")
    cyanD.config(bg="SystemButtonFace")
    greenD.config(bg="SystemButtonFace")
    limeD.config(bg="SystemButtonFace")
    orangeD.config(bg="SystemButtonFace")
    pinkD.config(bg="SystemButtonFace")
    purpleD.config(bg="SystemButtonFace")
    redD.config(bg="SystemButtonFace")
    whiteD.config(bg="SystemButtonFace")
    yellowD.config(bg="SystemButtonFace")
    if 'black' in nouse:
        blackD.config(bg="#000000")
    if 'blue' in nouse:
        blueD.config(bg="#000000")
    if 'brown' in nouse:
        brownD.config(bg="#000000")
    if 'cyan' in nouse:
        cyanD.config(bg="#000000")
    if 'green' in nouse:
        greenD.config(bg="#000000")
    if 'lime' in nouse:
        limeD.config(bg="#000000")
    if 'orange' in nouse:
        orangeD.config(bg="#000000")
    if 'pink' in nouse:
        pinkD.config(bg="#000000")
    if 'purple' in nouse:
        purpleD.config(bg="#000000")
    if 'red' in nouse:
        redD.config(bg="#000000")
    if 'white' in nouse:
        whiteD.config(bg="#000000")
    if 'yellow' in nouse:
        yellowD.config(bg="#000000")
    
    
        
def info():
    global target
    blackS.lower()
    blueS.lower()
    brownS.lower()
    cyanS.lower()
    greenS.lower()
    limeS.lower()
    orangeS.lower()
    pinkS.lower()
    purpleS.lower()
    redS.lower()
    whiteS.lower()
    yellowS.lower()
    suspectREM.lower()
    suspectADD.lower()
    clearedADD.lower()
    clearedREM.lower()
    killedADD.lower()
    killedREM.lower()
    storeE.lower()
    entrye.lower()
    suspects.lower()
    infoB.lower()
    b.config(text= str(globals()[target]))
    b.lift()
    backB.lift()
    nouseADD.lower()
    nouseREM.lower()
    editO.lower()
    scoreL.lower()
    minusL.lower()
    minusW.lower()
    plusW.lower()
    plusL.lower()

def back():
    global score
    b.lower()
    lowerMenu()
    blackD.lift()
    blueD.lift()
    brownD.lift()
    cyanD.lift()
    greenD.lift()
    limeD.lift()
    orangeD.lift()
    pinkD.lift()
    purpleD.lift()
    redD.lift()
    whiteD.lift()
    yellowD.lift()
    backB.lower()
    resetB.lift()
    editO.lift()
    scoreL.lift()
    lostL.lower()
    wonL.lower()
    scoreL.config(text= "W: " + str(score[1]) + " L: " + str(score[2]))
    minusL.lower()
    minusW.lower()
    plusW.lower()
    plusL.lower()
    resetS.lower()


    
def extraStore():
    global target
    global temp
    temp = entrye.get()
    if temp == '':
        temp=''
    else:
        globals()[target].append (temp)

    entrye.delete(0, tk.END)
    

def killedAdd():
    global target
    global sus
    global dead
    
    globals()[target].insert(3, "dead")

    killedADD.lower()
    killedREM.lift()
    if target in dead:
        pass  
    else:
        dead.append(target)

    if target in sus:
        sus.remove(target)
        suspects.config(text="Sus: " + str(sus))

def killedRem():
    global target
    global dead
    globals()[target].remove("dead")
    killedADD.lift()
    killedREM.lower()
    if target in dead:
        dead.remove(target)
    
def lowerMenu():
    suspectREM.lower()
    suspectADD.lower()
    clearedADD.lower()
    clearedREM.lower()
    killedADD.lower()
    killedREM.lower()
    nouseADD.lower()
    nouseREM.lower()
    infoB.lower()
    storeE.lower()
    entrye.lower()
    suspects.lift()
    resetB.lift()
    editO.lift()
    scoreL.lift()
    
def openMenu():
    susB()
    clearB()
    killedB()
    storeE.lift()
    entrye.lift()
    infoB.lift()
    suspects.lower()
    resetB.lower()
    nouseB()
    editO.lower()
    scoreL.lower()
    
def susAdd():
    global sus
    global target
    
    globals()[target].insert(1, "sus")
    if target in sus:
        pass
    else:
        sus.append(target)
        
    suspects.config(text="Sus: " + str(sus))
    suspectADD.lower()
    suspectREM.lift()
    
    
    
def susRem():
    global sus
    global target
    
    globals()[target].remove('sus')

    if target in sus:
        sus.remove(target)
    suspects.config(text="Sus: " + str(sus))
    suspectADD.lift()
    suspectREM.lower()

def susB():
    global sus
    if 'sus' in globals()[target]:
        suspectREM.lift()
    else:
        suspectADD.lift()
        
def clearB():
    global sus
    if 'clear' in globals()[target]:
        clearedREM.lift()
    else:
        clearedADD.lift()
        
def nouseB():
    global target
    global nouse
    if target in nouse:
        nouseREM.lift()
    else:
        nouseADD.lift()

def killedB():
    global sus
    if 'dead' in globals()[target]:
        killedREM.lift()
    else:
        killedADD.lift()

def clearAdd():
    global clear
    global target
    
    globals()[target].insert(2, "clear")
    clearedADD.lower()
    clearedREM.lift()
    if target in clear:
        pass
    else:
        clear.append(target)


def clearRem():
    global clear
    global target
    globals()[target].remove("clear")
    clearedADD.lift()
    clearedREM.lower()
    if target in clear:
        clear.remove(target)

def nouseAdd():
    global nouse
    global target
    nouseADD.lower()
    nouseREM.lift()
    if target in nouse:
        pass
    else:
        nouse.append(target)


def nouseRem():
    global nouse
    global target
    nouseADD.lift()
    nouseREM.lower()
    if target in nouse:
        nouse.remove(target)

def resetScore():
    global score
    score.clear()
    score.insert(0, int("0"))
    score.insert(1, int("0"))
    score.insert(2, int("0"))
    wonL.config(text= "W: " + str(score[1]))
    lostL.config(text= "L: " + str(score[2]))
    scoreL.config(text= "W: " + str(score[1]) + " L: " + str(score[2]))

a = 8

scoreL =tk.Label(root, text= "W: 0 - L: 0", anchor="n", wraplength=110 ,bg='#141414', fg='#FFFFFF', justify='left',font=("Arial", 8))
canvas1.create_window(40, 345, window=scoreL)


wonL =tk.Label(root, text= "W:" + str(score[1]), anchor="n", wraplength=110 ,bg='#141414', fg='#FFFFFF', justify='left',font=("Arial", 12))
canvas1.create_window(30, 100, window=wonL)
wonL.lower()

lostL =tk.Label(root, text= "L:" + str(score[2]), anchor="n", wraplength=110 ,bg='#141414', fg='#FFFFFF', justify='left',font=("Arial", 12))
canvas1.create_window(30, 200, window=lostL)
lostL.lower()

plusW = tk.Button(text='+', command=wonAdd, width= 2)
canvas1.create_window(70, 100, window=plusW)
plusW.lower()

plusL = tk.Button(text='+', command=lostAdd, width= 2)
canvas1.create_window(70, 200, window=plusL)
plusL.lower()

minusW = tk.Button(text='-', command=wonRem, width= 2)
canvas1.create_window(100, 100, window=minusW)
minusW.lower()

minusL = tk.Button(text='-', command=lostRem, width= 2)
canvas1.create_window(100, 200, window=minusL)
minusL.lower()


editO = tk.Button(text='edit', command=editB)
canvas1.create_window(95, 345, window=editO)


nouseREM = tk.Button(text='Not In Use', bg='#FF0000', command=nouseRem, width=a)
nouseADD = tk.Button(text='In Use', command=nouseAdd, width=a, bg='#00FF00')
canvas1.create_window(40, 380, window=nouseADD)
canvas1.create_window(40, 380, window=nouseREM)
nouseADD.lower()
nouseREM.lower()

entrye = tk.Entry (root)
canvas1.create_window(40, 345, window=entrye, width=70)
storeE = tk.Button(text='Log', command=extraStore)
canvas1.create_window(95, 345, window=storeE)
storeE.lower()
entrye.lower()

clearedREM = tk.Button(text='Clear', bg='#00FF00', command=clearRem, width=a)
clearedADD = tk.Button(text='Clear', command=clearAdd, width=a)
canvas1.create_window(40, 240, window=clearedADD)
canvas1.create_window(40, 240, window=clearedREM)
clearedADD.lower()
clearedREM.lower()


suspectREM = tk.Button(text='Suspect', bg='#FF0000', command=susRem, width=a)
suspectADD = tk.Button(text='Suspect', command=susAdd, width=a)
canvas1.create_window(40, 205, window=suspectADD)
canvas1.create_window(40, 205, window=suspectREM)
suspectADD.lower()
suspectREM.lower()


infoB = tk.Button(text='Info', command=info, width=a)
backB = tk.Button(text='Back', command=back, width=a)
canvas1.create_window(40, 310, window=infoB)
canvas1.create_window(40, 380, window=backB)
infoB.lower()
backB.lower()

resetB = tk.Button(text='RESET', bg='#FF0000', command=clearInfo, width=a)
canvas1.create_window(40, 380, window=resetB)

resetS = tk.Button(text='RESET', bg='#FF0000', command=resetScore, width=a)
canvas1.create_window(40, 30, window=resetS)
resetS.lower()

killedREM = tk.Button(text='Dead', bg='#FF0000', command=killedRem, width=a)
killedADD = tk.Button(text='Dead', command=killedAdd, width=a)
canvas1.create_window(40, 275, window=killedADD)
canvas1.create_window(40, 275, window=killedREM)
killedADD.lower()
killedREM.lower()

#black

black = []

def blackS():
    blackD.lift()
    blueD.lift()
    brownD.lift()
    cyanD.lift()
    greenD.lift()
    limeD.lift()
    orangeD.lift()
    pinkD.lift()
    purpleD.lift()
    redD.lift()
    whiteD.lift()
    yellowD.lift()
    blackS.lower()
    lowerMenu()
    if target not in nouse:
        if blackD.cget("bg") == "#000000":
            blackD.config(bg="SystemButtonFace")
    if "sus" in black:
        blackD.config(bg="#FFA500")
    elif "sus" not in black:
        if blackD.cget("bg") == "#FFA500":
            blackD.config(bg="SystemButtonFace")
    if "clear" in black:
        blackD.config(bg="#00FF00")
    elif "clear" not in black:
        if blackD.cget("bg") == "#00FF00":
            blackD.config(bg="SystemButtonFace")
    if "dead" in black:
        blackD.config(bg="#000000")
    elif "dead" not in black:
        if blackD.cget("bg") == "#000000":
            blackD.config(bg="SystemButtonFace")
    if target in nouse:
        blackD.config(bg="#000000")
    
    

    
    
def blackD():
    blackS.lift()
    blackD.lower()
    blueD.lower()
    brownD.lower()
    cyanD.lower()
    greenD.lower()
    limeD.lower()
    orangeD.lower()
    pinkD.lower()
    purpleD.lower()
    redD.lower()
    whiteD.lower()
    yellowD.lower()

    global target
    
    target = 'black'
    openMenu()
   
blackI = ImageTk.PhotoImage(Image.open('black.png'))
blackS = tk.Button(image=blackI, bg='#FF0000', command=blackS)
blackD = tk.Button(image=blackI, command=blackD)
canvas1.create_window(20, 30, window=blackS)
canvas1.create_window(20, 30, window=blackD)
blackS.lower()


#blue

blue = []

def blueS():
    blackD.lift()
    blueD.lift()
    brownD.lift()
    cyanD.lift()
    greenD.lift()
    limeD.lift()
    orangeD.lift()
    pinkD.lift()
    purpleD.lift()
    redD.lift()
    whiteD.lift()
    yellowD.lift()
    blueS.lower()
    lowerMenu()
    if target not in nouse:
        if blueD.cget("bg") == "#000000":
            blueD.config(bg="SystemButtonFace")
    if "sus" in blue:
        blueD.config(bg="#FFA500")
    elif "sus" not in blue:
        if blueD.cget("bg") == "#FFA500":
            blueD.config(bg="SystemButtonFace")
    if "clear" in blue:
        blueD.config(bg="#00FF00")
    elif "clear" not in blue:
        if blueD.cget("bg") == "#00FF00":
            blueD.config(bg="SystemButtonFace")
    if "dead" in blue:
        blueD.config(bg="#000000")
    elif "dead" not in blue:
        if blueD.cget("bg") == "#000000":
            blueD.config(bg="SystemButtonFace")
    if target in nouse:
        blueD.config(bg="#000000")
    
    
def blueD():
    blueS.lift()
    blackD.lower()
    blueD.lower()
    brownD.lower()
    cyanD.lower()
    greenD.lower()
    limeD.lower()
    orangeD.lower()
    pinkD.lower()
    purpleD.lower()
    redD.lower()
    whiteD.lower()
    yellowD.lower()

    global target

    target = 'blue'
    openMenu()
    
blueI = ImageTk.PhotoImage(Image.open('blue.png'))
blueS = tk.Button(image=blueI, bg='#FF0000', command=blueS)
blueD = tk.Button(image=blueI, command=blueD)
canvas1.create_window(60, 30, window=blueS)
canvas1.create_window(60, 30, window=blueD)
blueS.lower()


#brown

brown = []

def brownS():
    blackD.lift()
    blueD.lift()
    brownD.lift()
    cyanD.lift()
    greenD.lift()
    limeD.lift()
    orangeD.lift()
    pinkD.lift()
    purpleD.lift()
    redD.lift()
    whiteD.lift()
    yellowD.lift()
    brownS.lower()
    lowerMenu()
    if target not in nouse:
        if brownD.cget("bg") == "#000000":
            brownD.config(bg="SystemButtonFace")
    if "sus" in brown:
        brownD.config(bg="#FFA500")
    elif "sus" not in brown:
        if brownD.cget("bg") == "#FFA500":
            brownD.config(bg="SystemButtonFace")
    if "clear" in brown:
        brownD.config(bg="#00FF00")
    elif "clear" not in brown:
        if brownD.cget("bg") == "#00FF00":
            brownD.config(bg="SystemButtonFace")
    if "dead" in brown:
        brownD.config(bg="#000000")
    elif "dead" not in brown:
        if brownD.cget("bg") == "#000000":
            brownD.config(bg="SystemButtonFace")
    if target in nouse:
        brownD.config(bg="#000000")
    
    
def brownD():
    brownS.lift()
    blackD.lower()
    blueD.lower()
    brownD.lower()
    cyanD.lower()
    greenD.lower()
    limeD.lower()
    orangeD.lower()
    pinkD.lower()
    purpleD.lower()
    redD.lower()
    whiteD.lower()
    yellowD.lower()

    global target
    
    target = 'brown'
    openMenu()

brownI = ImageTk.PhotoImage(Image.open('brown.png'))
brownS = tk.Button(image=brownI, bg='#FF0000', command=brownS)
brownD = tk.Button(image=brownI, command=brownD)
canvas1.create_window(100, 30, window=brownS)
canvas1.create_window(100, 30, window=brownD)
brownS.lower()


#cyan

cyan = []

def cyanS():
    blackD.lift()
    blueD.lift()
    brownD.lift()
    cyanD.lift()
    greenD.lift()
    limeD.lift()
    orangeD.lift()
    pinkD.lift()
    purpleD.lift()
    redD.lift()
    whiteD.lift()
    yellowD.lift()
    cyanS.lower()
    lowerMenu()
    if target not in nouse:
        if cyanD.cget("bg") == "#000000":
            cyanD.config(bg="SystemButtonFace")
    if "sus" in cyan:
        cyanD.config(bg="#FFA500")
    elif "sus" not in cyan:
        if cyanD.cget("bg") == "#FFA500":
            cyanD.config(bg="SystemButtonFace")
    if "clear" in cyan:
        cyanD.config(bg="#00FF00")
    elif "clear" not in cyan:
        if cyanD.cget("bg") == "#00FF00":
            cyanD.config(bg="SystemButtonFace")
    if "dead" in cyan:
        cyanD.config(bg="#000000")
    elif "dead" not in cyan:
        if cyanD.cget("bg") == "#000000":
            cyanD.config(bg="SystemButtonFace")
    if target in nouse:
        cyanD.config(bg="#000000")
    
def cyanD():
    cyanS.lift()
    blackD.lower()
    blueD.lower()
    brownD.lower()
    cyanD.lower()
    greenD.lower()
    limeD.lower()
    orangeD.lower()
    pinkD.lower()
    purpleD.lower()
    redD.lower()
    whiteD.lower()
    yellowD.lower()
    
    global target

    target = 'cyan'
    openMenu()
    
cyanI = ImageTk.PhotoImage(Image.open('cyan.png'))
cyanS = tk.Button(image=cyanI, bg='#FF0000', command=cyanS)
cyanD = tk.Button(image=cyanI, command=cyanD)
canvas1.create_window(20, 75, window=cyanS)
canvas1.create_window(20, 75, window=cyanD)
cyanS.lower()


#green

green = []
def greenS():
    blackD.lift()
    blueD.lift()
    brownD.lift()
    cyanD.lift()
    greenD.lift()
    limeD.lift()
    orangeD.lift()
    pinkD.lift()
    purpleD.lift()
    redD.lift()
    whiteD.lift()
    yellowD.lift()
    greenS.lower()
    lowerMenu()
    if target not in nouse:
        if greenD.cget("bg") == "#000000":
            greenD.config(bg="SystemButtonFace")
    if "sus" in green:
        greenD.config(bg="#FFA500")
    elif "sus" not in green:
        if greenD.cget("bg") == "#FFA500":
            greenD.config(bg="SystemButtonFace")
    if "clear" in green:
        greenD.config(bg="#00FF00")
    elif "clear" not in green:
        if greenD.cget("bg") == "#00FF00":
            greenD.config(bg="SystemButtonFace")
    if "dead" in green:
        greenD.config(bg="#000000")
    elif "dead" not in green:
        if greenD.cget("bg") == "#000000":
            greenD.config(bg="SystemButtonFace")
    if target in nouse:
        greenD.config(bg="#000000")
        
def greenD():
    greenS.lift()
    blackD.lower()
    blueD.lower()
    brownD.lower()
    cyanD.lower()
    greenD.lower()
    limeD.lower()
    orangeD.lower()
    pinkD.lower()
    purpleD.lower()
    redD.lower()
    whiteD.lower()
    yellowD.lower()

    global target

    target = 'green'
    openMenu()
    
greenI = ImageTk.PhotoImage(Image.open('green.png'))
greenS = tk.Button(image=greenI, bg='#FF0000', command=greenS)
greenD = tk.Button(image=greenI, command=greenD)
canvas1.create_window(60, 75, window=greenS)
canvas1.create_window(60, 75, window=greenD)
greenS.lower()


#lime

lime = []

def limeS():
    blackD.lift()
    blueD.lift()
    brownD.lift()
    cyanD.lift()
    greenD.lift()
    limeD.lift()
    orangeD.lift()
    pinkD.lift()
    purpleD.lift()
    redD.lift()
    whiteD.lift()
    yellowD.lift()
    limeS.lower()
    lowerMenu()
    if target not in nouse:
        if limeD.cget("bg") == "#000000":
            limeD.config(bg="SystemButtonFace")
    if "sus" in lime:
        limeD.config(bg="#FFA500")
    elif "sus" not in lime:
        if limeD.cget("bg") == "#FFA500":
            limeD.config(bg="SystemButtonFace")
    if "clear" in lime:
        limeD.config(bg="#00FF00")
    elif "clear" not in lime:
        if limeD.cget("bg") == "#00FF00":
            limeD.config(bg="SystemButtonFace")
    if "dead" in lime:
        limeD.config(bg="#000000")
    elif "dead" not in lime:
        if limeD.cget("bg") == "#000000":
            limeD.config(bg="SystemButtonFace")
    if target in nouse:
        limeD.config(bg="#000000")
    
    
def limeD():
    limeS.lift()
    blackD.lower()
    blueD.lower()
    brownD.lower()
    cyanD.lower()
    greenD.lower()
    limeD.lower()
    orangeD.lower()
    pinkD.lower()
    purpleD.lower()
    redD.lower()
    whiteD.lower()
    yellowD.lower()

    global target

    target = 'lime'
    openMenu()

limeI = ImageTk.PhotoImage(Image.open('lime.png'))
limeS = tk.Button(image=limeI, bg='#FF0000', command=limeS)
limeD = tk.Button(image=limeI, command=limeD)
canvas1.create_window(100, 75, window=limeS)
canvas1.create_window(100, 75, window=limeD)
limeS.lower()


#orange

orange = []

def orangeS():
    blackD.lift()
    blueD.lift()
    brownD.lift()
    cyanD.lift()
    greenD.lift()
    limeD.lift()
    orangeD.lift()
    pinkD.lift()
    purpleD.lift()
    redD.lift()
    whiteD.lift()
    yellowD.lift()
    orangeS.lower()
    lowerMenu()
    if target not in nouse:
        if orangeD.cget("bg") == "#000000":
            orangeD.config(bg="SystemButtonFace")
    if "sus" in orange:
        orangeD.config(bg="#FFA500")
    elif "sus" not in orange:
        if orangeD.cget("bg") == "#FFA500":
            orangeD.config(bg="SystemButtonFace")
    if "clear" in orange:
        orangeD.config(bg="#00FF00")
    elif "clear" not in orange:
        if orangeD.cget("bg") == "#00FF00":
            orangeD.config(bg="SystemButtonFace")
    if "dead" in orange:
        orangeD.config(bg="#000000")
    elif "dead" not in orange:
        if orangeD.cget("bg") == "#000000":
            orangeD.config(bg="SystemButtonFace")
    if target in nouse:
        orangeD.config(bg="#000000")
    
    
def orangeD():
    orangeS.lift()
    blackD.lower()
    blueD.lower()
    brownD.lower()
    cyanD.lower()
    greenD.lower()
    limeD.lower()
    orangeD.lower()
    pinkD.lower()
    purpleD.lower()
    redD.lower()
    whiteD.lower()
    yellowD.lower()

    global target

    target = 'orange'
    openMenu()
 
orangeI = ImageTk.PhotoImage(Image.open('orange.png'))
orangeS = tk.Button(image=orangeI, bg='#FF0000', command=orangeS)
orangeD = tk.Button(image=orangeI, command=orangeD)
canvas1.create_window(20, 120, window=orangeS)
canvas1.create_window(20, 120, window=orangeD)
orangeS.lower()


#pink
pink = []

def pinkS():
    blackD.lift()
    blueD.lift()
    brownD.lift()
    cyanD.lift()
    greenD.lift()
    limeD.lift()
    orangeD.lift()
    pinkD.lift()
    purpleD.lift()
    redD.lift()
    whiteD.lift()
    yellowD.lift()
    pinkS.lower()
    lowerMenu()
    if target not in nouse:
        if pinkD.cget("bg") == "#000000":
            pinkD.config(bg="SystemButtonFace")
    if "sus" in pink:
        pinkD.config(bg="#FFA500")
    elif "sus" not in pink:
        if pinkD.cget("bg") == "#FFA500":
            pinkD.config(bg="SystemButtonFace")
    if "clear" in pink:
        pinkD.config(bg="#00FF00")
    elif "clear" not in pink:
        if pinkD.cget("bg") == "#00FF00":
            pinkD.config(bg="SystemButtonFace")
    if "dead" in pink:
        pinkD.config(bg="#000000")
    elif "dead" not in pink:
        if pinkD.cget("bg") == "#000000":
            pinkD.config(bg="SystemButtonFace")
    if target in nouse:
        pinkD.config(bg="#000000")
    

    
def pinkD():
    pinkS.lift()
    blackD.lower()
    blueD.lower()
    brownD.lower()
    cyanD.lower()
    greenD.lower()
    limeD.lower()
    orangeD.lower()
    pinkD.lower()
    purpleD.lower()
    redD.lower()
    whiteD.lower()
    yellowD.lower()

    global target

    target = 'pink'
    openMenu()
    
pinkI = ImageTk.PhotoImage(Image.open('pink.png'))
pinkS = tk.Button(image=pinkI, bg='#FF0000', command=pinkS)
pinkD = tk.Button(image=pinkI, command=pinkD)
canvas1.create_window(60, 120, window=pinkS)
canvas1.create_window(60, 120, window=pinkD)
pinkS.lower()


#purple

purple = []

def purpleS():
    blackD.lift()
    blueD.lift()
    brownD.lift()
    cyanD.lift()
    greenD.lift()
    limeD.lift()
    orangeD.lift()
    pinkD.lift()
    purpleD.lift()
    redD.lift()
    whiteD.lift()
    yellowD.lift()
    purpleS.lower()
    lowerMenu()
    if target not in nouse:
        if purpleD.cget("bg") == "#000000":
            purpleD.config(bg="SystemButtonFace")
    if "sus" in purple:
        purpleD.config(bg="#FFA500")
    elif "sus" not in purple:
        if purpleD.cget("bg") == "#FFA500":
            purpleD.config(bg="SystemButtonFace")
    if "clear" in purple:
        purpleD.config(bg="#00FF00")
    elif "clear" not in purple:
        if purpleD.cget("bg") == "#00FF00":
            purpleD.config(bg="SystemButtonFace")
    if "dead" in purple:
        purpleD.config(bg="#000000")
    elif "dead" not in purple:
        if purpleD.cget("bg") == "#000000":
            purpleD.config(bg="SystemButtonFace")
    if target in nouse:
        purpleD.config(bg="#000000")
    
    
    
def purpleD():
    purpleS.lift()
    blackD.lower()
    blueD.lower()
    brownD.lower()
    cyanD.lower()
    greenD.lower()
    limeD.lower()
    orangeD.lower()
    pinkD.lower()
    purpleD.lower()
    redD.lower()
    whiteD.lower()
    yellowD.lower()

    global target

    target = 'purple'
    openMenu()
    
purpleI = ImageTk.PhotoImage(Image.open('purple.png'))
purpleS = tk.Button(image=purpleI, bg='#FF0000', command=purpleS)
purpleD = tk.Button(image=purpleI, command=purpleD)
canvas1.create_window(100, 120, window=purpleS)
canvas1.create_window(100, 120, window=purpleD)
purpleS.lower()


#red

red = []

def redS():
    blackD.lift()
    blueD.lift()
    brownD.lift()
    cyanD.lift()
    greenD.lift()
    limeD.lift()
    orangeD.lift()
    pinkD.lift()
    purpleD.lift()
    redD.lift()
    whiteD.lift()
    yellowD.lift()
    redS.lower()
    lowerMenu()
    if target not in nouse:
        if redD.cget("bg") == "#000000":
            redD.config(bg="SystemButtonFace")
    if "sus" in red:
        redD.config(bg="#FFA500")
    elif "sus" not in red:
        if redD.cget("bg") == "#FFA500":
            redD.config(bg="SystemButtonFace")
    if "clear" in red:
        redD.config(bg="#00FF00")
    elif "clear" not in red:
        if redD.cget("bg") == "#00FF00":
            redD.config(bg="SystemButtonFace")
    if "dead" in red:
        redD.config(bg="#000000")
    elif "dead" not in red:
        if redD.cget("bg") == "#000000":
            redD.config(bg="SystemButtonFace")
    if target in nouse:
        redD.config(bg="#000000")
    
    
def redD():
    redS.lift()
    blackD.lower()
    blueD.lower()
    brownD.lower()
    cyanD.lower()
    greenD.lower()
    limeD.lower()
    orangeD.lower()
    pinkD.lower()
    purpleD.lower()
    redD.lower()
    whiteD.lower()
    yellowD.lower()

    global target

    target = 'red'
    openMenu()

redI = ImageTk.PhotoImage(Image.open('red.png'))
redS = tk.Button(image=redI, bg='#FF0000', command=redS)
redD = tk.Button(image=redI, command=redD)
canvas1.create_window(20, 165, window=redS)
canvas1.create_window(20, 165, window=redD)
redS.lower()


#white
white = []

def whiteS():
    blackD.lift()
    blueD.lift()
    brownD.lift()
    cyanD.lift()
    greenD.lift()
    limeD.lift()
    orangeD.lift()
    pinkD.lift()
    purpleD.lift()
    redD.lift()
    whiteD.lift()
    yellowD.lift()
    whiteS.lower()
    lowerMenu()
    if target not in nouse:
        if whiteD.cget("bg") == "#000000":
            whiteD.config(bg="SystemButtonFace")
    if "sus" in white:
        whiteD.config(bg="#FFA500")
    elif "sus" not in white:
        if whiteD.cget("bg") == "#FFA500":
            whiteD.config(bg="SystemButtonFace")
    if "clear" in white:
        whiteD.config(bg="#00FF00")
    elif "clear" not in white:
        if whiteD.cget("bg") == "#00FF00":
            whiteD.config(bg="SystemButtonFace")
    if "dead" in white:
        whiteD.config(bg="#000000")
    elif "dead" not in white:
        if whiteD.cget("bg") == "#000000":
            whiteD.config(bg="SystemButtonFace")
    if target in nouse:
        whiteD.config(bg="#000000")
    
    
def whiteD():
    whiteS.lift()
    blackD.lower()
    blueD.lower()
    brownD.lower()
    cyanD.lower()
    greenD.lower()
    limeD.lower()
    orangeD.lower()
    pinkD.lower()
    purpleD.lower()
    redD.lower()
    whiteD.lower()
    yellowD.lower()

    global target

    target = 'white'
    openMenu()
    
whiteI = ImageTk.PhotoImage(Image.open('white.png'))
whiteS = tk.Button(image=whiteI, bg='#FF0000', command=whiteS)
whiteD = tk.Button(image=whiteI, command=whiteD)
canvas1.create_window(60, 165, window=whiteS)
canvas1.create_window(60, 165, window=whiteD)
whiteS.lower()


#yellow

yellow = []

def yellowS():
    blackD.lift()
    blueD.lift()
    brownD.lift()
    cyanD.lift()
    greenD.lift()
    limeD.lift()
    orangeD.lift()
    pinkD.lift()
    purpleD.lift()
    redD.lift()
    whiteD.lift()
    yellowD.lift()
    yellowS.lower()
    lowerMenu()
    if target not in nouse:
        if yellowD.cget("bg") == "#000000":
            yellowD.config(bg="SystemButtonFace")
    if "sus" in yellow:
        yellowD.config(bg="#FFA500")
    elif "sus" not in yellow:
        if yellowD.cget("bg") == "#FFA500":
            yellowD.config(bg="SystemButtonFace")
    if "clear" in yellow:
        yellowD.config(bg="#00FF00")
    elif "clear" not in yellow:
        if yellowD.cget("bg") == "#00FF00":
            yellowD.config(bg="SystemButtonFace")
    if "dead" in yellow:
        yellowD.config(bg="#000000")
    elif "dead" not in yellow:
        if yellowD.cget("bg") == "#000000":
            yellowD.config(bg="SystemButtonFace")
    if target in nouse:
        yellowD.config(bg="#000000")
    
    
def yellowD():
    yellowS.lift()
    blackD.lower()
    blueD.lower()
    brownD.lower()
    cyanD.lower()
    greenD.lower()
    limeD.lower()
    orangeD.lower()
    pinkD.lower()
    purpleD.lower()
    redD.lower()
    whiteD.lower()
    yellowD.lower()

    global target

    target = 'yellow'
    openMenu()
 
yellowI = ImageTk.PhotoImage(Image.open('yellow.png'))
yellowS = tk.Button(image=yellowI, bg='#FF0000', command=yellowS)
yellowD = tk.Button(image=yellowI, command=yellowD)
canvas1.create_window(100, 165, window=yellowS)
canvas1.create_window(100, 165, window=yellowD)
yellowS.lower()


 
    



root.mainloop()
