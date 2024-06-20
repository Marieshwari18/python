s='APple orange'
print(s)
print('type of a',type(s))
print('lenght',len(s))
#words starts with  capital another is small 
print('s.title',s.title())


#string starts with capital another small
print('s.capitalize   ',s.capitalize())

       
#upper case
print('s.upper()  ',s.upper())


#lower case
print('s.lower()   ',s.lower())

#upper to lower ,lower to upper using swapcase
print("swapcase()    ",s.swapcase())

#find any letter  index in string
print("s.find(l)   ",s.find('l'))
print("s.find(l,3)   ",s.find('l',3))

print("'a' in s", 'a' in s)
print("'g' not in s",'g' not in s)


print('s.casefold()  ',s.casefold())

print("s.isalpha()     ",s.isalpha())   #to check characters only

print('s.isalnum()     ',s.isalnum())    #to check numbers only

print('s.strip()    ',s.strip())

print("s.lstrip()    ",s.lstrip())

print('s.rstrip()   ',s.rstrip())

#to check numeric

print('s.isnumeric()   ',s.isnumeric())
print('s.isdigit()     ',s.isdigit())

#To spilt string
print('s.split()    ',s.split())

# to check upper and lower
print('s.isupper()    ',s.isupper())

print("s.islower()     ",s.islower())

#starts with

print('s.startswith()    ',s.startswith('mac'))
print('s.endswith()     ',s.endswith('ge'))
print('s.stratswith()    ',s.startswith('learing',3))

print("replace   ",s.replace('p','d'))

print("count   ",s.count('a',0,4))
#string format
print('string format')
a='laptap'
b='35k'
c='mobile'
print(f'price of{a} is {b}')
print(f'price of',a,'is',b)
print('price of {1}is {0}'.format(a,b))
print('price of{}is{}'.format(b,c))




















                                    
