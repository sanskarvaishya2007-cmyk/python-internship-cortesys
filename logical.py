age=int(input("Enter your age"))
if age<0 :
    print("not born yet")
elif age>=18 and age<=100:
    print("eligible to vote")
elif age<18 or age>100:
    print("not eligible to vote")
else:
    print("yo!!")


#expressions 
print("eligible" if 0 else "not eligible")
