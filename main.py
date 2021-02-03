# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from compute_dataframe import *
from compute_pdf import *

import numpy as np
import time
import pandas as pd
import matplotlib.pyplot as plt

import os
import glob
import sys
import datetime
import pathlib

from app import *

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.




def parse_InputData_csv_file(files_stats_dataframe, dir_path) :
    # Print the current working directory
    #print("previous working directory: {0}".format(os.getcwd()))
    # Change the current working directory
    os.chdir(dir_path)
    # Print the new current working directory
    #print("Current working directory: {0}".format(os.getcwd()))
    #print(os.getcwd())

    extension = 'csv'
    all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

    for file_name in all_filenames:

        prefix_file_name_terminal = file_name[:29]
        prefix_file_name_trades = file_name[:22]
        prefix_file_name_stocks = file_name[:26]

        # Terminal States files
        if   (prefix_file_name_terminal == "portfolio_terminal_step_state") :
            type_file = "terminal"
            #print("File_name:          ", file_name)
            #print("prefix file name:   ", prefix_file_name_terminal)
            terminal_run_date = file_name[30:38]
            #print("terminal date:      ", terminal_run_date)
            terminal_run_time = file_name[39:45]
            #print("terminal time:      ", terminal_run_time)
            terminal_market = file_name[46:49]
            #print("terminal market:    ", terminal_market)
            terminal_algo = file_name[50:53]
            #print("terminal algo:      ", terminal_algo)
            if (file_name[54:63] == "MlpPolicy") :
                terminal_policy = file_name[54:63]
                #print("terminal policy:    ", terminal_policy)
            elif (file_name[54:67] == "MlpLstmPolicy") :
                terminal_policy = file_name[54:67]
                #print("terminal policy:    ", terminal_policy)
            elif (file_name[54:69] == "MlpLnLstmPolicy") :
                terminal_policy = file_name[54:69]
                #print("terminal policy:    ", terminal_policy)
            df_new_row = pd.DataFrame(data=np.array([[file_name, prefix_file_name_terminal, type_file, terminal_run_date , terminal_run_time, terminal_policy, terminal_market, terminal_algo]]),
                                      columns=['file_name','prefix_file_name','file_type','run_date','run_time','policy','market','algo'])


        # Stocks States files
        elif (prefix_file_name_stocks == "stock_daily_trading_status") :
            type_file = "stocks"
            #print("File_name:           ", file_name)
            #print("prefix file name:    ", prefix_file_name_stocks)
            stocks_run_date = file_name[27:35]
            #print("stocks date:         ", stocks_run_date)
            stocks_run_time = file_name[36:42]
            #print("stocks time:         ", stocks_run_time)
            stocks_market = file_name[43:46]
            #print("stocks market:       ", stocks_market)
            stocks_algo = file_name[47:50]
            #print("stocks algo:         ", stocks_algo)

            if (file_name[51:60] == "MlpPolicy") :
                stocks_policy = file_name[51:60]
                #print("stocks policy:       ", stocks_policy)
            elif (file_name[51:64] == "MlpLstmPolicy") :
                stocks_policy = file_name[51:64]
                #print("stocks policy:    ", stocks_policy)
            elif (file_name[51:66] == "MlpLnLstmPolicy") :
                stocks_policy = file_name[51:66]
                #print("stocks policy:    ", stocks_policy)

            df_new_row = pd.DataFrame(data=np.array([[file_name, prefix_file_name_stocks, type_file, stocks_run_date , stocks_run_time, stocks_policy, stocks_market, stocks_algo]]),
                                      columns=['file_name','prefix_file_name','file_type','run_date','run_time','policy','market','algo'])

        # Daily trades States files
        elif (prefix_file_name_trades == "portfolio_daily_status") :
            type_file = "trades"
            #print("File_name:          ", file_name)
            #print("prefix file name:   ", prefix_file_name_trades)
            trades_run_date = file_name[23:31]
            #print("trades date:        ", trades_run_date)
            trades_run_time = file_name[32:38]
            #print("trades time:        ", trades_run_time)
            trades_market = file_name[39:42]
            #print("trades market:      ", trades_market)
            trades_algo = file_name[43:46]
            #print("trades algo:        ", trades_algo)
            if (file_name[47:56] == "MlpPolicy") :
                trades_policy = file_name[47:56]
                #print("trades policy:      ", trades_policy)
            elif (file_name[47:60] == "MlpLstmPolicy") :
                trades_policy = file_name[47:60]
                #print("trades policy:      ", trades_policy)
            elif (file_name[47:62] == "MlpLnLstmPolicy") :
                trades_policy = file_name[47:62]
                #print("trades policy:      ", trades_policy)
            df_new_row = pd.DataFrame(data=np.array([[file_name, prefix_file_name_trades, type_file, trades_run_date , trades_run_time, trades_policy, trades_market, trades_algo]]),
                                      columns=['file_name','prefix_file_name','file_type','run_date','run_time','policy','market','algo'])
        files_stats_dataframe = files_stats_dataframe.append(df_new_row, ignore_index=True)
    return files_stats_dataframe

def dataframe_save_to_csv(files_dataframe, dir_path, file_name_csv) :

    #print("previous working directory: {0}".format(os.getcwd()))
    # Change the current working directory
    current_path = os.getcwd()
    os.chdir(dir_path)

    # Print the new current working directory
    #print("Current working directory: {0}".format(os.getcwd()))

    if os.path.exists(file_name_csv):
      os.remove(file_name_csv)

    files_dataframe.to_csv(file_name_csv)
    #print("output file created  ", file_name_csv)
    os.chdir(current_path)
    #print("back to previous working directory: {0}".format(current_path))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    app.run_server(debug=True)


    #print_hi('PyCharm')




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
