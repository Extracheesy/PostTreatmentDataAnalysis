MOVE_MERGE_PDF = "OFF"

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
from main import *


MOVE_MERGE_PDF = "OFF"

def data_calculation_percent (value1 , value2):
    return((value1 - value2) *100 / value2)

def data_calculation_percent_normal (value1 , value2):
    return((value1) *100 / value2)

def get_count(df_data, column, filter):

    df_filter = df_data.loc[df_data[column] == filter]
    return (df_filter['counts'].sum() / 3)

def get_info_df(df_info_whole_data, filter_type):

    if (filter_type == "algo"):
        nb_PPO = get_count(df_info_whole_data, "algo", "PPO")
        nb_A2C = get_count(df_info_whole_data, "algo", "A2C")
        df_retun_data = pd.DataFrame({"filter": ["PPO",
                                                 "A2C"],
                                      "color_bar": ["10",
                                                    "20"],
                                      "iter": [np.int64(nb_PPO),
                                               np.int64(nb_A2C)]})
    elif (filter_type == "policy"):
        nb_MlpPolicy = get_count(df_info_whole_data, "policy", "MlpPolicy")
        nb_MlpLstmPolicy = get_count(df_info_whole_data, "policy", "MlpLstmPolicy")
        nb_MlpLnLstmPolicy = get_count(df_info_whole_data, "policy", "MlpLnLstmPolicy")
        df_retun_data = pd.DataFrame({"filter": ["MlpPolicy",
                                                 "MlpLstmPolicy",
                                                 "MlpLnLstmPolicy"],
                                      "color_bar": ["10",
                                                    "20",
                                                    "30"],
                                      "iter": [np.int64(nb_MlpPolicy),
                                               np.int64(nb_MlpLstmPolicy),
                                               np.int64(nb_MlpLnLstmPolicy)]})

    elif (filter_type == "market"):
        nb_CAC = get_count(df_info_whole_data, "market", "CAC")
        nb_DJI = get_count(df_info_whole_data, "market", "DJI")
        nb_DAX = get_count(df_info_whole_data, "market", "DAX")
        df_retun_data = pd.DataFrame({"filter": ["CAC",
                                                 "DJI",
                                                 "DAX"],
                                      "color_bar": ["10",
                                                    "20",
                                                    "30"],
                                      "iter": [np.int64(nb_CAC),
                                               np.int64(nb_DJI),
                                               np.int64(nb_DAX)]})
    return(df_retun_data)

def get_info_text(df_info_whole_data):

    nb_PPO = get_count(df_info_whole_data, "algo", "PPO")
    nb_A2C = get_count(df_info_whole_data, "algo", "A2C")

    nb_MlpPolicy = get_count(df_info_whole_data, "policy", "MlpPolicy")
    nb_MlpLstmPolicy = get_count(df_info_whole_data, "policy", "MlpLstmPolicy")
    nb_MlpLnLstmPolicy = get_count(df_info_whole_data, "policy", "MlpLnLstmPolicy")

    nb_CAC = get_count(df_info_whole_data, "market", "CAC")
    nb_DJI = get_count(df_info_whole_data, "market", "DJI")
    nb_DAX = get_count(df_info_whole_data, "market", "DAX")

    info_text_0 = "nbr total run: " + str(np.int64(nb_PPO + nb_A2C))
    info_text_1 = "PPO iteration: " + str(np.int64(nb_PPO)) + " / A2C iteration: "+ str(np.int64(nb_A2C))
    info_text_2 = "MlpPolicy iteration: " + str(np.int64(nb_MlpPolicy)) + " / MlpLstmPolicy iteration: " + str(np.int64(nb_MlpLstmPolicy)) + " / MlpLnLstmPolicy iteration: " + str(np.int64(nb_MlpLnLstmPolicy))
    info_text_3 = "CAC iteration: " + str(np.int64(nb_CAC)) + " / DJI iteration: " + str(np.int64(nb_DJI)) + " / DAX iteration: " + str(np.int64(nb_DAX))

    info_text = [info_text_0, info_text_1, info_text_2, info_text_3]
    return(info_text)



