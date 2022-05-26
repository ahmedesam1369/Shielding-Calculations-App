import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import numpy as np


root = Tk()

root.title('Shielding Calculator')

root.geometry("1013x670")


Label(text = 'Primary and Secondary Barriers',
      font=('times new roman', 16, 'bold'), 
      bd=10, 
      fg="purple",).place(x=240, y=10, width=400, height=30)

F1 = LabelFrame(root, 
                font=('times new roman', 16, 'bold'),
                bd=10, 
                fg="Black",)
F1.place(x=20, y=50, width=430, height=600)


Label(F1, text = 'Number of Patient/day (W) ',
      font=('times new roman', 12), 
      bd=10, 
      fg="Black",).grid(row=1,column=1, padx=2, pady=0, sticky='W', )

num_of_patient = Entry(F1, width=20)
num_of_patient.grid(row=1,column=2, padx=2, pady=0, sticky='W')

Label(F1, text = 'Dose Per Patient',
      font=('times new roman', 12), 
      bd=10, 
      fg="Black",).grid(row=2,column=1, padx=2, pady=0, sticky='W', )
dose_per_patient = Entry(F1, width=20)
dose_per_patient.grid(row=2,column=2, padx=2, pady=0, sticky='W')
Label(F1, text = 'Gy/Pt',
      font=('times new roman', 12), 
      bd=10, 
      fg="Black",).grid(row=2,column=3, padx=2, pady=0, sticky='W', )



def display_selected(choice):
    choice = energy_variable.get()
    print(choice)
Label(F1, text = 'Choose Energy (MV)',
      font=('times new roman', 12), 
      bd=10, 
      fg="Black",).grid(row=3,column=1, padx=2, pady=0, sticky='W', )

energy = ['6 MV','18 MV', '24 MV']

energy_variable = StringVar()
energy_variable.set('Energy')
dropdown = OptionMenu(
    F1,
    energy_variable,
    *energy,
    command=display_selected
)
dropdown.config(width=14)
dropdown.config(height=1)
dropdown.config(bg='light blue')
dropdown.grid(row=3,column=2,padx=2, pady=0, sticky='W')



def display_selected2(choice):
    choice = occupancy_variable.get()
    print(choice)
Label(F1, text = 'Occupancy Factor (T)',
      font=('times new roman', 12), 
      bd=10, 
      fg="Black",).grid(row=4,column=1, padx=2, pady=0, sticky='W', )

occupancy = ['1','1/4', '1/16']

occupancy_variable = StringVar()
occupancy_variable.set('Occupancy Factor')
dropdown = OptionMenu(
    F1,
    occupancy_variable,
    *occupancy,
    command=display_selected2
)
dropdown.config(width=14)
dropdown.config(height=1)
dropdown.config(bg='light blue')
dropdown.grid(row=4,column=2,padx=2, pady=0, sticky='W')

Label(F1, text = 'Usage Factor (U)',
      font=('times new roman', 12), 
      bd=10, 
      fg="Black",).grid(row=5,column=1, padx=2, pady=0, sticky='W', )
usage_factor = Entry(F1, width=20)
usage_factor.grid(row=5,column=2, padx=2, pady=0, sticky='W')


Label(F1, text = 'Distance (d)',
      font=('times new roman', 12), 
      bd=10, 
      fg="Black",).grid(row=6,column=1, padx=2, pady=0, sticky='W', )
distance = Entry(F1, width=20)
distance.grid(row=6,column=2, padx=2, pady=0, sticky='W')
Label(F1, text = 'm',
      font=('m', 12), 
      bd=10, 
      fg="Black",).grid(row=6,column=3, padx=2, pady=0, sticky='W', )


   
Label(F1, text = 'Shielding Material',
      font=('times new roman', 12), 
      bd=10, 
      fg="Black",).grid(row=7,column=1, padx=2, pady=0, sticky='W', )
concrete = IntVar()
steal = IntVar()
lead = IntVar()
Checkbutton(F1, text="Concrete",font=('times new roman', 12), fg="Black", bd=0, 
            variable=concrete).grid(row=8,column=1, padx=0, pady=0,  )
Checkbutton(F1, text="Steal",font=('times new roman', 12), fg="Black", bd=10, 
            variable=steal).grid(row=8,column=2, padx=0, pady=0,)
Checkbutton(F1, text="Lead",font=('times new roman', 12), fg="Black", bd=10, 
            variable=lead).grid(row=8,column=3, padx=0, pady=0, )


