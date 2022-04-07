import math
from collections import defaultdict
def cal_dist(vac_cord,person_cord):

	ans = 0
	minn = float("inf")
	x2,y2 = person_cord
	for center,x1,y1 in vac_cord:

		dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
		if dist < minn:
			minn = dist
			ans = center

	return ans

center = int(input())

centers = defaultdict(list)

vac_cord = []

for i in range(center):
	lat,lon = map(float,input().split())
	vac_cord.append((i,lat,lon))

num_person = int(input())

persons = []

for i in range(num_person):
	name,age,cat,lat,lon = map(str,input().split())

	persons.append((name,int(age),cat,float(lat),float(lon)))


for person in persons :
	dist = cal_dist(vac_cord,(person[3],person[4]))
	print(dist)

	centers[dist].append((person[0],person[1],person[2]))

result = dict(centers.items())

# di = sorted(centers.items(),key = lambda x : (x[1],[0]) )

# print(di)
ans = []

for key,value in result.items():

	for i in range(len(result[key])):
		ans.append((key,result[key][i]))


# res =[]
# names = []
# ages =[]
# cats = []

# for i in range(len(ans)) :
# 	name,age,cat = ans[i][1]
# 	names.append(name)
# 	ages.append(age)
# 	cats.append(cat)
# sort_age=sorted(ages)
# sort_name = sorted(ages)
# sort_cat = sorted(cats)
# # cats.sort()

# maxx = max(ages)

# for i in range(len(ages)-1):
# 	if sort_age[i] > sort_age[i+1]:
# 		res.append()

print(ans)

# for i in range(len(ans)-1):
# 	if ans[i][0] == ans[i+1][0] and ans[i][1][1] >

# for 
# for key in centers :

# 	for val in centers[key]



# i/p

# 2
# 0 0
# 0 10
# 5
# atul 24 A 0 1
# sunil 24 B 0 5
# rajni 23 A 0 1
# salman 21 B 0 12
# kunal 24 A 0 2

# 3
# 0 1
# 0 5
# 0 10
# 3
# atul 24 A 0 2
# niraj 22 A 0 3
# shivam 21 B 0 2