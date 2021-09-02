"""
Alice is a cryptanalyst who is in charge of transmitting messages to bob without any intruder getting hands on it. Alice thinks of transmitting the message by reversing it with a random character appended as prefix to the encoded message. 
Input 	: Pentafox 
Ouput: Oxofatnep 

"""
a=input()
b=""
for i in range(len(a)-1,-1,-1):
    b+=a[i]
c=b[1]

print(c.upper()+b.lower())

#OUTPUT:
#Pentafox 
#Oxofatnep