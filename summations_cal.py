lower_bd,upper_bd,exp,val=input('Enter lower bound upper bound expression,value').split(' ')
# print(lower_bound,upper_bound,exp,val)
value=0
val=int(val)
string=''
for num in range(int(lower_bd), int(upper_bd)+1):
    if exp == '*':
        value +=(num*val)
        string +='{}*{} + '.format(num,val)
    elif exp == '/':
        value +=(num/val)
        string +='{}/{} + '.format(num,val)
    elif exp == '%':
        value +=(num%val)
        string +='{}%{} + '.format(num,val)
print(str(value)+'('+string[:-2]+')')
