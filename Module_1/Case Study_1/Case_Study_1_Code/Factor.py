import sys


def factors(val) -> None:

    print("The factors of", val, "are:")
    factcnt = 0
    for i in range(1, val + 1):
        if val % i == 0:
            factcnt += 1
            print(i)

    if factcnt % 2 == 0:
        print("The given Number " + str(val) + " has even no.of factors")
    else:
        print("The given Number " + str(val) + " has odd no.of factors")




if __name__ == '__main__':
    val = int(input("Enter the Value:"))
    if val <= 0:
        print("Please provide  value grater than 0")
        sys.exit(0)
    factors(val)
