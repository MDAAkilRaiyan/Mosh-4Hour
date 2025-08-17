# If Else Statement Test

# Without the numerical
has_good_credit = True

if has_good_credit:
    print("Down Payment is 10%")
else:
    print("Down Payment is 20%")

# With Numerical

price = 1000000

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price

print(f"Down payment: ${down_payment}")
