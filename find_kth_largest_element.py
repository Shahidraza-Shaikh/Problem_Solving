'''
Methode 1
def findElement(li,k):
  li.sort()
  return li[-k]
li=list(map(int,input('Enter elements : ').split(" ")))
k=int(input('Enter k : '))
print(findElement(li,k))
'''
#Method 2
def findElement(li,k):
  l=[]
  for i in range(k-1):
    li.remove(max(li))
  return max(li)
li=list(map(int,input('Enter element : ').split(' ')))
k=int(input('Enter vakue of K : '))
print(findElement(li,k))
