import tkinter as tk 
from tkinter import ttk
import euro_option_pricer as eop
import implied_vol as ipv
import binarytree_option_pricer as bop
import geoasian_option_pricer as gaop
import aritasian_option_pricer as aaop
import geobasket_option_pricer as gbop
import aritbasket_option_pricer as abop

def euroWin():
    euroW = tk.Toplevel()
    euroW.title("European Option Pricer")

    etext0 = tk.Label(euroW, text = 'Choose Asset Type: ').grid(row=0) 
    etypex = tk.StringVar()
    echooseType = ttk.Combobox(euroW, width = 26, textvariable = etypex)
    echooseType['values'] = ('Call Option', 'Put Option')
    echooseType.grid(row=0, column=1)


    etext1 = tk.Label(euroW, text = 'Asset Price: ').grid(row=1) 
    epriceA = tk.StringVar()
    eentry1 = tk.Entry(euroW, textvariable = epriceA) 
    eentry1.grid(row=1, column=1)


    etext2 = tk.Label(euroW, text = 'Strike Price: ').grid(row=2) 
    epriceK = tk.StringVar()
    eentry2 = tk.Entry(euroW, textvariable = epriceK)
    eentry2.grid(row=2, column=1)


    etext3 = tk.Label(euroW, text = 'Maturity Time: ').grid(row=3) 
    etimeM = tk.StringVar()
    eentry3 = tk.Entry(euroW, textvariable = etimeM)
    eentry3.grid(row=3, column=1)


    etext4 = tk.Label(euroW, text = 'Volatility: ').grid(row=4) 
    evol = tk.StringVar()
    eentry4 = tk.Entry(euroW, textvariable = evol)
    eentry4.grid(row=4, column=1)


    etext5 = tk.Label(euroW, text = 'Risk Free Rate: ').grid(row=5)
    erate = tk.StringVar()
    eentry5 = tk.Entry(euroW, textvariable = erate)
    eentry5.grid(row=5, column=1)


    etext6 = tk.Label(euroW, text = 'Repo Rate: ').grid(row=6) 
    erepoR = tk.StringVar()
    eentry6 = tk.Entry(euroW, textvariable = erepoR)
    eentry6.grid(row=6, column=1)


    etext7 = tk.Label(euroW, text = 'Price:').grid(row=7) 
    etext8 = tk.Label(euroW)
    etext8.grid(row=7, column=1)


    ebutton = tk.ttk.Button(euroW, text="Calculate", command=lambda : euroCal(etext8, etypex.get(), epriceA.get(), epriceK.get(), etimeM.get(), evol.get(), erate.get(), erepoR.get()))
    ebutton.grid()

def ivWin():
    ivW = tk.Toplevel()
    ivW.title("Implied Volatility Calculation")

    text0 = tk.Label(ivW, text = 'Choose Asset Type: ').grid(row=0) 
    typex = tk.StringVar()
    chooseType = ttk.Combobox(ivW, width = 26, textvariable = typex)
    chooseType['values'] = ('Call Option', 'Put Option')
    chooseType.grid(row=0, column=1)


    text1 = tk.Label(ivW, text = 'Asset Price: ').grid(row=1) 
    priceA = tk.StringVar()
    entry1 = tk.Entry(ivW, textvariable = priceA) 
    entry1.grid(row=1, column=1)


    text2 = tk.Label(ivW, text = 'Strike Price: ').grid(row=2) 
    priceK = tk.StringVar()
    entry2 = tk.Entry(ivW, textvariable = priceK)
    entry2.grid(row=2, column=1)


    text3 = tk.Label(ivW, text = 'Maturity Time: ').grid(row=3) 
    timeM = tk.StringVar()
    entry3 = tk.Entry(ivW, textvariable = timeM)
    entry3.grid(row=3, column=1)


    text4 = tk.Label(ivW, text = 'Risk Free Rate: ').grid(row=4)
    rate = tk.StringVar()
    entry4 = tk.Entry(ivW, textvariable = rate)
    entry4.grid(row=4, column=1)


    text5 = tk.Label(ivW, text = 'Repo Rate: ').grid(row=5) 
    repoR = tk.StringVar()
    entry5 = tk.Entry(ivW, textvariable = repoR)
    entry5.grid(row=5, column=1)


    text6 = tk.Label(ivW, text = 'Observable Value: ').grid(row=6) 
    observeP = tk.StringVar()
    entry6 = tk.Entry(ivW, textvariable = observeP)
    entry6.grid(row=6, column=1)


    text7 = tk.Label(ivW, text = 'Implied Volatility: ').grid(row=7) 
    text8 = tk.Label(ivW)
    text8.grid(row=7, column=1)


    button = tk.ttk.Button(ivW, text="Calculate", command=lambda : ivCal(text8, typex.get(), priceA.get(), priceK.get(), timeM.get(), rate.get(), repoR.get(), observeP.get()))
    button.grid()

