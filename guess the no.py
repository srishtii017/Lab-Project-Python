import random
print("*****Welcome To Guess The Number*****")
name=input("Enter Your Good Name : ")
print(f"WELCOME {name} !")
l=input("Select Your Level: ")
while(True):
    
    if l=="easy":
        rd=random.randrange(1,50)
        print(f"You Have Selected {l} level.")
    while(1):
        n=int(input("Enter Your Guess Number: "))
        if n<rd:
            print("Oops! Wrong Answer. Your Answer is small than the actual answer.")
        elif n>rd:
            print("Oops! Wrong Answer. Your Answer is large than the actual answer.")
        elif n==rd:
            print("Hurrah! You Won The Game")
            break
    print()

    choice=input("Do You Want To Play it Again : ")
    if choice=="no":
        print(f"Thank You {name}! Have A Nice Day.")
        break


