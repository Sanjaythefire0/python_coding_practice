def seat(thresh):
    while True:
        n=int(input("Enter the number of people: "))
        if thresh-n>=0:
            print("Seat allocated")
            thresh-=n
        else:
            print("waitlisted")
            break
        
if __name__=="__main__":
    thresh=int(input("Enter the threshold: "))
    seat(thresh)