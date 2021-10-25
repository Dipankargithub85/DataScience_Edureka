import re
from cryptography.fernet import Fernet


def checkrefid(newstr) -> tuple:

    numlist = re.findall(r'[\d]+', newstr)
    splist = re.findall(r'[\$#@]+', newstr)
    smallist = re.findall(r'[a-z]+', newstr)
    biglist = re.findall(r'[A-Z]+', newstr)

    if len(newstr) < 12:
        print(" Password require minimum length 12")

    elif len(numlist) == 0:
        print(" Password require At least 1 number between 0-9")
    elif len(smallist) == 0:
        print(" Password require At least 1 letter between [a-z]")

    elif len(biglist) == 0:
        print(" Password require At least 1 letter between [A-Z]")

    elif len(splist) == 0:
        print(" Password require  At least 1 character from [$#@&%*]")
    else:
        enmsgtup = encryptval(newstr)

    return enmsgtup


def encryptval(newstr) -> tuple:
    key = Fernet.generate_key()
    fernet = Fernet(key)
    encMessage = fernet.encrypt(newstr.encode())
    return (encMessage,key)


def getdryptval(enrmsg) -> str:
    fernet = Fernet(enrmsg[1])
    decMessage = fernet.decrypt(enrmsg[0]).decode()
    return decMessage


if __name__ == '__main__':
    inppwd = input("Enter the Password:")
    encrypmsgtup = checkrefid(inppwd)
    print("encrypted reference-id is ",encrypmsgtup[0])
    confmval= input("Do you want to see the decrypted value(y/n):")
    if confmval.lower() == 'y':
        derypmsg = getdryptval(encrypmsgtup)
        print("decrypted reference-id is ",derypmsg)
    else:
        print("Thank you for your input")
