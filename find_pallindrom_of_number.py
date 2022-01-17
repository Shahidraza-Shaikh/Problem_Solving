
# iterative sollution

# rev = 0
# n = 1525
# o = n
# while n :
#     remainder = n % 10;
#     rev = rev * 10 + remainder;
#     print(rev)
#     n //= 10;
# # print(o,rev)


# Recursive sollution
def find_pallindrom(num,rev):

    if num ==0:
        return rev
    rem = num%10
    rev = rev *10 +rem
    # print(num)
    return find_pallindrom(num//10,rev)
    

print(find_pallindrom(12345,0))