Label(F1, text = 'Type of area',
      font=('times new roman', 12), 
      bd=10, 
      fg="Black",).grid(row=9,column=1, padx=2, pady=0, sticky='W', )
radio_area_type = IntVar()
R1 = Radiobutton(F1, text = 'Controlled', font=('times new roman', 12), bd=5,  fg="Black",
                 variable = radio_area_type ,
                 value = 1).grid(row=10,column=1, padx=40, pady=0, sticky='W')
R2 = Radiobutton(F1, text = 'UnControlled', font=('times new roman', 12), bd=5,  fg="Black",
                 variable = radio_area_type ,
                 value = 2).grid(row=10,column=2, padx=0, pady=0, sticky='W')

Label(F1, text = 'IMRT',
      font=('times new roman', 12), 
      bd=10, 
      fg="Black",).grid(row=11,column=1, padx=2, pady=0, sticky='W', )
imrt = Entry(F1, width=20)
imrt.grid(row=11,column=2, padx=2, pady=0, sticky='W')
Label(F1, text = '%',
      font=('times new roman', 12), 
      bd=10, 
      fg="Black",).grid(row=11,column=3, padx=2, pady=0, sticky='W', )

Label(F1, text = 'DeModulation Factor (C)',
      font=('times new roman', 12), 
      bd=10, 
      fg="Black",).grid(row=12,column=1, padx=2, pady=0, sticky='W', )
demodulation_factor = Entry(F1, width=20)
demodulation_factor.grid(row=12,column=2, padx=2, pady=0, sticky='W')
Label(F1, text = '2:10',
      font=('times new roman', 12), 
      bd=10, 
      fg="Black",).grid(row=12,column=3, padx=2, pady=0, sticky='W', )


F2 = LabelFrame(root, 
                font=('times new roman', 16, 'bold'),
                bd=10, 
                fg="Black",)
F2.place(x=460, y=50, width=520, height=250)

img = ImageTk.PhotoImage(Image.open("myimage9.jpg"))

Label_img = Label(F2, image = img)
Label_img.pack()

ds_iso = 1
# fmax = 0.75*0.75
fmax = 3.53

patient_per_day_val = 1
dose_perpatient_val = 1
energy_val = 1
occupancy_val = 1
usage_factor_val =1
distance_val = 1
p_controlled_uncontrolled = 1
imrt_val = 1
deModulation_val = 1
alpha = 1
n = 1
n_secondary = 1

def update_values():
    global patient_per_day_val, dose_perpatient_val, deModulation_val
    global energy_val, occupancy_val, imrt_val, alpha
    global usage_factor_val, distance_val, p_controlled_uncontrolled, n, n_secondary
    
    patient_per_day_val = float(num_of_patient.get())
    dose_perpatient_val = float(dose_per_patient.get())
    if(energy_variable.get() == '6 MV'):
        energy_val = 6
    elif(energy_variable.get() == '18 MV'):
        energy_val = 18
    elif(energy_variable.get() == '24 MV'):
        energy_val = 24
    
    if(occupancy_variable.get() == '1'):
        occupancy_val = 1
    elif(occupancy_variable.get() == '1/4'):
        occupancy_val = 1/4
    elif(occupancy_variable.get() == '1/16'):
        occupancy_val = 1/16   
    
    usage_factor_val = float(usage_factor.get())
    distance_val = float(distance.get())
    
    if(radio_area_type.get() == 1):
        p_controlled_uncontrolled = 0.1
    elif(radio_area_type.get() == 2):
        p_controlled_uncontrolled = 0.02
        
    imrt_val = float(imrt.get())
    deModulation_val = float(demodulation_factor.get())
    
    if(energy_val == 6):
        alpha = 0.000426
    elif(energy_val == 18):
        alpha = 0.000189
    elif(energy_val == 24):
        alpha = 0.000174
    
    # Primary
    workload = patient_per_day_val * dose_perpatient_val * 270 *1000 # mSV/Year
    B = (p_controlled_uncontrolled *((distance_val)**2)) / (workload * usage_factor_val * occupancy_val)
    n = np.log10(1/B) 
    # Secondary
    workload_leakage = (workload*deModulation_val*(imrt_val/100)) + (workload*((1-imrt_val)/100))
    B_leakage = (p_controlled_uncontrolled * ((distance_val)**2)) / ((10**-3) * workload_leakage * occupancy_val)
    B_scatter = ((p_controlled_uncontrolled*((ds_iso)**2)*((distance_val)**2)*400) / 
                                        (alpha * workload_leakage * occupancy_val * fmax))
    B_max = max(B_leakage, B_scatter)
    n_secondary = np.log10(1/B_max) 
                                                
