import tkinter as tk 
from tkinter import ttk
import aritbasket_option_pricer as abop

#future_type, asset_price1, asset_price2,mature_time,strike_price,rate,vol1,vol2,rol
def mainCal(typ, asset_price1, asset_price2, mature_time, strike_price, rate, vol1, vol2, rol, path, ctl_car):
    if typ == 'Call Option':
        tp = 'c'
    elif typ == 'Put Option':
        tp = 'p'
    
    asset_price1 = float(asset_price1)
    asset_price2 = float(asset_price2)
    strike_price = float(strike_price)
    mature_time = float(mature_time)
    vol1 = float(vol1)
    vol2 = float(vol2)
    rate = float(rate)
    rol = float(rol)
    path = int(path)

    #future_type, asset_price1, asset_price2,mature_time,strike_price,rate,vol1,vol2,rol
    abopx = abop.aritbasket_opt(tp, asset_price1, asset_price2, mature_time, strike_price, rate, vol1, vol2, rol, path, ctl_var)
    value = abopx.value()

    text12['text'] = value[0]
    text14['text'] = value[1]


def main():
    win = tk.Tk()
    win.title("Geometirc Basket Option Pricer")


    text0 = tk.Label(win, text = 'Choose Asset Type: ').grid(row=0) 
    typex = tk.StringVar()
    chooseType = ttk.Combobox(win, width = 26, textvariable = typex)
    chooseType['values'] = ('Call Option', 'Put Option')
    chooseType.grid(row=0, column=1)


    text1 = tk.Label(win, text = '1st Asset Price: ').grid(row=1) 
    priceA1 = tk.StringVar()
    entry1 = tk.Entry(win, textvariable = priceA1) 
    entry1.grid(row=1, column=1)


    text2 = tk.Label(win, text = '2nd Asset Price: ').grid(row=2) 
    priceA2 = tk.StringVar()
    entry2 = tk.Entry(win, textvariable = priceA2) 
    entry2.grid(row=2, column=1)

    text3 = tk.Label(win, text = 'Strike Price: ').grid(row=3) 
    priceK = tk.StringVar()
    entry3 = tk.Entry(win, textvariable = priceK)
    entry3.grid(row=3, column=1)


    text4 = tk.Label(win, text = 'Maturity Time: ').grid(row=4) 
    timeM = tk.StringVar()
    entry4 = tk.Entry(win, textvariable = timeM)
    entry4.grid(row=4, column=1)


    text5 = tk.Label(win, text = '1st Volatility: ').grid(row=5) 
    vol1 = tk.StringVar()
    entry5 = tk.Entry(win, textvariable = vol1)
    entry5.grid(row=5, column=1)


    text6 = tk.Label(win, text = '2nd Volatility: ').grid(row=6) 
    vol2 = tk.StringVar()
    entry6 = tk.Entry(win, textvariable = vol2)
    entry6.grid(row=6, column=1)


    text7 = tk.Label(win, text = 'Risk Free Rate: ').grid(row=7)
    rate = tk.StringVar()
    entry7 = tk.Entry(win, textvariable = rate)
    entry7.grid(row=7, column=1)


    text8 = tk.Label(win, text = 'Correlation: ').grid(row=8)
    rol = tk.StringVar()
    entry8 = tk.Entry(win, textvariable = rol)
    entry8.grid(row=8, column=1)


    text9 = tk.Label(win, text = 'Control Variate: ').grid(row=9) 
    ctl_var = tk.BooleanVar()
    ctl_var.set(True)
    check9 = ttk.Checkbutton(win, variable=ctl_var).grid(row=9, column=1)
 


    text10 = tk.Label(win, text = 'Monte Carlo Path: ').grid(row=10) 
    path = tk.StringVar()
    entry10 = ttk.Entry(win, textvariable = path)
    entry10.grid(row=10, column=1)
    path.set(10000)

    text11 = tk.Label(win, text = 'Price: ').grid(row=11) 
    text12 = tk.Label(win)
    text12.grid(row=11, column=1)


    text13 = tk.Label(win, text = '95% Confidence Interval: ').grid(row=12)
    text14 = tk.Label(win)
    text14.grid(row=12, column=1)

    #future_type, asset_price1, asset_price2,mature_time,strike_price,rate,vol1,vol2,rol
    button = tk.ttk.Button(win, text="Calculate", command=lambda : mainCal(typex.get(), priceA1.get(), priceA2.get(), \
                    timeM.get(), priceK.get(), rate.get(), vol1.get(), vol2.get(), rol.get(), path.get(), ctl_var.get()))
    button.grid()


    win.mainloop()

