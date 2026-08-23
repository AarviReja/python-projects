import turtle
t = turtle.Pen()
print("For long sentences enter in fullscreen")
word = input("Type in a word or sentence. (No special characters)\n\n")

cool = list(word)
lenght = len(word)

def space():
    t.up()
    t.forward(60)
    t.down()


def period():
    t.down()
    t.circle(5)


def letterA():
    t.up()
    t.forward(30)
    t.down()
    t.left(60)
    t.forward(100)
    t.right(130)
    t.forward(50)
    t.right(110)
    t.forward(45)
    t.backward(45)
    t.left(110)
    t.forward(50)
    t.left(70)


def lettera():
    t.up()
    t.forward(30)
    t.down()
    t.circle(25)
    t.up()
    t.forward(20)
    t.left(90)
    t.forward(40)
    t.left(180)
    t.down()
    t.left(20)
    t.forward(45)
    t.left(70)


def letterB():
    t.up()
    t.forward(30)
    t.down()
    t.left(90)
    t.forward(100)
    t.right(90)
    for lB1 in range(0, 12):
        t.forward(7)
        t.right(15)
    t.forward(5)
    t.right(180)
    for lB2 in range(0, 12):
        t.forward(7)
        t.right(15)
    t.up()
    t.right(180)
    t.forward(35)
    t.down()


def letterb():
    t.up()
    t.forward(30)
    t.down()
    t.left(90)
    t.forward(100)
    t.backward(50)
    t.right(90)
    for lb in range(0, 12):
        t.forward(7)
        t.right(15)
    t.up()
    t.right(180)
    t.forward(35)
    t.down()


def letterC():
    t.up()
    t.forward(80)
    t.left(180)
    t.down()
    for lC in range(0,20):
        t.forward(7)
        t.right(9)
    t.up()
    t.right(90)
    t.forward(100)
    t.left(90)
    t. forward(20)
    t.down()

def letterc():
    t.up()
    t.forward(50)
    t.left(180)
    t.down()
    for lc in range(0,20):
        t.forward(4)
        t.right(9)
    t.up()
    t.right(90)
    t.forward(50)
    t.left(90)
    t.forward(20)
    t.down()


def letterD():
    t.up()
    t.forward(30)
    t.down()
    t.left(90)
    t.forward(100)
    t.right(90)
    for lD in range(0,16):
        t.forward(10)
        t.right(11)
    t.forward(10)
    t.right(180)
    t.up()
    t.forward(35)
    t.down()


def letterd():
    t.up()
    t.forward(40)
    t.left(90)
    t.down()
    t.forward(100)
    t.backward(50)
    t.left(90)
    for ld in range (0,12):
        t.forward(7)
        t.left(15)
    t.forward(10)
    t.up()
    t.forward(10)
    t.down()


def letterE():
    t.up()
    t.forward(30)
    t.down()
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(40)
    t.backward(40)
    t.left(90)
    t.backward(50)
    t.right(90)
    t.forward(40)
    t.backward(40)
    t.left(90)
    t.backward(50)
    t.right(90)
    t.forward(40)

    
def lettere():
    t.up()
    t.forward(30)
    t.down()
    t.left(180)
    t.backward(20)
    t.forward(20)
    for le in range(0,30):
        t.forward(4)
        t.right(9)
    t.right(90)
    t.forward(50)
    t.up()
    t.left(90)
    t.forward(25)
    t.left(90)
    t.forward(60)


def letterF():
    t.up()
    t.forward(20)
    t.down()
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(40)
    t.backward(40)
    t.left(90)
    t.backward(40)
    t.right(90)
    t.forward(35)
    t.backward(35)
    t.left(90)
    t.backward(60)
    t.right(90)
    t.up()
    t.forward(45)


def letterf():
    t.up()
    t.forward(30)
    t.down()
    t.left(90)
    t.forward(80)
    for lf1 in range(0,10):
        t.forward(9)
        t.right(18)
    t.left(180)
    for lf2 in range(0,10):
        t.left(18)
        t.forward(9)
    t.forward(30)
    t.right(90)
    t.forward(15)
    t.backward(30)
    t.forward(15)
    t.left(90)
    t.forward(50)
    t.up()
    t.left(90)
    t.forward(45)
    t.down()


