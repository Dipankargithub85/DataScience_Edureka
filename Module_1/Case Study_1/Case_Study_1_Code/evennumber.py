
def oddeven() -> None:
    print ("Even Number are:-")
    strval=""
    for i in range(1000, 3001):
        if i % 2 == 0:
            strval = strval + str(i) + ','
            #print(i, end=",")
    actualval= strval[0:len(strval)-1]
    print(actualval)


if __name__ == '__main__':

    oddeven()
