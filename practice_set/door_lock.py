def lock(code):
    cnt=0
    while True:
        attempt=input("Enter the code: ")
        if attempt==code:
            print("Door unlocked")
            break
        else:
            print("Wrong code")
            cnt+=1
            if cnt==3:
                print("Locked")
                break
    
if __name__=="__main__":
    code=input("Set the code: ")
    lock(code)
        