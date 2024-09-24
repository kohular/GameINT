# Imports
import random
import sys 
# Intializing of variables
Guess = []
R1 = 0
R2 = 0
R3 = 0
R4 = 0
G1 = ""
G2 = ""
G3 = ""
G4 = ""
yes= "Yes"
White = 1
Blue = 2
Red = 3
Yellow = 4
Green = 5
Purple = 6
count = 0
Q = ""
Name = ""
ans = "y"
# Start
Q = input("Shall we start the game?(Y/N) ")
if Q!= "N" and Q!="n" and Q!= "Y" and Q!= "y":
    print("Wrong input. Try again")
    Q = input("Shall we start the game?(Y/N) ")
print("INSTRUCTIONS")
print(" Find the correct color pegs!")
print(" You have 8 attempts to guess it!")
print(" There are four colors you need to find!")
print(" If the Guess numbers are not equal to 4, it's an error. 1 attempt over. Try Again")
print(" If you want to terminate the game, Enter 0000 ")
print("Good Luck")
if Q == "N" or Q == "n":
    print("Thank you")
elif Q == "Y" or Q == "y":
    Name = input("Enter the players name: ")
    print("                                Hi", Name, "Welcome to GameInt")
    print("Number to Guess- X X X X", "                                      Color Mapping")
    print("                                                                      1-White 2-Blue 3-Red")
    print("                                                                      4-Yellow 5-Green 6-Purple")
    while ans == "y" or ans == "Y":
        R1 = (random.randint(White, Purple))
        R2 = (random.randint(White, Purple))
        R3 = (random.randint(White, Purple))
        R4 = (random.randint(White, Purple))
        Count = 0
        for count in range(1, 9):
            Count = Count + 1
            Score = 900 - (100 * Count)
            Guess = str(input('Enter the color guesses(Maximum four values) '))
            Guess = [int(Guess) for Guess in Guess]
            if len(Guess) != 4:
                print("Invalid guesses. Enter four values")
                print("You have", 8 - Count ,"attempts remaining. Try Again")
                continue
            if Guess[0] == 0 and Guess[1] == 0 and Guess[2] == 0 and Guess[3] == 0:
                print("Game over")
                sys.exit()
            if Guess[0]<=6:
                if Guess[0]==R1:
                    G1= "1"
                elif Guess[0]==R2 or Guess[0]==R3 or Guess[0]==R4:
                    G1= "0"
                elif Guess[0]!=R1 and Guess[0]!=R2 and Guess[0]!=R3 and Guess[0]!=R4:
                    G1= "."
            else:
                print("Invalid Guess. Try Again")
                continue
            if Guess[1]<=6:
                if Guess[1]==R2:
                    G2= "1"
                elif Guess[1]==R1 or Guess[1]==R3 or Guess[1]==R4:
                    G2= "0"
                elif Guess[1]!=R1 and Guess[1]!=R2 and Guess[1]!=R3 and Guess[1]!=R4:
                    G2= "."
            else:
                print("Invalid Guess. Try Again")
                continue
            if Guess[2]<=6:
                if Guess[2]==R3:
                    G3= "1"
                elif Guess[2]==R1 or Guess[2]==R2 or Guess[2]==R4:
                    G3= "0"
                elif Guess[2]!=R1 and Guess[2]!=R2 and Guess[2]!=R3 and Guess[2]!=R4:
                    G3= "."
            else:
                print("Invalid Guess. Try Again")
                continue
            if Guess[0]<=6:
                if Guess[3]==R4:
                    G4= "1"
                elif Guess[3]==R1 or Guess[3]==R2 or Guess[3]==R3:
                    G4= "0"
                elif Guess[3]!=R1 and Guess[3]!=R2 and Guess[3]!=R3 and Guess[3]!=R4:
                    G4= "."
            else:
                print("Invalid Guess. Try Again")
                continue
            if Count <= 8 :
                print('_________________________________________________________________')
                print("Attempt", "                 Guess", "                           Result")
                print(Count, "                      ", Guess, "              ","       ",G1, G2,"\n                                                            ",G3, G4)
                print('_________________________________________________________________')
            if G1== "1" and G2== "1" and G3=="1" and G4=="1":
                break
            else:
                continue
        if Guess[0]==R1 and Guess[1]==R2 and Guess[2]==R3 and Guess[3]==R4:
            print("Congratulations",Name, "You have won the game… ")
            print("                                You have scored", Score, "points")
        else:
            print("Sorry. You have lost the game. ")
            print("The number to guess was",R1,R2,R3,R4)
            print("                                You have scored 0 points")
        ans = input("Do you want to play another game(Y/N)")
print("Game Over")
