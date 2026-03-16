
print("\n\t|||---HI! Welcome!---||| ")
shoes =0
ball= 0
"""
shoes= float(input("Type the cleats prices: "))
ball= float(input("Type the ball price: "))
bicycle= float(input("Type the bicycle price: "))
thermos= float(input("Type the thermos price: "))
"""
product_list=[]
for p in range(2):
    product_name= input("Type the name of the product: ")
    product_price= float(input("Type the product price:"))
    def dic():
        p_n = product_name
        p_p= product_price
        return  {
            "name" : p_n,
            "price" : p_p
            }
    product_list.append(dic())

for each_price in product_list:
    prices = each_price["price"]
    if prices >=100000:
        expensive=[prices]
        print(expensive)
        counter= len(expensive)
        print (counter)
    elif prices < 100000:
        print ("There are not prices more than 100000")