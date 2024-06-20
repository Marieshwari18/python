
'''li2=[89,9,56,45,87,12,77,11,1]
li2.sort()
print(li2)
print("the minimum value of list",li2[0])
print(" the maximum value of list ",li2[7])
print("minimum ",min(li2))
print("maximum ",max(li2))

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
    print(" not palinrome") '''
'''#leap year
yr=int(input("enter the year"))
if yr%100==0:
    if yr%400==0:
        print(" thr year is leap year")
    else:
        print("not leap year")
else:
    if(yr%4==0):
        print(" the year is leap")
    else:
        print("the year is not leap year")'''
#find prime number
'''num=int(input("enter the number"))
if(num==1 or num ==0):
    if num==1:
        print("one is not prime and composite  number")
    else:
        print("zero is composite number ")
else:
    if(num%1==0 and num%num==0):
        print(" the number is prime number ")
    else:
        print("the number composite number")'''
#week day
'''num=int(input("enter a number "))
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
     print("enter number between 1 to 7")'''


#divisiple by 2 or 3
'''num=int(input("enter the number "))
if(num%2==0 and num%3==0):
    print("the number is divisiple by 2 and 3")
elif(num%2==0 or num%3==0):
    if(num%2==0):
        print("the number is divisiple by 2 ")
    else:
        print(" the number is divisiple by 3")        
else:
    print(" the number is  not divisiple by 2 and 3")

#isalpha,isdigit,isspecilcharacter
x=input("enter the x ")
if x.isalpha():
    print(" it is alphapect")
elif x.isdigit():
    print("it is digit ")
else:
    print("it is special character")
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

#bmi weight
height=float(input("enter the height"))
weight=float(input("enter the weight"))
             
bmi=weight/(
print(bmi)

if(0<bmi<18.5):
    print(" under weight")
elif(18.5<=bmi<24.9):
    print("normal weight")
elif(24.9<=bmi<29.9):
    print("over weight")
elif(bmi>30):
    print("obensity")
else:
    print("invalid value")
 #year is century
year=int(input("enter the year  "))
if year%100==0:
    print(" the year is century ")
else:
    print("the year is not century")'''
#divisible by 3 and 5
num =int(input("enter a number "))
if(num%3==0 and num%5==0):
         print("the number is divisible by both 5 and 3")
else:
    print("the  number is not divisible by 5 and 3")



























    




























     
























