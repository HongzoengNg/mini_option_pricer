import tkinter as tk 
from tkinter import ttk
import aritasian_option_pricer as aaop


def arithaCal(typ, asset_price, mature_time, strike_price, rate, vol, n, path, ctl_var):
    
    if typ == 'Call Option':
        tp = 'c'
    elif typ == 'Put Option':
        tp = 'p'

    asset_price = float(asset_price)
    strike_price = float(strike_price)
    mature_time = float(mature_time)
    vol = float(vol)
    rate = float(rate)
    path = int(path)
    n = int(n)
    
    # future_type, asset_price,mature_time,strike_price,rate,vol,n,path=100000,ctl_var=True
    aaopx = aaop.aritasian_opt(tp, asset_price, mature_time, strike_price, rate, vol, n, path, ctl_var)
    value = aaopx.value()
    text10['text'] = value[0]
    text12['text'] = value[1]


def main():
    win = tk.Tk()
    win.title("Arithmetic Asian Option Pricer")


    text0 = tk.Label(win, text = 'Choose Asset Type: ').grid(row=0) 
    typex = tk.StringVar()
    chooseType = ttk.Combobox(win, width = 26, textvariable = typex)
    chooseType['values'] = ('Call Option', 'Put Option')
    chooseType.grid(row=0, column=1)


    text1 = tk.Label(win, text = 'Asset Price: ').grid(row=1) 
    priceA = tk.StringVar()
    entry1 = ttk.Entry(win, textvariable = priceA) 
    entry1.grid(row=1, column=1)


    text2 = tk.Label(win, text = 'Strike Price: ').grid(row=2) 
    priceK = tk.StringVar()
    entry2 = ttk.Entry(win, textvariable = priceK)
    entry2.grid(row=2, column=1)


    text3 = tk.Label(win, text = 'Maturity Time: ').grid(row=3) 
    timeM = tk.StringVar()
    entry3 = ttk.Entry(win, textvariable = timeM)
    entry3.grid(row=3, column=1)


    text4 = tk.Label(win, text = 'Volatility: ').grid(row=4) 
    vol = tk.StringVar()
    entry4 = ttk.Entry(win, textvariable = vol)
    entry4.grid(row=4, column=1)


    text5 = tk.Label(win, text = 'Risk Free Rate: ').grid(row=5)
    rate = tk.StringVar()
    entry5 = ttk.Entry(win, textvariable = rate)
    entry5.grid(row=5, column=1)


    text6 = tk.Label(win, text = 'n Value: ').grid(row=6) 
    n = tk.StringVar()
    entry6 = ttk.Entry(win, textvariable = n)
    entry6.grid(row=6, column=1)


    text7 = tk.Label(win, text = 'Control Variate').grid(row=7) 
    ctl_var = tk.BooleanVar()
    ctl_var.set(True)
    check7 = ttk.Checkbutton(win, variable=ctl_var).grid(row=7, column=1)
    

    text8 = tk.Label(win, text = 'Monte Carlo Path: ').grid(row=8) 
    path = tk.StringVar()
    entry8 = ttk.Entry(win, textvariable = path)
    entry8.grid(row=8, column=1)
    path.set(1000)

    text9 = tk.Label(win, text = 'Price: ').grid(row=9)
    text10 = tk.Label(win)
    text10.grid(row=9, column=1)

    text11 = tk.Label(win, text = '95% Confidence Interval: ').grid(row=10)
    text12 = tk.Label(win)
    text12.grid(row=10, column=1)


    button = tk.ttk.Button(win, text="Calculate", command=lambda : arithaCal(typex.get(), priceA.get(), timeM.get(), priceK.get(), rate.get(), vol.get(), n.get(), path.get(), ctl_var.get()))
    #button = tk.ttk.Button(win, text="Calculate", command=lambda : prin())
    button.grid()


    win.mainloop()