def Init_data():

    print("Initialiation STARTING kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")

    input_dir  = 'C:/Users/despo/PycharmProjects/pythonProject2/InputData'
    output_dir = 'C:/Users/despo/PycharmProjects/pythonProject2/OutputData'
    formated_time = time.strftime("%Y%m%d-%H%M%S")
    output_dir = output_dir + "/" + formated_time
    os.mkdir(output_dir)

    output_dir_terminal_state = output_dir + "/terminal_state"
    output_dir_stocks_state   = output_dir + "/stocks_state"
    output_dir_trades_states  = output_dir + "/trades_states"
    output_dir_terminal_state_pdfs  = output_dir_terminal_state + "/pdfs"
    os.mkdir(output_dir_terminal_state)
    os.mkdir(output_dir_stocks_state)
    os.mkdir(output_dir_trades_states)
    os.mkdir(output_dir_terminal_state_pdfs)

    file_extention = ".csv"

    ####################################################
    # Parse whole Data files and group all in one file #
    ####################################################
    df_files_list = pd.DataFrame(columns=['file_name','prefix_file_name','file_type','run_date','run_time','policy','market','algo'])
    df_files_list = parse_InputData_csv_file(df_files_list,input_dir)
    output_file_name = "full_list_data_file_" + formated_time + file_extention
    dataframe_save_to_csv(df_files_list,output_dir,output_file_name)

    ####################################
    # group / pivot to count iteration #
    ####################################
    df_group_test = df_files_list
    df_group_test = df_group_test.groupby(['policy', 'algo', 'market']).size().reset_index(name='counts')
    output_file_name = "pivot_" + formated_time + file_extention
    dataframe_save_to_csv(df_group_test, output_dir, output_file_name)


    ####################################################
    # Parse and save as .csv the whole terminal files  #
    ####################################################
    df_full_terminal_data = fill_terminal_dataframe(df_files_list,input_dir,output_dir_terminal_state,formated_time)
    # analyse_terminal_dataframe(df_full_terminal_data,output_dir_terminal_state,formated_time)


    #################################################
    # Parse and save as .csv the whole stocks files #
    #################################################
#    df_full_stocks_data = fill_stocks_dataframe(df_files_list,input_dir,output_dir_terminal_state,formated_time)
    df_empty = pd.DataFrame({'A' : []})
    df_full_stocks_data = df_empty.empty

    #################################################
    # Parse and save as .csv the whole trades files #
    #################################################
    df_full_trades_data = fill_trades_dataframe(df_files_list,input_dir,output_dir_trades_states,formated_time)




    INIT_DATA = "OFF"
    print("Initialiation completed init set to ",INIT_DATA," kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")


    return (df_group_test, df_full_terminal_data, df_full_stocks_data, df_full_trades_data)


def filter_raw_dataframe(df_data, filter):

    if (filter == "NO FILTER"):
        df_filtered_data = df_data[(df_data.iter_num == 1197)]
        return (df_filtered_data)

    if ((filter == "MlpPolicy") or (filter == "MlpLstmPolicy") or (filter == "MlpLnLstmPolicy")):
        df_filtered_data =  df_data[ (df_data.policy == filter) & (df_data.iter_num == 1197)]
        return (df_filtered_data)

    if ((filter == "CAC") or (filter == "DAX") or (filter == "DJI")):
        df_filtered_data = df_data[(df_data.market == filter)  & (df_data.iter_num == 1197)]
        return (df_filtered_data)

    if ((filter == "PPO") or (filter == "A2C")):
        df_filtered_data = df_data[(df_data.algo == filter) & (df_data.iter_num == 1197)]
        return (df_filtered_data)


def filter_dataframe(df_data, filter):

    if (filter == "NO FILTER"):
        return (df_data)

    if ((filter == "MlpPolicy") or (filter == "MlpLstmPolicy") or (filter == "MlpLnLstmPolicy")):
        df_filtered_data =  df_data[ (df_data.policy == filter)]
        return (df_filtered_data)

    if ((filter == "CAC") or (filter == "DAX") or (filter == "DJI")):
        df_filtered_data = df_data[(df_data.market == filter)]
        return (df_filtered_data)

    if ((filter == "PPO") or (filter == "A2C")):
        df_filtered_data = df_data[(df_data.algo == filter)]
        return (df_filtered_data)

