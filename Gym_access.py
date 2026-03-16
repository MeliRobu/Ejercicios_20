print("\n\t***HI! Welcome to the GYM***\nHere you can verify age category and if you can enter to the gym")

name= input("\nWhat is your name?: ").capitalize()
age = int(input(f"Please {name} type your age: "))
if age < 13:
    print(f"We are sorry {name}, you cannot ingress to the gym yet")
elif 13 <= age <= 17:
    print(f"{name}, you are in the young group")
elif 18 <= age <=59:
    print(f"{name}, you are in the general group")    
elif age >= 60:
    print(f"{name}, you are in the senior group")

print("\n\t***We are glad to assit you, have a nice day!***")
