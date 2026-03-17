
print("\n\t|||---HI! Welcome! to the sport storage---||| ")
product_list=[]
expensive_product= []
for p in range(6):
    product_name= input("\nType the name of the sport product: ")
    product_price= float(input("Type the product price:"))
    dic= { 
            "Product name" : product_name,
            "Product price" : product_price
            }
    product_list.append(dic)

for each_one in product_list:
    prices = each_one["Product price"]
    names = each_one["Product name"]
    if prices >=100000:
        print(f"\nThe product greater than 100000 are: \n=>{names.capitalize()}:{prices}")
        expensive_product.append(prices)
count= len(expensive_product)
print(f"\n=>There is/are {count} expensive product(s)")
