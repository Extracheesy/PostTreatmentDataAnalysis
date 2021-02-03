
import numpy as np
import time
import pandas as pd
import matplotlib.pyplot as plt

import os
import glob
import sys
import datetime
import pathlib

from display_data import *
from ploty_dash_data import *

INITIAL_INVESTMENT = 1000000

def calculation_percent (value1 , value2):
    return((value1 - value2) *100 / value2)

def calculation_percent_normal (value1 , value2):
    return((value1) *100 / value2)

def computed_data_in_dataframe(df_group_by_policies_at_final_states, policy,output_dir_terminal_state,formated_time) :

    os.chdir(output_dir_terminal_state)
    # print(os.getcwd())

    computed_data_quantile_terminal_csv = "computed_terminal_data_quantile_" + policy + "_" + formated_time + ".csv"
    computed_data_table_terminal_csv = "computed_terminal_data_table_" + policy + "_" + formated_time + ".csv"
    computed_data_end_total_asset_terminal_csv = "computed_terminal_data_end_total_asset_" + policy + "_" + formated_time + ".csv"


    column_end_total_asset = df_group_by_policies_at_final_states["end_total_asset"]

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

    # CD for test quantile -> 1/4
    #quantile_1_end_total_asset = column_end_total_asset.quantile(0.2)
    #quantile_2_end_total_asset = column_end_total_asset.quantile(0.4)
    #quantile_3_end_total_asset = column_end_total_asset.quantile(0.6)
    #quantile_4_end_total_asset = column_end_total_asset.quantile(0.8)

    quantile_1_end_total_asset = min_end_total_asset + (max_end_total_asset - min_end_total_asset) / 5
    quantile_2_end_total_asset = min_end_total_asset + (max_end_total_asset - min_end_total_asset) / 5 * 2
    quantile_3_end_total_asset = min_end_total_asset + (max_end_total_asset - min_end_total_asset) / 5 * 3
    quantile_4_end_total_asset = min_end_total_asset + (max_end_total_asset - min_end_total_asset) / 5 * 4



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

    output_dir =  output_dir_terminal_state + "/" + policy
    os.mkdir(output_dir)
    os.chdir(output_dir)

    df_return_analysed_data_quantile.to_csv(computed_data_quantile_terminal_csv,index=None)
    df_return_analysed_data_table.to_csv(computed_data_table_terminal_csv,index=None)
    df_return_end_total_asset_data.to_csv(computed_data_end_total_asset_terminal_csv,index=None)

    display_end_total_asset_data(df_return_end_total_asset_data,
                                 policy,
                                 max_percent_end_total_asset,
                                 min_percent_end_total_asset,
                                 count_quantile_0_end_total_asset,
                                 count_quantile_1_end_total_asset,
                                 count_quantile_2_end_total_asset,
                                 count_quantile_3_end_total_asset,
                                 count_quantile_4_end_total_asset)

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
    return df_return_analysed_data


