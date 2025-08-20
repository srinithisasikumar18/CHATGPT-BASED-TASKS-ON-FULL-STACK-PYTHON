total_bill=int(input("enter the number"))
discount_percentage=10
if total_bill<1000:
    print("Sorry no discount")
else:
    bill_amount=(total_bill*discount_percentage)/100
    total_amoun=total_bill-bill_amount
    print(total_amoun)