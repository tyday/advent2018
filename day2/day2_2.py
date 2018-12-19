# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 17:34:52 2018

@author: tyrda
"""
file = 'day2_input.txt'
#file = 'day2_2_test_2.txt'
with open(file) as f:
    box_ids = f.read().split()

def number_of_same_letters(first_item, second_item):
    same_letters = 0
    for i in range(0,len(first_item)):
        if first_item[i] == second_item[i]:
            same_letters += 1
    return same_letters

''' most similar contains a tuple
    index of first instance
    index of second instance
    number of similar letters
'''
most_similar = (0,0,0)
highest_count = 0

for i in range(0,len(box_ids)):
    print(f'{i}/{len(box_ids)}')
    first_id_to_compare = box_ids[i]
    for j in range(i+1,len(box_ids)):
        second_id_to_compare = box_ids[j]
        samecount = number_of_same_letters(first_id_to_compare,second_id_to_compare)
        if samecount > highest_count:
            highest_count = samecount
            most_similar = (i,j,samecount)
print (most_similar)
i,j,max = most_similar
print(f'{box_ids[i]} {box_ids[j]}')
first_box, second_box = box_ids[i], box_ids[j]
common_letters = []
for i in range(0,len(first_box)):
    if first_box[i] == second_box[i]:
        common_letters.append(first_box[i])
print(''.join(common_letters))

        