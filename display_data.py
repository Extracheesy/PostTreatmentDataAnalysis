
# libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd

import os
import glob
import sys
import datetime
import pathlib

from ploty_dash_data import *

ACTIVATE_DASH_DISPLAY = "ON"
#ACTIVATE_DASH_DISPLAY = "OFF"


def display_terminal_dataframe_comparison(df_Policy_1_data,
                                          df_Policy_2_data,
                                          df_Policy_3_data,
                                          policy_filter_1,
                                          policy_filter_2,
                                          policy_filter_3,
                                          output_dir_terminal_state,
                                          formated_time):

    if ACTIVATE_DASH_DISPLAY == "ON":
        display_terminal_dataframe_comparison_plotly(df_Policy_1_data,
                                                     df_Policy_2_data,
                                                     df_Policy_3_data,
                                                     policy_filter_1,
                                                     policy_filter_2,
                                                     policy_filter_3,
                                                     output_dir_terminal_state,
                                                     formated_time)
    else:
        display_terminal_dataframe_comparison_plot(df_Policy_1_data,
                                                   df_Policy_2_data,
                                                   df_Policy_3_data,
                                                   policy_filter_1,
                                                   policy_filter_2,
                                                   policy_filter_3,
                                                   output_dir_terminal_state,
                                                   formated_time)

def display_whole_dataframe(df_full_terminal_data, output_dir_terminal_state):

    if ACTIVATE_DASH_DISPLAY == "ON" :
        display_whole_dataframe_plotly(df_full_terminal_data, output_dir_terminal_state)
    else :
        display_whole_dataframe_plot(df_full_terminal_data, output_dir_terminal_state)

def display_end_total_asset_data(df_return_end_total_asset_data,
                                 policy,
                                 max_percent_end_total_asset,
                                 min_percent_end_total_asset,
                                 count_quantile_0_end_total_asset,
                                 count_quantile_1_end_total_asset,
                                 count_quantile_2_end_total_asset,
                                 count_quantile_3_end_total_asset,
                                 count_quantile_4_end_total_asset):

    if ACTIVATE_DASH_DISPLAY == "ON" :
        display_end_total_asset_data_plotly(df_return_end_total_asset_data,
                                            policy,
                                            max_percent_end_total_asset,
                                            min_percent_end_total_asset,
                                            count_quantile_0_end_total_asset,
                                            count_quantile_1_end_total_asset,
                                            count_quantile_2_end_total_asset,
                                            count_quantile_3_end_total_asset,
                                            count_quantile_4_end_total_asset)
    else:
        display_end_total_asset_data_plot(df_return_end_total_asset_data,
                                          policy,
                                          max_percent_end_total_asset,
                                          min_percent_end_total_asset,
                                          count_quantile_0_end_total_asset,
                                          count_quantile_1_end_total_asset,
                                          count_quantile_2_end_total_asset,
                                          count_quantile_3_end_total_asset,
                                          count_quantile_4_end_total_asset)

