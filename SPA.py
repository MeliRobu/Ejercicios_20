#SPA
print("\t|||--Hi! Welcome to the SPA--|||\n\nHere you can find this services: \no)Massage\no)Facial\no)Manicure")
choice= input("\nWhich service do you want (type the name): ").lower()
if choice == "massage" or choice == "facial" or choice == "manicure":
    print("\nThis service is available, contact us to schedule an appoiment") 
else:
    print("\nThis service is not available")
print("\nHave a nice day!")