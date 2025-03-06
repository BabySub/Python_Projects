name = input("Enter your name: ")
print("hello",name,"welcome to the game")
should_we_play = input("Do you want to play?").lower() #lower() converts input string to lowercase
#conditions use->
play= should_we_play=="yes"

#if statement->
if should_we_play=="yes" or should_we_play=="y": #or and use
    print("Let's play!")
    weapon=input("choose your weapon: marshmallow or axe?")
    direction=input("Do you want to go right or left?").lower()
    if direction =="left":
        print("you went left and fell off  a cliff, you died!")
    elif direction=="right":
        choice=input("we went right, and found a bridge. Do you want to swim under or cross it? (swim/cross)").lower()
        if choice=="swim" and weapon=="marshmallow":
            print("you were eaten by an alligator you died!")
        elif choice=="swim" and weapon=="axe":
            print("You faced an alligator in the water and killed it with your axe, found the gold on the other side and won!")
        else:
            print("You found the gold on the other side, you won!")
    else: 
        print("not a valid input, you died")
else:
    print("OK, returning to home...")