def letterG():
    t.up()
    t.forward(60)
    t.down()
    t.left(180)
    for lG1 in range(0,20):
        t.forward(7)
        t.right(9)
    t.left(180)
    for lG2 in range(0,20):
        t.left(9)
        t.forward(7)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(30)
    t.up()
    t.backward(30)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(10)


def letterg():
    t.up()
    t.forward(30)
    t.down()
    t.circle(25)
    t.up()
    t.forward(25)
    t.left(90)
    t.forward(15)
    t.left(180)
    t.down()
    t.forward(25)
    for lg in range(0,10):
        t.right(17)
        t.forward(9)
    t.right(90)
    t.up()
    t.forward(60)
    t.left(90)
    t.forward(13)
    t.right(108)
    t.forward(10)


def letterH():
    t.up()
    t.forward(30)
    t.left(90)
    t.down()
    t.forward(100)
    t.backward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.backward(50)
    t.forward(100)
    t.left(90)
    t.up()
    t.forward(10)
    t.down()


def letterh():
    t.up()
    t.forward(30)
    t.down()
    t.left(90)
    t.forward(100)
    t.backward(70)
    for lh in range(0,20):
        t.right(10)
        t.forward(5)
    t.left(20)
    t.forward(15)
    t.left(90)
    t.up()
    t.forward(10)


def letterI():
    t.up()
    t.forward(30)
    t.down()
    t.forward(50)
    t.backward(25)
    t.left(90)
    t.forward(100)
    t.right(90)
    t.backward(25)
    t.forward(50)
    t.right(90)
    t.up()
    t.forward(100)
    t.left(90)
    t.forward(10)


def letteri():
    t.up()
    t.forward(30)
    t.down()
    t.left(90)
    t.forward(40)
    t.up()
    t.forward(7)
    t.right(90)
    t.down()
    t.circle(4)
    t.right(90)
    t.up()
    t.forward(47)
    t.left(90)
    t.forward(10)
    t.down()


def letterJ():
    t.up()
    t.forward(30)
    t.down()
    for lJ in range(0,20):
        t.forward(2)
        t.left(3)
    t.left(35)
    t.forward(70)
    t.left(90)
    t.forward(10)
    t.up()
    t.left(180)
    t.forward(10)
    t.right(90)
    t.forward(100)
    t.left(90)
    t.forward(10)
    t.down()


def letterj():
    t.up()
    t.forward(30)
    t.right(90)
    t.forward(20)
    t.down()
    for lj in range(0, 10):
        t.left(18)
        t.forward(5)
    t.forward(70)
    t.up()
    t.forward(7)
    t.right(90)
    t.down()
    t.circle(4)
    t.up()
    t.right(90)
    t.forward(50)
    t.left(90)
    t.forward(10)
    t.down()


def letterK():
    t.up()
    t.forward(30)
    t.left(90)
    t.down()
    t.forward(100)
    t.backward(50)
    t.right(45)
    t.forward(70)
    t.backward(70)
    t.right(90)
    t.forward(70)
    t.up()
    t.left(45)
    t.forward(10)
    t.down()


def letterk():
    t.up()
    t.forward(30)
    t.down()
    t.left(90)
    t.forward(100)
    t.backward(70)
    t.right(45)
    t.forward(40)
    t.backward(40)
    t.right(90)
    t.forward(40)
    t.up()
    t.left(45)
    t.forward(10)


def letterL():
    t.up()
    t.forward(30)
    t.left(90)
    t.down()
    t.forward(100)
    t.backward(100)
    t.right(90)
    t.forward(50)
    t.up()
    t.forward(10)
    t.down()


def letterl():
    t.up()
    t.forward(30)
    t.down()
    t.left(90)
    t.forward(100)
    t.backward(100)
    t.right(90)
    t.up()
    t.forward(10)


