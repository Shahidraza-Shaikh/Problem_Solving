
# Print all subsets of given string 
def superset(string):
    subsets = []

    for i in range(len(string)):
        for j in range(i,len(string)+1):
            temp = string[i:j]
            if temp not in subsets and temp !='':
                subsets.append(string[i:j])
            else:
                print(temp)

    return subsets,len(subsets)

print(superset('ABC'))



'''
Output : -

A
AB
ABC
B
BC
C

'''