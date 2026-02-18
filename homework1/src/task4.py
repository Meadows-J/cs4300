def calculate_discount(basePrice, discountPercent):
    price = basePrice * discountPercent
    return price

#main

#two ints
basePrice = 100
discountPercent = 10
print("The base price is ", basePrice, "and the discount is ", discountPercent)
print("The new total is ", calculate_discount(basePrice, discountPercent))

#one int one float
basePrice = 100
discountPercent = .10
print("The base price is ", basePrice, "and the discount is ", discountPercent)
print("The new total is ", calculate_discount(basePrice, discountPercent))

#two float
basePrice = 100.1
discountPercent = .10
print("The base price is ", basePrice, "and the discount is ", discountPercent)
print("The new total is ", calculate_discount(basePrice, discountPercent))
