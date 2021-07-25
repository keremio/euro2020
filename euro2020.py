import random

groupa = ["Italy","Turkey","Switzerland","Wales"]
groupb = ["Belgium","Finland","Russia","Denmark"]
groupc = ["Netherlands","Austria","Ukraine","North Macedonia"]
groupd = ["England","Croatia","Czech Republic","Scotland"]
groupe = ["Sweden", "Spain", "Slovakia","Poland"]
groupf = ["France","Germany","Portugal","Hungary"]
qualified = []
#group stage
thirds = {}
groups = [groupa, groupb, groupc, groupd, groupe, groupf]
for group in groups:
    result = ""
    points = [0,0,0,0]
    goal_difference = [0,0,0,0]
    for i in range (0,len(group)):
        for j in range (0,i):
            print("For the match, enter the result:" , group[i], "v", group[j])
            result = input()
            result = result.split("-")
            goal_difference[i] = int(result[0]) - int(result[1])
            goal_difference[j] = int(result[1]) - int(result[0])
            if (int(result[0]) > int(result[1])):
                points[i] += 3
            elif(int(result[1]) > int(result[0])):
                points[j] += 3
            elif(int(result[0]) == int(result[0])):
                points[i] += 1
                points[j] += 1

    dictgroup = {}
    dictgroup_2 = {}
    dictgroup_3 = {}
    last_group = ["","","",""]
    'print(goal_difference)'
    for i in range (0,len(group)):
        dictgroup[group[i]] = points[i]
    dictionary_items = dictgroup.items()
    sorted_items = sorted(dictionary_items, key = lambda x:x[1], reverse = True)
    for i in range (0, len(group)):
        last_group[i] = sorted_items[i][0]
    

    for i in range (0,len(group)):
        dictgroup_2[group[i]] = goal_difference[i]
    dictionary_items = dictgroup_2.items()
    sorted_items_2 = sorted(dictionary_items, key = lambda x:x[1], reverse = True)
    'print(sorted_items_2)'

    for i in range (0, len(sorted_items)):
        for j in range (0,i):
            if sorted_items[i][1] == sorted_items[j][1]:
                if sorted_items_2[i][1] < sorted_items_2[j][1]:
                    last_group[i],last_group[j] = last_group[j], last_group[i]
                    
    'print(last_group)'
    for i in range(0, len(last_group)):
        print(last_group[i], sorted_items[i][1])
    qualified.append(last_group[0])
    qualified.append(last_group[1])
    print(last_group[0], "and", last_group[1], "have been qualified.")
    thirds[last_group[2]] = sorted_items[2][1]
    dictgroup_3[last_group[2]] = goal_difference[2]
    
    group_of_thirds = ["","","","","",""]
    dictionary_items = thirds.items()
    sorted_items_3 = sorted(dictionary_items, key = lambda x:x[1], reverse = True)
    for i in range (0, len(sorted_items_3)):
        group_of_thirds[i] = sorted_items_3[i][0]
    for i in range (0,len(group)):
        dictgroup_3[group[i]] = goal_difference[i]
    dictionary_items = dictgroup_3.items()
    sorted_items_3 = sorted(dictionary_items, key = lambda x:x[1], reverse = True)
    for i in range (0, len(sorted_items_3)):
        for j in range (0,i):
            if sorted_items_3[i][1] == sorted_items_3[j][1]:
                if sorted_items_3[i][1] < sorted_items_3[j][1]:
                    group_of_thirds[i],group_of_thirds[j] = group_of_thirds[j], group_of_thirds[i]

print(dictgroup_3)
qualified_3rds = group_of_thirds[0:4]
print("These are the qualified thirds:")
for team in qualified_3rds:
    print(team)
qualified.append(group_of_thirds[0])
qualified.append(group_of_thirds[1])
qualified.append(group_of_thirds[2])
qualified.append(group_of_thirds[3])
print("The qualified teams for EURO 2020:")
for team in qualified:
    print(team)


#semi-quarter finals
first_group = random.sample(qualified, k = len(qualified)//2)
second_group = list(set(qualified) - set(first_group))
qualified_for_quarter = []
for i in range (0, len(first_group)):
    print("For the match:" , first_group[i], "v", second_group[i])
    result = input()
    result = result.split("-")
    if (int(result[0]) > int(result[1])):
        qualified_for_quarter.append(first_group[i])
    elif(int(result[1]) > int(result[0])):
        qualified_for_quarter.append(second_group[i])
for team in qualified_for_quarter:
    print(team)
#quarter finals
first_group = random.sample(qualified_for_quarter, k = len(qualified_for_quarter)//2)
second_group = list(set(qualified_for_quarter) - set(first_group))
qualified_for_semi = []
for i in range (0, len(first_group)):
    print("For the match, enter the result:" , first_group[i], "v", second_group[i])
    result = input()
    result = result.split("-")
    if (int(result[0]) > int(result[1])):
        qualified_for_semi.append(first_group[i])
    elif(int(result[1]) > int(result[0])):
        qualified_for_semi.append(second_group[i])
for team in qualified_for_semi:
    print(team)
#semi finals
first_group = random.sample(qualified_for_semi, k = len(qualified_for_semi)//2)
second_group = list(set(qualified_for_semi) - set(first_group))
qualified_for_the_final = []
for i in range (0, len(first_group)):
    print("For the match, enter the result:" , first_group[i], "v", second_group[i])
    result = input()
    result = result.split("-")
    if (int(result[0]) > int(result[1])):
        qualified_for_the_final.append(first_group[i])
    elif(int(result[1]) > int(result[0])):
        qualified_for_the_final.append(second_group[i])
for team in qualified_for_the_final:
    print(team)
#the_final
finalist_1 = first_group[0]
finalist_2 = first_group[1]
print("For the match, enter the result:" , finalist_1, "v", finalist_2)
result = input()
result = result.split("-")
if (int(result[0]) > int(result[1])):
    print("CHAMPIONS:", finalist_1)
elif(int(result[1]) > int(result[0])):
    print("CHAMPIONS:", finalist_2)



    
