def discount(amount):
    if amount>=1000 and amount<3000:
        return amount-amount*0.05
    elif amount>=3000 and amount<5000:
        return amount-amount*0.10
    elif amount>=5000:
        return amount-amount*0.20
    else:
        return amount
    
if __name__=="__main__":
    amount=float(input("Enter the total amount: "))
    discounted_amount=discount(amount)
    print("The discounted amount is:",discounted_amount)