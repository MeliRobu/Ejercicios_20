#ICE CREAM PARLOR
print("Hi!Welcome\n\nThis are our product: \n1. Ice cream cone\n2. Ice cream cup \n3. Banana split \n4. Exit and watch the invoid")
product = {
    "cone" : 3000,
    "cup":4000, 
    "banana split" : 9000
}
cone_counter= 0
cup_counter= 0
banana_counter= 0
client_counter= 0
total_sold=0
choice= int(input("\nWhat product do you want (type the number): "))
while choice!= 4:
    try: 
        amount= int(input("Type the product amount that you want: "))
        if choice == 1:
            total= amount*product.get("cone")
            print(f"\nYour product is: Cone\nAmount: {amount}\nTotal: {total}")
            cone_counter +=1
            client_counter +=1
        elif choice == 2:
            total= amount*product.get("cup")
            print(f"\nYour product is: Cup\nAmount: {amount}\nTotal: {total}")
            cup_counter +=1
            client_counter +=1
        elif choice == 3:
            total= amount*product.get("banana split")
            print(f"\nYour product is: Banana split\nAmount: {amount}\nTotal: {total}")  
            banana_counter +=1  
            client_counter +=1
        else:
            print("This option is invalid, try again")
    except ValueError:
        print("This is an invalid choice  please try again")
    total_sold += total
    choice= int(input("\nWhat product do you want (type the number): "))

if cup_counter< cone_counter > banana_counter: 
    print(f"\n\t***Final Invoid***: \nTotal sold: {total_sold} \nTotal of clients: {client_counter}\nBest seller product: Cone with {cone_counter} sells over cup ({cup_counter}) and banana split ({banana_counter}))")
elif cone_counter< cup_counter > banana_counter: 
    print(f"\nFinal Invoid: \nTotal sold: {total_sold} \nTotal of clients: {client_counter}\nBest seller product: Cup with {cup_counter} sells over cone ({cone_counter}) and banana split ({banana_counter}))")
elif cup_counter< banana_counter > cone_counter: 
    print(f"\nFinal Invoid: \nTotal sold: {total_sold} \nTotal of clients: {client_counter}\nBest seller product: Banan split with {banana_counter} sells over cup ({cup_counter}) and cone ({cone_counter}))")

print("\nThat is it!")
