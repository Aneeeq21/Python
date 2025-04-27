def slash(height):
    gap=height-1
    str1=''
    for i in range(height):
        str1=str1+(' '*gap)+'*'+'\n'
        gap-=1
    
    return str1


def make_dict(key_lst, val_tuple):
    my_dict={}
    j=list(val_tuple)
    z=0
    if len(key_lst)==0:
        return my_dict
    else:
        for i in key_lst:
            my_dict[i]=j[z]
            z+=1
    return my_dict


def get_unique(pos_list, def_dict = {}):
    my_list=[]
    for i in pos_list:
        for j in i:
            if j in def_dict.values():
                a=0
            else:
                if j in my_list:
                    a=1
                else:
                    my_list.append(j)
            
            
        
            
    
    return my_list
