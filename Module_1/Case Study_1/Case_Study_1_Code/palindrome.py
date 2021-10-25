
def getpalindrome(val) -> None:
    if val == val[::-1]:
        print(" The Value is Palindrome")
    else:
        print(" The Value is Not Palindrome")


if __name__ == '__main__':
    val= input("Enter the value to check Palindrome: ")
    getpalindrome(val.lower())