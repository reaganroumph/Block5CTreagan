


myList = []
import

def mainProgram():
    while True:
        try:
            print("Hello, there! Let's work with lists!")
            print("Choose from the following options, Type a number below!")
            choice = input("""1. add to a list or
2. return the value at an index position!
3. random search
4. quit program """)
            if choice == "1":
            addToList()
            elif choice == "2":
            indexValues()
            elif choice == "3":
            randomSearch()
            else:
                break
        except:
        print("you made a whoopsie!") 
    
def addToList():
    print("Adding to a list! Great choice!")
    newItem = input("Type an integer here!  ")
    myList.append(int(newItem))
    

def indexValues():
    print("ohhh! I heard you need a particular piece of data!")
    indexPos = input("What index position are you curious about?")
    print (myList[int(indexPos)])

def randomSearch():
    print("RaNdOm SeArCh?!")
    print(myList[random.randint(0,len(myList)-1)])

if __name__ == "__main__":
    mainProgram()