def analyse_terminal_dataframe(df_full_terminal_data,output_dir_terminal_state,formated_time):
    # Group, analyse and plot terminal data
    # Group by policies / market / algo

    display_whole_dataframe(df_full_terminal_data,output_dir_terminal_state)

    ##########################
    # Grouped by policies
    ##########################
    df_group_by_MlpPolicy_policies_at_final_states = df_full_terminal_data[(df_full_terminal_data.policy == "MlpPolicy") & (df_full_terminal_data.iter_num == 1197)]
    df_group_by_MlpLstmPolicy_policies_at_final_states = df_full_terminal_data[(df_full_terminal_data.policy == "MlpLstmPolicy") & (df_full_terminal_data.iter_num == 1197)]
    df_group_by_MlpLnLstmPolicy_policies_at_final_states = df_full_terminal_data[(df_full_terminal_data.policy == "MlpLnLstmPolicy") & (df_full_terminal_data.iter_num == 1197)]

    df_MlpPolicy_data = computed_data_in_dataframe(df_group_by_MlpPolicy_policies_at_final_states, "MlpPolicy", output_dir_terminal_state, formated_time)
    df_MlpLstmPolicy_data = computed_data_in_dataframe(df_group_by_MlpLstmPolicy_policies_at_final_states, "MlpLstmPolicy", output_dir_terminal_state, formated_time)
    df_MlpLnLstmPolicy_data = computed_data_in_dataframe(df_group_by_MlpLnLstmPolicy_policies_at_final_states, "MlpLnLstmPolicy", output_dir_terminal_state, formated_time)

    display_terminal_dataframe_comparison(df_MlpPolicy_data,
                                          df_MlpLstmPolicy_data,
                                          df_MlpLnLstmPolicy_data,
                                          "MlpPolicy",
                                          "MlpLstmPolicy",
                                          "MlpLnLstmPolicy",
                                          output_dir_terminal_state,
                                          formated_time)

    ##########################
    # Grouped by market
    ##########################
    df_group_by_CAC_market_at_final_states = df_full_terminal_data[(df_full_terminal_data.market == "CAC") & (df_full_terminal_data.iter_num == 1197)]
    df_group_by_DJI_market_at_final_states = df_full_terminal_data[(df_full_terminal_data.market == "DJI") & (df_full_terminal_data.iter_num == 1197)]
    df_group_by_DAX_market_at_final_states = df_full_terminal_data[(df_full_terminal_data.market == "DAX") & (df_full_terminal_data.iter_num == 1197)]

    df_CAC_data = computed_data_in_dataframe(df_group_by_CAC_market_at_final_states, "CAC", output_dir_terminal_state, formated_time)
    df_DJI_data = computed_data_in_dataframe(df_group_by_DJI_market_at_final_states, "DJI", output_dir_terminal_state, formated_time)
    df_DAX_data = computed_data_in_dataframe(df_group_by_DAX_market_at_final_states, "DAX", output_dir_terminal_state, formated_time)

    display_terminal_dataframe_comparison(df_CAC_data,
                                          df_DJI_data,
                                          df_DAX_data,
                                          "CAC",
                                          "DJI",
                                          "DAX",
                                          output_dir_terminal_state,
                                          formated_time)

    ##########################
    # Grouped by algo
    ##########################
    df_group_by_A2C_algo_at_final_states = df_full_terminal_data[(df_full_terminal_data.algo == "A2C") & (df_full_terminal_data.iter_num == 1197)]
    df_group_by_PPO_algo_at_final_states = df_full_terminal_data[(df_full_terminal_data.algo == "PPO") & (df_full_terminal_data.iter_num == 1197)]

    df_A2C_data = computed_data_in_dataframe(df_group_by_A2C_algo_at_final_states, "A2C", output_dir_terminal_state, formated_time)
    df_PPO_data = computed_data_in_dataframe(df_group_by_PPO_algo_at_final_states, "PPO", output_dir_terminal_state, formated_time)
    df_empty = pd.DataFrame({'A': []})

    display_terminal_dataframe_comparison(df_A2C_data,
                                          df_PPO_data,
                                          df_empty,
                                          "A2C",
                                          "PPO",
                                          "NO_FILTER",
                                          output_dir_terminal_state,
                                          formated_time)

    #################################
    # Grouped by policies + market
    #################################
    df_group_by_MlpPolicy_CAC_policies_at_final_states = df_full_terminal_data[(df_full_terminal_data.policy == "MlpPolicy") & (df_full_terminal_data.market == "CAC") & (df_full_terminal_data.iter_num == 1197)]
    df_group_by_MlpPolicy_DAX_policies_at_final_states = df_full_terminal_data[(df_full_terminal_data.policy == "MlpPolicy") & (df_full_terminal_data.market == "DAX") & (df_full_terminal_data.iter_num == 1197)]
    df_group_by_MlpPolicy_DJI_policies_at_final_states = df_full_terminal_data[(df_full_terminal_data.policy == "MlpPolicy") & (df_full_terminal_data.market == "DJI") & (df_full_terminal_data.iter_num == 1197)]

    df_group_by_MlpLstmPolicy_CAC_policies_at_final_states = df_full_terminal_data[(df_full_terminal_data.policy == "MlpLstmPolicy") & (df_full_terminal_data.market == "CAC") & (df_full_terminal_data.iter_num == 1197)]
    df_group_by_MlpLstmPolicy_DAX_policies_at_final_states = df_full_terminal_data[(df_full_terminal_data.policy == "MlpLstmPolicy") & (df_full_terminal_data.market == "DAX") & (df_full_terminal_data.iter_num == 1197)]
    df_group_by_MlpLstmPolicy_DJI_policies_at_final_states = df_full_terminal_data[(df_full_terminal_data.policy == "MlpLstmPolicy") & (df_full_terminal_data.market == "DJI") & (df_full_terminal_data.iter_num == 1197)]

    df_group_by_MlpLnLstmPolicy_CAC_policies_at_final_states = df_full_terminal_data[(df_full_terminal_data.policy == "MlpLnLstmPolicy") & (df_full_terminal_data.market == "CAC") & (df_full_terminal_data.iter_num == 1197)]
    df_group_by_MlpLnLstmPolicy_DAX_policies_at_final_states = df_full_terminal_data[(df_full_terminal_data.policy == "MlpLnLstmPolicy") & (df_full_terminal_data.market == "DAX") & (df_full_terminal_data.iter_num == 1197)]
    df_group_by_MlpLnLstmPolicy_DJI_policies_at_final_states = df_full_terminal_data[(df_full_terminal_data.policy == "MlpLnLstmPolicy") & (df_full_terminal_data.market == "DJI") & (df_full_terminal_data.iter_num == 1197)]

    df_MlpPolicy_CAC_data = computed_data_in_dataframe(df_group_by_MlpPolicy_CAC_policies_at_final_states, "MlpPolicy_CAC", output_dir_terminal_state, formated_time)
    df_MlpPolicy_DAX_data = computed_data_in_dataframe(df_group_by_MlpPolicy_DAX_policies_at_final_states, "MlpPolicy_DAX", output_dir_terminal_state, formated_time)
    df_MlpPolicy_DJI_data = computed_data_in_dataframe(df_group_by_MlpPolicy_DJI_policies_at_final_states, "MlpPolicy_DJI", output_dir_terminal_state, formated_time)

    display_terminal_dataframe_comparison(df_MlpPolicy_CAC_data,
                                          df_MlpPolicy_DAX_data,
                                          df_MlpPolicy_DJI_data,
                                          "MlpPolicy_CAC",
                                          "MlpPolicy_DAX",
                                          "MlpPolicy_DJI",
                                          output_dir_terminal_state,
                                          formated_time)

    df_MlpLstmPolicy_CAC_data = computed_data_in_dataframe(df_group_by_MlpLstmPolicy_CAC_policies_at_final_states, "MlpLstmPolicy_CAC", output_dir_terminal_state, formated_time)
    df_MlpLstmPolicy_DAX_data = computed_data_in_dataframe(df_group_by_MlpLstmPolicy_DAX_policies_at_final_states, "MlpLstmPolicy_DAX", output_dir_terminal_state, formated_time)
    df_MlpLstmPolicy_DJI_data = computed_data_in_dataframe(df_group_by_MlpLstmPolicy_DJI_policies_at_final_states, "MlpLstmPolicy_DJI", output_dir_terminal_state, formated_time)

    display_terminal_dataframe_comparison(df_MlpLstmPolicy_CAC_data,
                                          df_MlpLstmPolicy_DAX_data,
                                          df_MlpLstmPolicy_DJI_data,
                                          "MlpLstmPolicy_CAC",
                                          "MlpLstmPolicy_DAX",
                                          "MlpLstmPolicy_DJI",
                                          output_dir_terminal_state,
                                          formated_time)

    df_MlpLnLstmPolicy_CAC_data = computed_data_in_dataframe(df_group_by_MlpLnLstmPolicy_CAC_policies_at_final_states, "MlpLnLstmPolicy_CAC", output_dir_terminal_state, formated_time)
    df_MlpLnLstmPolicy_DAX_data = computed_data_in_dataframe(df_group_by_MlpLnLstmPolicy_DAX_policies_at_final_states, "MlpLnLstmPolicy_DAX", output_dir_terminal_state, formated_time)
    df_MlpLnLstmPolicy_DJI_data = computed_data_in_dataframe(df_group_by_MlpLnLstmPolicy_DJI_policies_at_final_states, "MlpLnLstmPolicy_DJI", output_dir_terminal_state, formated_time)

    display_terminal_dataframe_comparison(df_MlpLnLstmPolicy_CAC_data,
                                          df_MlpLnLstmPolicy_DAX_data,
                                          df_MlpLnLstmPolicy_DJI_data,
                                          "MlpLnLstmPolicy_CAC",
                                          "MlpLnLstmPolicy_DAX",
                                          "MlpLnLstmPolicy_DJI",
                                          output_dir_terminal_state,
                                          formated_time)


    #################################
    # Not available yet CD
    # Grouped by policies + algo
    #################################
    # df_group_by_MlpPolicy_A2C_policies_at_final_states = df_full_terminal_data[(df_full_terminal_data.policy == "MlpPolicy") & (df_full_terminal_data.algo == "A2C") & (df_full_terminal_data.iter_num == 1197)]
    # df_group_by_MlpPolicy_PPO_policies_at_final_states = df_full_terminal_data[(df_full_terminal_data.policy == "MlpPolicy") & (df_full_terminal_data.algo == "PPO") & (df_full_terminal_data.iter_num == 1197)]

    # df_group_by_MlpLstmPolicy_A2C_policies_at_final_states = df_full_terminal_data[(df_full_terminal_data.policy == "MlpLstmPolicy") & (df_full_terminal_data.algo == "A2C") & (df_full_terminal_data.iter_num == 1197)]
    # Not yet available CD
    # df_group_by_MlpLstmPolicy_PPO_policies_at_final_states = df_full_terminal_data[(df_full_terminal_data.policy == "MlpLstmPolicy") & (df_full_terminal_data.algo == "PPO") & (df_full_terminal_data.iter_num == 1197)]

    # df_group_by_MlpLnLstmPolicy_A2C_policies_at_final_states = df_full_terminal_data[(df_full_terminal_data.policy == "MlpLnLstmPolicy") & (df_full_terminal_data.algo == "A2C") & (df_full_terminal_data.iter_num == 1197)]
    # Not yet available CD
    # df_group_by_MlpLnLstmPolicy_PPO_policies_at_final_states = df_full_terminal_data[(df_full_terminal_data.policy == "MlpLnLstmPolicy") & (df_full_terminal_data.algo == "PPO") & (df_full_terminal_data.iter_num == 1197)]

    # computed_data_in_dataframe(df_group_by_MlpPolicy_A2C_policies_at_final_states, "MlpPolicy_A2C", output_dir_terminal_state, formated_time)
    # computed_data_in_dataframe(df_group_by_MlpPolicy_PPO_policies_at_final_states, "MlpPolicy_PPO", output_dir_terminal_state, formated_time)

    # computed_data_in_dataframe(df_group_by_MlpLstmPolicy_A2C_policies_at_final_states, "MlpLstmPolicy_A2C", output_dir_terminal_state, formated_time)
    # computed_data_in_dataframe(df_group_by_MlpLstmPolicy_PPO_policies_at_final_states, "MlpLstmPolicy_PPO", output_dir_terminal_state, formated_time)

    # computed_data_in_dataframe(df_group_by_MlpLnLstmPolicy_A2C_policies_at_final_states, "MlpLnLstmPolicy_A2C", output_dir_terminal_state, formated_time)
    # computed_data_in_dataframe(df_group_by_MlpLnLstmPolicy_PPO_policies_at_final_states, "MlpLnLstmPolicy_PPO", output_dir_terminal_state, formated_time)


