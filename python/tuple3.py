a=(12,34,53,23,89,90)
b=(23,67,90,77,80,56)
print(a)
print(type(a))
print(len(a))
print(' convert tuple into  dictionary')
z=dict(zip(a,b))
print(z)
print('type',type(z))
print('lengh',len(z))
z.update({56:78})
print(z)
print(z.keys())
print(z.values())
print(z.items())
z.pop(89)
print(z)
z.popitem()
print(z)
print("convert tuple into set ")
s=set(a)
print(s)
print("type   ",type(s))
print('length   ',len(s))
s.add(40)
print( 'add one element in set  ',s)
s.update([13,45])
print(' add multiple element in set  ',s)
s.pop()
print("randamely delect ",s)
s.remove(23)
print('to remove an element  ',s)

c=(12,67,10,23,89,60,11,55)
d=(12,89,11)
e=set(c)
print(e)
f=set(d)
print(f)
print('subset    ')
print(f.issubset(e))
print("superset")
print(f.issuperset(e))
print('disjoint')
print(f.isdisjoint(e))


print("set  operators")
print("union  ",e|f)
print("union   ",e.union(f))
print("intersection   ",e&f)
print("intersection    ",e.intersection(f))
print("difference       ",e-f)
print("difference       ",e.difference(f))
print("symmertic difference   ",e^f)
print("symmertic difference   ",e.symmetric_difference(f))
