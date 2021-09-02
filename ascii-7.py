"""
The alphabetical value is represented from 1-26 for characters A-Z respectively. Using this principle generate a crypto decoder that can generate the message for transmitted sequence of alphabetical values. 
 Input 	: 1,2,3,4,26 Output : ABCDZ 
"""

a=list(map(int,input().split(',')))
b=''
c=64
for i in a:
    d=c+i
    b+=chr(d)
print(b)

#OUTPUT:
    #1,2,3,4,26
    #ABCDZ