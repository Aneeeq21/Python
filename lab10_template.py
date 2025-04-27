'''
-------------------------------------------------------------------------------
Name: Aneeq Altaf
Partner's Name: Alexander Powell
Assignment: Lab 10
Due by end of your lab class
-------------------------------------------------------------------------------
Honor Code Statement: I received no assistance on this assignment that
violates the ethical guidelines set forth by the professor and class syllabus.
-------------------------------------------------------------------------------
'''

#Part 1 -- Working with Strings
def str_combo(str1):
    str2=''
    if len(str1)<3:
        str2=str1
    else:
        str2=str1[0]+str1[len(str1)//2]+str1[len(str1)]
    return str2    
        



#Part 2 -- Reading from and Writing to File 


