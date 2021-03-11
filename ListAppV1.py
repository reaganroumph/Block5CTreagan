


myList = []

def mainProgram():
    while True:
    print("Hello, there! Let's work with lists!")
    print("Choose from the following options, Type a number below!")
    choice = input("""1. add to a list or
2. return the value at an index position!
3. exit program  """)
    if choice == "1":
        addToList()
    elif choice == "2":
        indexValues()
    elif choice == "3":
        break
    #TO ADD: 1. a way to loop the action 2. a way to quit 3. think of repitition 
    
def addToList():
    print("Adding to a list! Great choice!")
    newItem = input("Type an integer here!  ")
    myList.append(int(newItem))
    

def indexValues():
    print("ohhh! I heard you need a particular piece of data!")
    indexPos = input("What index position are you curious about?")
    print (myList[int(indexPos)])

if __name__ == "__main__":
    mainProgram()