def filter_dataframe_date(df_data, filter_date, filter_time):

    print("df_data            ", df_data)


    for i in df_data.run_time:
        if i == filter_time :
            print("yes 2:   ",i)

    df_filtered_data_1 =  df_data[ (df_data.run_date == filter_date) & (df_data.run_time == filter_time)]


    print("df_filtered_data_1           ", df_filtered_data_1)

    df_filtered_data_1.sort_values(by=['iter_num'], inplace=True, ascending=True)

    return (df_filtered_data_1)


def df_compute_terminal_end_total_asset_graph(df_filtered_full_terminal_data):

    column_end_total_asset = df_filtered_full_terminal_data["end_total_asset"]

    max_end_total_asset = column_end_total_asset.max()
    max_percent_end_total_asset = calculation_percent(max_end_total_asset,INITIAL_INVESTMENT)
    min_end_total_asset = column_end_total_asset.min()
    min_percent_end_total_asset = calculation_percent(min_end_total_asset,INITIAL_INVESTMENT)
    mean_end_total_asset = column_end_total_asset.mean()
    mean_percent_end_total_asset = calculation_percent(mean_end_total_asset,INITIAL_INVESTMENT)
    # median_end_total_asset = column_end_total_asset.median()
    median_end_total_asset = min_end_total_asset + (max_end_total_asset - min_end_total_asset) /2
    median_percent_end_total_asset = calculation_percent(median_end_total_asset,INITIAL_INVESTMENT)
    count_end_total_asset = column_end_total_asset.count()

    quantile_1_end_total_asset = min_end_total_asset + (max_end_total_asset - min_end_total_asset) / 5
    quantile_2_end_total_asset = min_end_total_asset + (max_end_total_asset - min_end_total_asset) / 5 * 2
    quantile_3_end_total_asset = min_end_total_asset + (max_end_total_asset - min_end_total_asset) / 5 * 3
    quantile_4_end_total_asset = min_end_total_asset + (max_end_total_asset - min_end_total_asset) / 5 * 4

    # count_quantile_0 nb of values between min and quantile_1


    values_between_quantiles_between_min_q1 = column_end_total_asset[(column_end_total_asset <= quantile_1_end_total_asset)]
    count_quantile_0_end_total_asset = values_between_quantiles_between_min_q1.count()

    # count_quantile_1 nb of values between quantile_1 and quantile_2
    values_between_quantiles_between_q1_q2 = column_end_total_asset[
        ((column_end_total_asset > quantile_1_end_total_asset) & (column_end_total_asset <= quantile_2_end_total_asset))]
    count_quantile_1_end_total_asset = values_between_quantiles_between_q1_q2.count()

    # count_quantile_2 nb of values between quantile_2 and quantile_3
    values_between_quantiles_between_q2_q3 = column_end_total_asset[
        ((column_end_total_asset > quantile_2_end_total_asset) & (column_end_total_asset <= quantile_3_end_total_asset))]
    count_quantile_2_end_total_asset = values_between_quantiles_between_q2_q3.count()

    # count_quantile_3 nb of values between quantile_3 and quantile_4
    values_between_quantiles_between_q3_q4 = column_end_total_asset[
        ((column_end_total_asset > quantile_3_end_total_asset) & (column_end_total_asset <= quantile_4_end_total_asset))]
    count_quantile_3_end_total_asset = values_between_quantiles_between_q3_q4.count()

    # count_quantile_4 nb of values between quantile_4 and max
    values_between_quantiles_between_q4_max = column_end_total_asset[(column_end_total_asset > quantile_4_end_total_asset)]
    count_quantile_4_end_total_asset = values_between_quantiles_between_q4_max.count()

    count_percent_quantile_0_end_total_asset = calculation_percent_normal(count_quantile_0_end_total_asset , count_end_total_asset)
    count_percent_quantile_1_end_total_asset = calculation_percent_normal(count_quantile_1_end_total_asset , count_end_total_asset)
    count_percent_quantile_2_end_total_asset = calculation_percent_normal(count_quantile_2_end_total_asset , count_end_total_asset)
    count_percent_quantile_3_end_total_asset = calculation_percent_normal(count_quantile_3_end_total_asset , count_end_total_asset)
    count_percent_quantile_4_end_total_asset = calculation_percent_normal(count_quantile_4_end_total_asset , count_end_total_asset)

    df_return_analysed_data_table = pd.DataFrame({"table_content": ["max_value",
                                                                    "bottom",
                                                                    "mean",
                                                                    "median",
                                                                    "variation",
                                                                    "iteration"],
                                                  "values": [max_end_total_asset,
                                                             min_end_total_asset,
                                                             mean_end_total_asset,
                                                             median_end_total_asset,
                                                             max_end_total_asset - min_end_total_asset,
                                                             count_end_total_asset],
                                                  "_%_": [max_percent_end_total_asset,
                                                          min_percent_end_total_asset,
                                                          mean_percent_end_total_asset,
                                                          median_percent_end_total_asset,
                                                          0,
                                                          0],
                                                  "_yearly_%_": [max_percent_end_total_asset/4,
                                                                 min_percent_end_total_asset/4,
                                                                 mean_percent_end_total_asset/4,
                                                                 median_percent_end_total_asset/4,
                                                                 0,
                                                                 0]})

    df_return_analysed_data_table['values'] = df_return_analysed_data_table['values'].apply(np.int64)
    df_return_analysed_data_table['_%_'] = df_return_analysed_data_table['_%_'].apply(np.int64)
    df_return_analysed_data_table['_yearly_%_'] = df_return_analysed_data_table['_yearly_%_'].apply(np.int64)

    df_return_analysed_data_quantile = pd.DataFrame({"quantile": [quantile_1_end_total_asset,
                                                                  quantile_2_end_total_asset,
                                                                  quantile_3_end_total_asset,
                                                                  quantile_4_end_total_asset,
                                                                  max_end_total_asset],
                                                     "quantile_values": [count_quantile_0_end_total_asset,
                                                                         count_quantile_1_end_total_asset,
                                                                         count_quantile_2_end_total_asset,
                                                                         count_quantile_3_end_total_asset,
                                                                         count_quantile_4_end_total_asset],
                                                     "quantile_percent_values": [count_percent_quantile_0_end_total_asset,
                                                                                 count_percent_quantile_1_end_total_asset,
                                                                                 count_percent_quantile_2_end_total_asset,
                                                                                 count_percent_quantile_3_end_total_asset,
                                                                                 count_percent_quantile_4_end_total_asset]})

    df_return_end_total_asset_data = pd.DataFrame({"end_total_asset": column_end_total_asset})

    index_iter = []
    nb_index = 0
    for value in df_return_end_total_asset_data["end_total_asset"]:
        index_iter.append(nb_index)
        nb_index = nb_index + 1

    df_return_end_total_asset_data.insert(1, 'max_value', max_end_total_asset)
    df_return_end_total_asset_data.insert(2, 'bottom', min_end_total_asset)
    df_return_end_total_asset_data.insert(3, 'mean', mean_end_total_asset)
    df_return_end_total_asset_data.insert(4, 'median', median_end_total_asset)
    df_return_end_total_asset_data.insert(5, 'quantile_1', quantile_1_end_total_asset)
    df_return_end_total_asset_data.insert(6, 'quantile_2', quantile_2_end_total_asset)
    df_return_end_total_asset_data.insert(7, 'quantile_3', quantile_3_end_total_asset)
    df_return_end_total_asset_data.insert(8, 'quantile_4', quantile_4_end_total_asset)
    df_return_end_total_asset_data["index_iter"] = index_iter


    df_return_end_total_asset_data['end_total_asset'] = df_return_end_total_asset_data['end_total_asset'].apply(np.int64)
    df_return_end_total_asset_data['max_value'] = df_return_end_total_asset_data['max_value'].apply(np.int64)
    df_return_end_total_asset_data['bottom'] = df_return_end_total_asset_data['bottom'].apply(np.int64)
    df_return_end_total_asset_data['mean'] = df_return_end_total_asset_data['mean'].apply(np.int64)
    df_return_end_total_asset_data['median'] = df_return_end_total_asset_data['median'].apply(np.int64)
    df_return_end_total_asset_data['quantile_1'] = df_return_end_total_asset_data['quantile_1'].apply(np.int64)
    df_return_end_total_asset_data['quantile_2'] = df_return_end_total_asset_data['quantile_2'].apply(np.int64)
    df_return_end_total_asset_data['quantile_3'] = df_return_end_total_asset_data['quantile_3'].apply(np.int64)
    df_return_end_total_asset_data['quantile_4'] = df_return_end_total_asset_data['quantile_4'].apply(np.int64)

    df_return_analysed_data = pd.DataFrame({"values": [max_end_total_asset,
                                                       min_end_total_asset,
                                                       mean_end_total_asset,
                                                       count_end_total_asset,
                                                       0],
                                            "quantile_values": [count_quantile_0_end_total_asset,
                                                                count_quantile_1_end_total_asset,
                                                                count_quantile_2_end_total_asset,
                                                                count_quantile_3_end_total_asset,
                                                                count_quantile_4_end_total_asset],
                                            "quantile_percent_values": [count_percent_quantile_0_end_total_asset,
                                                                        count_percent_quantile_1_end_total_asset,
                                                                        count_percent_quantile_2_end_total_asset,
                                                                        count_percent_quantile_3_end_total_asset,
                                                                        count_percent_quantile_4_end_total_asset]})

    return(df_return_end_total_asset_data)


