def valid(n):
    prev=n%10
    n/=10
    while n>0:
        curr=n%10
        if curr<prev:
            prev=curr
        else:
            return False
        n/=10
    return True

if __name__=="__main__":
    n=int(input("Enter a number: "))
    if valid(n):
        print("Yes")
    else:
        print("No")
        