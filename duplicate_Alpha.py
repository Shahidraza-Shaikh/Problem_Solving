
from itertools import groupby

strr = "bcsabcehb"

a = [list(g) for i,g in groupby(strr)]

print(a)
