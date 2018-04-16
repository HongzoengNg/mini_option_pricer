import tkinter as tk 
from tkinter import ttk
import GUI_EuroOpt as euro
import GUI_ImpVol as iv
import GUI_BinTree as bi
import GUI_GeoAsianOpt as geoAsian
import GUI_ArithAsianOpt as geoArith
import GUI_GeoBasketOpt as geoBask 
import GUI_ArithBasketOpt as arithBask 


win = tk.Tk()
win.title("Assigment 3")

text0 = tk.Label(win, text='European Option Pricer:', font=("Helvetica", 16), height=2)
text0.grid(row=0)
button0 = tk.Button(win, text="Open", font=("Helvetica", 15), command=lambda : euro.main())
button0.grid(row=0, column=1)


text1 = tk.Label(win, text='Implied Volatility Calculation:', font=("Helvetica", 16), height=2)
text1.grid(row=1)
button1 = tk.Button(win, text="Open", font=("Helvetica", 15), command=lambda : iv.main())
button1.grid(row=1, column=1)


text2 = tk.Label(win, text='Binary Tree Option Pricer:', font=("Helvetica", 16), height=2)
text2.grid(row=2)
button2 = tk.Button(win, text="Open", font=("Helvetica", 15), command=lambda : bi.main())
button2.grid(row=2, column=1)


text3 = tk.Label(win, text='Geometirc Asian Option Pricer:', font=("Helvetica", 16), height=2)
text3.grid(row=3)
button3 = tk.Button(win, text="Open", font=("Helvetica", 15), command=lambda : geoAsian.main())
button3.grid(row=3, column=1)


text4 = tk.Label(win, text='Arithmetic Asian Option Pricer:', font=("Helvetica", 16), height=2)
text4.grid(row=4)
button4 = tk.Button(win, text="Open", font=("Helvetica", 15), command=lambda : geoArith.main())
button4.grid(row=4, column=1)


text5 = tk.Label(win, text='Geometirc Basket Option Pricer:', font=("Helvetica", 16), height=2)
text5.grid(row=5)
button1 = tk.Button(win, text="Open", font=("Helvetica", 15), command=lambda : geoBask.main())
button1.grid(row=5, column=1)


text6 = tk.Label(win, text='Arithmetirc Basket Option Pricer:', font=("Helvetica", 16), height=2)
text6.grid(row=6)
button6 = tk.Button(win, text="Open", font=("Helvetica", 15), command=lambda : arithBask.main())
button6.grid(row=6, column=1)


win.mainloop()