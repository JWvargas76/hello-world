# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 03:49:01 2021

@author: Marcos Vargas
"""

largest = None
smallest = None


while True:
    num = input("Enter a number: ")
    if num == 'done':
            break
    
    try:
        
            
        n = int(num)
        if largest is None or n > largest :
            largest =n
        elif smallest is None or n < smallest:
            smallest = n			
    except:
        print("Invalid input")
        continue
        
   


print("Maximum is", largest)
print("Minimum is", smallest)		


