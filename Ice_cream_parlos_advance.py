#ICE CREAM PARLOR
print("Hi!Welcome\n\nThis are our product: \n1. Cone\n2. Cup \n3. Banana split")
product = {
    "cone" : 3000,
    "cup":4000, 
    "banana split" : 9000
}
client_list = []
def clients():
    product= input("\nWhat product do you want (type the number): ")
    amount= int(input("Type the product amount: "))
    if product == 1:
        print(f"\nYour product is: Cone\nAmount: {amount}\nTotal: {amount*product.get("cone")}")
    return product

client_list.append(clients())
clients()
print(client_list)
