#Dance_academy
print("|||--Hi! Here you can watch how your attendence was in this month--|||")
try:
    attendence= int(input("\nHow many attencences did you have this last month: "))
    if attendence < 5:
        print("You had a low attendence this last month")
    elif 5 <= attendence <= 8:
        print("You had a medium attendence this last month")
    elif attendence >=9:
        print("You had a high attendence this last month")
    else:
        print("This option is invalid")
except ValueError:
    print("This option is invalid")



