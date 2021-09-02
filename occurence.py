"""
As a computer engineer, you are requested to reduce the storage space needed to store the textual content in the computer. Write a logic that can compress the content as given in the below example. Input : All is well. 
Output : Al2 is wel2 (Character followed by its number of occurrence) 

"""
s=input()
i = 0
while( i < len(s) - 1) :
    count = 1
    while s[i] == s[i + 1] :
        i += 1
        count += 1
        if i + 1 == len(s):
            break
    if(count>1):
        print(str(s[i]),end="")
        print(str(count),end="")
    else:
        print(str(s[i]),end="")
            
    i += 1
    
#OUTPUT:
#   All is well
#   Al2 is wel2