conc_thick_prim = 0
conc_cost_prim = 0
conc_thick_sec = 0
conc_cost_sec = 0
con_6=[0.350, 0.350]
con_18=[0.470, 0.430]
con_24=[0.510, 0.460]
    
def concrete_calc():
    global conc_lbl1, conc_lbl2, conc_lbl3, conc_lbl4
    global conc_thick_prim, conc_cost_prim, conc_thick_sec, conc_cost_sec
        
    if(energy_val == 6):
        conc_thick_prim = con_6[0] + (n -1 )* con_6[1]
        conc_cost_prim = conc_thick_prim * 39.3701  
        conc_thick_sec =  con_6[0] + (n_secondary -1 )* con_6[1]
        conc_cost_sec = conc_thick_sec * 39.3701  
    if(energy_val == 18):
        conc_thick_prim = con_18[0] + (n -1 )* con_18[1]
        conc_cost_prim = conc_thick_prim * 39.3701
        conc_thick_sec =  con_18[0] + (n_secondary -1 )* con_18[1]
        conc_cost_sec = conc_thick_sec * 39.3701  
    if(energy_val == 24):
        conc_thick_prim = con_24[0] + (n -1 )* con_24[1]
        conc_cost_prim = conc_thick_prim * 39.3701
        conc_thick_sec =  con_24[0] + (n_secondary -1 )* con_24[1]
        conc_cost_sec = conc_thick_sec * 39.3701 
        
    conc_lbl1 = Label(F3, text = f'{np.round(conc_thick_prim, 2)} m',anchor="center",font=('times new roman', 15), bd=10, fg="Black")
    conc_lbl1.grid(row=3,column=2, padx=2, pady=0 ) 
    conc_lbl2 = Label(F3, text = f'{int(np.round(conc_cost_prim))} $',anchor="center",font=('times new roman', 15), bd=10, fg="Black",)
    conc_lbl2.grid(row=3,column=3, padx=2, pady=0 ) 
    conc_lbl3 = Label(F3, text = f'{np.round(conc_thick_sec, 2)} m',anchor="center",font=('times new roman', 15), bd=10, fg="Black",)
    conc_lbl3.grid(row=3,column=4, padx=2, pady=0 ) 
    conc_lbl4 = Label(F3, text = f'{int(np.round(conc_cost_sec))} $',anchor="center",font=('times new roman', 15), bd=10, fg="Black",)
    conc_lbl4.grid(row=3,column=5, padx=2, pady=0 ) 
        
    
 
steal_thick_prim = 0
steal_cost_prim = 0
steal_thick_sec = 0
steal_cost_sec = 0
steel_6=[0.099,0.099]
steel_18=[0.108,0.108]
steel_24=[0.109,0.109]

             
def steal_calc():
    global steal_lbl1, steal_lbl2, steal_lbl3, steal_lbl4
    global steal_thick_prim, steal_cost_prim, steal_thick_sec, steal_cost_sec
        
    if(energy_val == 6):
        steal_thick_prim = steel_6[0] + (n -1 )* steel_6[1]
        steal_cost_prim = steal_thick_prim * 39.3701 * 80 
        steal_thick_sec =  steel_6[0] + (n_secondary -1 )* steel_6[1]
        steal_cost_sec = steal_thick_sec * 39.3701  *80
    if(energy_val == 18):
        steal_thick_prim = steel_18[0] + (n -1 )* steel_18[1]
        steal_cost_prim = steal_thick_prim * 39.3701 * 80 
        steal_thick_sec =  steel_18[0] + (n_secondary -1 )* steel_18[1]
        steal_cost_sec = steal_thick_sec * 39.3701  *80
    if(energy_val == 24):
        steal_thick_prim = steel_24[0] + (n -1 )* steel_24[1]
        steal_cost_prim = steal_thick_prim * 39.3701 * 80 
        steal_thick_sec =  steel_24[0] + (n_secondary -1 )* steel_24[1]
        steal_cost_sec = steal_thick_sec * 39.3701  *80
        
    steal_lbl1 = Label(F3, text = f'{np.round(steal_thick_prim, 2)} m',anchor="center",font=('times new roman', 15), bd=10, fg="Black",)
    steal_lbl1.grid(row=4,column=2, padx=2, pady=0 ) 
    steal_lbl2 = Label(F3, text = f'{int(np.round(steal_cost_prim))} $',anchor="center",font=('times new roman', 15), bd=10, fg="Black",)
    steal_lbl2.grid(row=4,column=3, padx=2, pady=0 ) 
    steal_lbl3 = Label(F3, text = f'{np.round(steal_thick_sec, 2)} m',anchor="center",font=('times new roman', 15), bd=10, fg="Black",)
    steal_lbl3.grid(row=4,column=4, padx=2, pady=0 ) 
    steal_lbl4 = Label(F3, text = f'{int(np.round(steal_cost_sec))} $',anchor="center",font=('times new roman', 15), bd=10, fg="Black",)
    steal_lbl4.grid(row=4,column=5, padx=2, pady=0 ) 
        
        
    
                   
        
