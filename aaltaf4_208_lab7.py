'''
-------------------------------------------------------------------------------
Name: Aneeq Altaf
Partner's Name: Laith Muwakki
Assignment: Lab 7
Due by end of your lab class
-------------------------------------------------------------------------------
Honor Code Statement: I received no assistance on this assignment that
violates the ethical guidelines set forth by the professor and class syllabus.
-------------------------------------------------------------------------------
'''

#Part 1 -- Identify mistakes and fix the code

#Task 1

#Mistakes: the mistake was function is not iterating in correct list. and if statement is needed to check whether item to be purchased is in dictionary.

#Write fixed code here
def total_cost(dictionary, cart):
    total = 0
    for item in cart:
        if item in dictionary:
                cost=dictionary[item]
                total += cost
        
    return round(total, 2)


#Task 2

#Mistakes:'$' sign was missing maxx wasnt initialized first and it was directly put into if statement. in result declaration maxx was not converted to string. 

#Write fixed code here
def most_expensive(dictionary):
    max_item = ''
    maxx=0
    for item in dictionary:
        if dictionary[item] > maxx:
            max_item = item
            maxx = dictionary[item]
    result = "The most expensive item in the store is " + str(max_item) + " and costs " +"$"+ str(maxx) + "."
    return result



# Part 2 -- Write your own function with dictionaries 

#Task 3

#write code here
def big_cities(dictionary, threshold):
    list1=[]
    for item in dictionary:
        if dictionary[item]>=threshold:
            list1.append(item)
            
    return list1
#Task 4

#write code here
def vacation_destinations(places):
    result1={}
    for place in range(len(places)):
        new1=places[place][0]
        new2=places[place][1:]
        result1[new1]=new2
            
    return result1
