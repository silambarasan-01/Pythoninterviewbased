def longsubstring(s):
    n=len(s)
    unique_list=[]
    res=0
    for i in range(n):
        for j in range(i,n):
            if s[j] in unique_list:
                unique_list.clear()
                break
            else:
                unique_list.append(s[j])
                if(res<j-i+1):
                    res=j-i+1
                    print(s[j])
    return res
obj=longsubstring("abcbac")
print(obj)