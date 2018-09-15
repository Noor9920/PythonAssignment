def Calculator():
    Principal_Amount=int(input("Enter the principal amount: "))
    Years=int(input("Enter no of years: "))
    months=Years*12
    Rate=float(input("Enter the rate of interest: "))
    global EMI
    EMI=((Principal_Amount*Rate*((1+Rate)**months))/(((1+Rate)**(months-1))))
    return EMI
Calculator()
print("EMI is: ",EMI)
