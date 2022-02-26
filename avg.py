# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 17:48:52 2022

@author: asreno
"""

sum=0
name=input("enter student name: ")
for i in range(3):
    grad=int(input("enter student grad: "))
    sum=sum+grad
avg=sum/3
print("name student",name)
print("average is:",avg)
