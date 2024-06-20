set1={23,4,5,67,89,90,2}
set2={26,80,2,67,10,34}
print("union of two sets")
u=set1|set2
print(u)
u1=set1.union(set2)
print(u1)
u2=set2.union(set1)
print(u2)
print("intersection of two set")
i=set1&set2
print(i)
i2=set1.intersection(set2)
print(i2)
print("diffence between two set")
d=set1-set2
print(d)
d1=set1.difference(set2)
print(d1)
d2=set2.difference(set2)
print(d2)

sd1=set1^set2
print(sd1)
sd2=set1.symmetric_difference(set2)
print(sd2)


