# calculate_discount.py
def calculate_discount(price, discount_percent):
    """
    Returns the final price after applying discount_percent
    if discount_percent >= 20. Otherwise returns the original price.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price


def main():
    try:
        price = float(input("Enter the original price: "))
        discount_percent = float(input("Enter the discount percentage: "))

        final_price = calculate_discount(price, discount_percent)

        if discount_percent >= 20:
            print(f"Discount applied! 🎉 Final price: {final_price:.2f}")
        else:
            print(f"No discount applied. Original price: {final_price:.2f}")

    except ValueError:
        print("Please enter valid numbers for price and discount percentage.")


if __name__ == "__main__":
    main()
