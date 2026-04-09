def decitobin(n):
    res = ""
    while n>0:
        res+=str(n%2)
        n>>=1
    return res

if __name__=="__main__":
    n=int(input("Enter a decimal number: "))
    print("The binary representation is:",decitobin(n))