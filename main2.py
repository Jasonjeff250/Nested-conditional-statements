units=float(input("Enter number of units consumed: "))
if units <= 50:
    rate=2.60
    tax=25
else:
    if units <100:
        rate=3.25
        tax=35
    else:
        if units <200:
            rate = 5.26
            tax=45
        else:
            rate=8.45
            tax=75
total_bill=units*rate
taxable_bill=total_bill+tax
print("\n------------Electricity Bill---------")
print("Units Consumed: ",units)
print("Rate Per Unit: ",rate)
print(f"Bill Amount:{total_bill:.2f}")
print(f"Tax: {tax}")
print(f"Total bill Payable: {taxable_bill:.2f}")
print("------------------End of Receipt-------------------")