def biWin():
    biW = tk.Toplevel()
    biW.title("Binary Tree Option Pricer")

    text0 = tk.Label(biW, text = 'Choose Asset Type: ').grid(row=0) 
    typex = tk.StringVar()
    chooseType = ttk.Combobox(biW, width = 26, textvariable = typex)
    chooseType['values'] = ('American Call Option', 'American Put Option', 'European Call Option', 'European Put Option')
    chooseType.grid(row=0, column=1)


    text1 = tk.Label(biW, text = 'Asset Price: ').grid(row=1) 
    priceA = tk.StringVar()
    entry1 = tk.ttk.Entry(biW, textvariable = priceA) 
    entry1.grid(row=1, column=1)


    text2 = tk.Label(biW, text = 'Strike Price: ').grid(row=2) 
    priceK = tk.StringVar()
    entry2 = tk.ttk.Entry(biW, textvariable = priceK)
    entry2.grid(row=2, column=1)


    text3 = tk.Label(biW, text = 'Maturity Time: ').grid(row=3) 
    timeM = tk.StringVar()
    entry3 = tk.ttk.Entry(biW, textvariable = timeM)
    entry3.grid(row=3, column=1)


    text4 = tk.Label(biW, text = 'Volatility: ').grid(row=4) 
    vol = tk.StringVar()
    entry4 = tk.ttk.Entry(biW, textvariable = vol)
    entry4.grid(row=4, column=1)


    text5 = tk.Label(biW, text = 'Risk Free Rate: ').grid(row=5)
    rate = tk.StringVar()
    entry5 = tk.ttk.Entry(biW, textvariable = rate)
    entry5.grid(row=5, column=1)


    text6 = tk.Label(biW, text = 'Repo Rate: ').grid(row=6) 
    repoR = tk.StringVar()
    entry6 = tk.ttk.Entry(biW, textvariable = repoR)
    entry6.grid(row=6, column=1)


    text7 = tk.Label(biW, text = 'Steps: ').grid(row=7) 
    st = tk.StringVar()
    entry7 = tk.ttk.Entry(biW, textvariable = st)
    entry7.grid(row=7, column=1)


    text8 = tk.Label(biW, text = 'Price: ').grid(row=8) 
    text9 = tk.Label(biW)
    text9.grid(row=8, column=1)


    button = tk.ttk.Button(biW, text="Calculate", command=lambda : biCal(text9, typex.get(), priceA.get(), priceK.get(), timeM.get(), vol.get(), rate.get(), repoR.get(), st.get()))
    button.grid()

