'''
-------------------------------------------------------------------------------
Name: Aneeq Altaf
Partner's Name: Alexander Powell
Assignment: Lab 8
Due by end of your lab class
-------------------------------------------------------------------------------
Honor Code Statement: I received no assistance on this assignment that
violates the ethical guidelines set forth by the professor and class syllabus.
-------------------------------------------------------------------------------
'''

#Part 1 -- Returning a Value vs. Changing In-Place

#Function 1
def len_to_area_in_place(list1):
    
    for i in range(len(list1)):
        list1[i]=list1[i]*list1[i]
        
 

    
    


#Function 2
#write code here
def len_to_area_new_lst(inplace):
    len_to_area_in_place(inplace)
    return inplace

    


#Part 2 -- Using Default Arguments

#write code here
def plane_ticket_cost(base_cost, str1, cat_str='domestic', tax_rate=10):
    
    tax_rate=tax_rate
    if cat_str=='international':
        base_cost+=100
    base_cost+=base_cost*(tax_rate/100)
    str2=f'A ticket to {str1} costs ${base_cost}'
    return str2
    
        
    