lead_thick_prim = 0
lead_cost_prim = 0
lead_thick_sec = 0
lead_cost_sec = 0      

lead_6=[0.055,0.057]

def lead_calc():
    global lead_lbl1, lead_lbl2, lead_lbl3, lead_lbl4
    global lead_thick_prim, lead_cost_prim, lead_thick_sec, lead_cost_sec
        
    if(energy_val == 6):
        lead_thick_prim = lead_6[0] + (n -1 )* lead_6[1]
        lead_cost_prim = lead_thick_prim * 39.3701  * 200
        lead_thick_sec =  lead_6[0] + (n_secondary -1 )* lead_6[1]
        lead_cost_sec = lead_thick_sec * 39.3701  *200
    if(energy_val == 18):
        lead_thick_prim = lead_6[0] + (n -1 )* lead_6[1]
        lead_cost_prim = lead_thick_prim * 39.3701  * 200
        lead_thick_sec =  lead_6[0] + (n_secondary -1 )* lead_6[1]
        lead_cost_sec = lead_thick_sec * 39.3701  *200
    if(energy_val == 24):
        lead_thick_prim = lead_6[0] + (n -1 )* lead_6[1]
        lead_cost_prim = lead_thick_prim * 39.3701  * 200
        lead_thick_sec =  lead_6[0] + (n_secondary -1 )* lead_6[1]
        lead_cost_sec = lead_thick_sec * 39.3701  *200
        
    lead_lbl1 = Label(F3, text = f'{np.round(lead_thick_prim, 2)} m',anchor="center",font=('times new roman', 15), bd=10, fg="Black",)
    lead_lbl1.grid(row=5,column=2, padx=2, pady=0 ) 
    lead_lbl2 = Label(F3, text = f'{int(np.round(lead_cost_prim))} $',anchor="center",font=('times new roman', 15), bd=10, fg="Black",)
    lead_lbl2.grid(row=5,column=3, padx=2, pady=0 ) 
    lead_lbl3 = Label(F3, text = f'{np.round(lead_thick_sec, 2)} m',anchor="center",font=('times new roman', 15), bd=10, fg="Black",)
    lead_lbl3.grid(row=5,column=4, padx=2, pady=0 ) 
    lead_lbl4 = Label(F3, text = f'{int(np.round(lead_cost_sec))} $',anchor="center",font=('times new roman', 15), bd=10, fg="Black",)
    lead_lbl4.grid(row=5,column=5, padx=2, pady=0 ) 
        
    
                   


clear_validate = 1

def get_clear_validate():
    return clear_validate
def set_clear_validate(val):
    global clear_validate
    clear_validate = val 