def geoAsianWin():
    geoaW = tk.Toplevel()
    geoaW.title("Geometirc Asian Option Pricer")

    text0 = tk.Label(geoaW, text = 'Choose Asset Type: ').grid(row=0) 
    typex = tk.StringVar()
    chooseType = ttk.Combobox(geoaW, width = 26, textvariable = typex)
    chooseType['values'] = ('Call Option', 'Put Option')
    chooseType.grid(row=0, column=1)


    text1 = tk.Label(geoaW, text = 'Asset Price: ').grid(row=1) 
    priceA = tk.StringVar()
    entry1 = tk.Entry(geoaW, textvariable = priceA) 
    entry1.grid(row=1, column=1)


    text2 = tk.Label(geoaW, text = 'Strike Price: ').grid(row=2) 
    priceK = tk.StringVar()
    entry2 = tk.Entry(geoaW, textvariable = priceK)
    entry2.grid(row=2, column=1)


    text3 = tk.Label(geoaW, text = 'Maturity Time: ').grid(row=3) 
    timeM = tk.StringVar()
    entry3 = tk.Entry(geoaW, textvariable = timeM)
    entry3.grid(row=3, column=1)


    text4 = tk.Label(geoaW, text = 'Volatility: ').grid(row=4) 
    vol = tk.StringVar()
    entry4 = tk.Entry(geoaW, textvariable = vol)
    entry4.grid(row=4, column=1)


    text5 = tk.Label(geoaW, text = 'Risk Free Rate: ').grid(row=5)
    rate = tk.StringVar()
    entry5 = tk.Entry(geoaW, textvariable = rate)
    entry5.grid(row=5, column=1)


    text6 = tk.Label(geoaW, text = 'n Value: ').grid(row=6) 
    n = tk.StringVar()
    entry6 = tk.Entry(geoaW, textvariable = n)
    entry6.grid(row=6, column=1)


    text7 = tk.Label(geoaW, text = 'Price:').grid(row=7) 
    text8 = tk.Label(geoaW)
    text8.grid(row=7, column=1)


    button = tk.ttk.Button(geoaW, text="Calculate", command=lambda : geoaCal(text8, typex.get(), priceA.get(), timeM.get(), priceK.get(), rate.get(), vol.get(), n.get()))
    button.grid()

def arithAsianWin():
    arithAW = tk.Toplevel()
    arithAW.title("Arithmetic Asian Option Pricer")

    text0 = tk.Label(arithAW, text = 'Choose Asset Type: ').grid(row=0) 
    typex = tk.StringVar()
    chooseType = ttk.Combobox(arithAW, width = 26, textvariable = typex)
    chooseType['values'] = ('Call Option', 'Put Option')
    chooseType.grid(row=0, column=1)


    text1 = tk.Label(arithAW, text = 'Asset Price: ').grid(row=1) 
    priceA = tk.StringVar()
    entry1 = ttk.Entry(arithAW, textvariable = priceA) 
    entry1.grid(row=1, column=1)


    text2 = tk.Label(arithAW, text = 'Strike Price: ').grid(row=2) 
    priceK = tk.StringVar()
    entry2 = ttk.Entry(arithAW, textvariable = priceK)
    entry2.grid(row=2, column=1)


    text3 = tk.Label(arithAW, text = 'Maturity Time: ').grid(row=3) 
    timeM = tk.StringVar()
    entry3 = ttk.Entry(arithAW, textvariable = timeM)
    entry3.grid(row=3, column=1)


    text4 = tk.Label(arithAW, text = 'Volatility: ').grid(row=4) 
    vol = tk.StringVar()
    entry4 = ttk.Entry(arithAW, textvariable = vol)
    entry4.grid(row=4, column=1)


    text5 = tk.Label(arithAW, text = 'Risk Free Rate: ').grid(row=5)
    rate = tk.StringVar()
    entry5 = ttk.Entry(arithAW, textvariable = rate)
    entry5.grid(row=5, column=1)


    text6 = tk.Label(arithAW, text = 'n Value: ').grid(row=6) 
    n = tk.StringVar()
    entry6 = ttk.Entry(arithAW, textvariable = n)
    entry6.grid(row=6, column=1)


    text7 = tk.Label(arithAW, text = 'Control Variate').grid(row=7) 
    ctl_var = tk.BooleanVar()
    ctl_var.set(True)
    check7 = ttk.Checkbutton(arithAW, variable=ctl_var).grid(row=7, column=1)
    

    text8 = tk.Label(arithAW, text = 'Monte Carlo Path: ').grid(row=8) 
    path = tk.StringVar()
    entry8 = ttk.Entry(arithAW, textvariable = path)
    entry8.grid(row=8, column=1)
    path.set(1000)


    text9 = tk.Label(arithAW, text = 'Price: ').grid(row=9)
    text10 = tk.Label(arithAW)
    text10.grid(row=9, column=1)


    text11 = tk.Label(arithAW, text = '95% Confidence Interval: ').grid(row=10)
    text12 = tk.Label(arithAW)
    text12.grid(row=10, column=1)


    button = tk.ttk.Button(arithAW, text="Calculate", command=lambda : arithaCal(text10, text12, typex.get(), priceA.get(), timeM.get(), priceK.get(), rate.get(), vol.get(), n.get(), path.get(), ctl_var.get()))
    #button = tk.ttk.Button(arithAW, text="Calculate", command=lambda : prin())
    button.grid()

