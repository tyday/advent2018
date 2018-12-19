# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 17:03:12 2018

@author: tyrda

Opens a list of ids
Searches each id for 2 and 3 character repeats

multiplies the number of ids with 2 character repeates with the ids with 3 character repeats
"""

with open('day2_input.txt') as f:
    box_ids = f.read().split()

exactly_two = 0
exactly_three = 0

for item in box_ids:
    exactly_two_has_match = 0
    exactly_three_has_match = 0
    unique_letter_count = {}
    for letter in item:
        try:
            if unique_letter_count[letter]>0:
                unique_letter_count[letter] += 1
        except:
            unique_letter_count[letter] = 1
#    print(item,unique_letter_count)
    for letter in unique_letter_count:
        if unique_letter_count[letter] == 2:
            exactly_two_has_match = 1
        if unique_letter_count[letter] == 3:
            exactly_three_has_match = 1
    exactly_two += exactly_two_has_match
    exactly_three += exactly_three_has_match
    
print(exactly_two, exactly_three)
print(int(exactly_two)*int(exactly_three))