def calc():
    if( energy_variable.get() == 'Energy' or occupancy_variable.get() == 'Occupancy Factor' or
               num_of_patient.get()=="" or dose_per_patient.get()=="" or 
               usage_factor.get() =="" or distance.get()=="" or
               imrt.get()=="" or demodulation_factor.get()==""or
               radio_area_type.get()==0 ):
                messagebox.showwarning("warning","Please Enter All inputs to continue")
    else:
        update_values()
        
    
    if (get_clear_validate() == 1): 
        set_clear_validate(0)    
        global lbl1
        global lbl2
        global lbl3
        
        if(concrete.get() == 1 and steal.get() == 0 and lead.get() ==0):
            concrete_calc()
            
            lbl1 = Label(F3, text = 'Concrete',
                font=('times new roman', 15,'bold'), bd=10, 
                fg="Black",)
            lbl1.grid(row=3,column=1, padx=0, pady=0, sticky='W', )
            
        
        elif(concrete.get() == 0 and steal.get() == 1 and lead.get() ==0): 
            steal_calc()
            
            lbl2 = Label(F3, text = 'Steal',
                  font=('times new roman', 15,'bold'), bd=10, 
                  fg="Black",)
            lbl2.grid(row=4,column=1, padx=0, pady=0, sticky='W', )
            
        
        elif(concrete.get() == 0 and steal.get() == 0 and lead.get() ==1):
            lead_calc()
            
            lbl3 = Label(F3, text = 'Lead',
              font=('times new roman', 15,'bold'), bd=10, 
              fg="Black",)
            lbl3.grid(row=5,column=1, padx=0, pady=0, sticky='W', )
            
        
        elif(concrete.get() == 1 and steal.get() == 1 and lead.get() ==0):
            concrete_calc()
            steal_calc()
            
            lbl1 = Label(F3, text = 'Concrete',
                font=('times new roman', 15,'bold'), bd=10, 
                fg="Black",)
            lbl1.grid(row=3,column=1, padx=0, pady=0, sticky='W', )
            lbl2 = Label(F3, text = 'Steal',
                  font=('times new roman', 15,'bold'), bd=10, 
                  fg="Black",)
            lbl2.grid(row=4,column=1, padx=0, pady=0, sticky='W', )
            
            
        
        elif(concrete.get() == 1 and steal.get() == 0 and lead.get() ==1):
            concrete_calc()
            lead_calc()
            
            lbl1 = Label(F3, text = 'Concrete',
                font=('times new roman', 15,'bold'), bd=10, 
                fg="Black",)
            lbl1.grid(row=3,column=1, padx=0, pady=0, sticky='W', )
            lbl3 = Label(F3, text = 'Lead',
              font=('times new roman', 15,'bold'), bd=10, 
              fg="Black",)
            lbl3.grid(row=5,column=1, padx=0, pady=0, sticky='W', )
            
        
        elif(concrete.get() == 0 and steal.get() == 1 and lead.get() ==1):
            steal_calc()
            lead_calc()
            
            lbl2 = Label(F3, text = 'Steal',
                  font=('times new roman', 15,'bold'), bd=10, 
                  fg="Black",)
            lbl2.grid(row=4,column=1, padx=0, pady=0, sticky='W', )
            lbl3 = Label(F3, text = 'Lead',
              font=('times new roman', 15,'bold'), bd=10, 
              fg="Black",)
            lbl3.grid(row=5,column=1, padx=0, pady=0, sticky='W', )
    
        elif(concrete.get() == 1 and steal.get() == 1 and lead.get() ==1):
            concrete_calc()
            steal_calc()
            lead_calc()
            
            lbl1 = Label(F3, text = 'Concrete',
                font=('times new roman', 15,'bold'), bd=10, 
                fg="Black",)
            lbl1.grid(row=3,column=1, padx=0, pady=0, sticky='W', )
            lbl2 = Label(F3, text = 'Steal',
                  font=('times new roman', 15,'bold'), bd=10, 
                  fg="Black",)
            lbl2.grid(row=4,column=1, padx=0, pady=0, sticky='W', )
            lbl3 = Label(F3, text = 'Lead',
              font=('times new roman', 15,'bold'), bd=10, 
              fg="Black",)
            lbl3.grid(row=5,column=1, padx=0, pady=0, sticky='W', ) 
            
              
        else:
            set_clear_validate(1) 
            
    else:
        messagebox.showwarning("warning","You must make Clear First")  
        
   
Button(text = 'Calculate',
       font=('times new roman', 15, 'bold'), 
       bd=5, fg="purple",
       command = calc ).place(x=150, y=590, width=120, height=40)    

F3 = LabelFrame(root, 
                font=('times new roman', 16, 'bold'),
                bd=10, 
                fg="Black",)
F3.place(x=460, y=305, width=533, height=340)


Label(F3, text = 'Material',
      font=('times new roman', 16), bd=10, 
      fg="Black",).grid(row=1,column=1, padx=2, pady=0, sticky='W', )
Label(F3, text = "Primary \n Thickness",
      font=('times new roman', 14), bd=10, 
      fg="purple").grid(row=1,column=2, padx=2, pady=0, sticky='W' )
Label(F3, text = 'Primary \n Cost',
      font=('times new roman', 14), bd=10, 
      fg="purple",).grid(row=1,column=3, padx=2, pady=0, sticky='W', )
Label(F3, text = "Secondary \n Thickness",
      font=('times new roman', 14), bd=10, 
      fg="purple",).grid(row=1,column=4, padx=2, pady=0, sticky='W', )
