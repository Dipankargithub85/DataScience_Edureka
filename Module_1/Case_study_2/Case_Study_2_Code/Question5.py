from typing import List


def printchar(mystr) -> None:
    listr= strtolist(mystr)
    strval=""
    for i in listr:
        if listr.index(i) % 2 == 0:
            strval = strval + i

    print ("The string value is :", strval)



def strtolist(mystr) -> List:
    list1 = []
    list1[:0] = mystr
    return list1



if __name__ == '__main__':
    mystr = input("Enter the String:")
    printchar(mystr)
