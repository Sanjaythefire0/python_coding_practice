def vowfreq(s):
    s=s.lower()
    vowels="aeiou"
    cnt=0
    for char in s:
        if char in vowels:
            cnt+=1
    return cnt

if __name__=="__main__":
    s=input("Enter a string: ")
    print("The number of vowels in the string is:",vowfreq(s))