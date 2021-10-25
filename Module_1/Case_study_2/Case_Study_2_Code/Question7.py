from collections import Counter
from typing import List


def getcnt(mystr) -> None:
    strlist = strtolist(mystr)
    for k,v in dict((Counter(strlist))).items():
        print(str(k) + "," + str(v))



def strtolist(mystr) -> List:
    list1 = []
    list1[:0] = mystr
    return list1



if __name__ == '__main__':
    mystr = input("Enter the String:")
    getcnt(mystr)