def fill_terminal_dataframe(df_files_list,input_dir,output_dir_terminal_state,formated_time):

    df_terminal_list = df_files_list[(df_files_list.file_type == "terminal")]
    # print("output_dir_terminal_state: ", output_dir_terminal_state)
    os.chdir(output_dir_terminal_state)
    # print(os.getcwd())
    full_list_terminal_csv = "full_list_terminal_data_file_" + formated_time + ".csv"
    df_terminal_list.to_csv(full_list_terminal_csv,index=None)
    os.chdir(input_dir)

    count = 0

    for i in df_terminal_list.file_name :
        df_tmp_terminal_data = pd.read_csv(i, index_col=[0])

        first_column = df_tmp_terminal_data.columns[0]

        df_tmp_terminal_data.drop([first_column], axis=1)

        # insert specifics values from .csv infos regarding market, Policies and Algo

        df_tmp_terminal_data.insert(0, 'run_date', df_files_list.run_date[count])
        df_tmp_terminal_data.insert(0, 'run_time', df_files_list.run_time[count])
        df_tmp_terminal_data.insert(0, 'market', df_files_list.market[count])
        df_tmp_terminal_data.insert(0, 'algo', df_files_list.algo[count])
        df_tmp_terminal_data.insert(0, 'policy', df_files_list.policy[count])

        if count == 0:
            list_of_df_terminal_files = [df_tmp_terminal_data]
        else :
            list_of_df_terminal_files.append(df_tmp_terminal_data)
        count = count + 1

    df_full_terminal_data = pd.concat(list_of_df_terminal_files)

    os.chdir(output_dir_terminal_state)
    full_data_terminal_csv = "full_data_terminal_data_file_" + formated_time + ".csv"
    # df_full_terminal_data.to_csv(full_data_terminal_csv,index=None)


    return (df_full_terminal_data)



