
def intersection(lst1, lst2) -> None:
    list3 = [value for value in lst1 if value in lst2]
    print(list3)



if __name__ == '__main__':
    list1= [1,3,6,78,35,55]
    list2=[12,24,35,24,88,120,155]
    intersection(list1, list2)