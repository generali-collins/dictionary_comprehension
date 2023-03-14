# Collins Wanga

# Updating dictionary with other dictionary using dictionary comprehension

dict1 = {'Manchester' : 1, 'United' : 2, 'For' : 4, 'Life' : 6}
dict2 = {'For' : 3, 'Life' : 5}

print("The original dictionary 1 is : " + str(dict1))
print("The original dictionary 2 is : " + str(dict2))

res = {key : dict2.get(key, val) for key, val in dict1.items()}

print("The updated dictionary is : " + str(res))
