import random
print("******Welcome To Dice Game******")
name=input("Enter Your Good Name: ")
print(f"WELCOME! {name}")
r=[]
while(True):
    
    while(True):
        
        c1=random.choice([1,2,3,4,5,6])
        c2=random.choice([1,2,3,4,5,6])
        print(f"You Rolled {c1,c2}")
        r.append([c1,c2])
        
        break
    choice=input("Do You Want To Play It Again: ")
    if choice=="no":

        print("Your Result : ",r)
        print(f"Thanks {name} for Playing !")
        break