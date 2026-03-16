#Hairdressing
print("\n\t|||---HI! Welcome to the hairdressing salon---|||\n\n*Our working hours are between 6 to 22* ")
def arrival ():
    try:
        arrival_time = int(input("\nWhat is going to be your arrival time?: "))
        if 6 <= arrival_time <=11:
            print("\nThis is our morning schedule, you are assigned to it! ") 
            return arrival_time
        elif 12 <= arrival_time <= 17:
            print("\nThis is our afternoon schedule, you are assignet to it!")
            return arrival_time
        elif 18 <= arrival_time <=22:
            print("\nThis is our evening schedule, you are assignet to it!")
            return arrival_time
        else:
            print("\nThis is not between or working hours, please try again")
            return arrival()
    except ValueError:
        print("\nThis is an invalid option, please try again")
        return arrival()
arrival()
print("\tWe will be waiting for you! See you! ")


