

def mainProgram():
    myList = []
    print("Hello, there! Let's work with lists!")
    print("Choose from the following options, Type a number below!")
    choice = input("1, add to a list, 2, return the value at an index position! ")
    if choice == "1":
        addToList()
    elif choice == "2":
        indexValues()
    #TO ADD: 1. a way to loop the action 2. a way to quit 3. think of repitition 
    
def addToList():
    print("Adding to a list! Great choice!")
    newItem = input("Type an integer here!  ")
    myList.append(int(newItem))
    

def indexValues():

if __name__ == "__main__":
    mainProgram()

