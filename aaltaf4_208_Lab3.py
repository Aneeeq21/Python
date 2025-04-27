'''
-------------------------------------------------------------------------------
Name: <Aneeq Altaf>
Partner's Name: <Alexander Powell>
Assignment: Lab 3
Due by end of your lab class
-------------------------------------------------------------------------------
Honor Code Statement: I received no assistance on this assignment that
violates the ethical guidelines set forth by the professor and class syllabus.
-------------------------------------------------------------------------------
'''

# Part 1 -- Understanding Branching 

def branches_function():
    x = 1
    result = False
    if x==1:
        result = True
    return result

'''
Run the function above. What does it always return? Why?

Answer: it always return the same value because expression under if statement will always be false because 'and' operator requires both statment 
to be true but in expression one conditon is true and one false so if statment not executes so it will skip the block of statements
 and return the same  value(false).

Change the function so that it will always return True. Explain what you changed and why it will now always return True.

Answer: 
I changed the expression(condition) of if statement to 'equals to' operator and as expression of if statement is true so result will be equal to
true and it will always return value true.
'''

# Part 2 -- Writing Code with Branching
def categorize(item_price, num_units):
    if (item_price <= 10) and (num_units < 10):
        category = 'Low-priced'
    elif ((item_price <= 20) and (item_price>=10)) and (num_units < 20):
        category = 'Mid-priced'
    elif (item_price>20) and (num_units < 30):
        category = 'High-priced'
    elif (item_price > 20)  and (num_units >= 20):
        category = 'Premium'    
    else:
        category = 'Other'
    return category   
        
        