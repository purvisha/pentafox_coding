
"""
In a puzzle contest, the chairman of your English club posts a problem to compare a given pair of words and eliminate all common characters in them. To speed up the process of judging, the computer club head was requested to prepare computer logic. Please code a solution to the above problem applying your own skillset. 

Input 	: Word-1: Rajesh 	Word-2: Ganesh Output 	: RjGn 

"""
a=list(input())
b=list(input())
c=""
d=""
for i in range(len(a)):
    if a[i] not in b:
        c+=a[i]
for j in range(len(b)):
    if b[j] not in a:
        d+=b[j]

print(c+d)

#OUTPUT:
#Rajesh
#Ganesh
#RjGn