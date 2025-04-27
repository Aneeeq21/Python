'''
-------------------------------------------------------------------------------
Name: Aneeq Altaf
Assignment: PA 6
Due Date: 11/25/2024
-------------------------------------------------------------------------------
Honor Code Statement: I received no assistance on this assignment that
violates the ethical guidelines set forth by the professor and class syllabus.
-------------------------------------------------------------------------------
'''

#In this function i read the file and then split it with , then with 1 iteration append the name if score value matches.
def get_students_by_score(score_file, score):
    score2=open(score_file, 'r')
    a=[]            
    score2.readline() 
    j=score2.readlines()
    
    for i in j:
        z=i.split(',')
        c=int(z[2])
        d=z[0]
        if c==score:
            a.append(d)
    score2.close()            
##returning to the function in variable a        
    return a


'''In this function I read the file and then split with respect to ',' then with on iteration I check the first age and calculated avg of scores
with age above the criteria'''
def filter_score_by_age(score_file, age_threshold):
    score2=open(score_file, 'r')
    c=0
    num=0    
    score2.readline() 
    j=score2.readlines()
    for i in j:
        z=i.split(',')
        age=int(z[1])
        scores=int(z[2])
        if age>age_threshold:
            num+=1
            c+=scores
    avg1=round(c/num, 2)
##returning to the function in variable avg1    
    return avg1
    
    
    


'''In this function first I read the file and then split it with , then i check the student name if student name found then add
the score of student and id of student  and return in the end'''

def gather_id_score(gpa_file, score_file, student_name):
    score2=open(score_file, 'r')
    score3=open(gpa_file, 'r')      
    score2.readline() 
    score3.readline()
    j=score2.readlines()
    k=score3.readlines()
    student_id=''
    for i in j:
        z=i.split(',')
        name=z[0]
        score5=int(z[2])
        if student_name==name:
            score=score5
    for line in k:
        m=line.split(',')
        name1=m[1]
        id1=m[0]
        if student_name==name1:
            student_id=id1
##returning to the function in 2 variables student_id and score          
    return (student_id, score)


'''In this function I do the exception handling if the file is present then no execption handling else throw exception. and if file is found
 then first read  first line to create dictionary with key as coloumn of file and append the values in list in its repective order and 
 return in end'''
def file_to_dict(filename):
    try:
        score2=open(filename, 'r')
        my_dict={}
        b=[]
        c=[]
        e=[]
        z=score2.readline()
        y=z.strip().split(',')
        
        j=score2.readlines()
        for i in j:
            m=i.strip().split(',')
            b.append(m[0])
            c.append(m[1])
            e.append(m[2])
        my_dict[y[0]]=b
        my_dict[y[1]]=c
        my_dict[y[2]]=e    
            
        score2.close()
        
    except FileNotFoundError:
        return "The file " +  filename +' does not exist'
    
    
    
##return to the function in my_dict variable    
    return my_dict


'''In this function it checks for the exception handling for different errors and it also do functionality for maximum number
 in a given column via for loop'''
def find_max(filename, column_name):
    score=0
    my_dict=file_to_dict(filename)
    if column_name in my_dict:
        for i in my_dict[column_name]:
            try:
                j=float(i)
                if (score==0) or (score<j):             
                    score=j
##returning to function non numberic execption
            except ValueError:
                return "Non-numeric value found in column "+ column_name
 ##returning to function col not found               
    else:
        return "Column "+ column_name+" not found in file"
        
        
                
            
            
        
    
##returning to function the score    
    return score