def df_compute_quantile(df_filtered_computed):

    column_end_total_asset = df_filtered_computed["end_total_asset"]

    count_end_total_asset = column_end_total_asset.count()
    quantile_1_end_total_asset = df_filtered_computed['quantile_1'].values[0]
    quantile_2_end_total_asset = df_filtered_computed['quantile_2'].values[0]
    quantile_3_end_total_asset = df_filtered_computed['quantile_3'].values[0]
    quantile_4_end_total_asset = df_filtered_computed['quantile_4'].values[0]

    # count_quantile_0 nb of values between min and quantile_1
    values_between_quantiles_between_min_q1 = column_end_total_asset[(column_end_total_asset <= quantile_1_end_total_asset)]
    count_quantile_0_end_total_asset = values_between_quantiles_between_min_q1.count()

    # count_quantile_1 nb of values between quantile_1 and quantile_2
    values_between_quantiles_between_q1_q2 = column_end_total_asset[((column_end_total_asset > quantile_1_end_total_asset) & (column_end_total_asset <= quantile_2_end_total_asset))]
    count_quantile_1_end_total_asset = values_between_quantiles_between_q1_q2.count()

    # count_quantile_2 nb of values between quantile_2 and quantile_3
    values_between_quantiles_between_q2_q3 = column_end_total_asset[((column_end_total_asset > quantile_2_end_total_asset) & (column_end_total_asset <= quantile_3_end_total_asset))]
    count_quantile_2_end_total_asset = values_between_quantiles_between_q2_q3.count()

    # count_quantile_3 nb of values between quantile_3 and quantile_4
    values_between_quantiles_between_q3_q4 = column_end_total_asset[((column_end_total_asset > quantile_3_end_total_asset) & (column_end_total_asset <= quantile_4_end_total_asset))]
    count_quantile_3_end_total_asset = values_between_quantiles_between_q3_q4.count()

    # count_quantile_4 nb of values between quantile_4 and max
    values_between_quantiles_between_q4_max = column_end_total_asset[(column_end_total_asset > quantile_4_end_total_asset)]
    count_quantile_4_end_total_asset = values_between_quantiles_between_q4_max.count()

    count_percent_quantile_0_end_total_asset = data_calculation_percent_normal(count_quantile_0_end_total_asset , count_end_total_asset)
    count_percent_quantile_1_end_total_asset = data_calculation_percent_normal(count_quantile_1_end_total_asset , count_end_total_asset)
    count_percent_quantile_2_end_total_asset = data_calculation_percent_normal(count_quantile_2_end_total_asset , count_end_total_asset)
    count_percent_quantile_3_end_total_asset = data_calculation_percent_normal(count_quantile_3_end_total_asset , count_end_total_asset)
    count_percent_quantile_4_end_total_asset = data_calculation_percent_normal(count_quantile_4_end_total_asset , count_end_total_asset)

    max_end_total_asset = df_filtered_computed['max_value'].values[0]
    min_end_total_asset = df_filtered_computed['bottom'].values[0]
    mean_end_total_asset = df_filtered_computed['mean'].values[0]
    median_end_total_asset = df_filtered_computed['median'].values[0]

    df_return_analysed_data = pd.DataFrame({"values": [max_end_total_asset,
                                                       min_end_total_asset,
                                                       mean_end_total_asset,
                                                       median_end_total_asset,
                                                       count_end_total_asset],
                                            "quantile_values": [count_quantile_0_end_total_asset,
                                                                count_quantile_1_end_total_asset,
                                                                count_quantile_2_end_total_asset,
                                                                count_quantile_3_end_total_asset,
                                                                count_quantile_4_end_total_asset],
                                            "quantile_percent_values": [count_percent_quantile_0_end_total_asset,
                                                                        count_percent_quantile_1_end_total_asset,
                                                                        count_percent_quantile_2_end_total_asset,
                                                                        count_percent_quantile_3_end_total_asset,
                                                                        count_percent_quantile_4_end_total_asset]})

    return(df_return_analysed_data)