def fill_trades_dataframe(df_files_list,input_dir,output_dir,formated_time):

    df_trades_list = df_files_list[(df_files_list.file_type == "trades")]
    # print("output_dir_trades_state: ", output_dir)
    os.chdir(output_dir)
    # print(os.getcwd())
    full_list_trades_csv = "full_list_trades_data_file_" + formated_time + ".csv"
    df_trades_list.to_csv(full_list_trades_csv,index=None)
    os.chdir(input_dir)

    count = 0

    for i in df_trades_list.file_name :
        df_tmp_trades_data = pd.read_csv(i, index_col=[0])

        first_column = df_tmp_trades_data.columns[0]

        df_tmp_trades_data.drop([first_column], axis=1)

        # insert specifics values from .csv infos regarding market, Policies and Algo

        #df_tmp_trades_data.insert(0, 'run_date', df_files_list.run_date[count])
        #df_tmp_trades_data.insert(0, 'run_time', df_files_list.run_time[count])
        df_tmp_trades_data.insert(0, 'run_time', df_files_list.run_date[count] + df_files_list.run_time[count])
        df_tmp_trades_data.insert(0, 'market', df_files_list.market[count])
        df_tmp_trades_data.insert(0, 'algo', df_files_list.algo[count])
        df_tmp_trades_data.insert(0, 'policy', df_files_list.policy[count])

        if count == 0:
            list_of_df_trades_files = [df_tmp_trades_data]
        else :
            list_of_df_trades_files.append(df_tmp_trades_data)
        count = count + 1

    df_full_trades_data = pd.concat(list_of_df_trades_files)

    os.chdir(output_dir)
    full_data_trades_csv = "full_data_trades_data_file_" + formated_time + ".csv"
    df_full_trades_data.to_csv(full_data_trades_csv,index=None)


    return (df_full_trades_data)



