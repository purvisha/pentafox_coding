'''A fixed set of positive integers is dictated by the mathematics professor during a puzzle contest. The professor asks the students to find a pair of numbers that result in a given sum. Code a logic that can automate this puzzle. Use the below input for your exercise. Case – 1 
Input 	: arr = [1, 2, 3, 4, 6] & Sum = 8 
Output : 2,6 
 
Case – 2 
Input 	: arr = [1, 2, 3, 4, 9] & Sum = 8 
Ouput: No Pairs found '''

arr=list(map(int,input().split()))
su=int(input())
flag=0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if (arr[i]+arr[j]==su):
            flag=1
            print(arr[i]," ",arr[j])
            break
if(flag==0):
    print("No pair found")


#OUTPUT:
 #   1 2 3 4 6
 #   8
  #  2,6 