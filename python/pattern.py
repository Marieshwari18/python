for i in range(5):
    print(' * '*5)

for i in range(5):
    print('*'*5,end=" ")
#triangle
for i in range(0,7):
    for j in range(i):
        print(" * ",end=" ")

        
    print()   #for next line

#triangle2
for i in range(7):
    print(" * "*i)
#decresing triangle
for i in range(6):
    for i in range(i,6):
        print(" * ",end=' ')
    print()  #for next line

#numbers
for i in range(5):
    for j in range(i,5):
        print(j,end="  ")
    print()   

#decresing triangle
for i in range(6,0):
    print(" * "*i)
#rightside triangle
for i in range(5):
    for j in  range(i,5):
        print(" ",end=" ")

    for k in range(i+1):
        print("*",end=" ")
    print()

#hill pattern

for i in range(5):
    for j in range(i,5):
        print(" ",end=" ")
    for k in range(i):
        print('*',end=" ")
    for  l in range(i+1):
        print("*",end=" ")
    print()


#reverse hill pattern
for i in range(5):
    for j in range(i+1):
        print(" ",end=" ")
    for k in range(i,5):
        print("*",end=" ")

    for l in range(i+1,5):
        print("*",end=" ")


    print()
#diamond pattern
for i in range(4):
    for j in range(i,5):
        print(" ",end=" ")
    for k in range(i):
        print("*",end=" ")
    for l in range(i+1):
        print("*",end=" ")

    print()
for i  in range(5):
    for j in range(i+1):
        print(" ",end=" ")
    for k in range(i,5):
        print("*",end=" ")
    for l in range(i+1,5):
        print("*",end=" ")

    print()




 




















