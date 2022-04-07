#EXP  :- 2
# Name :- Shahidraja Shaikh
# ROll :- 18CO56
# Class:- TECO
# Sub :-CSS
# Aim -- implementation of Playfair cipher

import string 
key =input('Enter a Kay : ')
key=key.upper()
li=[]
for i in key:
    if i not in li:
        li.append(i)
atoz=string.ascii_uppercase # A - Z
atoz=atoz.replace('J','')
mat=[]

for c in key:
    if c in atoz:
        atoz=atoz.replace(c,'')
li = li +list(atoz)
c=0
for i in range(0,25,5):
    mat.append(li[i:i+5]) # 0 + 5 =10 +5 =15 +5 =20
# print(mat)
text =input('Enter text : ')
text=text.replace(' ','')
text=text.replace('j','i')
text=text.upper()

i=0
pair=[]
while i < len(text)-1:
    if text[i] != text[i+1]:
        pair.append(text[i]+text[i+1])
        i +=2
    else:
        pair.append(text[i]+'X') 
        i +=1
if i+1 == len(text):
    pair.append(text[-1]+'X')

a,b,c,d=0,0,0,0
result=[]
for i in pair:
    first,second = i[0],i[1] 
    for j in range(5):
        for k in range(5):
            if mat[j][k] == first:
                a,b=j,k
            elif mat[j][k] == second:
                c,d=j,k
    if a ==c:
        b +=1
        d +=1

        if b > 4 :
            b = b %4
            b=b-1
        if d > 4 :
            d = d %4
            d=d-1
        result.append(mat[a][b] +mat[c][d])
    elif b == d:
        a +=1
        c +=1
        if a > 4:
            a = a%4
            a = a-1
        if c >4:
            c =c%4
            c = c-1
        result.append(mat[a][b]+mat[c][d])
    else:
        temp = 0
        temp=b
        b=d
        d=temp
        result.append(mat[a][b] + mat[c][d])
temp=result.copy()
print("Encrypted Text is : ",''.join(result))

pai =temp

a,b,c,d=0,0,0,0
result=[]
for i in pai:
    first,second = i[0],i[1] 
    for j in range(5):
        for k in range(5):
            if mat[j][k] == first:
                a,b=j,k
            elif mat[j][k] == second:
                c,d=j,k
    if a ==c:
        b -=1
        d -=1
        result.append(mat[a][b] +mat[c][d])
        
    elif b == d:
        a -=1
        c -=1
        result.append(mat[a][b]+mat[c][d])
        
    else:
        temp = 0
        temp=b
        b=d
        d=temp
        result.append(mat[a][b] + mat[c][d])
result=''.join(result)
result=result.replace('X','')
print("Decrypted text is : ",result)

#OUTPUT
# E:\Competative-programs\Problem_Solving>python playfaircipher.py
# Enter a Kay : monarchy
# Enter text : instruments
# Encrypted Text is :  GATLMZCLRQXA
# Decrypted text is :  INSTRUMENTS




        


