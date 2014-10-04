#get your averages and standard deviations here!! 
#10/3/14 9:59 pm, est -completed in one day! I wonder if I can get a GUI for this?

#for now, you can get both the average and standard deviation with one function.

def stddev():
    print ('how many numbers?')
    a = int(input())
    print ('please list your numbers')
    b=input()
    c=sum(float(number) for number in b.split(','))/a    #c is the average
    print (str(c) + ' is the average')
    a=list(float(number) for number in b.split(','))
    i=-1
    d=list(float(number)-c for number in b.split(','))
    i=-1
    e=list(float(number)**2 for number in d)
    f = math.sqrt((sum(e))/len(a))
    print( str(f) + ' is the standard deviation.')
    
#much thanks to stackoverflow for showing me how to make a generator to simplify things (i.e. float(x) for x in b.split(','))
