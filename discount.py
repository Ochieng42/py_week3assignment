def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount if the discount is 20% or higher.
    """
    price=int(input("Enter the original price of the product please"))
    discount_percent=int(input("Enter the percentage dixcount offered!!!"))
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

print(calculate_discount(100, 10))