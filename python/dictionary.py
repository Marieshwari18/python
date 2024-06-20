x={'name':"maris",'age':'21','degree':"Bsc",}
'''print(x)
print("type of x   ",type(x))
print("length of x  ",len(x))
print(x.items())
x.update({'married status':'married','gender':'female'})
print(x)
print("key   ",x.keys())
print('values   ',x.values())
print("items  ",x.items())

print(x.get('name'))
x.popitem()
print('remove last element  ',x)
x.pop('age')
print('remove age in x  ',x)
x.clear()
print(x)
del x
print(x)'''
w=x.copy()
print(w)
x.update({'gender':'female','married status':'married'})
print(" after update  ",x)
print(w)
a=[23,45,54,24]
b=dict.fromkeys(a)
print("coverting list into dictionary  ",b)
y=['one','two','three','four']
z=dict(zip(a,y))
print("combing two list into dictionary    ",z)
