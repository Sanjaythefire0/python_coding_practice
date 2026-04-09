def inflow_check(inflow,N,threshold):
    cnt=0
    for i in range(N):
        if threshold>0:
            threshold-=inflow[i]
            cnt+=1
        
    return cnt

if __name__=="__main__":
    N=int(input("Enter flow count:"))
    threshold=int(input("Enter the threshold: "))
    inflow=list(map(int,input("Enter the inflow for each day: ").split()))
    result=inflow_check(inflow,N,threshold)
    print("Number of minutes before threshold is reached:",result)

            