def geoBaskWin():
    geoBW = tk.Toplevel()
    geoBW.title("Geometirc Basket Option Pricer")

    text0 = tk.Label(geoBW, text = 'Choose Asset Type: ').grid(row=0) 
    typex = tk.StringVar()
    chooseType = ttk.Combobox(geoBW, width = 26, textvariable = typex)
    chooseType['values'] = ('Call Option', 'Put Option')
    chooseType.grid(row=0, column=1)


    text1 = tk.Label(geoBW, text = '1st Asset Price: ').grid(row=1) 
    priceA1 = tk.StringVar()
    entry1 = tk.Entry(geoBW, textvariable = priceA1) 
    entry1.grid(row=1, column=1)


    text2 = tk.Label(geoBW, text = '2nd Asset Price: ').grid(row=2) 
    priceA2 = tk.StringVar()
    entry2 = tk.Entry(geoBW, textvariable = priceA2) 
    entry2.grid(row=2, column=1)

    text3 = tk.Label(geoBW, text = 'Strike Price: ').grid(row=3) 
    priceK = tk.StringVar()
    entry3 = tk.Entry(geoBW, textvariable = priceK)
    entry3.grid(row=3, column=1)


    text4 = tk.Label(geoBW, text = 'Maturity Time: ').grid(row=4) 
    timeM = tk.StringVar()
    entry4 = tk.Entry(geoBW, textvariable = timeM)
    entry4.grid(row=4, column=1)


    text5 = tk.Label(geoBW, text = '1st Volatility: ').grid(row=5) 
    vol1 = tk.StringVar()
    entry5 = tk.Entry(geoBW, textvariable = vol1)
    entry5.grid(row=5, column=1)


    text6 = tk.Label(geoBW, text = '2nd Volatility: ').grid(row=6) 
    vol2 = tk.StringVar()
    entry6 = tk.Entry(geoBW, textvariable = vol2)
    entry6.grid(row=6, column=1)


    text7 = tk.Label(geoBW, text = 'Risk Free Rate: ').grid(row=7)
    rate = tk.StringVar()
    entry7 = tk.Entry(geoBW, textvariable = rate)
    entry7.grid(row=7, column=1)


    text8 = tk.Label(geoBW, text = 'Correlation: ').grid(row=8)
    rol = tk.StringVar()
    entry8 = tk.Entry(geoBW, textvariable = rol)
    entry8.grid(row=8, column=1)


    text9 = tk.Label(geoBW, text = 'Price: ').grid(row=9) 
    text10 = tk.Label(geoBW)
    text10.grid(row=9, column=1)

    #future_type, asset_price1, asset_price2,mature_time,strike_price,rate,vol1,vol2,rol
    button = tk.ttk.Button(geoBW, text="Calculate", command=lambda : geobCal(text10, typex.get(), priceA1.get(), priceA2.get(), \
                    timeM.get(), priceK.get(), rate.get(), vol1.get(), vol2.get(), rol.get()))
    button.grid()

