#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "xiaogui"
# Date: 2017/11/6


#在一个包含N个整数的list中找出三个数，使它们的绝对值求和最小
def find_three_number(list_number):
   rl=[]
   for i in list_number:
      rl.append(abs(i))
      rl.sort()
   return (rl[0], rl[1], rl[2])


#在一个包含N个整数的list中，找出所有没有出现重复的数字
def find_not_duplicate(list_number):
   rl = []
   for i in range(len(list_number)):
      for j in range(len(list_number)):
         #print(i,j, len(list_number)-1)
         if list_number[i] == list_number[j]:
            if i != j:
               break
            elif j == len(list_number)-1:
                rl.append(list_number[i])
         elif j == len(list_number)-1:
               rl.append(list_number[i])
   return (rl)
#
# l = [0,3,3,-3,3,4,0.5]
# result = find_three_number(l)
# print(result)
# result = find_not_duplicate(l)
# print(result)

