shop_name = "My Coffee Shop"
item1 = "Tea"
item2 = "Coffee"
item3 = "Cake"
unit_price1 = 2.5
unit_price2 = 4.5
unit_price3 = 5.5
qty1 = 3
qty2 = 2
qty3 = 1
tax_rate = 0.1
line1 = unit_price1 * qty1
line2 = unit_price2 * qty2
line3 = unit_price3 * qty3
subtotal = line1 + line2 + line3
tax = subtotal * tax_rate
total = subtotal + tax

print("="*28)
print(f"{shop_name.upper():^28}")
print("="*28)
print(f"{item1:<12} x {qty1}    ${line1:>6.2f}")
print(f"{item2:<12} x {qty2}    ${line2:>6.2f}")
print(f"{item3:<12} x {qty3}    ${line3:>6.2f}")
print("-"*28)
print(f"{'Subtotal:':<13}       ${subtotal:6.2f}")
print(f"{'Tax:':<13}       ${tax:6.2f}")
print("="*28)
print(f"{'Total:':<13}       ${total:6.2f}")
print("="*28)