def arithBaskWin():
    arithBW = tk.Toplevel()
    arithBW.title("Arithmetirc Basket Option Pricer")

    text0 = tk.Label(arithBW, text = 'Choose Asset Type: ').grid(row=0) 
    typex = tk.StringVar()
    chooseType = ttk.Combobox(arithBW, width = 26, textvariable = typex)
    chooseType['values'] = ('Call Option', 'Put Option')
    chooseType.grid(row=0, column=1)


    text1 = tk.Label(arithBW, text = '1st Asset Price: ').grid(row=1) 
    priceA1 = tk.StringVar()
    entry1 = tk.Entry(arithBW, textvariable = priceA1) 
    entry1.grid(row=1, column=1)


    text2 = tk.Label(arithBW, text = '2nd Asset Price: ').grid(row=2) 
    priceA2 = tk.StringVar()
    entry2 = tk.Entry(arithBW, textvariable = priceA2) 
    entry2.grid(row=2, column=1)

    text3 = tk.Label(arithBW, text = 'Strike Price: ').grid(row=3) 
    priceK = tk.StringVar()
    entry3 = tk.Entry(arithBW, textvariable = priceK)
    entry3.grid(row=3, column=1)


    text4 = tk.Label(arithBW, text = 'Maturity Time: ').grid(row=4) 
    timeM = tk.StringVar()
    entry4 = tk.Entry(arithBW, textvariable = timeM)
    entry4.grid(row=4, column=1)


    text5 = tk.Label(arithBW, text = '1st Volatility: ').grid(row=5) 
    vol1 = tk.StringVar()
    entry5 = tk.Entry(arithBW, textvariable = vol1)
    entry5.grid(row=5, column=1)


    text6 = tk.Label(arithBW, text = '2nd Volatility: ').grid(row=6) 
    vol2 = tk.StringVar()
    entry6 = tk.Entry(arithBW, textvariable = vol2)
    entry6.grid(row=6, column=1)


    text7 = tk.Label(arithBW, text = 'Risk Free Rate: ').grid(row=7)
    rate = tk.StringVar()
    entry7 = tk.Entry(arithBW, textvariable = rate)
    entry7.grid(row=7, column=1)


    text8 = tk.Label(arithBW, text = 'Correlation: ').grid(row=8)
    rol = tk.StringVar()
    entry8 = tk.Entry(arithBW, textvariable = rol)
    entry8.grid(row=8, column=1)


    text9 = tk.Label(arithBW, text = 'Control Variate: ').grid(row=9) 
    ctl_var = tk.BooleanVar()
    ctl_var.set(True)
    check9 = ttk.Checkbutton(arithBW, variable=ctl_var).grid(row=9, column=1)



    text10 = tk.Label(arithBW, text = 'Monte Carlo Path: ').grid(row=10) 
    path = tk.StringVar()
    entry10 = ttk.Entry(arithBW, textvariable = path)
    entry10.grid(row=10, column=1)
    path.set(10000)

    text11 = tk.Label(arithBW, text = 'Price: ').grid(row=11) 
    text12 = tk.Label(arithBW)
    text12.grid(row=11, column=1)


    text13 = tk.Label(arithBW, text = '95% Confidence Interval: ').grid(row=12)
    text14 = tk.Label(arithBW)
    text14.grid(row=12, column=1)

    #future_type, asset_price1, asset_price2,mature_time,strike_price,rate,vol1,vol2,rol
    button = tk.ttk.Button(arithBW, text="Calculate", command=lambda : arithbCal(text12, text14, typex.get(), priceA1.get(), priceA2.get(), \
                    timeM.get(), priceK.get(), rate.get(), vol1.get(), vol2.get(), rol.get(), path.get(), ctl_var.get()))
    button.grid()
    
def euroCal(text, typ, asset_price, strike_price, mature_time, vol, rate, repo_q):
    if typ == 'Call Option':
        tp = 'c'
    elif typ == 'Put Option':
        tp = 'p'
    
    asset_price = float(asset_price)
    strike_price = float(strike_price)
    mature_time = float(mature_time)
    vol = float(vol)
    rate = float(rate)
    repo_q = float(repo_q)

    eopx = eop.euro_opt(tp, asset_price, strike_price, mature_time, vol, rate,repo_q)

    text['text'] = eopx.value()
    pass

def ivCal(text, typ, asset_price, strike_price, mature_time, rate, repo_q, observeP):
    if typ == 'Call Option':
        tp = 'c'
    elif typ == 'Put Option':
        tp = 'p'
    
    asset_price = float(asset_price)
    strike_price = float(strike_price)
    mature_time = float(mature_time)
    rate = float(rate)
    repo_q = float(repo_q)
    observeP = float(observeP)

    #Type,S0,K,T,r,q,V
    iv = ipv.imp_vol(tp, asset_price, strike_price, mature_time, rate, repo_q, observeP)

    text['text'] = iv