def letterM():
    t.up()
    t.forward(30)
    t.down()
    t.left(90)
    t.forward(100)
    t.right(135)
    t.forward(40)
    t.left(90)
    t.forward(40)
    t.right(130)
    t.forward(100)
    t.left(90)
    t.up()
    t.forward(10)
    t.down()


def letterm():
    t.up()
    t.forward(30)
    t.down()
    t.left(90)
    t.forward(50)
    t.backward(10)
    for lm1 in range(0,19):
        t.right(9)
        t.forward(2)
    t.left(180)
    for lm2 in range(0,19):
        t.right(9)
        t.forward(2)
    t.right(15)
    t.forward(42)
    t.left(90)
    t.up()
    t.forward(10)
    t.down()


def letterN():
    t.up()
    t.forward(30)
    t.down()
    t.left(90)
    t.forward(100)
    t.right(150)
    t.forward(120)
    t.left(150)
    t.forward(100)
    t.up()
    t.left(180)
    t.forward(100)
    t.left(90)
    t.forward(10)
    t.down()


def lettern():
    t.up()
    t.forward(30)
    t.down()
    t.left(90)
    t.forward(50)
    t.backward(10)
    for ln in range(0,19):
        t.right(9)
        t.forward(4)
    t.right(10)
    t.forward(42)
    t.left(90)
    t.up()
    t.forward(10)
    t.down()


def letterO():
    t.up()
    t.forward(80)
    t.down()
    t.circle(50)
    t.up()
    t.forward(50)
    t.down()


def lettero():
    t.up()
    t.forward(35)
    t.down()
    t.circle(25)
    t.up()
    t.forward(35)
    t.down()


def letterP():
    t.up()
    t.forward(30)
    t.down()
    t.left(90)
    t.forward(100)
    t.right(90)
    for lP in range(0, 12):
        t.forward(7)
        t.right(15)
    t.forward(7)
    t.left(90)
    t.forward(48)
    t.up()
    t.left(90)
    t.forward(25)
    t.down()


def letterp():
    t.up()
    t.forward(30)
    t.down()
    t.left(90)
    t.forward(52)
    t.right(90)
    for lp in range(0, 12):
        t.forward(7)
        t.right(15)
    t.forward(7)
    t.left(90)
    t.forward(48)
    t.backward(48)
    t.left(90)
    t.up()
    t.forward(25)
    t.down()


def letterQ():
    t.up()
    t.forward(80)
    t.down()
    t.circle(50)
    t.up()
    t.forward(20)
    t.left(90)
    t.forward(30)
    t.right(135)
    t.down()
    t.forward(40)
    t.left(45)
    t.up()
    t.forward(10)
    t.down()


def letterq():
    t.up()
    t.forward(50)
    t.down()
    t.circle(25)
    t.up()
    t.forward(25)
    t.right(90)
    t.forward(40)
    t.down()
    t.left(135)
    t.forward(20)
    t.backward(20)
    t.left(45)
    t.forward(65)
    t.backward(25)
    t.up()
    t.right(90)
    t.forward(10)
    t.down()


def letterR():
    t.up()
    t.forward(30)
    t.down()
    t.left(90)
    t.forward(100)
    t.right(90)
    for lR in range(0, 12):
        t.forward(7)
        t.right(15)
    t.forward(7)
    t.left(125)
    t.forward(60)
    t.up()
    t.left(55)
    t.forward(10)
    t.down()


def letterr():
    t.up()
    t.forward(30)
    t.down()
    t.left(90)
    t.forward(50)
    t.backward(10)
    for lr in range(0,19):
        t.right(9)
        t.forward(2)
    t.up()
    t.forward(40)
    t.left(80)
    t.forward(10)
    t.down()


def letterS():
    t.up()
    t.forward(30)
    t.down()
    t.forward(10)
    for lS1 in range(0,12):
        t.forward(7)
        t.left(15)
    for lS2 in range(0,12):
        t.forward(7)
        t.right(15)
    t.forward(10)
    t.up()
    t.right(90)
    t.forward(105)
    t.left(90)
    t.forward(40)
    t.down()