def display_terminal_comparison_bar_plot(df_raw_data, filter_1, filter_2, filter_3, output_dir_terminal_state,formated_time):

    # Data
    r = [0, 1, 2]

    os.chdir(output_dir_terminal_state)

    # From raw value to percentage
    totals = [ i+j+k+l+m for i,j,k,l,m in zip(df_raw_data['greenBars'],
                                              df_raw_data['orangeBars'],
                                              df_raw_data['blueBars'],
                                              df_raw_data['violetBars'],
                                              df_raw_data['pinkBars'])]

    greenBars = [i / j * 100 for i ,j in zip(df_raw_data['greenBars'], totals)]
    orangeBars = [i / j * 100 for i ,j in zip(df_raw_data['orangeBars'], totals)]
    blueBars = [i / j * 100 for i ,j in zip(df_raw_data['blueBars'], totals)]
    violetBars = [i / j * 100 for i ,j in zip(df_raw_data['violetBars'], totals)]
    pinkBars = [i / j * 100 for i ,j in zip(df_raw_data['pinkBars'], totals)]

    # plot
    barWidth = 0.85
    if filter_3 != "NO_FILTER" :
        names = (filter_1 + '\n' + "Iteration: " + str(int(totals[0])),
                 filter_2 + '\n' + "Iteration: " + str(int(totals[1])),
                 filter_3 + '\n' + "Iteration: " + str(int(totals[2])))
    else :
        names = (filter_1 + '\n' + "Iteration: " + str(int(totals[0])),
                 filter_2 + '\n' + "Iteration: " + str(int(totals[1])),
                 filter_3)

    # Create green Bars
    bar_green = plt.bar(r, greenBars, color='#b5ffb9', edgecolor='white', width=barWidth)
    # Create orange Bars
    bar_orange = plt.bar(r, orangeBars, bottom=greenBars, color='#f9bc86', edgecolor='white', width=barWidth)
    # Create blue Bars
    bar_blue = plt.bar(r, blueBars, bottom=[ i+j for i,j in zip(greenBars, orangeBars)], color='#a3acff', edgecolor='white', width=barWidth)
    # Create violet Bars
    bar_violet = plt.bar(r, violetBars, bottom=[ i+j+k for i,j,k in zip(greenBars, orangeBars, blueBars)], color='violet', edgecolor='white', width=barWidth)
    # Create pink Bars
    bar_pink = plt.bar(r, pinkBars, bottom=[ i+j+k+l for i,j,k,l in zip(greenBars, orangeBars, blueBars, violetBars)], color='lightpink', edgecolor='white', width=barWidth)

    for r_green, r_orange, r_blue, r_violet, r_pink in zip(bar_green, bar_orange, bar_blue, bar_violet, bar_pink):
        h_g = r_green.get_height()
        h_o = r_orange.get_height()
        h_b = r_blue.get_height()
        h_v = r_violet.get_height()
        h_p = r_pink.get_height()

        if h_g > 0 :
            plt.text(r_green.get_x() + r_green.get_width() / 2., h_g / 2., "%d" % h_g, ha="center", va="center", color="white",
                     fontsize=16, fontweight="bold")
        if h_o > 0 :
            plt.text(r_orange.get_x() + r_orange.get_width() / 2., h_g + h_o / 2., "%d" % h_o, ha="center", va="center", color="white",
                     fontsize=16, fontweight="bold")
        if h_b > 0 :
            plt.text(r_blue.get_x() + r_blue.get_width() / 2., h_g + h_o + h_b / 2., "%d" % h_b, ha="center", va="center", color="white",
                     fontsize=16, fontweight="bold")
        if h_v > 0 :
            plt.text(r_violet.get_x() + r_violet.get_width() / 2., h_g + h_o + h_b + h_v / 2., "%d" % h_v, ha="center", va="center", color="white",
                     fontsize=16, fontweight="bold")
        if h_p > 0 :
            plt.text(r_pink.get_x() + r_pink.get_width() / 2., h_g + h_o + h_b + h_v + h_p / 2., "%d" % h_p, ha="center", va="center", color="white",
                     fontsize=16, fontweight="bold")

    # Custom x axis
    plt.xticks(r, names)

    # Save graphic
    if filter_3 != "NO_FILTER":
        save_to_file_jpg = "comparison_" + filter_1 + "_" + filter_2 + "_" + filter_3 + ".jpg"
        save_to_file_pdf = "comparison_" + filter_1 + "_" + filter_2 + "_" + filter_3 + ".pdf"
    else:
        save_to_file_jpg = "comparison_" + filter_1 + "_" + filter_2 + ".jpg"
        save_to_file_pdf = "comparison_" + filter_1 + "_" + filter_2 + ".pdf"

    plt.savefig(save_to_file_jpg)
    plt.savefig(save_to_file_pdf)
    plt.show()

