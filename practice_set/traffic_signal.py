def sig(T):
    if T>0 and T<=30:
        return "Red"
    elif T>30 and T<=45:
        return "Yellow"
    elif T>45 and T<=90:
        return "Green"
    else:
        
        return "Invalid"
    
if __name__=="__main__":
    T=int(input("Enter the time in seconds: "))
    print(sig(T))