def letters():
    t.up()
    t.forward(30)
    t.down()
    t.forward(5)
    for ls1 in range(0,12):
        t.forward(4)
        t.left(15)
    for ls2 in range(0,12):
        t.forward(4)
        t.right(15)
    t.forward(5)
    t.up()
    t.right(90)
    t.forward(55)
    t.left(90)
    t.forward(15)
    t.down()


def letterT():
    t.up()
    t.forward(30)
    t.down()
    t.left(90)
    t.forward(100)
    t.right(90)
    t.backward(25)
    t.forward(50)
    t.up()
    t.right(90)
    t.forward(100)
    t.left(90)
    t.forward(10)


def lettert():
    t.up()
    t.forward(30)
    t.down()
    t.left(90)
    t.forward(100)
    t.backward(40)
    t.right(90)
    t.backward(10)
    t.forward(20)
    t.up()
    t.right(90)
    t.forward(60)
    t.left(90)
    t.forward(10)


def letterU():
    t.up()
    t.forward(30)
    t.left(90)
    t.forward(100)
    t.left(180)
    t.down()
    t.forward(80)
    for lU in range(0,19):
        t.left(9)
        t.forward(4)
    t.left(8)
    t.forward(80)
    t.up()
    t.left(180)
    t.forward(100)
    t.left(90)
    t.forward(10)
    t.down()


def letteru():
    t.up()
    t.forward(30)
    t.left(90)
    t.forward(50)
    t.down()
    t.left(180)
    t.forward(30)
    for lu in range(0,19):
        t.left(9)
        t.forward(4)
    t.left(8)
    t.forward(30)
    t.up()
    t.left(180)
    t.forward(50)
    t.left(90)
    t.forward(10)
    t.down()


def letterV():
    t.up()
    t.forward(30)
    t.left(90)
    t.forward(100)
    t.down()
    t.right(150)
    t.forward(110)
    t.left(135)
    t.forward(110)
    t.right(165)
    t.up()
    t.forward(100)
    t.left(90)
    t.forward(10)
    t.down()


def letterv():
    t.up()
    t.forward(30)
    t.left(90)
    t.forward(50)
    t.right(150)
    t.down()
    t.forward(60)
    t.left(135)
    t.forward(60)
    t.right(165)
    t.up()
    t.forward(60)
    t.left(90)
    t.forward(10)
    t.down()


def letterW():
    t.up()
    t.forward(30)
    t.left(90)
    t.forward(100)
    t.down()
    t.right(158)
    t.forward(110)
    t.left(135)
    t.forward(90)
    t.right(135)
    t.forward(90)
    t.left(135)
    t.forward(110)
    t.right(158)
    t.up()
    t.forward(100)
    t.left(90)
    t.down()


def letterw():
    t.up()
    t.forward(30)
    t.left(90)
    t.forward(50)
    t.down()
    t.right(158)
    t.forward(60)
    t.left(135)
    t.forward(40)
    t.right(135)
    t.forward(40)
    t.left(135)
    t.forward(60)
    t.right(158)
    t.up()
    t.forward(60)
    t.left(90)
    t.down()


def letterX():
    t.up()
    t.forward(30)
    t.down()
    t.left(45)
    t.forward(120)
    t.backward(120)
    t.right(45)
    t.up()
    t.forward(80)
    t.down()
    t.left(135)
    t.forward(120)
    t.backward(120)
    t.right(135)
    t.up()
    t.forward(10)
    t.down()


def letterx():
    t.up()
    t.forward(30)
    t.down()
    t.left(45)
    t.forward(70)
    t.backward(70)
    t.right(45)
    t.up()
    t.forward(45)
    t.down()
    t.left(135)
    t.forward(70)
    t.backward(70)
    t.right(135)
    t.up()
    t.forward(10)
    t.down()


def letterY():
    t.up()
    t.forward(30)
    t.left(90)
    t.forward(100)
    t.right(150)
    t.down()
    t.forward(50)
    t.left(135)
    t.forward(50)
    t.backward(50)
    t.right(165)
    t.forward(55)
    t.left(90)
    t.up()
    t.forward(10)
    t.down()


