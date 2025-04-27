'''
-------------------------------------------------------------------------------
Name: Aneeq Altaf
Partner's Name:Laith Muwakki
Assignment: Lab 11
Due by end of your lab class
-------------------------------------------------------------------------------
Honor Code Statement: I received no assistance on this assignment that
violates the ethical guidelines set forth by the professor and class syllabus.
-------------------------------------------------------------------------------
'''


#PART 1 -- Identifying Exceptions
'''
sum_of_items errors:index error
    
    #write explanation here
    every list postion's starts from 0 index and end at one less than total element number but here it will iterate 0 to last element number so 
    index at last element number dont exist as it exceeds one more than last index so list out of index.
    

feet_to_miles errors:syntax error
    
    #write explanation here
    every parenthesis should end with its pair of end parenthesis ')' and here closing parenthesis is missing in line4.

square_area errors:type error

    #write explanation here
    here in the initialization of result whether two string can be concatenate with '+' sign or two integer can be added with '+' sign
    but here there are mixture of string and integer so neither integer can be concatenate with string nor string added with integer so its 
    type error as two different types 'string' and int'.

dict_search errors: Name error
    

    #write explanation here
    here '_dict' dictionary not exist so it will give name error because python is also case sensitive and every name should be unique.
    
'''

#PART 2 -- Handling Exceptions 
#Write code for the programming task here

#original
'''
def calculate_decimal(lst, numer_index, denom_index):
    numer = lst[numer_index]
    denom = lst[denom_index]
    dec = round(numer/denom, 4)
    return dec
'''

#with exception handling
def calculate_decimal(lst, numer_index, denom_index):
    try:
        numer = lst[numer_index]
        denom = lst[denom_index]
        dec = round(numer/denom, 4)
        return dec
    except IndexError:
        return "Invalid index."
    except ZeroDivisionError:
        return "Cannot divide by zero."
    except TypeError:
        return "Incorrect type. Indices must be integers."      
        

        

