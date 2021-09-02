"""
A school camp is organized by a school to support the process of preparing their students for an examination. They are in need of a study timetable that has following assumptions: 
Assumptions: 
1.	Total Days of Camp 	– 5 Days 
2.	Total Hours a day 	– 5 Days 
3.	Total Subjects 	– 5 Subjects 
Note: The timetable should not follow the same order and should be in random everyday. Prepare code logic to help the School. 
"""
import random
days=['mon','tues','wednes','thurs','fri']
hr=['9','10','11','12','1']
subject=['tamil','english','maths','computer','physics']
print("       "+hr[0]+"       "+hr[1]+"      "+hr[2]+"      "+hr[3]+"      "+hr[4])
for i in range(0,5):
    print(days[i],end="    ")
    print(subject[random.randrange(0,5)],end="    ")
    print(subject[random.randrange(0,5)],end="    ")
    print(subject[random.randrange(0,5)],end="    ")
    print(subject[random.randrange(0,5)],end="    ")
    print(subject[random.randrange(0,5)],end="    ")
    print()

