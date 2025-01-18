#!/usr/bin/python3

# PROJECT		calc_temp
# FILE			calc_temp.py
# DESIGNER		Jacob Romero 

'''
	Copyright (C) 4/28/2024 
	Jacob Romero, Creative Engineering Solutions, LLC
	cesllc876@gmail.com
 
	This program is free software; you can redistribute it
	and/or modify it under the terms of the GNU General Public  
	License as published by the Free Software Foundation, version 2.

	This program is distributed in the hope that it will be
	useful, but WITHOUT ANY WARRANTY; without even the implied 
	warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
	
	See the GNU General Public License for more details.
	
	You should have received a copy of the GNU General Public
	License along with this program; if not, write to:
	The Free Software Foundation, Inc.
	59 Temple Place, Suite 330
	Boston, MA 02111-1307 USA
 
	References:	
		
'''

#################################
####### IMPORT STATEMENTS #######
import os
import sys
import math
import tkinter as tk
from tkinter import *

#############################################
############### TKINTER SETUP ###############
root = tk.Tk()
root.title("Thermal Calculator for Electronic Components")
root.geometry("800x750")  ## preferred
# ~ root.geometry("1000x750")
# ~ root.geometry("1200x750")
# ~ root.geometry("1200x900")
column_size = 60
row_size = 25
#############################################
################## GLOBALS ##################

MILLI 		= 1e-3
MICRO 		= 1e-6
NANO		= 1e-9
PICO		= 1e-12
KILO		= 1e3
MEGA		= 1e6
GIGA		= 1e9
TERA		= 1e12

INPUT_V 	= 0
OUTPUT_V 	= 0
V_DROP	 	= 0
MEASURED_I	= 0
MEASURED_W	= 0
TEMP_RISE	= 0
RTH		= 0
MAX_AMBIENT 	= 0
JUNCT_TEMP 	= 0
MAX_ALLOWED 	= 0

####################################################
############### Button Declarations ################
gen_temp_button = tk.Button(text="Calc Temp",
		command=lambda: gen_temp(), width=13)
                    
ambient_button = tk.Button(text="Ambient Temp",   
		command=lambda: show_AT_Labels(), width=13)                     
                       
clear_AT_button = tk.Button(text="Clear AT",   
		command=lambda: clear_AT_Data_Labels(), width=13)                     
  
gen_temp_button.grid		(row=0,		column=0)
ambient_button.grid		(row=10,	column=0)
clear_AT_button.grid		(row=11,	column=0)

################### Functions and Commands ################### 

def gen_temp_rise(inV, outV, mcurr, rth):
	pwr_diss = (float(inV)-float(outV)) * float(mcurr)
	globals()[MEASURED_W]	= pwr_diss
	temp_rise = float(rth) * float(pwr_diss)
	globals()[TEMP_RISE]	= temp_rise
	return temp_rise

def gen_count(end, start):
	count = (int(end) - int(start))
	return int(count)

def gen_target(value, inc):
	target = (float(value) + float(inc))
	return float(target)

def pass_fail(juncTemp, maxTemp):
	diff = float(maxTemp) - float(juncTemp)
	result = ""
	if diff > 0: result = "Pass"
	elif diff <= 0: result = "Fail"
	return result

def gen_temp():	
	globals()[INPUT_V]	= IVset.get()
	globals()[OUTPUT_V] 	= OVset.get()
	globals()[V_DROP]	= Vdropset.get()
	globals()[MEASURED_I]	= MAset.get()
	globals()[MEASURED_W]	= MWset.get()
	globals()[RTH]		= RTHset.get()
	globals()[TEMP_RISE]	= TRiseset.get()
	globals()[MAX_AMBIENT] 	= MAXambset.get()
	globals()[JUNCT_TEMP] 	= JTempset.get()
	globals()[MAX_ALLOWED] 	= MAXallset.get()
	
	TRiseset.set(round(gen_temp_rise(IVset.get(), OVset.get(), MAset.get(), RTHset.get()),4))
	globals()[TEMP_RISE]	= TRiseset.get()
	Vdropset.set(float(IVset.get()) - float(OVset.get()))
	globals()[V_DROP]	 	= Vdropset.get()
	mwset = (float(Vdropset.get()) * float(MAset.get()))
	MWset.set(float(round(mwset,5)))
	globals()[MEASURED_W]	= MWset.get()
	jtempset = (float(TRiseset.get()) + float(MAXambset.get()))
	JTempset.set(float(round(jtempset,4)))	
	globals()[JUNCT_TEMP] 	= JTempset.get
	
	clear_AT_Data_Labels()
	
	Amb_val_label_text = tk.StringVar()
	Amb_val_label_text.set(MAXambset.get())
	Amb_val_label = tk.Label(root, textvariable=Amb_val_label_text, width=10)
	Amb_val_label.grid(row=1, column=4)

	JTemp_Amb_val_label_text = tk.StringVar()
	JTemp_Amb_val_label_text.set(JTempset.get())
	JTemp_Amb_val_label = tk.Label(root, textvariable=JTemp_Amb_val_label_text, width=10)
	JTemp_Amb_val_label.grid(row=1, column=5)

	JTemp_Amb_PF_val_label_text = tk.StringVar()
	JTemp_Amb_PF_val_label_text.set(pass_fail(JTempset.get(), MAXallset.get()))
	JTemp_Amb_PF_val_label = tk.Label(root, textvariable=JTemp_Amb_PF_val_label_text, width=10)
	JTemp_Amb_PF_val_label.grid(row=1, column=6)


