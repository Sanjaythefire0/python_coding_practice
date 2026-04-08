
def trans(amount,tot):
    for i in range(len(amount)):
        if amount[i]%100==0 and tot>=amount[i]:
            tot=tot-amount[i]
            print("Sucess")
        else:
            print("Failed")


if __name__=="__main__":         
    tot=int(input("Enter the total amount: "))
    n=int(input("Enter the number of transactions: "))
    amount=[]
    for i in range(n):
        a=int(input("Enter the amount: "))
        amount.append(a)

    trans(amount,tot)

    