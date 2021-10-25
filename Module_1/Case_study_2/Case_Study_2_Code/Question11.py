
def removevalfromlst(lst1) -> None:
    list3 = [value for value in lst1 if value % 5 != 0 and value % 7 != 0 ]
    print(list3)




if __name__ == '__main__':
    list1=  [12,24,35,70,88,120,155]
    removevalfromlst(list1)