# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 14:47:14 2018

@author: tyrda

This parses a file of number into a list of integers
It then adds each frequency change to the running total.
It searches for a repeat frequency and returns that number
"""
import bisect, datetime

f_file = open('day1_input.txt','r')
frequency_change_list = []
for change in f_file:
    frequency_change_list.append(int(change.rstrip('\n')))
f_file.close()

frequency_list = []
current_frequency = 0
latest_frequency = 0
frequency_list.append(current_frequency)

frequency_found = False
loop_iteration = 0 #needed to add this because it was taking so long
start_time = datetime.datetime.now()
lap_time = datetime.datetime.now()-start_time

while frequency_found == False:
    loop_start = datetime.datetime.now()
    print(f'Loop: {loop_iteration}, loop time: {lap_time}, total time: {datetime.datetime.now()- start_time}')
    for change in frequency_change_list:
        latest_frequency = current_frequency + change
        
        possible_index = bisect.bisect_left(frequency_list, latest_frequency)
        if possible_index != len(frequency_list) and frequency_list[possible_index] == latest_frequency:
            frequency_found = True
            break
        else:
            current_frequency = latest_frequency
            bisect.insort(frequency_list, current_frequency)
    lap_time = datetime.datetime.now() - loop_start
    loop_iteration += 1
print(latest_frequency)