def lettery():
    t.up()
    t.forward(30)
    t.left(90)
    t.forward(50)
    t.right(150)
    t.down()
    t.forward(60)
    t.left(135)
    t.forward(60)
    t.backward(60)
    t.right(175)
    t.forward(60)
    t.backward(60)
    t.left(100)
    t.up()
    t.forward(20)
    t.down()
    


def letterZ():
    t.up()
    t.forward(30)
    t.down()
    t.forward(60)
    t.backward(60)
    t.left(50)
    t.forward(120)
    t.left(130)
    t.forward(60)
    t.up()
    t.backward(60)
    t.left(90)
    t.forward(95)
    t.left(90)
    t.forward(10)
    t.down()


def letterz():
    t.up()
    t.forward(30)
    t.down()
    t.forward(30)
    t.backward(30)
    t.left(50)
    t.forward(60)
    t.left(130)
    t.forward(30)
    t.up()
    t.right(180)
    t.forward(30)
    t.right(90)
    t.forward(50)
    t.left(90)
    t.forward(10)
    t.down()
    


t.up()
if lenght > 7 and lenght < 15:
    t.backward(lenght * 70)
elif lenght > 14:
    t.backward(lenght * 20)
else:
    t.backward(lenght * 60)
t.down()
for i in range(0, lenght):   
    if cool[i] == " ":
        space()
    elif cool[i] == ".":
        period()
    elif cool[i] == "A":
        letterA()
    elif cool[i] == "a":
        lettera()
    elif cool[i] == "B":
        letterB()
    elif cool[i] == "b":
        letterb()
    elif cool[i] == "C":
        letterC()
    elif cool[i] == "c":
        letterc()
    elif cool[i] == "D":
        letterD()
    elif cool[i] == "d":
        letterd()
    elif cool[i] == "E":
        letterE()
    elif cool[i] == "e":
        lettere()
    elif cool[i] == "F":
        letterF()
    elif cool[i] == "f":
        letterf()
    elif cool[i] == "G":
        letterG()
    elif cool[i] == "g":
        letterg()
    elif cool[i] == "H":
        letterH()
    elif cool[i] == "h":
        letterh()
    elif cool[i] == "I":
        letterI()
    elif cool[i] == "i":
        letteri()
    elif cool[i] == "J":
        letterJ()
    elif cool[i] == "j":
        letterj()
    elif cool[i] == "K":
        letterK()
    elif cool[i] == "k":
        letterk()
    elif cool[i] == "L":
        letterL()
    elif cool[i] == "l":
        letterl()
    elif cool[i] == "M":
        letterM()
    elif cool[i] == "m":
        letterm()
    elif cool[i] == "N":
        letterN()
    elif cool[i] == "n":
        lettern()
    elif cool[i] == "O":
        letterO()
    elif cool[i] == "o":
        lettero()
    elif cool[i] == "P":
        letterP()
    elif cool[i] == "p":
        letterp()
    elif cool[i] == "Q":
        letterQ()
    elif cool[i] == "q":
        letterq()
    elif cool[i] == "R":
        letterR()
    elif cool[i] == "r":
        letterr()
    elif cool[i] == "S":
        letterS()
    elif cool[i] == "s":
        letters()
    elif cool[i] == "T":
        letterT()
    elif cool[i] == "t":
        lettert()
    elif cool[i] == "U":
        letterU()
    elif cool[i] == "u":
        letteru()
    elif cool[i] == "V":
        letterV()
    elif cool[i] == "v":
        letterv()
    elif cool[i] == "W":
        letterW()
    elif cool[i] == "w":
        letterw()
    elif cool[i] == "X":
        letterX()
    elif cool[i] == "x":
        letterx()
    elif cool[i] == "Y":
        letterY()
    elif cool[i] == "y":
        lettery()
    elif cool[i] == "Z":
        letterZ()
    elif cool[i] == "z":
        letterz()
    else:
        print("character %s is not defined yet" % cool[i])

t.hideturtle()
