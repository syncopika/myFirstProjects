#get your averages and standard deviations here!! 
#10/3/14 9:59 pm, est -completed in one day! I wonder if I can get a GUI for this?

#for now, you can get both the average and standard deviation with one function.

#10/4/14 12:58 pm, est - added import math (important!->but i guess you could also just multiply f like this-> **(1/2) and take out math.sqrt), also took away i=-1 which I was going to use if my while loops worked. 

import math 

def stddev():
    print ('how many numbers?')
    a = int(input())
    print ('please list your numbers')
    b=input()
    c=sum(float(number) for number in b.split(','))/a    #c is the average
    print (str(c) + ' is the average')
    a=list(float(number) for number in b.split(','))
    d=list(float(number)-c for number in b.split(','))
    e=list(float(number)**2 for number in d)
    f = math.sqrt((sum(e))/len(a))
    print( str(f) + ' is the standard deviation.')
    
#much thanks to stackoverflow for showing me how to make a generator to simplify things (i.e. float(x) for x in b.split(','))
