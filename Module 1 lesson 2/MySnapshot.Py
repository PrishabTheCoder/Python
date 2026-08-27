#part 1 - Types of Data
snack_name = "Chips" # str -Text
price = 1.50         # 
quantity = 10
is_avaliable = True

print("Snack", snack_name)
print("price:$", price)
print("In Stock", quantity)
print ("Avaliable?", is_avaliable)

print(type(snack_name))
print(type(price))
print(type(quantity))
print(type(is_avaliable))

#part 2 - arithmetic operators
total = price *quantity
print ("total value: $", total)
print("sale price:$", price - 0.25)
print("double stock:",quantity * 2)

#Part 3comparison operations
print ("is price under $2", price < 2)
print("more than 5 in stock?", quantity > 5)
print("is price exactly $1.50?", price == 1.50)


#part 4 String operations
shop_name = "quick" "+" "bites"
print ("shop name:", shop_name)
print("letters in snack name:", len(snack_name))
print("first letter:", snack_name[0])

#part 5  swapping values
price_a = 1.50
price_b = 3.00
print ("before:", price_a, "and", price_b)
temp = price_a
price_a = price_b
price_b = temp
print("after:", price_a, "and", price_b)