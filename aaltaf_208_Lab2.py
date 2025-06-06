'''
-------------------------------------------------------------------------------
Name: <Aneeq Altaf>
Partner's Name: <Alexander Powell>
Assignment: Lab 2
Due by end of your lab class
-------------------------------------------------------------------------------
Honor Code Statement: I received no assistance on this assignment that
violates the ethical guidelines set forth by the professor and class syllabus.
-------------------------------------------------------------------------------
'''

#Partner A -- write area_of_base function here
def area_of_base(length):
    area_of_square = length * length
    Area_of_square = round(area_of_square, 4)
    return Area_of_square


#Partner B -- write area_of_side function here
def area_of_side(base_length, height):
    Side_area= base_length * height * (1/2)
    side_area = round(Side_area, 4)
    return side_area


#Write pyramid_surface_area function to calculate surface area of pyramid here
def pyramid_surface_area(base_length, slant_height):
    Surface_area = area_of_base(base_length) + (4*area_of_side(base_length, slant_height))
    surface_area = round(Surface_area, 4)
    return surface_area
    


#Write pyramid_volume function to calculate the volume of the pyramid (and any other functions you make) here
def pyramid_volume(len_base, height):
    Volume = (1/3) * area_of_base(len_base) * height
    volume = round(Volume, 4)
    return volume
