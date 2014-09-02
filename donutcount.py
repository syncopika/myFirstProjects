#calculating donuts - for minimum price  9/1/14 6:20 pm, est

from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Calculating Best Price")
root.wm_iconbitmap('favicon.ico')

#code for the calculating
def donutCost():
    try:
        people=int(numberOfPeople.get())
        donuts=int(donutsPerPerson.get())
        T = people*donuts;
        lb=int(T/40);
        rem1= T-(40*lb);
        mb = int(rem1/20);
        rem2= T-(40*lb)-(20*mb);
        sb = int(rem2/10);
        i = T-(40*lb)-(20*mb)-(10*sb)
        #for if T>=40
        if T%40 == 0:
            result.set("You need " + str(lb) + " large boxes if everyone eats 5, which will cost " + str(lb*6.19))
        elif float(T/40) >= 1 and float(rem1)%20 == 0:
            result.set("You need " + str(lb)+ " large boxes and " + str(mb) + " medium boxes.")
        elif float(T/40) >= 1 and float(rem1/20) >=1 and rem2<10:
            result.set("You need " + str(lb)+ " large boxes and " + str(mb) + " medium boxes, and " + str(i)+ " inividual pieces.")
        elif float(T/40) >= 1 and float(rem1/20) >= 1 and  float(rem2%10) == 0:
            result.set("You need " + str(lb)+ " large boxes, " + str(mb) + " medium boxes, and " + str(sb) + " small boxes.")
        elif float(T/40) >= 1 and float(rem2/10) >= 1 and float(rem1/20) >= 1 and 0<i<10:
            result.set("You need " + str(lb)+ " large boxes, " + str(mb) + " medium boxes, and " + str(sb) + " small boxes, and "+ str(i)+" individual pieces.")
        elif float(T/40) >= 1 and 10<rem1<20:
            result.set("You need " + str(lb) + " large boxes and " + str(sb) + " small boxes, and " + str(i) + " individual pieces.")
        elif float(T/40) >= 1 and rem1 == 10:
            result.set("You need " + str(lb) + " large boxes and 1 small box.")
        elif float(T/40) >=1 and rem1<10:
            result.set("You need " + str(lb) + " large boxes and " + str(i) + " individual pieces.")
        #for if T<40
        elif T%20 == 0 and 20<=T<40:
            result.set("You need " + str(mb) + " medium boxes.")
        elif 20<=T<40 and float(T/20) >= 1 and float(rem2)%10 == 0:
            result.set("You need " + str(mb) + " medium boxes and " + str(sb) + " small boxes.")
        elif 20<=T<40 and float(T/20) >=1 and 1<=i<10:
            result.set("You need " + str(mb) + " medium boxes, " + str(sb)+ " small boxes and " + str(i)+ " individual pieces.")
        elif 10<T<20:
            result.set("You need " + str(sb) + " small boxes and " + str(i)+ " individual pieces.")
        elif T==10:
            result.set("You need 1 small box.")
        elif 0<T<10:
            result.set("You need " + str(T) + " individual pieces.")
        else:
            result.set('Sorry- does not compute')
    except ValueError:
        pass

#binds Enter key pressing with executing the function
def onclick(event=None):
    donutCost()
    
    
#here comes the GUI
mainframe = ttk.Frame(root, padding="18 15 18 15")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

numberOfPeople = StringVar()
donutsPerPerson = StringVar()
result = StringVar()

numberOfPeople_entry = ttk.Entry(mainframe, width=5, textvariable=numberOfPeople)
donutsPerPerson_entry = ttk.Entry(mainframe, width=5, textvariable=donutsPerPerson)
numberOfPeople_entry.grid(column=2, row=1, sticky=(W,E))
donutsPerPerson_entry.grid(column=2, row=2, sticky=(W,E))
ttk.Label(mainframe, textvariable=result).grid(column=2, row=3, sticky=W)
ttk.Button(mainframe, text="Calculate!", command=donutCost).grid(column=3, row=3, sticky=E)

ttk.Label(mainframe, text="number of people:").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="numer of donuts per person:").grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text="result:").grid(column=1, row=3, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=3, pady=3)
numberOfPeople_entry.focus()
root.bind('<Return>', onclick)

root.mainloop();
