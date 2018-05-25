def printArr(arr,m,n):
    for ctr in range(1,n+1):
        i,j= 0,ctr-1
        while i<m and j>=0:
            print(i,j,arr[i][j])
            i+=1
            j-=1
    for remaining in range(1,m):
        i=remaining
        j=ctr-1
        while i<m and j>=0:
            print(i,j,arr[i][j])
            i+=1
            j-=1
    return ""

if __name__=="__main__":
    arr=[[1,2,3,4,13],[5,6,7,8,14],[9,10,11,12,15],[16,17,18,19,20]]
    printArr(arr,len(arr),len(arr[0]))
