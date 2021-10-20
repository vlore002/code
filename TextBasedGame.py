# Valentina Lore
# defined function as "show_instructions"
# callback later
def show_instructions():
    # create instructions for the user to follow using print()
    print("******************************************************")
    print("Instructions")
    print("******************************************************")
    print("Jungle Temple Text Adventure Game")
    print("Collect 6 items to unlock the exit room.")
    print("However, the Cursed Hunter will be waiting for you...")
    print("Build the Angel Gauntlet of Crystals to defeat the Hunter")
    print("Move commands: go South, go North, go East, go West")
    print("Add to Inventory: get 'item name'")

# defined function as "current_status"
# callback later when using the function "main"
def current_status(currentPosition, inventory):
    print("******************************************************")
    print("Current Status")
    print("******************************************************")
    print("You are in " + currentPosition)
    print("Inventory: ", inventory)
    print("******************************************************")

# defined function as "endgame"
# callback later when using the function "main"
def endgame(inventory):
    if len(inventory) < 6:
        print("You are about to Escape. \n You see the light... \n But out of nowhere, the Cursed Hunter appears in "
              "front of you")
        print("You check your inventory to build the Angel Gauntlet of Crystals.")
        print("But you cannot finish the build.")
        print("This is because you only have " + str(len(inventory)) + " out of 6 items")
        print("You are defenseless. The Cursed Hunter punches through your chest and absorbs your soul...")
        print("Game over.")
    else:
        print("You are about to Escape. \n You see the light... \n But out of nowhere, the Cursed Hunter appears in "
              "front of you")
        print("You check your inventory to build the Angel Gauntlet of Crystals.")
        print("You have all 6 items to complete the build.")
        print("You use the Angel Gauntlet of Crystals and defeat the Cursed Hunter")
        print("Congratulations! You win!")

# defined function as "main"
def main():
    # we call back function "show_instructions" below
    show_instructions()

    inventory = []
    # variable called currentPosition equals string called 'Main Temple'
    currentPosition = 'Main Temple'
    current_status(currentPosition, inventory)

    #create dictionary for rooms
    rooms = {
        'Main Temple': {'West': 'West Temple', 'South': 'South Temple', 'North': 'North Temple', 'East': 'East Temple'},
        'West Temple': {'East': 'Main Temple', 'Item': 'Red Crystal'},
        'North Temple': {'South': 'Main Temple', 'East': 'Secret Room of North Temple', 'Item': 'Blue Crystal'},
        'Secret Room of North Temple': {'West': 'North Temple', 'Item': 'Green Crystal'},
        'East Temple': {'West': 'Main Temple', 'North': 'Secret Room of East Temple', 'Item': 'Yellow Crystal'},
        'Secret Room of East Temple': {'South': 'East Temple', 'Item': 'Purple Crystal'},
        'South Temple': {'North': 'Main Temple', 'East': 'Exit Room', 'Item': 'Angel Gauntlet'},
        'Exit Room': 'The Cursed Hunter'
    }
    #create dictionary for items
    items = {'West Temple': 'Red Crystal', 'North Temple': 'Blue Crystal',
             'Secret Room of North Temple': 'Green Crystal',
             'East Temple': 'Yellow Crystal', 'Secret Room of East Temple': 'Purple Crystal',
             'South Temple': 'Angel Gauntlet'
             }
    #create a while loop to begin executing the game with user input
    while True:
        # if direction == Exit Room, then break the while loop
        if currentPosition == 'Exit Room':
            break
        # variable called direction denotes an input from user of type string
        direction = input("\nPlease enter direction to move (East/West/North/South) or Q to quit: ")
        # if direction == Q, then break the while loop
        if direction == "Q":
            break
        # if direction in rooms[currentPosition] is true, then print:
        #... "You have reached the " + rooms[currentPosition][direction]
        if direction in rooms[currentPosition]:
            print("\nYou have reached the " + rooms[currentPosition][direction])
            #due to user input, currentPosition updates
            currentPosition = rooms[currentPosition][direction]
            # if there are items in currentPosition, then print:
            # ("You found the " + item)
            if currentPosition in items:
                item = items[currentPosition]
                print("\nYou found the " + item)
                collectItem = input("Collect Item? Yes/No: ")
                #If user selects "Yes", then print the following:
                if collectItem == "Yes" or collectItem == "yes":
                    print("You collected " + item)
                    inventory.append(item)
                    items.pop(currentPosition)
                #If user selects "No", then print the following:
                else:
                    print("\nYou must collect " + item + " if you hope to escape!")
                    print("Collecting " + item)
                    inventory.append(item)
                    items.pop(currentPosition)
                print(inventory)
        #If the above "if" statements are not "true" after user input, then print:
        else:
            print("\nSorry, no path in that direction!")
    #call endgame function to execute
    endgame(inventory)

# always true
if __name__ == '__main__':
    main()

