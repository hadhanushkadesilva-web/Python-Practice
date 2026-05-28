item_name = input("Enter item name: ")
item_price = float(input("Enter original price: "))
discount = float(input("Enter discount percentage: "))
tax = float(input("Enter tax percentage: "))
#____________________
dicount_amount = item_price * (discount / 100)
price_after_discount = item_price - dicount_amount
tax_amount = price_after_discount * (tax / 100)
final_price = price_after_discount + tax_amount

###############

print("---- Receipt ----")
print("Item:", item_name)
print("Original Price:", item_price)
print("Discount: ", discount, "%")
print("Tax: ", tax, "%")
print("Final Price:", final_price)
print("-----------------")