def show_AT_Labels():	
	globals()[INPUT_V]	= IVset.get()
	globals()[OUTPUT_V] 	= OVset.get()
	globals()[V_DROP]	= Vdropset.get()
	globals()[MEASURED_I]	= MAset.get()
	globals()[MEASURED_W]	= MWset.get()
	globals()[RTH]		= RTHset.get()
	globals()[TEMP_RISE]	= TRiseset.get()
	globals()[MAX_AMBIENT] 	= MAXambset.get()
	globals()[JUNCT_TEMP] 	= JTempset.get()
	globals()[MAX_ALLOWED] 	= MAXallset.get()
	
	TRiseset.set(round(gen_temp_rise(IVset.get(), OVset.get(), MAset.get(), RTHset.get()),4))
	globals()[TEMP_RISE]	= TRiseset.get()
	Vdropset.set(float(IVset.get()) - float(OVset.get()))
	globals()[V_DROP]	 = Vdropset.get()
	mwset = (float(Vdropset.get()) * float(MAset.get()))
	MWset.set(float(round(mwset,5)))
	globals()[MEASURED_W]	= MWset.get()
	jtempset = (float(TRiseset.get()) + float(MAXambset.get()))
	JTempset.set(float(round(jtempset,4)))	
	globals()[JUNCT_TEMP] 	= JTempset.get()
	
	clear_AT_Data_Labels()
	ACountset.set(int(gen_count(int(AEndset.get()) + int(AMultset.get()), int(AStartset.get())) / int(AMultset.get())))
	count = int(ACountset.get())
	
	for i in range (count):
		
		result = gen_target(float(AStartset.get()), i*float(AMultset.get()))
		Atemp_rise = gen_temp_rise(IVset.get(), OVset.get(), MAset.get(), RTHset.get())
		Ajtempset = float(Atemp_rise + result)
		
		Amb_val_label_text = tk.StringVar()
		Amb_val_label_text.set(result)
		Amb_val_label = tk.Label(root, textvariable=Amb_val_label_text, width=10)
		Amb_val_label.grid(row=1+i, column=4)

		JTemp_Amb_val_label_text = tk.StringVar()
		JTemp_Amb_val_label_text.set(Ajtempset)
		JTemp_Amb_val_label = tk.Label(root, textvariable=JTemp_Amb_val_label_text, width=10)
		JTemp_Amb_val_label.grid(row=1+i, column=5)

		JTemp_Amb_PF_val_label_text = tk.StringVar()
		JTemp_Amb_PF_val_label_text.set(pass_fail(float(Ajtempset), float(MAXallset.get())))
		JTemp_Amb_PF_val_label = tk.Label(root, textvariable=JTemp_Amb_PF_val_label_text, width=10)
		JTemp_Amb_PF_val_label.grid(row=1+i, column=6)	


def clear_AT_Data_Labels():
	count = int(ACountset.get())
	for i in range (count):
		
		Amb_val_label_text = tk.StringVar()
		Amb_val_label_text.set("")
		Amb_val_label = tk.Label(root, textvariable=Amb_val_label_text, width=10)
		Amb_val_label.grid(row=1+i, column=4)

		JTemp_Amb_val_label_text = tk.StringVar()
		JTemp_Amb_val_label_text.set("")
		JTemp_Amb_val_label = tk.Label(root, textvariable=JTemp_Amb_val_label_text, width=10)
		JTemp_Amb_val_label.grid(row=1+i, column=5)

		JTemp_Amb_PF_val_label_text = tk.StringVar()
		JTemp_Amb_PF_val_label_text.set("")
		JTemp_Amb_PF_val_label = tk.Label(root, textvariable=JTemp_Amb_PF_val_label_text, width=10)
		JTemp_Amb_PF_val_label.grid(row=1+i, column=6)

