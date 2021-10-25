
def liprint() -> None:
    a = [4, 7, 3, 2, 5, 9]
    for i in a:
        print ("List Item value is "+ str(i)+ " And position of the item is ", a.index(i))


if __name__ == '__main__':
    liprint()
