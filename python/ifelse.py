'''# find even or odd number
num=int(input("enter a number "))
if num%2==0:
    print(' it is even number')
else:
    print("it is odd number  ")

#eligible for voting
age=int(input('enter the age  '))
if age>=18:
        print("eligiple for voting  ")
else:
    print("not eligiple for voting   ")'''

'''#grade in marks

mark=int(input("enter the marks    "))
if mark >=90:
    print(" grade  A")
elif mark>=80 and mark<=90:
    print("grade   B")
elif mark>=60 and  mark<=80:
    print("grade   C")
elif mark<=60  and mark>=35:
    print("grade   D")
else:
    print("fail  ")


#tax
amount=int(input("enter the amount    "))
if amount<100000:
           tax=amount*15/100
           print("tax   ",tax)
elif amount>=50000 and amount<=100000:
    tax=amount*10/100
    print(" tax   ",tax)
elif amount<=50000 and amount>=10000:
    tax=amount*5/100
    print(" tax   ",tax)
else:
    print("no need to pay tax")'''


a=int(input("enter a number  a "))
b=int(input("enter a number  b "))
c=int(input("enter a number  c "))
d=int(input("enter a number  d "))
e=int(input("enter a number  e "))

if(a>=b and a>=c) and (a>=d and a>=e):
    print("a is first greatest number ")
    if(b>c>d>e) :
        print(" b is sencond  greatest number ")
        if (c>=d and c>=e):
            print(" c is third gretest")
            if(d>=e):
                print("d is forth greatest number ")
                print(" e is smallest number")
            
            else:
                print("e is fourth greatest number ")
                print("d is smallest number")
            
    elif c>b>d>e:
        print("c is second gretest number  ")
        if (b>=d and b>=e):
            print(" b is third gretest")
            if(d>=e):
                print("d is forth greatest number ")
                print(" e is smallest number")

            else:
                print("e is fourth greatest number ")
                print("d is smallest number")
        
    elif d>b>c>e:
        print("d is  second greatest number  ")
        if (b>=c and b>=e):
            print(" b is third gretest")
            if(c>=e):
                print("c is forth greatest number ")
                print(" e is smallest number")
            else:
                print("e is fourth greatest number")
                print("c is smallest number")
    
    else:
        print(" e is second greatest number ")
        if (b>=d and b>=c):
            print(" b is third gretest")
            if(c>=d):
                print("c is forth greatest number ")
                print(" d is smallest number")
            else:
                print("d is greatest number ")
                print("c is smallest number")
            
        
elif(b>=a and b>=c) and (b>=d and b>=e):
    print(" b is first greatest number ")
    if a>c>d>e:
        print(" a is sencond  greatest number ")
        if (c>=d and c>=e):
            print(" c is third gretest")
            if(d>=e):
                print("d is forth greatest number ")
                print(" e is smallest number")
            else:
                print("d is smallest number ")
                print("e is forth greatest number")
    elif(c>=a and c>=d) and c>=e:
        print("c is second gretest number  ")
        if (a>=d and a>=e):
            print(" a is third gretest")
            if(d>=e):
                print("d is forth greatest number ")
                print(" e is smallest number")
            else:
                print(" d is smallest number")
                print(" e is smallest number ")
        
    elif(d>=a and d>=c) and d>=e:
        print("d is  second greatest number  ")
        if (a>=c and a>=e):
            print(" a is third gretest")
            if(c>=e):
                print("c is forth greatest number ")
            
                print(" e is smallest number")
            else:
                print("e is fourth smallest ")
                print(" d is smallest number ")
    
    else:
        print(" e is second greatest number ")
        if (a>=d and a>=c):
            print(" a is third gretest")
            if(c>=d):
                print("c is forth greatest number ")
            
                print(" d is smallest number")

            else:
                 print(" d is fourth greatest number ")
                 print("c is smallest number ")
