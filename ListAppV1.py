


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
9. create letter list
10. iterative binary search
11. quit program""")
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
                letterList()
            elif choice == "10":
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

"""
AddToList()
the add to list function works by asking the user what integer they would like to add to the list and then
appending it to the end of the myList
"""
def addToList():
    print("Adding to a list! Great choice!")
    newItem = input("Type an integer here!  ")
    myList.append(int(newItem))

"""
AddABunch()
the add a bunch function asks the user how many integers and how high the
value they want the integers to be, this then adds the integers to myList
that follows the boundaries given by the user
"""

def addABunch():
    print("we're gonna add a bunch of integers here!")
    numToAdd = input("how many integers would you like to add?  ")
    numRange = input("and how high would you like these numbers to go?  ")
    for x in range(0,int(numToAdd)):
        myList.append(random.randint(0, int(numRange)))
    print("your list is now complete.")

"""
indexValues()
the index value pulls out a certain integer by the user at the index
position given by the user
"""
    
def indexValues():
    print("ohhh! I heard you need a particular piece of data!")
    indexPos = input("What index position are you curious about?")
    print (myList[int(indexPos)])

"""
sortList()
the sort list function works by sorting the myList function
and turning it into a 'new' list called uniqueList
"""

def sortList (myList):
    print("a little birdie told me you needed some sorted data!")
    for x in myList:
        if x not in uniqueList:
            uniqueList.append(x)
    uniqueList.sort()
    showMe = input("wanna see your new list?   Y/N")
    if showMe.lower() == "y":
        print(uniqueList)

"""
randomSearch()
the random search function gives you a random integer from either myList or uniqueList
"""
def randomSearch():
    print("RaNdOm SeArCh?!")
    print(myList[random.randint(0,len(myList)-1)])
    if len(uniqueList) > 0:
        print(uniqueList[random.randint(0, len(uniqueList)-1)])

"""
linearSearch()
linear search works by searching for a certain value of integer through the list by
going through every piece of data one by one, it then spits out what index pos the value is at
"""

def linearSearch():
    print("we're gonna check out each item one at a time in your list! this sucks.")
    searchItem = input("what you looking for, pardner?   ")
    for x in range(len(myList)):
        if myList[x] == int(searchItem):
            print("your item is at index position {}".format(x))

"""
recursiveBinarySearch()
this function works by giving the user the mid value index pos
"""

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

"""
printLists()
print lists works by printing either the myList or uniqueList depening on if
the user responds with sorted or unsorted
"""

def printLists():
    if len(uniqueList) == 0:
        print(myList)
    else:
        whichOne = input("which list? sorted or unsorted?   ")
        if whichOne.lower() == "sorted":
            print(uniqueList)
        else:
            print(myList)

"""
iterativeBinarySearch()
this function returns the user the mid value 
"""

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

"""
letterList()
this function works by asking the user for the string they want to add to the list
it then asks if the user would like to see their new list
"""

def letterList():
    letterList = []
    print("adding letters to a list i see pardner, nice")
    newLetter = input("type your word/letters here")
    letterList.append(newLetter)
    lemmeSee = input("would you like to see your new letter list?  Y/N?")
    if lemmeSee.lower() == "y":
        print(letterList)

    
    
    
    



if __name__ == "__main__":
    mainProgram()

