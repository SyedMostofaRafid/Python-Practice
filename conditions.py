age = float (input("What is your age ? "))
if age >= 18 and age <= 49:
    print("You are an adult")
elif age >=50 and age <= 99:
    print("You are old")
elif age < 18 and age>0:
    print("You are still young")
elif age ==0:
    print("You are dead") 
elif age <=100:
    print("You are gonna die soon")
else: 
    print("You are not born yet")