def digit_sum(n):
    sum=0
    while n>0:
        rem=n%10
        sum+=rem
        n//=10
    return sum
def lock(n):
    
    cnt=0
    while n>=10:
        sum=digit_sum(n)
        n=n-sum
        cnt+=1
    return cnt

if __name__=="__main__":
    n=int(input("Enter the code: "))
    print("Number of attempts to unlock the door is ",lock(n))
    