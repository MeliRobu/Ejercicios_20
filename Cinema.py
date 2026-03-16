#The solicitation says that we have to ask the client the age
# Based on the age the price of cinema tickets are diferent
print("\n\t***HI!, Welcome!*** \nHere you can find how much do you have to pay for cinema ticket based on your age")

prices = { 
    "kids under 12" : 8000,
    "adults between 12 and 59" : 12000,
    "older than 60" : 9000
}
def type_age():
    try:
        age = int(input("\n=>Please, type your age: "))
        if 0 < age < 12:
            print (f"\no)You may pay: ${prices.get("kids under 12")}")
        elif 59 >= age >= 12:
            print (f"\no)You may pay: ${prices.get("adults between 12 and 59")}")
        elif age >= 60 :
            print (f"\no)You may pay: ${prices.get("older than 60")}")
        else:
            print("o)You may insert a positive number")
            return type_age()
    except ValueError:
        print("You may insert a number")
        return type_age()
type_age()
print("\n\t***Have a nice day!***")

