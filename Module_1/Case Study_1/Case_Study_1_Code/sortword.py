
def sortwords(inpstr) -> None:
    # convert String to a list of words
    wordsli = [word.lower() for word in inpstr.split()]
    # sort the word list
    wordsli.sort()
    # print the sorted words
    print("The sorted words are:")
    for val in wordsli:
        print(val)


#main function to call the sortwords function

if __name__ == '__main__':
    strval = input("Enter a string OR sequence of words ")
    sortwords(strval)