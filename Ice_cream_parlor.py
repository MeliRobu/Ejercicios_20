#ICE CREAM PARLOR
print("\tHi welcome to the ICE CREAM PARLOR")
s= 0
c= 0
v= 0
def f():
    global s
    global c
    global v
    try:
        flavor=input("\nWhich flavor of ice cream do you want: vainilla, chocolate or strawberry?: ")
        if flavor == "strawberry":
            s+=1
            return flavor
        elif flavor == "chocolate":
            c+=1
            return flavor
        elif flavor == "vainilla":
            v +=1
            return flavor
        else:
            print("Incorrect choice, please try again")
            return f()
    except ValueError:
        print("Incorrect choise, please try again")
        return f()
    
for o in range (5):
    f()
print (f"\n***ORDER***:\nStrawbery ice cream: {s}\nChocolate ice cream: {c} \nVainila ice cream {v} ")