####################################################
################ Entry Declarations ################

IVset 		= tk.StringVar()
OVset 		= tk.StringVar()
Vdropset 	= tk.StringVar()
MAset 		= tk.StringVar()
MWset 		= tk.StringVar()
RTHset 		= tk.StringVar()
TRiseset 	= tk.StringVar()
MAXambset 	= tk.StringVar()
JTempset 	= tk.StringVar()
MAXallset 	= tk.StringVar()

AStartset 	= tk.StringVar()
AEndset 	= tk.StringVar()
AMultset 	= tk.StringVar()
ACountset 	= tk.StringVar()

IVset_entry 		= tk.Entry(root, textvariable=IVset, width=14)
OVset_entry 		= tk.Entry(root, textvariable=OVset,  width=14)
Vdropset_entry 		= tk.Entry(root, textvariable=Vdropset, width=14)
MAset_entry 		= tk.Entry(root, textvariable=MAset, width=14)
MWset_entry 		= tk.Entry(root, textvariable=MWset, width=14)
RTHset_entry 		= tk.Entry(root, textvariable=RTHset, width=14)
TRiseset_entry 		= tk.Entry(root, textvariable=TRiseset, width=14)
MAXambset_entry 	= tk.Entry(root, textvariable=MAXambset, width=14)
JTempset_entry 		= tk.Entry(root, textvariable=JTempset, width=14)
MAXallset_entry 	= tk.Entry(root, textvariable=MAXallset, width=14)

AStartset_entry 	= tk.Entry(root, textvariable=AStartset, width=14)
AEndset_entry 		= tk.Entry(root, textvariable=AEndset, width=14)
AMultset_entry 		= tk.Entry(root, textvariable=AMultset, width=14)
ACountset_entry 	= tk.Entry(root, textvariable=ACountset, width=14)

IVset.set(0.21)
OVset.set(0.0)
Vdropset.set(float(IVset.get()) - float(OVset.get()))
MAset.set(152.0 * MILLI)
mwset = (float(Vdropset.get()) * float(MAset.get()))
MWset.set(float(round(mwset,5)))
RTHset.set(263.8)
triset = (float(RTHset.get()) * float(MWset.get()))
TRiseset.set(float(round(triset,4)))
MAXambset.set(25.0)
jtempset = (float(TRiseset.get()) + float(MAXambset.get()))
JTempset.set(float(round(jtempset,4)))
MAXallset.set(100.0)

AStartset.set(10)
AEndset.set(100)
AMultset.set(5)
ACountset.set(int(gen_count(int(AEndset.get()) + int(AMultset.get()), 
			int(AStartset.get())) / int(AMultset.get())))

IVset_entry.grid	(row=0,  column=1)
OVset_entry.grid	(row=1,  column=1)
Vdropset_entry.grid	(row=2,  column=1)
MAset_entry.grid    	(row=3,  column=1)
MWset_entry.grid    	(row=4,  column=1)
RTHset_entry.grid	(row=5,  column=1)
TRiseset_entry.grid 	(row=6,  column=1)
MAXambset_entry.grid 	(row=7,  column=1)
JTempset_entry.grid 	(row=8,  column=1)
MAXallset_entry.grid 	(row=9,  column=1)

AStartset_entry.grid 	(row=10,  column=1)
AEndset_entry.grid 	(row=11,  column=1)
AMultset_entry.grid 	(row=12, column=1)
ACountset_entry.grid 	(row=13, column=1)

####################################
########## Create Labels ##########

IVset_label = tk.StringVar()
IVset_label_text = tk.StringVar()
IVset_label_text.set("Input Voltage")
IVset_label = tk.Label(root, textvariable=IVset_label_text, width=12)
IVset_label.grid(row=0, column=2)

OVset_label = tk.StringVar()
OVset_label_text = tk.StringVar()
OVset_label_text.set("Output Voltage")
OVset_label = tk.Label(root, textvariable=OVset_label_text, width=12)
OVset_label.grid(row=1, column=2)

Vdropset_label = tk.StringVar()
Vdropset_label_text = tk.StringVar()
Vdropset_label_text.set("Voltage Drop")
Vdropset_label = tk.Label(root, textvariable=Vdropset_label_text, width=12)
Vdropset_label.grid(row=2, column=2)

MAset_label = tk.StringVar()
MAset_label_text = tk.StringVar()
MAset_label_text.set("Measured I Amps")
MAset_label = tk.Label(root, textvariable=MAset_label_text, width=14)
MAset_label.grid(row=3, column=2)

