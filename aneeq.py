'''
-------------------------------------------------------------------------------
Name: <Aneeq Altaf>
Partner's Name: <Gia Pham>
Assignment: Lab 1
Due by end of your lab class
-------------------------------------------------------------------------------
Honor Code Statement: I received no assistance on this assignment that
violates the ethical guidelines set forth by the professor and class syllabus.
-------------------------------------------------------------------------------
'''

'''
Write out the algorithm (your plan) for the task:

Step 1: assign variables with their statements
Step2: read values
Step 3:output
...
...


'''


#Type your code below:
def triangular_cookies(no_of_boxes):
        labour_cost = no_of_boxes * ((20 * 6) + (25.50 * 2))
        total_cost = labour_cost + 10 
        print('\n***Triangular Cookies***\n' )
        print(f'Labor Cost: ${labour_cost:.2f}')
        print(f'Total Cost: ${total_cost:.2f}')
        return total_cost
        

def oval_cookies(noo_of_boxes):
    labor_cost = noo_of_boxes * ((20 * 7) + (25.50 * 3))
    totel_cost = labor_cost + 12
    print('\n***Oval Cookies***\n')
    print(f'Labor Cost: ${labor_cost:.2f}')
    print(f'Total Cost: ${totel_cost:.2f}')
    return totel_cost
    
def square_cookies(no_boxes):
    lab_cost = no_boxes * ((20*5) + (25.50*4))
    tot_cost = lab_cost + 13 
    print('\n***Square Cookies***\n')
    print(f'Labor Cost: ${lab_cost:.2f}')
    print(f'Total Cost: ${tot_cost:.2f}')
    return tot_cost
    
def charge_order(no_of_box, dev_charge):
    a = (triangular_cookies(no_of_box) * (110/100)) + dev_charge
    print(f'Charge for Order: ${a:.2f}')
    b = (oval_cookies(no_of_box) * (110/100)) + dev_charge
    print(f'Charge for Order: ${b:.2f}')
    c = (square_cookies(no_of_box) * (110/100)) + dev_charge
    print(f'Charge for Order: ${c:.2f}')
    
print('Welcome to Ava\'s Home made Decorated Cookies!\n')
box = int(input('No. of Boxes: '))
charge = float(input('Delivery Charge: '))
charge_order(box, charge)
  
    
    
    
    
    
 
    






 