Label(F3, text = 'Secondary \n Cost',
      font=('times new roman', 14), bd=10, 
      fg="purple",).grid(row=1,column=5, padx=2, pady=0, sticky='W', )




def clear():
    set_clear_validate(1) 
    
    try:
        lbl1.after(10, lbl1.destroy())
        lbl2.after(10, lbl2.destroy())
        lbl3.after(10, lbl3.destroy())
        
        conc_lbl1.after(10, conc_lbl1.destroy())
        conc_lbl2.after(10, conc_lbl2.destroy())
        conc_lbl3.after(10, conc_lbl3.destroy())
        conc_lbl4.after(10, conc_lbl4.destroy())
        
        steal_lbl1.after(10, steal_lbl1.destroy())
        steal_lbl2.after(10, steal_lbl2.destroy())
        steal_lbl3.after(10, steal_lbl3.destroy())
        steal_lbl4.after(10, steal_lbl4.destroy())
        
        lead_lbl1.after(10, lead_lbl1.destroy())
        lead_lbl2.after(10, lead_lbl2.destroy())
        lead_lbl3.after(10, lead_lbl3.destroy())
        lead_lbl4.after(10, lead_lbl4.destroy())
    except:
        print('HEllo')
    
    try:
        lbl1.after(10, lbl1.destroy())
        lbl2.after(10, lbl2.destroy())
        
        conc_lbl1.after(10, conc_lbl1.destroy())
        conc_lbl2.after(10, conc_lbl2.destroy())
        conc_lbl3.after(10, conc_lbl3.destroy())
        conc_lbl4.after(10, conc_lbl4.destroy())
        
        steal_lbl1.after(10, steal_lbl1.destroy())
        steal_lbl2.after(10, steal_lbl2.destroy())
        steal_lbl3.after(10, steal_lbl3.destroy())
        steal_lbl4.after(10, steal_lbl4.destroy())
        
    except:
        print('HEllo')
        
    try:
        lbl1.after(10, lbl1.destroy())
        lbl3.after(10, lbl3.destroy())
        
        conc_lbl1.after(10, conc_lbl1.destroy())
        conc_lbl2.after(10, conc_lbl2.destroy())
        conc_lbl3.after(10, conc_lbl3.destroy())
        conc_lbl4.after(10, conc_lbl4.destroy())
        
        lead_lbl1.after(10, lead_lbl1.destroy())
        lead_lbl2.after(10, lead_lbl2.destroy())
        lead_lbl3.after(10, lead_lbl3.destroy())
        lead_lbl4.after(10, lead_lbl4.destroy())
    except:
        print('HEllo')
        
    try:
        lbl2.after(10, lbl2.destroy())
        lbl3.after(10, lbl3.destroy())
        
        steal_lbl1.after(10, steal_lbl1.destroy())
        steal_lbl2.after(10, steal_lbl2.destroy())
        steal_lbl3.after(10, steal_lbl3.destroy())
        steal_lbl4.after(10, steal_lbl4.destroy())
        
        lead_lbl1.after(10, lead_lbl1.destroy())
        lead_lbl2.after(10, lead_lbl2.destroy())
        lead_lbl3.after(10, lead_lbl3.destroy())
        lead_lbl4.after(10, lead_lbl4.destroy())
    except:
        print('HEllo')
    
    try:
        lbl1.after(10, lbl1.destroy())
        
        conc_lbl1.after(10, conc_lbl1.destroy())
        conc_lbl2.after(10, conc_lbl2.destroy())
        conc_lbl3.after(10, conc_lbl3.destroy())
        conc_lbl4.after(10, conc_lbl4.destroy())
        
    except:
        print('HEllo')
        
    try:
        lbl2.after(10, lbl2.destroy())        
        
        steal_lbl1.after(10, steal_lbl1.destroy())
        steal_lbl2.after(10, steal_lbl2.destroy())
        steal_lbl3.after(10, steal_lbl3.destroy())
        steal_lbl4.after(10, steal_lbl4.destroy())
        
    except:
        print('HEllo')
    try:
        lbl3.after(10, lbl3.destroy())
        
        lead_lbl1.after(10, lead_lbl1.destroy())
        lead_lbl2.after(10, lead_lbl2.destroy())
        lead_lbl3.after(10, lead_lbl3.destroy())
        lead_lbl4.after(10, lead_lbl4.destroy())
    except:
        print('HEllo')
   
    
Button(text = 'Clear',
       font=('times new roman', 15, 'bold'), 
       bd=5, fg="Black",
       command = clear).place(x=700, y=570, width=90, height=40)    




root.mainloop()