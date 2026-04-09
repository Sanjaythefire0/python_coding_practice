def armstrong_number(num):
    x=0
    a=num
    
    while a>0:
        rem=a%10
        
        a=a//10
        x+=rem**3
        
    
    return x==num


if __name__=="__main__":
    num=int(input("Enter a number: "))
    if armstrong_number(num):
        print("Yes")
    else:
        print("No")
    