
def valid_string(string):
    valid=[]

    if string.startswith(('}',']',')')):
        return False
    for i in range(len(string)):
        if string[i] =='(' or string[i] =='[' or string[i] =='{':
            valid.append(string[i])
        else:
            val = valid[-1]
            if val + string[i] == "[]" :
                valid.pop()
            elif val + string[i] =='()' :
                valid.pop()
            elif val + string[i] == "{}":
                valid.pop()
            
    return valid == []
            
print(valid_string("{[}]}[]{}{{}[](){[}]"))

# {[}]  }[]{}   {{}[]()   {[}]  - invalid
# {[[()()()()][()]]}  (({}))   ({})  -valid
