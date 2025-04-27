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
    first_letter=str1[0]
    middle_index=(len(str1)-1)//2
    if len(str1)<=3:
        middle_letters=''
    elif len(str1)%2==0:
        middle_letters=str1[middle_index]+str1[middle_index+1]
    else:
        middle_letters=str1[middle_index]
    last_letter=str1[-1]
    full=first_letter+middle_letters+last_letter 
    return full
        



#Part 2 -- Reading from and Writing to File 
def pythagorean_theorem(file1):
    file2=open(file1, 'r')
    file3=open('result.txt', 'w')
    file2.readline()
    j=file2.readlines()
    for i in j:
        z=i.split(',')
        
        '''if type(z[0])!=type(3):
            continue
        else:'''
        a=float(z[0])
        b=float(z[1])
        c=round((a*a)+(b*b), 2)
        file3.write(f'If a = {a} and b = {b}, then c squared = {c}\n')
            
    
    file3.close()
    file2.close()    
        
        


