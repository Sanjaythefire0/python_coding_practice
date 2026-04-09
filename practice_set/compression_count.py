def compcount(n):
    cnt=0
    while n!=0 and n%2==0:
        cnt+=1
        n/=2
    return cnt

if __name__=="__main__":
    n=int(input("Enter a number: "))
    print("The count of 2's in the prime factorization is:",compcount(n))