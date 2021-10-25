
import re


def calulateval(newstr) -> None:

    numlist = re.findall(r'[-+]?[.]?[\d]+', newstr)
    numstr= ''.join(numlist)
    strlist = re.findall(r'[a-z]+', newstr)
    strval = ''.join(strlist)
    print("LETTERS:" + str(len(strval)))
    print("DIGITS:" + str(len(numstr)))


if __name__ == '__main__':
    mystr = input("Enter teh string")
    newstr = mystr.replace(" ", "").lower()
    calulateval(newstr)