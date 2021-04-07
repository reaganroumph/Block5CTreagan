


myList = []
uniqueList = []
import random

def mainProgram():
    while True:
        try:
            print("Hello, there! Let's work with lists!")
            print("Choose from the following options, Type a number below!")
            choice = input("""1. add to a list or
2. add a bunch of numbers
3. return the value at an index position
4. random search
5. linear search
6. sort list
7. print lists
8. recursive binary search
9. iterative binary search
10. quit program""")
            if choice == "1":
                addToList()
            elif choice == "2":
                addABunch()
            elif choice == "3":
                indexValues()
            elif choice == "4":
                randomSearch()
            elif choice == "5":
                linearSearch()
            elif choice == "6":
                sortList(myList)
            elif choice == "7":
                printLists()
            elif choice == "8":
                binSearch = input("what number are you looking for?  ")
                recursiveBinarySearch(uniqueList, 0, len(uniqueList)-1, int(binSearch))
            elif choice == "9":
                binSearch = input("what number are you looking for?  ")
                result = iterativeBinarySearch(uniqueList, int(binSearch))
                if result != -1:
                    print("your number is at index position {}".format(result))
                else:
                    print("your number is not found in that list, bud!")
            else:
                break
        except:
            print("you made a whoopsie!")
         
def addToList():
    print("Adding to a list! Great choice!")
    newItem = input("Type an integer here!  ")
    myList.append(int(newItem))

def addABunch():
    print("we're gonna add a bunch of integers here!")
    numToAdd = input("how many integers would you like to add?  ")
    numRange = input("and how high would you like these numbers to go?  ")
    for x in range(0,int(numToAdd)):
        myList.append(random.randint(0, int(numRange)))
    print("your list is now complete.")
    

def indexValues():
    print("ohhh! I heard you need a particular piece of data!")
    indexPos = input("What index position are you curious about?")
    print (myList[int(indexPos)])

def sortList (myList):
    print("a little birdie told me you needed some sorted data!")
    for x in myList:
        if x not in uniqueList:
            uniqueList.append(x)
    uniqueList.sort()
    showMe = input("wanna see your new list?   Y/N")
    if showMe.lower() == "y":
        print(uniqueList)
    
def randomSearch():
    print("RaNdOm SeArCh?!")
    print(myList[random.randint(0,len(myList)-1)])
    if len(uniqueList) > 0:
        print(uniqueList[random.randint(0, len(uniqueList)-1)])

def linearSearch():
    print("we're gonna check out each item one at a time in your list! this sucks.")
    searchItem = input("what you looking for, pardner?   ")
    for x in range(len(myList)):
        if myList[x] == int(searchItem):
            print("your item is at index position {}".format(x))

def recursiveBinarySearch(uniqueList, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if uniqueList[mid] == x:
            print("your number is at index position {}".format(mid))
            return mid
        
        elif uniqueList[mid] > x:
            return recursiveBinarySearch(uniqueList, low, mid - 1, x)
        
        else:
            return recursiveBinarySearch(uniqueList, mid + 1, high, x)
    else:
        print("your number isn't here!")

def printLists():
    if len(uniqueList) == 0:
        print(myList)
    else:
        whichOne = input("which list? sorted or unsorted?   ")
        if whichOne.lower() == "sorted":
            print(uniqueList)
        else:
            print(myList)

def iterativeBinarySearch(uniqueList, x):
    low = 0
    high = len(uniqueList)-1
    mid = 0

    while low <= high:
        mid = (High + low) // 2

        if uniqueList[mid] < x:
            low = mid + 1

        elif uniqueList[mid] > x:
            high - mid - 1
        else:
            return mid
    return -1


if __name__ == "__main__":
    mainProgram()

