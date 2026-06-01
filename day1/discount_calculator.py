amount = 50

if amount > 10000:
    discount_percent = 25
elif amount > 5000:
    discount_percent = 20
elif amount > 1000:
    discount_percent = 15
elif amount > 500:
    discount_percent = 10
elif amount > 100:
    discount_percent = 5
else:
    discount_percent = 0
    
discount_value = amount * discount_percent / 100
final_price = amount - discount_value

print(f"Original amount: ${amount:.2f}")
print(f"Discount: {discount_percent}%")
print(f"You save: ${discount_value:.2f}")
print(f"Final price: ${final_price:.2f}")