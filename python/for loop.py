#for loop
for i in range(1,11):
    print(i,end=' ')
print("   use list ",end=' ')
x=[10,20,30,40,50,60]
for i in x:
    print(i,end=' ')
print("    0 to 10  ",end=' ')
for i in range(0,11):
    print(i,end=' ') 
print("   1 to 5  ")
for i in range(1,6):
    print(i,end=' ')
print("   -10 to -1   ",end=' ')
for i in range(-10,0):
    print(i,end=' ')
print("   -10 to -5   ",end=' ')
for i in range(-10,-4):
    print(i,end=' ')
print("   name   ",end=' ')
x="MARIESHWARI"
for k in x:
    print(k,end=' ')
a=int(input("enter a starting value "))
b=int(input("enter a ending value"))
c=int(input(" enter stepper value"))
x=[11,15,6,10,12]
y=0
for i in x:
    y+=i
print(y)

#multiplication
y=1
for i in x:
    y*=i

print(y)

#even number
for i in range(a,b+1,c):
    print(i,end='  ')
x=[13,30,26,25,11,68]
for i in x:
    if(i%2==0):
        print(i)
y=0
z=0
a=0
b=0 
x="PyTHoN laNguAGE 123"
for i in x:
    if (i.isupper()):
        y+=i.count(i)
        print(i,end=' ')
for i in x:
    if(i.islower()):
        z+=i.count(i)
        print(i,end=' ')
for i in x:      
    if(i.isdigit()):
         b+=i.count(i)
         print(,i,end=' ')
    
        
print(y)
print(z)
print(a)
print(b)  



a=int(input("enter number to find a factorial value  :"))

fact=1
for i in range(1,a+1):
    fact=fact*i
    
print("factorial  :",fact)
b=int(input("enter to find fibbinocci series end term"))
n1=0
n2=1

for i in range(2,b+1):
      n3=n1+n2
      n2=n3
      n1=n2
      print(n3)

    

    
        

    









    


