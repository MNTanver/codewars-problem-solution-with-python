# You can print your name on a billboard ad. Find out how much it will cost you. Each character has a default price of £30, but that can be different if you are given 2 parameters instead of 1 (allways 2 for Java).

# You can not use multiplier "*" operator.

# If your name would be Jeong-Ho Aristotelis, ad would cost £600. 20 leters * 30 = 600 (Space counts as a character).

# def billboard(name, price=30):
#     result = len(name) * price
#     return result

def calculate_billboard_cost(name, char_price=30):
    cost = 0
    for char in name:
        cost += char_price
    return cost

name = "Jeong-Ho Aristotelis"
billboard_cost = calculate_billboard_cost(name)
print(f"The cost of printing '{name}' on a billboard ad is £{billboard_cost}")


