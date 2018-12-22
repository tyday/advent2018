# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 19:27:09 2018

@author: tyrda
"""
import pprint

class Point:
    
    def __init__(self,x=None,y=None):
        self.x = x
        self.y = y
        self.coords = (self.x,self.y)
    def __str__(self):
        return f'Point: ({self.x}, {self.y})'
    def __repr__(self):
        return f'({self.x}, {self.y})'
class Claim:
    
    def __init__(self,x=None,y=None, value='1', dimensions=(0,0)):
        self.x = x
        self.y = y
        self.coords = (self.x,self.y)
        self.value = value
        self.dimensions = dimensions
    def __str__(self):
        return f'Claim#{self.value} ({self.x}, {self.y}) - {self.dimensions} '
    def __repr__(self):
        return f'({self.x}, {self.y})'
    def calculate_points(self):
        '''
        returns a list of points that belong to this claim
        '''
        point_list = []
        width,height = self.dimensions
        for i in range(1,width+1):
            for j in range(1,height+1):
                new_point = Point(self.x + i, self.y+ j)
                point_list.append(new_point)
        return point_list


def interpret_claim(claim):
    #find first space and select from # to first space
#    if claim[0] == "#":
#        return False
    first_space = claim.find(" ")
    claim_number = claim.lstrip('#')[:first_space-1]
                                
    claim = claim[first_space+3:]
    first_colon = claim.find(":")
    claim_point = claim[:first_colon]
    claim_point = claim_point.split(',')
    
    claim = claim[first_colon+2:]
    first_x = claim.find("x")
    claim_width = claim[:first_x]
    claim_height = claim[first_x+1:]
    claim_dimensions=(int(claim_width),int(claim_height))
#    claim_dimensions=((claim_width),(claim_height))
    
    return Claim(int(claim_point[0]),int(claim_point[1]),int(claim_number),claim_dimensions)
#    return Claim((claim_point[0]),(claim_point[1]),(claim_number),claim_dimensions)

def add_point_to_dictionary(point,point_value,point_dictionary):
    if point in point_dictionary:
        point_dictionary[point].append(point_value)
    else:
        point_dictionary[point]=[point_value]

sample_claim = '#123 @ 3,2: 5x4'
sample_claim_list = [
        '#1 @ 1,3: 4x4',
        '#2 @ 3,1: 4x4',
        '#3 @ 5,5: 2x2',
#        '#4 @ 1,3: 4x4',
        ]
point_dictionary = {}
claim_list = []
#for item in sample_claim_list:
#    claim = interpret_claim(item)
#    claim_list.append(claim)
#    print(claim)
#    item_points = claim.calculate_points()
#    for point in item_points:
#        add_point_to_dictionary(point.coords,claim.value, point_dictionary)
##pprint.pprint(point_dictionary)
#multiple_claims_count = 0
#for item in point_dictionary:
#    if len(point_dictionary[item])>1:
#        multiple_claims_count += 1
#print(multiple_claims_count)

working_claim_list = []
fail_list = []
with open('day3_input.txt','r') as f:
    claim_list = f.read().split('\n')
#print(claim_list)
for item in claim_list:
    try:
        claim = interpret_claim(item)
        working_claim_list.append(claim)
        item_points = claim.calculate_points()
        for point in item_points:
            add_point_to_dictionary(point.coords,claim.value, point_dictionary)
    except:
        fail_list.append(item)

multiple_claims_count = 0
for item in point_dictionary:
    if len(point_dictionary[item])>1:
        multiple_claims_count += 1
print(multiple_claims_count)
claim_dictionary = {}
for item in point_dictionary:
    claims = point_dictionary[item]
    if len(claims) > 1:
        for a_claim in claims:
            claim_dictionary[a_claim] = 'overlaps'
for i in range(len(claim_list)):
    if i not in claim_dictionary:
        print(i)