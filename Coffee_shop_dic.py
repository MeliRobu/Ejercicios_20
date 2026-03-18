"""
order = []
product = ["coffee", "te", "jugo"]
final_order = []

for number,individual_p in enumerate(product):
    print(f"{number+1} => {individual_p}")

for number in product:
    choice = int(input("What of our product do you want?: "))
    order.append(choice)

for number,individual_p in enumerate(product):
    final_order.append ({
        "Product name": individual_p,
        "Amount": order.count(number+1)
    })

print(final_order)
"""
#This is a coffeshop that has 3 products with its prices
#This is teh dictionary with the product and its values
product = {"coffee": 4000, "te": 3500, "juice": 5500}
#Aqui enumeramos al diccionario, siendo i el numero a sumar por lo que colocamos +1 porque sino empieza a contar desde 0
#key y value son idividuos o asignaciones paa recorrec products con el método .items() que me permite obtener clave, valor dentro del diccionario
# casa "item" lo asigno a "key, value"
for i,(key,value) in enumerate(product.items()):
    print(f"{i+1} - {key.capitalize()} : {value}")
choice = input("What of our product do you want (type the name)?: ").lower()
amount= int(input("Type the amount you want: "))
#asigno a la nueva variable "price", product.get(choice), y "choice" representa la key del diccinario, arrojandome el valor
price= product.get(choice, "This product does not exist")
total = price*amount
print(f"The product is: {choice}\nAmout: {amount}\nTotal: {total}" )
