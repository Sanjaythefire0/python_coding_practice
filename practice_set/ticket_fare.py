def ticket_fare(age:int, distance:float):
    price = distance*2
    if age<=12:
        price*=0.3
    elif age>=65:
        price*=0.5
    return price

if __name__=="__main__":
    age=int(input("Enter the age of the passenger: "))
    distance=float(input("Enter the distance to be traveled in kilometers: "))
    fare=ticket_fare(age, distance)
    print("The ticket fare is:",fare)
    