MWset_label = tk.StringVar()
MWset_label_text = tk.StringVar()
MWset_label_text.set("Pwr Diss Watts")
MWset_label = tk.Label(root, textvariable=MWset_label_text, width=14)
MWset_label.grid(row=4, column=2)

RTHset_label = tk.StringVar()
RTHset_label_text = tk.StringVar()
RTHset_label_text.set("R Theta")
RTHset_label = tk.Label(root, textvariable=RTHset_label_text, width=14)
RTHset_label.grid(row=5, column=2)

TRiseset_label = tk.StringVar()
TRiseset_label_text = tk.StringVar()
TRiseset_label_text.set("Temp Rise")
TRiseset_label = tk.Label(root, textvariable=TRiseset_label_text, width=14)
TRiseset_label.grid(row=6, column=2)

MAXambset_label = tk.StringVar()
MAXambset_label_text = tk.StringVar()
MAXambset_label_text.set("Ambient Temp")
MAXambset_label = tk.Label(root, textvariable=MAXambset_label_text, width=14)
MAXambset_label.grid(row=7, column=2)

JTempset_label = tk.StringVar()
JTempset_label_text = tk.StringVar()
JTempset_label_text.set("Junct Temp")
JTempset_label = tk.Label(root, textvariable=JTempset_label_text, width=14)
JTempset_label.grid(row=8, column=2)

MAXallset_label = tk.StringVar()
MAXallset_label_text = tk.StringVar()
MAXallset_label_text.set("Max Temp")
MAXallset_label = tk.Label(root, textvariable=MAXallset_label_text, width=14)
MAXallset_label.grid(row=9, column=2)

amb_start_label = tk.StringVar()
amb_start_label_text = tk.StringVar()
amb_start_label_text.set("Start Ambient")
amb_start_label = tk.Label(root, textvariable=amb_start_label_text, width=14)
amb_start_label.grid(row=10, column=2)

amb_end_label = tk.StringVar()
amb_end_label_text = tk.StringVar()
amb_end_label_text.set("End Ambient")
amb_end_label = tk.Label(root, textvariable=amb_end_label_text, width=10)
amb_end_label.grid(row=11, column=2)

amb_mult_label = tk.StringVar()
amb_mult_label_text = tk.StringVar()
amb_mult_label_text.set("Loop Mult")
amb_mult_label = tk.Label(root, textvariable=amb_mult_label_text, width=10)
amb_mult_label.grid(row=12, column=2)

amb_count_label = tk.StringVar()
amb_count_label_text = tk.StringVar()
amb_count_label_text.set("Loop Count")
amb_count_label = tk.Label(root, textvariable=amb_count_label_text, width=10)
amb_count_label.grid(row=13, column=2)

###########

Amb_in_label   		= tk.Label(root, text="Ambient ")
JTemp_Amb_in_label  	= tk.Label(root, text="Junct T")
JTemp_Amb_PF_in_label	= tk.Label(root, text="P/F")

Amb_val_label		= tk.StringVar()
JTemp_Amb_val_label	= tk.StringVar()
JTemp_Amb_PF_val_label	= tk.StringVar()

Amb_val_label_text = tk.StringVar()
Amb_val_label_text.set(MAXambset.get())
Amb_val_label = tk.Label(root, textvariable=Amb_val_label_text, width=10)
Amb_val_label.grid(row=1, column=4)

JTemp_Amb_val_label_text = tk.StringVar()
JTemp_Amb_val_label_text.set(JTempset.get())
JTemp_Amb_val_label = tk.Label(root, textvariable=JTemp_Amb_val_label_text, width=10)
JTemp_Amb_val_label.grid(row=1, column=5)

JTemp_Amb_PF_val_label_text = tk.StringVar()
JTemp_Amb_PF_val_label_text.set(pass_fail(JTempset.get(), MAXallset.get()))
JTemp_Amb_PF_val_label = tk.Label(root, textvariable=JTemp_Amb_PF_val_label_text, width=10)
JTemp_Amb_PF_val_label.grid(row=1, column=6)

#####################################################
################ The Label Generator ################

for a in range(30):
	root.grid_columnconfigure	(a,  minsize=column_size)
	root.grid_rowconfigure		(a,  minsize=row_size)
	
	Amb_in_label.grid		(row=0, column=4)
	JTemp_Amb_in_label.grid 	(row=0, column=5)
	JTemp_Amb_PF_in_label.grid	(row=0, column=6)
 
root.update()
root.mainloop()

