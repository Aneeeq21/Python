def tax_calculator(base_price, tax_percentage):
    tax_amount=base_price*(tax_percentage/100)
    return tax_amount
    
def travel_cost(miles):
    if miles>=50:
        a=3
    elif (miles>50) and (miles<=100):
        a=6
    elif (miles>100) and (miles<500):
        a=8
    elif (miles>=500) and (miles<=1000):
        a=10
    elif miles>1000:
        a=12
    
    
def odd_indices(some_list):
    my_list=[]
    for i in some_list:        
        if (i%2)==1:
            my_list.append(some_list.index(some_list[i]))
    return my_list       
           
            
            
    
    
    
    
        
        
        
        
        
    