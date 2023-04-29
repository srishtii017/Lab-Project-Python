import random
print("Do You Want to Generate OTP")
choice=input()
if choice=="yes":
    print("********Generating OTP********")
    print()
    re=random.random()
    out=str(re)[-6:]
    print(f"Your One Time Password is {out}")
    print()
    print("******************************")
    print()
    print("Thank You and Have a Nice Day.")
    print()
else:
    print("Thank You !")
