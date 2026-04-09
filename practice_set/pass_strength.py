def pass_strength(password):
    if any(char.isdigit() for char in password) and any(char.isupper() for char in password) and len(password)>=8:
        return "Strong"
    else:
        return "Weak"
    
if __name__=="__main__":
    password=input("Enter password: ")
    print(pass_strength(password))