elif(c>=b and c>=a) and (a>=d and a>=e):
    print(" c is first greatest number ")
    if(b>=a and b>=d) and b>=e:
        print(" b is sencond  greatest number ")
        if (a>=d and a>=e):
            print(" a is third gretest")
            if(d>=e):
                print("d is forth greatest number ")
            
                print(" e is smallest number")
            else:
                print(" d is smallest number ")
                print(" e is fourth smallestnumber ")
    elif(a>=b and a>=d) and a>=e:
        print("a is second gretest number  ")
        if (b>=d and b>=e):
            print(" b is third gretest")
            if(d>=e):
                print("d is forth greatest number ")
            
                print(" e is smallest number")
            else:
                print(" d is smallest number ")
                print(" e is forth smallest number")
        
    elif(d>=b  and d>=a) and d>=e:
        print("d is  second greatest number  ")
        if (b>=a and b>=e):
            print(" b is third gretest")
            if(c>=e):
                print("a is forth greatest number ")
            
                print(" e is smallest number")
            else:
                 print(" a is smallest number ")
                 print("  e is fourth greatest number ")
    
    else:
        print(" e is second greatest number ")
        if (b>=d and b>=a):
            print(" b is third gretest")
            if(a>=d):
                print("a is forth greatest number ")
            
                print(" d is smallest number")
            else:
                print("a is smallest number ")
                print(" d is fourth greatest mumber")

elif(d>=b and d>=c) and (d>=a and d>=e):
    print(" d is first greatest number ")
    if(b>=c and b>=a) and b>=e:
        print(" b is sencond  greatest number ")
        if(c>=a and c>=e):
            print(" c is third gretest")
            if(a>=e):
                print("a is forth greatest number ")
            
                print(" e is smallest number")
            else:
                 print("a is smallest number")
                 print(" e is fourth greatest number")
    elif(c>=b and c>=a) and c>=e:
        print("c is second gretest number  ")
        if (b>=a and b>=e):
            print(" b is third gretest")
            if(a>=e):
                print("a is forth greatest number ")
            
                print(" e is smallest number")
            else:
                 print("a is smallest number")
                 print("e is fourth greatest number")
    elif(a>=b and a>=c) and a>=e:
        print("a is  second greatest number  ")
        if (b>=c and b>=e):
            print(" b is third gretest")
            if(c>=e):
                print("c is forth greatest number ")
            
                print(" e is smallest number")
            else:
                 print("e is fourth number")
                 print("c id smallest number ")
                
    
    else:
        print(" e is second greatest number ")
        if (b>=a and b>=c):
            print(" b is third gretest")
            if(c>=d):
                print("c is forth greatest number ")
            
                print(" a is smallest number")
            else:
                 print("a is fourt greatest number")
                 print("c is smallest number")




else:
    print(" e is first greatest number  ")

      
    if(b>=c and b>=d) and b>=a:
        print(" b is sencond  greatest number ")
        if (c>=d and c>=a):
            print(" c is third gretest")
            if(d>=a):
                print("d is forth greatest number ")
            
                print(" a is smallest number")
            else:
                print("a is fourth greatest number")
                print("d is smallest number")
                    
    elif(c>=b and c>=d) and c>=a:
        print("c is second gretest number  ")
        if (b>=d and b>=a):
            print(" b is third gretest")
            if(d>=a):
                print("d is forth greatest number ")
            
                print("  a is smallest number")
            else:
                 print(" a is fourth greatset number ")
                 print(" d is smallest number")
        
    elif(d>=b  and d>=c) and d>=a:
        print("d is  second greatest number  ")
        if (b>=c and b>=a):
            print(" b is third gretest")
            if(c>=a):
                print("c is forth greatest number ")
            
                print(" a is smallest number")
            else:
                print("a is fourth greatest number ")
                print("c is smallest number ")
    

    else:
         print(" a is second greatest number ")
         if (b>=a and b>=c):
             print(" b is third gretest")
             if(c>=d):
                print("c is forth greatest number ")
            
                print(" d is smallest number")
             else:
                 print("d is second greatest number ")
                 print(" c is smallest number")



    
        
        


    






























    

