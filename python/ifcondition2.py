mark=int(input("enter the mark"))
if 90<=mark<=100:
         print("grade A ")
elif(89>=mark>=80):
    print("grade B")
elif(70<=mark<=79):
    print("grade  C")
elif(60<=mark<=69):
    print("grade D")
else:
    print("grade  F")


#2nd

li=['monday','tuesday','wedensday','thursday','friday']
li2=['saturday','sunday']
day=input("enter a day ")
age=int(input("enter age "))
if(day in li):
    if(age<18):
        print("the ticket is $12")
    elif(age>=18):
        print("the ticket is $15")
    else:
        print("inavalid number")
elif(day in li2):
    if(age<18):
        print("the ticket is $15")
    elif(age>=18):
        print("the ticket is $20")
    else:
        print("inavalid number")
else:
    print("invalid statement")


#3

amount=int(input("enter the total amount"))
premem=(input("are you premimum member ?(yes/no)"))
if(premem=='yes'):
        print("amount   :",amount)
elif(premem=='no'):
    print("amount+deliverycharge rupees 10  :",amount+10)

else:
    print("invalid statement")























