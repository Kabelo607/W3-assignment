#Week 3 
#Question 1



def calculate_discount(price):
    return f"Discounted price is,{price}"


price = float(input("Enter original price :"))

discount = float(input("Enter deiscount percentage :"))

print(calculate_discount(price -(price*(discount/100))))