def  display_terminal_dataframe_comparison_plot(df_Policy_1_data,
                                                df_Policy_2_data,
                                                df_Policy_3_data,
                                                policy_filter_1,
                                                policy_filter_2,
                                                policy_filter_3,
                                                output_dir_terminal_state,
                                                formated_time) :
    count = 0
    for i in df_Policy_1_data.quantile_values :
        if count == 0 :
            q0_Policy_1 = i
            count = count + 1
        elif count == 1 :
            g1_Policy_1 = i
            count = count + 1
        elif count == 2 :
            g2_Policy_1 = i
            count = count + 1
        elif count == 3 :
            g3_Policy_1 = i
            count = count + 1
        elif count == 4 :
            g4_Policy_1 = i
            count = count + 1

    count = 0
    for i in df_Policy_2_data.quantile_values :
        if count == 0 :
            q0_Policy_2 = i
            count = count + 1
        elif count == 1 :
            g1_Policy_2 = i
            count = count + 1
        elif count == 2 :
            g2_Policy_2 = i
            count = count + 1
        elif count == 3 :
            g3_Policy_2 = i
            count = count + 1
        elif count == 4 :
            g4_Policy_2 = i
            count = count + 1
    if policy_filter_3 != "NO_FILTER" :
        count = 0
        for i in df_Policy_3_data.quantile_values :
            if count == 0 :
                q0_Policy_3 = i
                count = count + 1
            elif count == 1 :
                g1_Policy_3 = i
                count = count + 1
            elif count == 2 :
                g2_Policy_3 = i
                count = count + 1
            elif count == 3 :
                g3_Policy_3 = i
                count = count + 1
            elif count == 4 :
                g4_Policy_3 = i
                count = count + 1
    else :
        q0_Policy_3 = 1
        g1_Policy_3 = 1
        g2_Policy_3 = 1
        g3_Policy_3 = 1
        g4_Policy_3 = 1

    raw_Policies_bar = {'greenBars': [q0_Policy_1,
                                      q0_Policy_2,
                                      q0_Policy_3],
                        'orangeBars': [g1_Policy_1,
                                       g1_Policy_2,
                                       g1_Policy_3],
                        'blueBars': [g2_Policy_1,
                                     g2_Policy_2,
                                     g2_Policy_3],
                        'violetBars': [g3_Policy_1,
                                       g3_Policy_2,
                                       g3_Policy_3],
                        'pinkBars': [g4_Policy_1,
                                     g4_Policy_2,
                                     g4_Policy_3]}

    display_terminal_comparison_bar_plot(raw_Policies_bar, policy_filter_1, policy_filter_2, policy_filter_3, output_dir_terminal_state, formated_time)


