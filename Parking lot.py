#Parking lot
print("\t|||--HI! Here you can watch how much you have to pay in parking lot--|||")
first_hour= 5000
aditional_hour= 3000
ask=int(input("\nDid your vehicle spent ... \n1.Minutes \n2.Hours and minutes:\nSelect 1 or 2: "))
if ask ==1:
    minutes= int(input("How many minutes your vehicle spent on parking lot: "))
    if minutes<=60:
        convert_min= minutes/60
        minutes_pay= first_hour*convert_min
        print(f"\nYou may pay: {minutes_pay}")
    else:
        print("This option is only available for less than 1 hour")

elif ask ==2:
    hour= int(input("How many hours your vehicle spent in parking lot: "))
    minutes= int(input("How many aditional minutes your vehicle spent on parking lot: "))
    convert_min= minutes/60
    aditional_min_pay= aditional_hour*convert_min
    aditional_hour_pay= ((hour-1)+convert_min)*aditional_hour
    if hour ==1 :
        print(f"\nYou may pay: {first_hour+aditional_min_pay}")
    elif hour >1:
        print(f"\nYou may pay: {first_hour+ aditional_hour_pay}")

else:
    print("\nThe option is invalid")




