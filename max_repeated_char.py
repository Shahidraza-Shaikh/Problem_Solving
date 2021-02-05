def Charmap(string):
    dic ={}
    for str in string:
        if ord(str) >32:
            if str in dic:
                dic[str] +=1
            
            else:
                dic[str] = 1
    max =0
    k=""
    for ky in dic:
        if dic[ky] > max:
            max=dic[ky]
            k=ky
              
    return "{} is max and repeated {} times".format(k,max)

print(Charmap("shahidddddd shaikh"))