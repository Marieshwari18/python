print("maximum minimum value in list")
li2=[89,9,56,45,87,12,77,11,1]
li2.sort()
print(li2)
print("the minimum value of list",li2[0])
print(" the maximum value of list ",li2[7])
print("minimum ",min(li2))
print("maximum ",max(li2))
print("palindrome program")
#palindrome
li=['m','a','d','a','m']

li.reverse()
print(li)
li3=list(input("enter the list"))
palin=li3[::-1]
print(palin)
if li3==palin:
    print("palindrome")
else:
    print(" not palinrome") 
#leap year
yr=int(input("enter the year"))
if (yr%400==0 or yr%4==0 ):
        print(" thr year is leap year")
else:
     print("the year is not leap year")
print("check prime number")
#find prime number
num=int(input("enter the number"))
n=[2,3,4,5,6,7,8,9,10]
if(num==1 or num ==0):
    if num==1:
        print("one is not prime and composite  number")
    else:
        print("zero is composite number ")
else:
    if(num%1==0 and num%num==0):
        print(" the number is prime number ")
    else:
        print("the number composite number")
print("weak day") 
#week day
num=int(input("enter a number"))
if(num==1):
    print("sunday")
elif(num==2):
    print("monday")
elif(num==3):
    print("tues day")
elif(num==4):
    print("wednes day")
elif(num==5):
    print("thurs day")
elif(num==6):
    print("friday")
elif(num==7):
    print("saturday")
else:
     print("enter number between 1 to 7")

print("divisible by 3 and 2")
#divisiple by 2 or 3
num=int(input("enter the number "))
if(num%2==0 and num%3==0):
    print("the number is divisiple by 2 and 3")
elif(num%2==0 or num%3==0):
    if(num%2==0):
        print("the number is divisiple by 2 ")
    else:
        print(" the number is divisiple by 3")        
else:
    print(" the number is  not divisiple by 2 and 3")
print("check digit,alpha,special character")

#isalpha,isdigit,isspecilcharacter
x=input("enter the x ")
if x.isalpha():
    print(" it is alphapect")
elif x.isdigit():
    print("it is digit ")
else:
    print("it is special character")
print("elcteical bill")
#electical bill
unit=int(input("enter the unit of electricity"))
if( 0<unit<=100):
         amount=unit*5.0
         print("amount " ,amount)
elif(100<unit<=200):
    amount=((unit-100)*7.50)+500
    print(" amunt ",amount)
elif(200<unit):
    amount=unit*10
    print("amount  ",amount)
else:
    print(" invalid number")
print("bmi value")
#bmi weight
height=float(input("enter the height"))
weight=float(input("enter the weight"))
             
bmi=weight/((height/100)**2)
print(bmi)

if(0<bmi<18.5):
    print(" under weight")
elif(18.5<=bmi<24.9):
    print("normal weight")
elif(24.9<=bmi<29.9):
    print("over weight")
elif(bmi<=30):
    print("obensity")
else:
    print("invalid value")
 #year is century
year=int(input("enter the year  "))
if year%100==0:
    print(" the year is century ")    
else:
    print("the year is not century")
print("divisible by 3 and 5")
#divisible by 3 and 5
num =int(input("enter a number "))
if(num%3==0 and num%5==0):
         print("the number is divisible by both 5 and 3")
else:
    print("the  number is not divisible by 5 and 3")
print("calculater ")
#calculator
x=int(input("enter the number  "))
y=int(input("enter the number  "))
z=input("enter To perform calculator ")
if(z=="add"):
    print(" addtion ",x+y)
elif(z=="sub"):
    print("subraction ",x-y)
elif(z=="mul"):
    print("multiplication   ",x*y)
elif(z=="div"):
    print("division  ",x/y)
else:
    print("invalid statement")
print("armstrong number")   
#armstrong number
n=input("enter the  number")
num=list(n)
print(num)
l=len(num)
print(l)
a=int(num[0])
b=int(num[1])
c=int(num[2])
arm=(a**l)+(b**l)+(c**l)
s=str(arm)
print(n)
if(s==n):
    print("it is armstrong number")
else:
    print("it is not armstrong number ")







  























    




























     
