def biCal(text, typ, asset_price, strike_price, mature_time, vol, rate, repo_q, st):
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
    st = int(st)

    #Type,S0,K,T,r,q,V
    bopx = bop.BinaryTree(tp, asset_price, strike_price, mature_time, vol, rate, repo_q)

    text['text'] = bopx.bt(steps=st)

def geoaCal(text, typ, asset_price, mature_time, strike_price, rate, vol, n):
    if typ == 'Call Option':
        tp = 'c'
    elif typ == 'Put Option':
        tp = 'p'
    
    asset_price = float(asset_price)
    strike_price = float(strike_price)
    mature_time = float(mature_time)
    vol = float(vol)
    rate = float(rate)
    n = float(n)

    gaopx = gaop.geoasian_opt(tp, asset_price, mature_time, strike_price, rate, vol, n)

    text['text'] = gaopx.value()

def arithaCal(text1, text2, typ, asset_price, mature_time, strike_price, rate, vol, n, path, ctl_var):
    
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
    text1['text'] = value[0]
    text2['text'] = value[1]

def geobCal(text, typ, asset_price1, asset_price2, mature_time, strike_price, rate, vol1, vol2, rol):
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

    #future_type, asset_price1, asset_price2,mature_time,strike_price,rate,vol1,vol2,rol
    gbopx = gbop.geobasket_opt(tp, asset_price1, asset_price2, mature_time, strike_price, rate, vol1, vol2, rol)

    text['text'] = gbopx.value()

def arithbCal(text1, text2, typ, asset_price1, asset_price2, mature_time, strike_price, rate, vol1, vol2, rol, path, ctl_var):
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

    text1['text'] = value[0]
    text2['text'] = value[1]

win = tk.Tk()
win.title("Assigment 3")
win.config(bg='ghost white')
win.geometry("400x380") 
win.resizable(0, 0) 

text0 = tk.Label(win, text='European Option Pricer:', font=("Helvetica", 16), height=2)
text0.grid(row=0)
text0.config(bg='ghost white')
button0 = tk.Button(win, text="Open", font=("Helvetica", 13), command=euroWin, relief='groove')
button0.grid(row=0, column=1)


text1 = tk.Label(win, text='Implied Volatility Calculation:', font=("Helvetica", 16), height=2)
text1.grid(row=1)
text1.config(bg='ghost white')
button1 = tk.Button(win, relief='groove',  text="Open", font=("Helvetica", 13), command=ivWin)
button1.grid(row=1, column=1)


text2 = tk.Label(win, text='Binary Tree Option Pricer:', font=("Helvetica", 16), height=2)
text2.grid(row=2)
text2.config(bg='ghost white')
button2 = tk.Button(win, relief='groove',  text="Open", font=("Helvetica", 13), command=biWin)
button2.grid(row=2, column=1)


text3 = tk.Label(win, text='Geometirc Asian Option Pricer:', font=("Helvetica", 16), height=2)
text3.grid(row=3)
text3.config(bg='ghost white')
button3 = tk.Button(win, relief='groove',  text="Open", font=("Helvetica", 13), command=geoAsianWin)
button3.grid(row=3, column=1)


text4 = tk.Label(win, text='Arithmetic Asian Option Pricer:', font=("Helvetica", 16), height=2)
text4.grid(row=4)
text4.config(bg='ghost white')
button4 = tk.Button(win, relief='groove',  text="Open", font=("Helvetica", 13), command=arithAsianWin)
button4.grid(row=4, column=1)


text5 = tk.Label(win, text='Geometirc Basket Option Pricer:', font=("Helvetica", 16), height=2)
text5.grid(row=5)
text5.config(bg='ghost white')
button1 = tk.Button(win, relief='groove',  text="Open", font=("Helvetica", 13), command=geoBaskWin)
button1.grid(row=5, column=1)


text6 = tk.Label(win, text='Arithmetirc Basket Option Pricer:', font=("Helvetica", 16), height=2)
text6.grid(row=6)
text6.config(bg='ghost white')
button6 = tk.Button(win, relief='groove',  text="Open", font=("Helvetica", 13), command=arithBaskWin)
button6.grid(row=6, column=1)


win.mainloop()