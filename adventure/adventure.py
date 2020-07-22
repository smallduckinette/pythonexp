#!/usr/bin/python

hasSword = False

# Party
def party():
    print("** Party! You have won the adventure!")

# The castle
def castle():
    print("** The castle is really enormous! There are many people there, as there is a party.");
    if hasSword:
        print("Since you have a sword, they invite you to get into the party!\n1 - Enter the party\n2 - Go back to the lake")
        answer = input()
        if answer == "1":
            party()
        elif answer == "2":
            lake()
        else:
            castle()
    else:
        print("You cannot get into the castle, as you need a sword to get in.\n1 - Go back to the lake")
        answer = input()
        if answer == "1":
            lake()
        else:
            castle()

# The forest
def forest():
    global hasSword
    hasSword = True;
    print("** The forest is deep and silent. You see a beautiful sword stuck in a tree, and you grab it.\n1 - Go back to the lake")
    answer = input()
    if answer == "1":
        lake()
    else:
        forest()

def lake():
    print("** You are near a lake. The sky is blue, with just a few clouds. You can see on the other side of the lake a large castle. Closer to you, there is a dark forest.\nYou can:\n1 - Go to the castle\n2 - Enter the forest")
    answer = input()
    if answer == "1":
        castle();
    elif answer == "2":
        forest();
    else:
        lake()

        
lake()

    
