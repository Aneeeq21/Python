'''
-------------------------------------------------------------------------------
Name: Aneeq Altaf
Partner's Name: Laith Muwakki
Assignment: Lab 4
Due by end of your lab class
-------------------------------------------------------------------------------
Honor Code Statement: I received no assistance on this assignment that
violates the ethical guidelines set forth by the professor and class syllabus.
-------------------------------------------------------------------------------
'''

#PART 1: Complete the Program
#NOTE: TEST YOUR FUNCTIONS!!!!!

#Task 1
def add_to_this(top):
    x = 1
    sum = 0
    while x <= top:
        sum = sum + x
        x += 1
    return sum



'''Identify:
Control Variable: x
Initialization: x=1
Modification:x+=1
Describe the control: loop will calculate the sum of all numbers from 0 to top and calculate till the x is lessthan  or equal to  than top. 
'''


#Task 2
def exp_by_hand(base, exp):
    next_exp = 1
    result = 1
    while next_exp <= exp:
        result = result * base 
        next_exp += 1
    return result 
    
 




'''Identify:
Control Variable: next_exp 
Initialization: next_exp=1
Modification:next_exp+=1
 return result

Describe the control: loop will calculate the exponential value of base and multiply till the loop is false and store the desire result.
    
'''


#PART 2: Write Your Own Function with Loops

#Task 3
def sum_divisors(n):
    divisor = 1
    result=1
    sum1=0
    while result<=n:
        
        if (n%result==0):
            divisor= result
            sum1+=divisor     
        result+=1        
    return sum1        
        



'''Identify:
Control Variable: result
Initialization: result=1
Modification: result+=1
Describe the control: till  result is less than or equal to n it will sum the divisor of n according to the condtion and store in sum.
'''