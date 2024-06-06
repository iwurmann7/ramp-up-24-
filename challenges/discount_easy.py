def dis(price, discount):
    discount_percentage = float(discount)
    discounted_price = price * (1 - discount_percentage / 100)
    return round(discounted_price, 2)