def mirror_number(num):
    a=0
    
    while num>0:
        rem=num%10
        a=a*10+rem
        num=num//10
    return a

if __name__=="__main__":
    num=int(input("Enter a number: "))
    print("rev number is ",mirror_number(num))