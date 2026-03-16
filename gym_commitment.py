print("Hi! Welcome")
low_commitment= 0
medium_commitment = 0
high_commitment= 0
for i in range(5):
    name = input("What is your name?: ")
    attendence = int(input("How many days did you attendence this week?: "))
    minutes= float(input("How many time minutes did you spend in a gym day (aprox)?: "))
    if 0 < attendence <3:
        low_commitment +=1
    elif 3 <= attendence <=4:
        medium_commitment +=1
    elif attendence >=5:
        high_commitment += 1

print(f"\nAMOUT OF PEOPLE PER CLASSIFICATION: \nLow commitment: {low_commitment}\nMedium commitment: {medium_commitment}\nHigh commitment: {high_commitment}")