def display_terminal_dataframe_comparison_plotly(df_Policy_1_data,
                                                 df_Policy_2_data,
                                                 df_Policy_3_data,
                                                 policy_filter_1,
                                                 policy_filter_2,
                                                 policy_filter_3,
                                                 output_dir_terminal_state,
                                                 formated_time):

    #df_Policy_1_data = df_Policy_1_data.drop['values']
    df_Policy_1_data.insert(0, "filter", policy_filter_1)
    df_Policy_1_data.insert(0, "color", 5)
    df_Policy_1_data.insert(0, "text_font_size", 24)
    df_Policy_1_data.insert(0, "text_font_color", "white")

    #df_Policy_2_data = df_Policy_2_data.drop['values']
    df_Policy_2_data.insert(0, "filter", policy_filter_2)
    df_Policy_2_data.insert(0, "color", 10)
    df_Policy_2_data.insert(0, "text_font_size", 24)
    df_Policy_2_data.insert(0, "text_font_color", "white")

    #df_Policy_3_data = df_Policy_3_data.drop['values']
    df_Policy_3_data.insert(0, "filter", policy_filter_3)
    df_Policy_3_data.insert(0, "color", 15)
    df_Policy_3_data.insert(0, "text_font_size", 24)
    df_Policy_3_data.insert(0, "text_font_color", "white")

    df_Policy_1_data["color"][0] = 'lightpink'
    df_Policy_1_data["color"][1] = 'lightgreen'
    df_Policy_1_data["color"][2] = '#lightgoldenrodyellow'
    df_Policy_1_data["color"][3] = 'lightcyan'
    df_Policy_1_data["color"][4] = 'lightblue'

    df_Policy_2_data["color"][0] = 'lightpink'
    df_Policy_2_data["color"][1] = 'lightgreen'
    df_Policy_2_data["color"][2] = '#lightgoldenrodyellow'
    df_Policy_2_data["color"][3] = 'lightcyan'
    df_Policy_2_data["color"][4] = 'lightblue'

    df_Policy_3_data["color"][0] = 'lightpink'
    df_Policy_3_data["color"][1] = 'lightgreen'
    df_Policy_3_data["color"][2] = '#lightgoldenrodyellow'
    df_Policy_3_data["color"][3] = 'lightcyan'
    df_Policy_3_data["color"][4] = 'lightblue'

    frames = [df_Policy_1_data, df_Policy_2_data, df_Policy_3_data]

    df_merge_data = pd.concat(frames)


    fig = px.bar(df_merge_data, x="filter", y=["quantile_percent_values"], color="color", text="quantile_values", title="Wide-Form Input")

