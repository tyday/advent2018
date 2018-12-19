# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 14:30:44 2018

@author: tyrda
"""

#import requests
#
#frequency_list = requests.get('https://adventofcode.com/2018/day/1/input')
f_file = open('day1_input.txt', 'r')
f_list = []
for line in f_file:
    f_list.append(int(line.rstrip('\n')))
print(sum(f_list))