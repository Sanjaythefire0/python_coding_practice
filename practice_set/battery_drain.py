def battery(rate):
    n=100
    cnt=0
    while n>0:
         cnt+=1
         n-=rate
    return cnt

if __name__=="__main__":
    rate=int(input("Enter the rate of battery drain per minute: "))
    print("The battery will last for",battery(rate),"minutes")