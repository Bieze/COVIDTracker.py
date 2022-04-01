import tkinter as tk
from tkinter import Toplevel
from covid import Covid


gui = tk.Tk()


gui.title("COVID-19 Tracker/Traquer")
gui.iconbitmap("icon.ico")


gui.minsize(420, 450)
gui.maxsize(420, 450)


canvas = tk.Canvas(gui, width = 400, height = 435, bg="gray")


entry = tk.Entry(gui)
canvas.create_window(200, 140, window=entry)




def getcountry():
    covid = Covid()
    x = entry.get()

    y = covid.get_status_by_country_name(x)

    #label = tk.Label(gui, text=f"Cases/Cas: {y['confirmed']}\Active/Actives: {y['active']}\nDeaths/Morts: {y['deaths']}\nRecovered/Retabli(2): {y['recovered']}", bg="gray")
    #canvas.create_window(200, 230, window=label)
    gui2 = Toplevel(gui) 
  
    # sets the title of the 
    # Toplevel widget 
    gui2.title(f"{x}") 
    gui2.iconbitmap("icon.ico")
  
    # sets the geometry of toplevel 
    gui2.geometry("250x250") 
    gui2.minsize(210, 225)
    gui2.maxsize(225, 225)
  
    # A Label widget to show in toplevel
    canvasgui2 = tk.Canvas(gui2, width = 200, height = 218, bg="gray")
    label = tk.Label(gui2, text=f"Cases/Cas: {y['confirmed']}\nActive/Actives: {y['active']}\nDeaths/Morts: {y['deaths']}\nRecovered/Retabli(e): {y['recovered']}", bg="gray")
    canvasgui2.create_window(115, 117, window=label)
    canvasgui2.pack()


button = tk.Button(text='Get the information for your country', command=getcountry)
canvas.create_window(200, 180, window=button)
    

canvas.pack()
tk.mainloop()