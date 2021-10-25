
def removevalfromlst(lst1) -> None:
    list3 = [value for value in lst1 if value != 24]
    print(list3)




if __name__ == '__main__':
    list1=  [12,24,35,24,88,120,155]
    removevalfromlst(list1)