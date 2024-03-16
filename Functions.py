def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * discount_percent / 100
        final_price = price - discount_amount
    else:
        final_price = price
    return final_price
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))
final_price = calculate_discount(original_price, discount_percent)

# Print the final price
print(f"The final price is: ${final_price:}")