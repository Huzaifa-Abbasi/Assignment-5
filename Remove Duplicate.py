#Create a python list, add multiple values and remove the duplicate values from the list. and print the final list. Do not use any python builtin functions.

list = [1, 2, 3, 2, 4, 5, 1]


final_list = []
for num in list:
    if num not in final_list:
        final_list = final_list + [num]

print("Final List:", final_list)
