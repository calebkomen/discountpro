def calculate_discount(price, discount_percent):
    """
    Calculate the discounted price.

    :param price: Original price of the item.
    :param discount_percent: Discount percentage to be applied.
    :return: Price after discount.
    """
    if not (0 <= discount_percent <= 100):
        raise ValueError("Discount percent must be between 0 and 100.")
    
    if discount_percent < 20:
        return price
    
    discount_amount = (discount_percent / 100) * price
    discounted_price = price - discount_amount
    return discounted_price
# Example usage
original_price = 100.0
discount = 15.0
new_price = calculate_discount(original_price, discount)
print(f"Original Price: ${original_price}, Discount: {discount}%, New Price: ${new_price}") 
# Output: Original Price: $100.0, Discount: 15.0%, New Price: $85.0
# This function calculates the discounted price of an item given its original price and a discount percentage.
# It raises a ValueError if the discount percentage is not between 0 and 100.
# The function is useful for e-commerce applications, sales calculations, and financial software.

# Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. Print the final price after applying the discount, or if no discount was applied, print the original price.
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage (0-100): "))
    
    final_price = calculate_discount(original_price, discount_percent)
    
    if discount_percent > 20:
        print(f"The final price after a {discount_percent}% discount is: ${final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: ${original_price:.2f}")
except ValueError as e:
    print(f"Error: {e}")
# This function calculates the discounted price of an item given its original price and a discount percentage.
# It raises a ValueError if the discount percentage is not between 0 and 100.# The function is useful for e-commerce applications, sales calculations, and financial software.
# Example usage
# Original Price: $100.0, Discount: 15.0%, New Price: $85.0