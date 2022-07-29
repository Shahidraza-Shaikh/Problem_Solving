def  countSetBits(n):
    count = 0
    while (n):
        count += n & 1
        n >>= 1
    return count


i = 14
print(countSetBits(i))


bin_rep = bin(i)[2:]

res = []

for i in range(len(bin_rep)):

    if bin_rep[i] == '1':
        
        # print(bin_rep[i])

        res.append(i+1)

print(res)