
# Write a Python program to calculate the length of a string.

def length_string(string):
    return len(string)

def count_frequency(string):
    dicts = {}
    for n in string:
        keys = dicts.keys()
        if n in keys:
            dicts[n] +=1
        else:
            dicts[n] =1
    return dicts
#  Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
def  get_first_and_last_2_string(string):
    if len(string)<2:
        return ""
    return string[:2]+string[-2:]
# Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
def change_first_occurence(string):
    first_char =string[0]
    modified_string =first_char+string[1:].replace(first_char,'$')
    return modified_string

def get_single_string(str1,str2):
    return str1.replace(str[:2])+str2.replace(str2[:2])
"""Write a Python program to add 'ing' at the end of
 a given string (length should be at least 3). If the given 
 string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3,
 leave it unchanged."""
def excercise_6(string):
    if len(string)>2:
       if string[-3:]=="ing":
           string += "ly"
       else:
           string +="ing"
    return string
"""7Write a Python function that takes 
a list of words and return the longest word and
 the length of the longest one."""
def find_longest_word(lists):
    word_len = []
    for n in lists:
        word_len.append((len(n),n))
    word_len.sort()
    return word_len[-1][0], word_len[-1][1]
"""9. Write a Python program to remove the nth index character from a nonempty string.
"""
def remove_nth_index_string(string,index):
    first_part =string[:index]
    last_part =string[index+1:]
    return first_part+last_part

"""
Write a Python program to change a given string to a newly string 
where the first and last chars have been exchanged.
"""
def exchange_first_last(str1):
     return str1[-1:] + str1[1:-1] + str1[:1]

print(exchange_first_last("Shibabaw"))