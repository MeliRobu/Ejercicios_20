print("\n\t***HI! Welcome to the coffeeshop***\n\nOur current drinks are:\n1. Coffe\n2. Te\n3. Juice")

product = {'coffee': 4000,
            'te': 3500,
            'juice': 5000
}

def c ():
    try: 
        choice = int(input("\nWhich do you want? (type 1, 2 or 3): "))
        choice_2= int(input("How many units do you want?: "))

        if choice ==1:
            print(f"\nCoffee: {product.get("coffee")} \nThe total price is: {product.get("coffee")*choice_2}")

        elif choice ==2:
            print(f"\nTe: {product.get("te")} \nThe total price is: {product.get("coffee")*choice_2}")

        elif choice ==3:
            print(f"\nJuice: {product.get("juice")} \nThe total price is: {product.get("coffee")*choice_2}")

        else:
            print("\nThis choice is not available, plese try again")
            return c()
    except ValueError:
        print("\nThis choice is not available, plese try again")
        return c()

c ()

another_product= int(input("\nDo you want another product? 1. yes o 2. no): "))

while another_product== 1:
    print("\n1. Coffe\n2. Te\n3. Juice")
    c()
    another_product= int(input("\nDo you want another product? 1. yes o 2. no): "))

print("\nThanks for your purchase! ")


