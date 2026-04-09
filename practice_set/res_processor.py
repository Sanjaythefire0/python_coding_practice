def examres(marklist):
    if all(mark < 35 for mark in marklist):
        return "Fail"
    elif sum(marklist) / len(marklist) >= 75:
        return "Distinction"
    else:
        return "Pass"

if __name__=="__main__":
    marks = list(map(int, input("Enter the marks of 5 subjects separated by space: ").split()))
    print(examres(marks))