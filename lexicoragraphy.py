string = "abdc"

new_str=''

def lex(st):
    i = len(st)-2
    while not (i<0 or st[i]< st[i+1]):
        print(st[i])
        i-=1
    if i < 0:
        print("no answer")
    else:
        j=len(st)-1

        while not ( st[j] > st[i] ):
            j -=1
        st[i],st[j] = st[j],st[i]
        st[i+1:] = reversed(st[i+1:])
        print(''.join(st))

        
lex(list(string))