def fill_stocks_dataframe(df_files_list,input_dir,output_dir_stocks_state,formated_time):

    df_stocks_list = df_files_list[(df_files_list.file_type == "stocks")]
    # print("output_dir_stocks_state: ", output_dir_stocks_state)
    os.chdir(output_dir_stocks_state)
    # print(os.getcwd())
    full_list_stocks_csv = "full_list_stocks_data_file_" + formated_time + ".csv"
    df_stocks_list.to_csv(full_list_stocks_csv,index=None)
    os.chdir(input_dir)

    count = 0

    for i in df_stocks_list.file_name :
        df_tmp_stocks_data = pd.read_csv(i, index_col=[0])

        first_column = df_tmp_stocks_data.columns[0]

        df_tmp_stocks_data.drop([first_column], axis=1)

        # insert specifics values from .csv infos regarding market, Policies and Algo

        # df_tmp_stocks_data.insert(0, 'run_date', df_files_list.run_date[count])
        # df_tmp_stocks_data.insert(0, 'run_time', df_files_list.run_time[count])
        df_tmp_stocks_data.insert(0, 'run_date_time', df_files_list.run_date[count] + df_files_list.run_time[count])
        df_tmp_stocks_data.insert(0, 'market', df_files_list.market[count])
        df_tmp_stocks_data.insert(0, 'algo', df_files_list.algo[count])
        df_tmp_stocks_data.insert(0, 'policy', df_files_list.policy[count])

        df_tmp_stocks_data.insert(0, 'stocks_trade_value', 0)

        if count == 0:
            list_of_df_stocks_files = [df_tmp_stocks_data]
        else :
            list_of_df_stocks_files.append(df_tmp_stocks_data)
        count = count + 1

    df_full_stocks_data = pd.concat(list_of_df_stocks_files)

    df_full_stocks_data = fill_stock_trade_value(df_full_stocks_data)

    os.chdir(output_dir_stocks_state)
    full_data_stocks_csv = "full_data_stocks_data_file_" + formated_time + ".csv"

    IBM_stocks_data = df_full_stocks_data[(df_full_stocks_data.tic == "IBM")]

    IBM_stocks_data.to_csv(full_data_stocks_csv,index=None)

    # df_full_stocks_data.to_csv(full_data_stocks_csv,index=None)

    return (df_full_stocks_data)

def fill_stock_trade_value(df_tmp_stocks_data):

    nb_index = 0
    #for i in range(0,len(df_tmp_stocks_data),1):
    for i in df_tmp_stocks_data.action_performed:

        if( i == "buy"):
            trade_coef = -1
        else:
            trade_coef = 1

        df_tmp_stocks_data.loc[df_tmp_stocks_data.index == nb_index, "stocks_trade_value"] = trade_coef * df_tmp_stocks_data.iloc[nb_index]['nb_stock_traded'] * df_tmp_stocks_data.iloc[nb_index]['stock_value']
        nb_index = nb_index + 1


    return(df_tmp_stocks_data)