
c = 'shahid'

def findNonRepeatingChar(c):
    d={}
    uniq=''
    for i in range(len(c)):
        d[c[i]] = d.get(c[i],0) +1

        if d[c[i]] ==1:
            uniq = c[i]

    print(uniq)  
    # for k in d:
    #     if d[k] ==1 :
    #         return k
        
    return '_'

print(findNonRepeatingChar(c))