def display_end_total_asset_data_plot(df_return_end_total_asset_data,
                                      policy,
                                      max_percent_end_total_asset,
                                      min_percent_end_total_asset,
                                      count_quantile_0_end_total_asset,
                                      count_quantile_1_end_total_asset,
                                      count_quantile_2_end_total_asset,
                                      count_quantile_3_end_total_asset,
                                      count_quantile_4_end_total_asset):

    # gca stands for 'get current axis'
    ax = plt.gca()

    max_end_total_asset = df_return_end_total_asset_data.iloc[0]['max_value']
    min_end_total_asset = df_return_end_total_asset_data.iloc[0]['bottom']
    mean_end_total_asset = df_return_end_total_asset_data.iloc[0]['mean']
    median_end_total_asset = df_return_end_total_asset_data.iloc[0]['median']

    df_return_end_total_asset_data.plot(kind='line', x='index_iter', y='end_total_asset', color='blue', marker=".", markersize=5, ax=ax, figsize=(10, 8), legend=False)
    df_return_end_total_asset_data.plot(kind='line', x='index_iter', y='median', color='red', ax=ax, legend=False)
    df_return_end_total_asset_data.plot(kind='line', x='index_iter', y='mean', color='black', ax=ax, legend=False)
    df_return_end_total_asset_data.plot(kind='line', x='index_iter', y='bottom', color='fuchsia', ax=ax, legend=False)
    df_return_end_total_asset_data.plot(kind='line', x='index_iter', y='max_value', color='deeppink', ax=ax, legend=False)

    df_return_end_total_asset_data.plot(kind='line', x='index_iter', y='quantile_1', color='silver', linestyle='--', ax=ax, legend=False)
    df_return_end_total_asset_data.plot(kind='line', x='index_iter', y='quantile_2', color='silver', linestyle='--', ax=ax, legend=False)
    df_return_end_total_asset_data.plot(kind='line', x='index_iter', y='quantile_3', color='silver', linestyle='--', ax=ax, legend=False)
    df_return_end_total_asset_data.plot(kind='line', x='index_iter', y='quantile_4', color='silver', linestyle='--', ax=ax, legend=False)


    text_max = "max value: " + str(int(max_end_total_asset))
    plt.text(1, max_end_total_asset + 5000, text_max, color='deeppink')

    text_min = "min value: " + str(int(min_end_total_asset))
    plt.text(1, min_end_total_asset + 5000, text_min, color='fuchsia')

    if mean_end_total_asset > median_end_total_asset :
        text_mean = "mean: " + str(int(mean_end_total_asset))
        plt.text(1, mean_end_total_asset + 5000, text_mean, color='black')

        text_median = "median: " + str(int(median_end_total_asset))
        plt.text(1, median_end_total_asset - 15000, text_median, color='red')
    else :
        text_mean = "mean: " + str(int(mean_end_total_asset))
        plt.text(1, mean_end_total_asset - 15000, text_mean, color='black')

        text_median = "median: " + str(int(median_end_total_asset))
        plt.text(1, median_end_total_asset + 5000, text_median, color='red')

    max_ROI = "max ROI: " + str(int(max_percent_end_total_asset)) + "% / max yearly ROI: " + str(int(max_percent_end_total_asset)/4) + "%"
    min_ROI = "min ROI: " + str(int(min_percent_end_total_asset)) + "% / min yearly ROI: " + str(int(min_percent_end_total_asset)/4) + "%"
    nb_Q = "q0: " + str(int(count_quantile_0_end_total_asset)) \
           + " q1: " + str(int(count_quantile_1_end_total_asset)) \
           + " q2: " + str(int(count_quantile_2_end_total_asset)) \
           + " q3: " + str(int(count_quantile_3_end_total_asset)) \
           + " q4: " + str(int(count_quantile_4_end_total_asset))
    variance = "variance: " + str(int(max_end_total_asset - min_end_total_asset))
    header = "End_Total_Asset - Filter: " + policy + '\n'  +  max_ROI + '\n' + min_ROI

    iteration = str(int(count_quantile_0_end_total_asset
                        + count_quantile_1_end_total_asset
                        + count_quantile_2_end_total_asset
                        + count_quantile_3_end_total_asset
                        + count_quantile_4_end_total_asset))
    plt.title(header)
    plt.xlabel(nb_Q + '\n' + "iteration: " + iteration + '\n' + variance)

    #plt.show()
    save_to_file_jpg = "end_total_asset_" + policy + ".jpg"
    save_to_file_pdf = "end_total_asset_" + policy + ".pdf"

    plt.savefig(save_to_file_jpg)
    os.chdir("..")
    plt.savefig(save_to_file_pdf)
    plt.show()

def display_whole_dataframe_plot(df_full_terminal_data, output_dir_terminal_state):

    df_display_shape = pd.DataFrame(columns=['index_shape', 'max', 'min', 'mean', 'average'])

    for i in range(len(df_full_terminal_data.index.unique())) :
        df_end_total_asset_i = df_full_terminal_data[(df_full_terminal_data.index == i)]

        column_end_total_asset_i = df_end_total_asset_i["end_total_asset"]

        max_i = column_end_total_asset_i.max()
        min_i = column_end_total_asset_i.min()
        mean_i = column_end_total_asset_i.mean()
        average_i = (max_i - min_i) / 2
        new_row_i = {'index_shape': [i], 'max': [max_i], 'min': [min_i], 'mean': [mean_i], 'average': [average_i + min_i] }
        df_new_row_i = pd.DataFrame(new_row_i)
        df_display_shape = df_display_shape.append(df_new_row_i)

    #plt.scatter(df_full_terminal_data.index, df_full_terminal_data['end_total_asset'])
    plt.plot(df_display_shape['index_shape'], df_display_shape['max'], label='max')
    plt.plot(df_display_shape['index_shape'], df_display_shape['min'], label='min')
    plt.plot(df_display_shape['index_shape'], df_display_shape['mean'], label='mean')
    plt.plot(df_display_shape['index_shape'], df_display_shape['average'], label='median')

    # plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    plt.legend(loc='upper left', borderaxespad=0.5)

    os.chdir(output_dir_terminal_state)

    save_to_file_jpg = "display_max_min_mean_data.jpg"
    save_to_file_pdf = "display_max_min_mean_data.pdf"

    plt.savefig(save_to_file_jpg)
    plt.savefig(save_to_file_pdf)
    plt.show()