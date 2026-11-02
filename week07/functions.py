# AI USE: Explainer: on exercise 5.
# Self Reflection Questions:
# 1.) The first bug I spooted in Exercise 5 was the lack of a colon at the end of the line "for sale in sales" I found it from reading the code out loud to analyze the logic, and the lack of a colon was also emphaszied by the red underline, making it quite obvious to find. It shows me that my debugging instincts probably still need some work, but that I am also understanding the logic in play behind the code.
# 2.) apply_discounts(price, tier) calculates the discounted price that a person recieves based on their current tier within the company. The function will return the final price after the discount has been applied.The inputs are price which is the original price of the good, and tier which is what indicates what discount level to apply. A colleague likley could use it without reading the body.
# 3.) The only AI that I used in todays lab was for exercise 5, where it required us to have AI explain error messages without providing a direct fix. The AI helped build my understanding of what error messages mean and could apply to, allowing me to debug my code efficiently and effectivley.

# Exercise 1:

# Define calculate tax function

def calculate_tax(price, rate):
    return price * rate

# Calling the function

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax on $100 at 7%: ${tax1:.2f}") # 7.00
print(f"Tax on $250 at 8%: {tax2:.2f}") # 20.00

# Exercies 2:

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

# calling the function

price = 200
tiers = ["gold", "silver", "bronze", "none"]

for tier in tiers:
    print(f"{tier}: ${apply_discount(price, tier):.2f}")

# Exercise 3:

# Write it out manually first, then refractor into a function

discounted = apply_discount(200, "gold")
tax = calculate_tax(discounted, 0.07)
after_tax = discounted + tax
print(f"After gold discount: ${discounted:.2f}")
print(f"After tax: ${after_tax:.2f}")

# Refractor into function

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax

print(f"Final price: ${final_price(200, 'gold', 0.07):.2f}")

# Exercise 4:

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none)")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price:.2f}, Tier: {tier}, Final: ${total:.2f}")

# Exercise 5:

# broken_sales.py - trace and diagnose before fixing anything.

# for sale in sales is missing a colon, add a colon to remove the syntax error.
# Total was wrong and stuck at $90, to fix, I went to line 6 and changed it from just an = sign, to a += sign.
# Index error, remove the <= and just make it < to correct.

# Exercise 6:

x = 100 

def double_it():
    global x
    # x = 999
    return x * 2

print(x)
print(double_it())
print(x)
