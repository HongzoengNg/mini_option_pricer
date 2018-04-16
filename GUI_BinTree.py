import tkinter as tk 
from tkinter import ttk
import binarytree_option_pricer as bop

#type, S0, K, T, sigma, r, q
def mainCal(typ, asset_price, strike_price, mature_time, vol, rate, repo_q):
    if typ == 'American Call Option':
        tp = 'amcall'
    elif typ == 'American Put Option':
        tp = 'amput'
    elif typ == 'European Call Option':
        tp = 'eucall'
    elif typ == 'European Put Option':
        tp = 'euput'
    
    asset_price = float(asset_price)
    strike_price = float(strike_price)
    mature_time = float(mature_time)
    vol = float(vol)
    rate = float(rate)
    repo_q = float(repo_q)

    #Type,S0,K,T,r,q,V
    bopx = bop.BinaryTree(tp, asset_price, strike_price, mature_time, vol, rate, repo_q)

    text8['text'] = bopx.bt(steps=50)


win = tk.Tk()
win.title("Binary Tree Option Pricer")


text0 = tk.Label(win, text = 'Choose Asset Type: ').grid(row=0) 
typex = tk.StringVar()
chooseType = ttk.Combobox(win, width = 26, textvariable = typex)
chooseType['values'] = ('American Call Option', 'American Put Option', 'European Call Option', 'European Put Option')
chooseType.grid(row=0, column=1)


text1 = tk.Label(win, text = 'Asset Price: ').grid(row=1) 
priceA = tk.StringVar()
entry1 = tk.ttk.Entry(win, textvariable = priceA) 
entry1.grid(row=1, column=1)


text2 = tk.Label(win, text = 'Strike Price: ').grid(row=2) 
priceK = tk.StringVar()
entry2 = tk.ttk.Entry(win, textvariable = priceK)
entry2.grid(row=2, column=1)


text3 = tk.Label(win, text = 'Maturity Time: ').grid(row=3) 
timeM = tk.StringVar()
entry3 = tk.ttk.Entry(win, textvariable = timeM)
entry3.grid(row=3, column=1)


text4 = tk.Label(win, text = 'Volatility: ').grid(row=4) 
vol = tk.StringVar()
entry4 = tk.ttk.Entry(win, textvariable = vol)
entry4.grid(row=4, column=1)


text5 = tk.Label(win, text = 'Risk Free Rate: ').grid(row=5)
rate = tk.StringVar()
entry5 = tk.ttk.Entry(win, textvariable = rate)
entry5.grid(row=5, column=1)


text6 = tk.Label(win, text = 'Repo Rate: ').grid(row=6) 
repoR = tk.StringVar()
entry6 = tk.ttk.Entry(win, textvariable = repoR)
entry6.grid(row=6, column=1)


text7 = tk.Label(win, text = 'Price: ').grid(row=7) 
text8 = tk.Label(win)
text8.grid(row=7, column=1)


button = tk.ttk.Button(win, text="Calculate", command=lambda : mainCal(typex.get(), priceA.get(), priceK.get(), timeM.get(), vol.get(), rate.get(), repoR.get(), ))
button.grid()


win.mainloop()