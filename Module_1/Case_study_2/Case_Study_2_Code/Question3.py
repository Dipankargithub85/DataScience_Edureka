import re


def checkpwd(newstr) -> None:

    numlist = re.findall(r'[\d]+', newstr)
    splist = re.findall(r'[\$#@]+', newstr)
    smallist = re.findall(r'[a-z]+', newstr)
    biglist = re.findall(r'[A-Z]+', newstr)

    if len(newstr) < 6:
        print(" Password require minimum length 6")
    elif len(newstr) > 12:
        print(" Password require minimum length 12")
    elif len(numlist) == 0:
        print(" Password require At least 1 number between 0-9")
    elif len(smallist) == 0:
        print(" Password require At least 1 letter between [a-z]")

    elif len(biglist) == 0:
        print(" Password require At least 1 letter between [A-Z]")

    elif len(splist) == 0:
        print(" Password require  At least 1 character from [$#@]")
    else:
        print(" All Okay ")



if __name__ == '__main__':
    inppwd = input("Enter the Password:")
    checkpwd(inppwd)