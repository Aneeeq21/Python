'''
-------------------------------------------------------------------------------
Name: Aneeq Altaf
Partner's Name: Laith Muwakki
Assignment: Lab 5
Due by end of your lab class
-------------------------------------------------------------------------------
Honor Code Statement: I received no assistance on this assignment that
violates the ethical guidelines set forth by the professor and class syllabus.
-------------------------------------------------------------------------------
'''
#PART 1: Complete the Program

#Task 1
def add_to_this(top):
    sum = 0
    for i in range(top+1): #remove the placeholder blanks when you are ready to write your code
        sum +=i
    return sum   


#Task 2
def exp_by_hand(base, exp):
    result = 1 #remove the placeholder blanks when you are ready to write your code
    for i in range(exp):
        result = result*base
    return result


#PART 2: Write Your Own Function with for Loops

#Task 3
def add_every_third(add3):
    sum1=0
    y= (len(add3))
    for i in add3[2:y:3]:
        if i>0:
            sum1+=i
        
        
               
       
    return sum1