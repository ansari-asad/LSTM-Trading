import tkinter as tk
from tkinter import ttk

class CustomGui(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry('511x190')
        self.resizable(height=False, width=False)

        #Initialize the input frame
        self.f_input = tk.Frame(self, relief=tk.GROOVE, borderwidth=2)
        self.l_stk = tk.Label(self.f_input, text='Stock:')
        self.cb_stock = ttk.Combobox(self.f_input, width = 44)
        self.l_delta = tk.Label(self.f_input, text='Delta:')
        self.e_delta = tk.Entry(self.f_input, width=2)
        self.e_delta.insert(0, '10')
        self.l_yrs = tk.Label(self.f_input, text = 'years')
        self.l_ratio = tk.Label(self.f_input, text='Ratio:')
        self.e_ratio = tk.Entry(self.f_input, width=4)
        self.e_ratio.insert(0, '0.8')

        self.l_stk.grid(row = 0, column = 0, sticky = 'e')
        self.cb_stock.grid(row = 0, column = 1, sticky = 'w')
        self.l_delta.grid(row = 0, column = 2, sticky = 'e')
        self.e_delta.grid(row = 0, column = 3, sticky = 'e')
        self.l_yrs.grid(row = 0, column = 4, sticky = 'w')
        self.l_ratio.grid(row = 0, column = 5, sticky = 'e')
        self.e_ratio.grid(row = 0, column = 6, sticky = 'w')
        self.f_input.grid(row = 0, column = 0, padx = 10, pady = 10, ipadx = 5, ipady = 5)
        self.f_input.grid_rowconfigure(0, weight = 1)
        self.f_input.grid_columnconfigure(0, weight = 1)
        self.f_input.grid_columnconfigure(6, weight = 1)

        #Initialize the Predict Button
        self.b_pred = ttk.Button(self, text = 'Predict')
        self.b_pred.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = 'e')

        #Initialize the output frame
        self.f_output = tk.Frame(self, relief=tk.GROOVE, borderwidth=2)
        self.l_open = tk.Label(self.f_output, text='Open')
        self.l_low = tk.Label(self.f_output, text='Low')
        self.l_high = tk.Label(self.f_output, text='High')
        self.l_close = tk.Label(self.f_output, text='Close')
        self.l_deflection = tk.Label(self.f_output, text='RMS')
        self.l_open_deflection = tk.Label(self.f_output, text='N/A', width = 8)
        self.l_low_deflection = tk.Label(self.f_output, text='N/A', width = 8)
        self.l_high_deflection = tk.Label(self.f_output, text='N/A', width = 8)
        self.l_close_deflection = tk.Label(self.f_output, text='N/A', width = 8)
        self.l_price = tk.Label(self.f_output, text='Price')
        self.l_open_price = tk.Label(self.f_output, text='N/A', width = 8)
        self.l_low_price = tk.Label(self.f_output, text='N/A', width = 8)
        self.l_high_price = tk.Label(self.f_output, text='N/A', width = 8)
        self.l_close_price = tk.Label(self.f_output, text='N/A', width = 8)

        self.l_open.grid(row = 0, column = 1, sticky = 'we')
        self.l_low.grid(row = 0, column = 2, sticky = 'we')
        self.l_high.grid(row = 0, column = 3, sticky = 'we')
        self.l_close.grid(row = 0, column = 4, sticky = 'we')
        self.l_deflection.grid(row = 1, column = 0, sticky = 'we')
        self.l_open_deflection.grid(row = 1, column = 1, sticky = 'we')
        self.l_low_deflection.grid(row = 1, column = 2, sticky = 'we')
        self.l_high_deflection.grid(row = 1, column = 3, sticky = 'we')
        self.l_close_deflection.grid(row = 1, column = 4, sticky = 'we')
        self.l_price.grid(row = 2, column = 0, sticky = 'we')
        self.l_open_price.grid(row = 2, column = 1, sticky = 'we')
        self.l_low_price.grid(row = 2, column = 2, sticky = 'we')
        self.l_high_price.grid(row = 2, column = 3, sticky = 'we')
        self.l_close_price.grid(row = 2, column = 4, sticky = 'we')
        self.f_output.grid(row = 2, column = 0, padx = 10, pady = 10, ipadx = 5, ipady = 5)
        self.f_output.grid_rowconfigure(0, weight = 1)
        self.f_output.grid_rowconfigure(1, weight = 1)
        self.f_output.grid_rowconfigure(2, weight = 1)
        self.f_output.grid_columnconfigure(0, weight = 1)
        self.f_output.grid_columnconfigure(4, weight = 1)


    #Add Stock list to GUI
    def feedStocks(self, all_stocks):

        def update(*args):
            newvalues=[i for i in all_stocks if var.get().lower() in i.lower()]
            self.cb_stock['values'] = newvalues

        var = tk.StringVar()
        var.trace('w', update)

        self.cb_stock['values'] = all_stocks
        self.cb_stock['textvariable'] = var