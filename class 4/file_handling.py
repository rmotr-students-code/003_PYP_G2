"""
Write a function, that receives the path to a text file that contains JUST ONE word
per line, and returns a dictionary with the counter of words starting with each
letter from 'a' to 'z'.

Example:
  counter_by_letter('words.txt')  
  # {
    'a': 2,
    'b': 10,
    'c': 0,
    ...
    'z': 1
  }

"""

import string

def counter_by_letter(filepath):
    dic = {letter: 0 for letter in string.ascii_lowercase} 
    with open(filepath, 'r') as f:
        for word in f:
            dic[word[0]] += 1
    f.close()
    return dic


print(counter_by_letter('test.txt'))