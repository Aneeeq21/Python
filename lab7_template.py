'''
-------------------------------------------------------------------------------
Name: Aneeq Altaf
Partner's Name: Laith Muwakki
Assignment: Lab 7
Due by end of your lab class
-------------------------------------------------------------------------------
Honor Code Statement: I received no assistance on this assignment that
violates the ethical guidelines set forth by the professor and class syllabus.
-------------------------------------------------------------------------------
'''

#Part 1 -- Identify mistakes and fix the code

#Task 1

#Mistakes: the function wasnt checking the items of cart in dictionary.

#Write fixed code here
def total_cost(dictionary, cart):
    total = 0
    for item in dictionary:
        if item in cart:
            cost=round(dictionary[item], 2)
            total += cost
        
    return total


#Task 2

#Mistakes:

#Write fixed code here



# Part 2 -- Write your own function with dictionaries 

#Task 3

#write code here


#Task 4

#write code here