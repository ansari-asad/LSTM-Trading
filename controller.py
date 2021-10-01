from nsepy import get_history
from datetime import date
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt
from nsetools import Nse
from view import CustomGui
from model import compute
from tkinter import messagebox
from pathos.multiprocessing import ProcessingPool as Pool

# Set Stocks in GUI
def initialize():
    nse = Nse()
    all_stocks = nse.get_stock_codes()
    all_stocks.pop('SYMBOL', None)
    all_stocks = [key + ' : ' + value for key, value in all_stocks.items()]
    window.feedStocks(all_stocks)

#For calculation
def processData(event):
    window.b_pred['state'] = 'disabled'
    stock = window.cb_stock.get().split(' : ')[0].lower()
    nse = Nse()
    if not nse.is_valid_code(stock):
        messagebox.showerror('Error', 'Invalid Stock Code!')
        window.b_pred['state'] = 'active'
        return
    years = int(window.e_delta.get())
    ratio = float(window.e_ratio.get())
    df = get_history(symbol=stock, start=date.today() + relativedelta(years = -years), end=date.today())

    #For running all processes at once
    o, l, h, c = Pool(4).map(compute, [df, df, df, df], ['Open', 'Low', 'High', 'Close'], [ratio, ratio, ratio, ratio])
    open, open_rms, plot_open = o
    low, low_rms, plot_low = l
    high, high_rms, plot_high = h
    close, close_rms, plot_close = c

    #for updating GUI
    window.l_open_deflection.configure(text = "{:.2f}".format(open_rms))
    window.l_low_deflection.configure(text = "{:.2f}".format(low_rms))
    window.l_high_deflection.configure(text = "{:.2f}".format(high_rms))
    window.l_close_deflection.configure(text = "{:.2f}".format(close_rms))
    window.l_open_price.configure(text = "{:.2f}".format(open))
    window.l_low_price.configure(text = "{:.2f}".format(low))
    window.l_high_price.configure(text = "{:.2f}".format(high))
    window.l_close_price.configure(text = "{:.2f}".format(close))
    
    #for plotting
    plt.suptitle(stock.upper())
    plt.subplot(2, 2, 1)
    plt.plot(plot_open[['Open','Predictions']])
    plt.gca().set_title('Open')
    plt.grid()
    plt.legend(['Actual', 'Predicted'])
    plt.subplot(2, 2, 2)
    plt.plot(plot_close[['Close','Predictions']])
    plt.gca().set_title('Close')
    plt.grid()
    plt.legend(['Actual', 'Predicted'])
    plt.subplot(2, 2, 3)
    plt.plot(plot_low[['Low','Predictions']])
    plt.gca().set_title('Low')
    plt.grid()
    plt.legend(['Actual', 'Predicted'])
    plt.subplot(2, 2, 4)
    plt.plot(plot_high[['High','Predictions']])
    plt.gca().set_title('High')
    plt.get_current_fig_manager().full_screen_toggle()
    plt.grid()
    plt.legend(['Actual', 'Predicted'])
    plt.show()

    window.b_pred['state'] = 'active'

if __name__ == '__main__':
    window = CustomGui(className = ' LSTM Intraday Stock Predictor')
    initialize()
    window.b_pred.bind('<Button-1>', processData)
    window.mainloop()