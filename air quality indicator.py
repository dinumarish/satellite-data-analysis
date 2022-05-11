# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 09:43:16 2020

@author: user
"""

import requests
import json
import tkinter as tk
import textwrap as tw
#from PIL import ImageTk
root = tk.Tk()
root.title('AQI- USA')
root.geometry('450x400')

#img = ImageTk.PhotoImage(file= r'C:\\Users\\user\\Documents\\apps\\delhi.png' )

#background_label = tk.Label(image=img)
#background_label.place(x=0, y=0, relwidth=1, relheight=1)

root.configure(bg ='light blue')    

weat_label =tk.Label(root)
desc_label =tk.Label(root)
def consturl():
    global weat_label
    global desc_label
    
    if desc_label.winfo_exists():
       weat_label.grid_forget()
       desc_label.grid_forget()
    zipcode = zip_entry.get()
    url = f'https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode={zipcode}&date=2020-10-20&distance=2&API_KEY=***********************'
    try:
       
        call = requests.get(url)
        data = json.loads(call.text)
        city = data[0]['ReportingArea']
        air  = data[0]['AQI']
        catg = data[0]['Category']['Name']
        desc = data[0]['Discussion']
        wrapper = tw.TextWrapper(width = 60)
        wdesc = wrapper.fill(text=desc)
        
        if catg == 'Good':
            color = 'light green'
        elif catg == 'Moderate':
            color = 'light yellow'
        elif catg == 'Unhealthy for Sensitive Groups':
            color = 'light orange'
        elif catg == 'Unhealthy':
            color = 'light red'
        elif catg == 'Very Unhealthy':
            color = 'light purple'
        elif catg == 'Hazardous':
            color = 'light black'  
        weat_label = tk.Label(root, text = city +'\nAir Quality\n'+ str(air) +'\n'+ catg, height = 4, bg = color)
        desc_label = tk.Label(root, text = wdesc, anchor="e", bg='light blue')
        weat_label.grid(row=0, column=3, columnspan=5)
        desc_label.grid(row=2, column=1, columnspan =7, rowspan= 8)
       
                       
    except Exception as e:
        data = 'Error...'
        desc_label = tk.Label(root, text = data, anchor="e", bg='dark red')
        desc_label.grid(row=2, column=1, columnspan =7, rowspan= 8)
        
        
        
zip_label = tk.Label(root, text = 'Zip Code ')
zip_label.grid(row=0, column = 0)#sticky =E+W)
zip_entry = tk.Entry(root, bd= 4, cursor = 'circle')
zip_entry.grid(row =0, column=1)#sticky =E+W)
zip_button = tk.Button(root, text = 'find', command = consturl)
zip_button.grid(row=1, column = 1)#stick =N+E+W+S)


root.mainloop()
