def reverse01(s):
    split1 = s.split(" ")
    nw=[i[::-1] for i in split1]
    ns=" ".join(nw)
    return ns
print(reverse01("how are you"))




