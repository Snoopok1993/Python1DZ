#def square (side_square):
   
    #side_square = 2.8

    #area = side_square ** 2

    #return (area)


#print ("Площадь квадрата =",square ("area" ))

import math as m

def square (side):

    side = 22.4

    
    area = side **2

    if side == int:

        return area 
    
    else:

        return  m.ceil (side **2)
    

print ("Площадь квадрата:",square ("area"))