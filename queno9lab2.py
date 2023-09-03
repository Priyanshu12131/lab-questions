installment=float(input("enter amount you want to deposit: "))
month=int(input("for how many months you deposited the installments: "))
interest=float(installment*7.1*month)/(12*100)
if installment<500 or month<6:
    print("not eligible")
else:
    print(f"interest for {month} months is {interest}")
    