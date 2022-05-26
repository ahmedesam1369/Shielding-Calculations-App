from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

  
top = Tk()
top.title("simulation")
#top.minsize(640 , 400)
top.geometry("1000x620")

radio_arrival_distribution = IntVar()

radio_service_distribution = IntVar()

Label(text = 'Queuing System Simulation',
      font=('times new roman', 18, 'bold'), 
      bd=10, 
      fg="purple",).place(x=200, y=10, width=400, height=30)


F1 = LabelFrame(top, text="Choose Arrival distribution", 
                font=('times new roman', 16, 'bold'),
                bd=10, 
                fg="Black",)
F1.place(x=20, y=50, width=450, height=150)

R1 = Radiobutton(F1, text = 'Markovian', font=('times new roman', 14), bd=10,  fg="Black",
                 variable = radio_arrival_distribution ,
                 value = 1).grid(row=1,column=0, padx=4, pady=0, sticky='W')

Label(F1, text = 'Arrival rate',
      font=('times new roman', 12), 
      bd=10, 
      fg="Black",).grid(row=1,column=2, padx=2, pady=0, sticky='W', )
arrivalEntery = Entry(F1,width=6)
arrivalEntery.grid(row=1,column=3, padx=2, pady=0, sticky='W')
Label(F1, text = 'customer/minute',
      font=('times new roman',12),
      bd=10,
      fg="Black",).grid(row=1,column=4, padx=2, pady=0, sticky='W')


R2 = Radiobutton(F1, text = 'Deterministic', font=('times new roman', 14), bd=10,  fg="Black",
                 variable = radio_arrival_distribution ,
                 value = 2).grid(row=2,column=0, padx=4, pady=0, sticky='W')
Label(F1, text = 'Arrival rate',
      font=('times new roman', 12), 
      bd=10, 
      fg="Black",).grid(row=2,column=2, padx=2, pady=0, sticky='W', )
arrivalEntery2 = Entry(F1,width=6)
arrivalEntery2.grid(row=2,column=3, padx=2, pady=0, sticky='W')
Label(F1, text = 'customer/minute',
      font=('times new roman',12),
      bd=10,
      fg="Black",).grid(row=2,column=4, padx=2, pady=0, sticky='W')

F2 = LabelFrame(top, text="Choose Service distribution", 
                font=('times new roman', 16, 'bold'),
                bd=10, 
                fg="Black",)
F2.place(x=20, y=230, width=450, height=150)

R3 = Radiobutton(F2, text = 'Markovian', font=('times new roman', 14), bd=10,  fg="Black",
                 variable = radio_service_distribution ,
                 value = 1).grid(row=1,column=0, padx=4, pady=0, sticky='W')
Label(F2, text = 'Service rate',
      font=('times new roman', 12), 
      bd=10, 
      fg="Black",).grid(row=1,column=2, padx=2, pady=0, sticky='W', )
serviceEntery = Entry(F2,width=6)
serviceEntery.grid(row=1,column=3, padx=2, pady=0, sticky='W')
Label(F2, text = 'customer/minute',
      font=('times new roman',12),
      bd=10,
      fg="Black",).grid(row=1,column=4, padx=2, pady=0, sticky='W')


R4 = Radiobutton(F2, text = 'Uniform', font=('times new roman', 14), bd=10,  fg="Black",
                 variable = radio_service_distribution ,
                 value = 2).grid(row=2,column=0, padx=4, pady=0, sticky='W')
Label(F2, text = 'Arrival rate',
      font=('times new roman', 12), 
      bd=10, 
      fg="Black",).grid(row=2,column=2, padx=2, pady=0, sticky='W', )
serviceEntery2 = Entry(F2,width=6)
serviceEntery2.grid(row=2,column=3, padx=2, pady=0, sticky='W')
Label(F2, text = 'customer/minute',
      font=('times new roman',12),
      bd=10,
      fg="Black",).grid(row=2,column=4, padx=2, pady=0, sticky='W')



Label(text = 'Simulation Time',
      font=('times new roman', 14), 
      bd=10, 
      fg="Black",).place(x=20, y=420, width=200, height=25)
SimulationTimeEntery = Entry()
SimulationTimeEntery.place(x=200, y=420, width=70, height=25)
Label(text = 'minute',
      font=('times new roman', 12), 
      bd=10, 
      fg="Black",).place(x=280, y=410, width=100, height=50)

def simulate():
    print("Hello")
    print(radio_arrival_distribution.get())
    print(arrivalEntery2.get())
    
    Label(text ='Utilization factor of the system = '+str(1212)+'\n \n'+
          'Mean response time = '+str(15)+'\n \n'+
          'Average wait in queue Wq = '+str(121)+'\n \n'+
          'Proportion of customer spend >= 4 min is '+str(56515)+'\n \n'+
          'Max Queue length = '+str(515),
      font=('times new roman', 15), 
      bd=10, 
      justify= LEFT ,  
      fg="Black",).place(x=500, y=70, width=400, height=280)


Button(text = 'Simulate    ',
       font=('times new roman', 15, 'bold'), 
       bd=10, fg="Black",
       command = simulate ).place(x=80, y=490, width=200, height=60)


# Other Side
F3 = LabelFrame(top, text="Specifications", 
                font=('times new roman', 16, 'bold'),
                bd=10, 
                fg="Black",)
F3.place(x=490, y=50, width=460, height=350)


# y = x^2    
def plot():
    f, a = plt.subplots(1, 1)
    house_prices = np.random.normal(0., 1, 1000)
    a.hist(house_prices)
    plt.show()
  
   
  
    
  
plot_button = Button(master = top, 
                     command = plot,
                     bd=10, fg="Black",

                     text = "Plot",
                     font=('times new roman', 15, 'bold'), 
                     )
plot_button.place(x=320, y=500, width=100, height=40)

     
top.mainloop()


  
