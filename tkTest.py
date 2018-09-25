import tkinter as tk
import os as os
import STOCKMARKET as SM
import matplotlib.pyplot as plt
root = tk.Tk()
frame = tk.Frame(root)
frame.grid()
global x
x = None
def SelectSite():
    window = tk.Toplevel(root)
    window.grid()
    frame1 = tk.Frame(window)
    frame1.grid()
    label = tk.Label(frame1,text = "Enter Site")
    label.grid(row = 0, column = 0)
    text = tk.Entry(frame1)
    text.grid(row = 0, column = 1)
    def new():
        global x
        x = text.get()
        SM.tabular_data(x)
        a = SM.Graphical_data(x)
        a.figure()
        b = SM.Predicted_data(x)
        b.figure()
        plt.show(block = False)
        viewDB = tk.Button(frame1, text = "View Stock Database", command = ViewDatabase)
        viewDB.grid(row = 2, column = 0, columnspan = 2)
    button = tk.Button(frame1, text = "OK", command = new)
    button.grid(row = 2, column = 0, columnspan = 2)
    

def ViewDatabase():
    file = r'C:\Users\Shreyansh jain\Desktop\software\DBMS\test.xlsx'
    os.startfile(file)

siteSelect = tk.Button(frame, text = "Site Selection", command = SelectSite)
siteSelect.grid()

root.mainloop()
