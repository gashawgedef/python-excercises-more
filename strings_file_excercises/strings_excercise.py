
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
"""Write a Python program to remove characters that have odd index values in a given string.
"""
def remove_odd_string(str1):
     result =""
     for i in range(len(str1)):
         if i%2==0:
             result =result+str1[i]
     return result

"""Write a Python program to count the occurrences of each word in a given sentence.
"""
def count_occurence(str1):
    word_list= str1.split(' ')
    dicts={}
    for i in word_list:
        if i in dicts:
            dicts[i]+=1
        else:
            dicts[i] =1
            
    return dicts

"""Write a  Python  script that takes input from the user and displays 
that input back in upper and lower cases.
"""
def make_upper_lower(str1):
    return[str1.lower(),str1.upper()]

"""Write a Python program that accepts a comma-separated sequence of words as input and prints 
the distinct words in sorted form (alphanumerically).

"""
def comma_separated_words(str1):
    words =[word.strip() for word in str1.split(',')]
    words.sort()
    return words
"""Write a Python function to get a string made of 4 copies of the last two characters
of a specified string (length must be at least 2).
"""
def copy_last_two(str1):
    return str1[-2:]*4
"""Write a  Python function to get a string made of the first three characters of a specified string.
If the length of the string is less than 3, return the original string.
"""
def first_3_char(str1):
    if len(str1)>3:
        return str1[:3]
    else:
        return str1
"""Write a  Python function to reverse a
string if its length is a multiple of 4.
"""
def reverse_str_multiple_4(str1):
    if len(str1)%4 == 0:
        return str1[::-1]
    else:
        return str1

"""Write a Python function to convert a given string to all uppercase if it contains at least 2
uppercase characters in the first 4 characters.
"""
def count_first_4(str1):
    count=0
    letters =str1[:4]
    for letter in letters:
        if letter.upper() == letter:
            count+=1
    if count >2:
        return str1.upper()
    return str1
        
"""Write a  Python program to sort a string lexicographically.
"""
def sort_strings(str1):
    string_list =list(str1)
    string_list.sort()
    string_list= ''.join(string_list)
    return  string_list

"""Write a Python program to remove a newline in Python.
"""
def remove_new_line(str1):
    return str1.replace('\n','')
"""Write a Python program to check whether
a string starts with specified characters.
"""
def check_starts_with(str1,s):
    return str1.startswith(s)
"""Write a Python program to create a Caesar encryption.
"""

def caesar_cipher(str1):
    return str1

    
    
print(check_starts_with("Gashaw","Gashaw"))