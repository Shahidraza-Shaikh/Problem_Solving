
def find_set_bit(binary):
    bit =0
    for  i in range(len(binary)):
        if binary[i] == '1':
            bit = i
            break
    return len(binary) - bit - 1


def find_bits(num):

    binary = bin(num)
    print(binary)
    binary = binary[2:]
    

    set_bits= 0
    lsb = 0
    msb = find_set_bit(binary)

    for j in range(len(binary)):
        if binary[j] == '1':
            set_bits +=1

    binary = binary[::-1]
    for i in range(len(binary)):
        if binary[i] == '1':
            lsb = i
            break
    print(binary)

    print(f"{set_bits}#{lsb}#{msb}")
num = int(input())
find_bits(num)

