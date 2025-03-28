l = [['1','2','3'],
     ['4','5','6'],
     ['7','8','9']]

def replaceUser(u,sign):
    if   u == 1 : l[0][0] = sign
    elif u == 2 : l[0][1] = sign
    elif u == 3 : l[0][2] = sign
    elif u == 4 : l[1][0] = sign
    elif u == 5 : l[1][1] = sign
    elif u == 6 : l[1][2] = sign
    elif u == 7 : l[2][0] = sign
    elif u == 8 : l[2][1] = sign
    elif u == 9 : l[2][2] = sign

def horizontalcheck():
    if 'O' == l[0][0] == l[0][1] == l[0][2] or 'O' == l[1][0] == l[1][1] == l[1][2] or 'O' == l[2][0] == l[2][1] == l[2][2] :
        return True
    elif 'X' == l[0][0] == l[0][1] == l[0][2] or 'X' == l[1][0] == l[1][1] == l[1][2] or 'X' == l[2][0] == l[2][1] == l[2][2] :
        return True

def verticlecheck():
    if 'O' == l[0][0] == l[1][0] == l[2][0] or 'O' == l[0][1] == l[1][1] == l[2][1] or 'O' == l[0][2] == l[1][2] == l[2][2]:
        return True
    elif 'X' == l[0][0] == l[1][0] == l[2][0] or 'X' == l[0][1] == l[1][1] == l[2][1] or 'X' == l[0][2] == l[1][2] == l[2][2]:
        return True

def diagonalcheck():
    if 'O' == l[0][0] == l[1][1] == l[2][2] or 'O' == l[0][2] == l[1][1] == l[2][0]:
        return True
    elif 'X' == l[0][0] == l[1][1] == l[2][2] or 'X' == l[0][2] == l[1][1] == l[2][0]:
        return True

def printMatrix():
    print(l[0])
    print(l[1])
    print(l[2])

def resetdb():
    global l
    l = [['1','2','3'],
         ['4','5','6'],
         ['7','8','9']]

print("User 1 represents O")
print("User 2 represents X")
resetdb()
nl = []
flagu1= True
flagu2 = True
while True:
    if len(nl) == 9:
        print("Match Tie")
        break
    if flagu1:
        u1 = int(input("User O Chance : enter 1 to 9 : ", ))
        if u1 not in nl:
            nl.append(u1)
            replaceUser(u1,'O')
            printMatrix()
            flagu2 = True
            if horizontalcheck() or verticlecheck() or diagonalcheck() :
                print("User 1 wins")
                break
        else :
            print("Position already filled")
            flagu2 = False
    if len(nl) == 9:
        print("Match Tie")
        break
    if flagu2:
        u2 = int(input("User X Chance : enter 1 to 9 : ", ))
        if u2 not in nl :
            nl.append(u2)
            replaceUser(u2,'X')
            printMatrix()
            flagu1 = True
            if horizontalcheck() or verticlecheck() or diagonalcheck() :
                print("User 2 wins")
                break
        else :
            print("Position already filled")
            flagu1 = False