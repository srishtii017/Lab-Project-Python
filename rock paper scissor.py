import random
print("******Welcome To Rock , Paper and Scissor Game******")
print()
name=input("Enter Your Good Name :")
print(f'WELCOME {name} !')
while(True):
    c=random.choice(('rock','paper','scissor'))
    h=input("Enter Your Choice: ")
    while(True):
        if c=="rock" and h=="scissor":
            print("Computer Wins! Oops You Lose The Game.")
            break
        elif c=="paper" and h=="rock":
            print("Computer Wins! Oops You Lose The Game.")
            break
   
        elif c=="scissor" and h=="paper":
            print("Computer Wins! Oops You Lose The Game.")
            break
        elif c==h:
            print("Its a Tie.")
            break

        else:
            print(f"Congratualtions {name}! You Win.")
            break
    choice=input("Do You Want To Play It Again: ")
    if choice=="no":
        print(f"Thank You {name}!")
        break
        
