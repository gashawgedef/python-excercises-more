

# This are dictionary excercises with solutions
"""2. Write a Python script to add a key to a dictionary."""



from multiprocessing import Value
from unittest import result


def add_key(dict,key,value):
    dict[key]=value
    return dict

""" Write a  Python script to concatenate the following dictionaries to create a new one."""
def concatenate_dict(dict1,dict2,dict3):
    dicts={}
    for d in (dict1,dict2,dict3):
        dicts.update(d)
    return dicts
""" Write a  Python script to check whether a given key already exists in a dictionary."""
def check_key(dicts,key):
     for key_1 in dicts:
         if key==key_1:
             return True
     return False

""". Write a Python program to iterate over dictionaries using for loops."""
def iterate_dicts(dicts):
    for d in dicts:
        print(dicts[d])
"""Write a Python script to generate and print a dictionary that contains a number (between 1 and"""
def generate_square(n):
    dicts={}
    if n<1:
        return
    else:
        for i in range(1,n+1):
            dicts[i]=i*i
        return dicts
"""8. Write a  Python script to merge two Python dictionaries."""
def merge_two_dicts(d1,d2):
    d={}
    d= d1.copy()
    d.update(d2)
    return d

"""10. Write a Python program to sum all the items in a dictionary."""
def multiply_dict_items(dicts):
    product=1
    for d in dicts.values():
        product*=d
    return product
"""10. Write a Python program to sum all the items in a dictionary."""
def sum_dict_values(dicts):
    result = sum(dicts.values())
    return result
"""rite a  Python program to remove a key from a dictionary."""
def remove_dict_key(dicts,key):
    if key in dicts:
          del dicts[key]
    return dicts
"""13. Write a Python program to map two lists into a dictionary.
"""
def map_lists(keys,values):
    return dict(zip(keys,values))
"""Write a Python program to sort a given dictionary by key."""
def sort_dict_by_key(dicts):
    sorted_keys=sorted(dicts.keys())
    sorted_dict={key:dicts[key] for key in sorted_keys}
    return sorted_dict
"""Write a Python program to get the maximum and minimum values of a dictionary."""
def find_min_max(dicts):
    min_value=min(dicts.values())
    max_value=max(dicts.values())
    return[min_value,max_value]
"""Write a  Python program to get a dictionary from an object's fields."""
class Example:
    def __init__(self,a,b,c) -> None:
        self.first_name=a
        self.middle_name=b
        self.last_name=c
    def get_object_fields(obj):
        return vars(obj)
    def get_object_fields1(obj):
        return obj.__dict__
"""17. Write a Python program to remove duplicates from the dictionary.
"""
def remove_duplicates(dicts):
    result={}
    for key,value in dicts.items():
        if value not in result.values():
            result[key]=value
    return result
""" Write a Python program to check if a dictionary is empty or not."""
def isEmpty(dicts):
    if len(dicts)==0:
        return True
    else:
        return False
"""Write a Python program to combine two dictionary by adding values for common keys."""
def combine_from_common(dict1,dict2):
    for key,value in dict1.items():
        if key in dict2.keys():
            dict1[key]=dict1[key]+dict2[key]
    return dict1
""" Write a  Python program to print all distinct values in a dictionary."""
def dict_distinict_values(dicts):
    result=set()
    for dictionary in dicts:
       for value in dictionary.values():
            result.add(value)
    return result
"""Write a  Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary."""
def generate_combinations(data):
    # Convert dictionary values to a list of lists
    lists = list(data.values())
    
    # Recursive function to generate combinations
    def combine(current, depth):
        # If depth equals the length of lists, print the combination
        if depth == len(lists):
            print(''.join(current))
            return
        # Iterate through the current list and call combine recursively
        for letter in lists[depth]:
            combine(current + [letter], depth + 1)
    
    # Start the recursion with an empty list and depth 0
    combine([], 0)
"""Write a Python program to find the highest 3 values of corresponding keys in a dictionary."""

def highest_three(dicts):
    sorted_items=sorted(dicts.items(),key=lambda item:item[1],reverse=True)
    top_3 =sorted_items[:3]
    return top_3
"""24. Write a  Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
Sample string : 'w3resource'
Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}"""

def creat_dict_letter(strings):
     result={}
     for s in strings:
         result[s]=strings.count(s)
     return result
"""26. Write a Python program to count the values associated with a key in a dictionary.
"""
def count_values(students, key, value):
    count = 0
    for student in students:
        if student.get(key) == value:
            count += 1
    return count
"""Write a Python program to convert a list into a nested dictionary of keys."""
def convert_list_dict(lists):
    result=current ={}
    for i in lists:
        current[i]={}
        current =current[i]
    return result

"""Write a Python program to sort a list alphabetically in a dictionary."""
def sort_alpabetically(dicts):
    for key, value in dicts.items():
        dicts[key]=sorted(value)
    return dicts

"""Write a  Python program to remove spaces from dictionary keys."""
def remove_spaces(dicts):
    new_dict={}
    for key, value in dicts.items():
        new_key=key.replace(" ","")
        new_dict[new_key]=value
    return new_dict
    
"""30. Write a Python program to get the top three items in a shop."""
def top_three_items(dicts):
    sorted_dicts=sorted(dicts.items(),key=lambda item:item[1],reverse=True)
    top_three=sorted_dicts[:3]
    return top_three
"""Write a  Python program to get the key, value and item in a dictionary."""
def get_count_key_value(dicts):
    for key,value in dicts.items():
        item=(key,value)
        yield key,value,item
""" Write a Python program to count the number of items in a dictionary value that is a list"""
def count_dict_type_list(dicts):
    count=0
    for value in dicts.values():
        if isinstance(value,list):
            count+=len(value)
    return count

"""Write a  Python program to sort Counter by value."""
def sort_by_counter(dicts):
    sorted_dict=sorted(dicts.items(),key=lambda item:item[1],reverse=True)
    return sorted_dict

print(sort_by_counter( {'Math':81, 'Physics':83, 'Chemistry':87}))