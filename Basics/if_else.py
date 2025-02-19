number=7
if number > 10:
    print("The number is greater than 10.")
elif number > 5:
    print("The number is greater than 5.")
    if number>8:
        print("The number is greater than 8.")
    else:
         print("The number is smaller than 8.")
else:
    print("The number is 5 or smaller.")


# Discount system
# premium=20% disc
# not premium
    #purchase>100, 10% disc
    #no discount

is_premium_member=False
purchase_amount=80

if is_premium_member:
    discount=0.2
else:
    if purchase_amount>100:
        discount=0.1
    else:
        discount=0.0

final_price=purchase_amount*(1-discount)
print(f'final_price is {final_price}')