def countf(s):
    count={}
    for i in s:
        count[i]=count.get(i,0)+1
    return count
print(countf(input("enter the value:")))