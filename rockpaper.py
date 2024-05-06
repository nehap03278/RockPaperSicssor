from random import *
x="y"
while (x =="Y" or x=="y"):
    print("For rock enter 1\nFor paper enter 2\nFor sisscors enter 3")
    print("Enter your choice")
    user_input=int(input())
    computer_ip=randint(1,3)
    print("Computer choose"+str(computer_ip))
    if(computer_ip==user_input):
        print("It is a Tie!")
    elif(computer_ip== 3 and user_input==1):
        print("You Win!")
    elif(computer_ip==1 and user_input==3):
        print("Computer Wins!")
    elif(computer_ip>user_input):
        print("Computer Wins!")
    elif(computer_ip<user_input):
        print("You Win!")
    else:
        print("Enter valid number")
    x=input("To continue enter y or Y")
