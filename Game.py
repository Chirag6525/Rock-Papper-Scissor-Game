#Rock, Paper, Scissor Game

import random
#sign a value to the Rock, paper and Scissor
Rock = 1
Paper = 2
Scissor = 3
L = [Rock, Paper, Scissor]
UserPoint = 0 
CompPoint = 0
i = 1
Choice = input("Are you ready to Play(y/n): ")
while(Choice == 'y'):
    print("Play will Commenced Five Times/n")
    while(i < 3):#Play for five times
        print("\n\n1.🪨\n2.📄\n3.✂️")
        #take a input from user
        User = int(input("Enter Your Choice(1/2/3): "))
        #computer generate its choice
        Computer = random.choice(L)
        print("Computer: {}".format(Computer))
        if User == 1:
            if Computer == 1:
                print("Its a Tie!!!")
                UserPoint += 1
                CompPoint += 1
            elif Computer == 2:
                print("Computer won!!!")
                CompPoint += 1
            else:
                print("User won!!!")
                UserPoint += 1
        elif User == 2:
            if Computer == 2:
                print("Its a Tie!!!")
                UserPoint += 1
                CompPoint += 1
            elif Computer == 3:
                print("Computer won!!!")
                CompPoint += 1
            else:
                print("User won!!!")
                UserPoint += 1
        elif User == 3:
            if Computer == 3:
                print("Its a Tie!!!")
                UserPoint += 1
                CompPoint += 1
            elif Computer == 1:
                print("Computer won!!!")
                CompPoint += 1
            else:
                print("User won!!!")
                UserPoint += 1
        i += 1
    print("UserPoint : {}\nComputerPoint: {}".format(UserPoint, CompPoint))
    if UserPoint > CompPoint:
        print("The Winner is User!!!")
    else :
        print("The Winner is Computer!!!")
    Choice = input("Are you ready to Play Again(y/n): ")
if Choice == 'n':
    print("\nThank You for Playing!!!! \nGood Bye!!!!")
    

