import random
from random import randint

def Game():
    y = random.randint(1, 20)
    print("Guess the Number")
    i = int(input())
    gameengine(y,i)
    

def gameengine(y, i):
    if i == y:
        print("Yay you guessed right on your first attempt")
    else:
        count = 0
        while count < 3:
            while i != y:    
                if ((i-y)>=3):
                    print("BLUE")
                elif ((i-y)<=(-3)):
                    print("RED")
                elif ((1)<=(i-y)<=3):
                    print("YELLOW")
                elif((-1)>=(i-y)>=(-3)):
                    print("YELLOW")
                i = int(input())
                break
            else:
                print("Yay, you guessed it")
                break
            count += 1
        else:
             print("Sorry your out of chances.\nThe number was",y)
                
reset = True

while reset == True:
    Game()
    print("Do you want play again say 1 else 0")
    reset  = int(input())
else:
    print("Bye Bye")
                
    