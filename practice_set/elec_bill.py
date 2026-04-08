def elec_bill(tot_units):
    if tot_units<=100:
        return tot_units*3
    elif tot_units<=200:
        return 100*3+(tot_units-100)*5
    elif tot_units>200 and tot_units<=300:
        return 100*3+100*5+(tot_units-200)*8
    else:
        bill=100*3+100*5+(tot_units-200)*8
        return bill+bill*0.1

if __name__=="__main__":
    tot_units=int(input("Enter the total units consumed: "))
    bill_amount=elec_bill(tot_units)
    print("The electricity bill amount is:",bill_amount)
    