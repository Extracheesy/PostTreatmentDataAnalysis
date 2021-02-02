import dash
import dash_core_components as dcc
import dash_html_components as html

import plotly
import plotly.graph_objects as go
import plotly.express as px


from plotly.graph_objs import Scatter, Layout
import numpy as np
import pandas as pd

import os
import glob
import sys
import datetime
import pathlib

def display_whole_dataframe_plotly(df_full_terminal_data, output_dir_terminal_state):

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

    # Create traces
    trace0 = go.Scatter(
        x = df_display_shape['index_shape'],
        y = df_display_shape['max'],
        mode = 'lines',
        name = 'max'
    )

    trace1 = go.Scatter(
        x = df_display_shape['index_shape'],
        y = df_display_shape['min'],
        mode = 'lines',
        name = 'min'
    )

    trace2 = go.Scatter(
        x = df_display_shape['index_shape'],
        y = df_display_shape['mean'],
        mode = 'lines+markers',
        name = 'mean'
    )

    trace3 = go.Scatter(
        x = df_display_shape['index_shape'],
        y = df_display_shape['average'],
        mode = 'lines+markers',
        name = 'median'
    )

    data = [trace0, trace1, trace2, trace3]

    if(output_dir_terminal_state == "DASH_BOARD"):
        return (df_display_shape)
    else:
        chdir(output_dir_terminal_state)
        plotly.offline.plot(data, filename='scatter-mode')


def display_end_total_asset_data_plotly(df_return_end_total_asset_data,
                                        policy,
                                        max_percent_end_total_asset,
                                        min_percent_end_total_asset,
                                        count_quantile_0_end_total_asset,
                                        count_quantile_1_end_total_asset,
                                        count_quantile_2_end_total_asset,
                                        count_quantile_3_end_total_asset,
                                        count_quantile_4_end_total_asset):

    max_end_total_asset = df_return_end_total_asset_data.iloc[0]['max_value']
    min_end_total_asset = df_return_end_total_asset_data.iloc[0]['bottom']
    mean_end_total_asset = df_return_end_total_asset_data.iloc[0]['mean']
    median_end_total_asset = df_return_end_total_asset_data.iloc[0]['median']

    text_median = []
    text_mean = []
    for i in df_return_end_total_asset_data.index_iter:
        if(i == 0):
            text_median.append("median")
            text_mean.append("mean")
        else:
            text_median.append("")
            text_mean.append("")

    trace1 = go.Scatter(
        x = df_return_end_total_asset_data['index_iter'],
        y = df_return_end_total_asset_data['end_total_asset'],
        mode = 'lines+markers',
        name = 'end_total_asset'
    )

    if(mean_end_total_asset > median_end_total_asset):
        trace2 = go.Scatter(
            x = df_return_end_total_asset_data['index_iter'],
            y = df_return_end_total_asset_data['median'],
            mode = 'lines + text',
            name = 'median',
            text = text_median,
            textposition = 'bottom right'
        )
        trace3 = go.Scatter(
            x = df_return_end_total_asset_data['index_iter'],
            y = df_return_end_total_asset_data['mean'],
            mode = 'lines + text',
            line_color='green',
            name = 'mean',
            text = text_mean,
            textposition = 'top right'
        )
    else:
        trace2 = go.Scatter(
            x=df_return_end_total_asset_data['index_iter'],
            y=df_return_end_total_asset_data['median'],
            mode='lines + text',
            name='median',
            text=text_median,
            textposition='top right'
        )
        trace3 = go.Scatter(
            x=df_return_end_total_asset_data['index_iter'],
            y=df_return_end_total_asset_data['mean'],
            mode='lines + text',
            line_color='black',
            name='mean',
            text=text_mean,
            textposition='bottom right'
        )


    trace4 = go.Scatter(
        x = df_return_end_total_asset_data['index_iter'],
        y = df_return_end_total_asset_data['bottom'],
        mode = 'lines',
        name = 'bottom'
    )
    trace5 = go.Scatter(
        x = df_return_end_total_asset_data['index_iter'],
        y = df_return_end_total_asset_data['max_value'],
        mode = 'lines',
        name = 'median',
    )
    trace6 = go.Scatter(
        x = df_return_end_total_asset_data['index_iter'],
        y = df_return_end_total_asset_data['quantile_1'],
        mode = 'lines',
        name = 'quantile_1',
        line_color = 'grey',
        line_dash = 'dash'
    )
    trace7 = go.Scatter(
        x = df_return_end_total_asset_data['index_iter'],
        y = df_return_end_total_asset_data['quantile_2'],
        mode = 'lines',
        name = 'quantile_2',
        line_color = 'grey',
        line_dash = 'dash'
    )
    trace8 = go.Scatter(
        x=df_return_end_total_asset_data['index_iter'],
        y=df_return_end_total_asset_data['quantile_3'],
        mode='lines',
        name='quantile_3',
        line_color = 'grey',
        line_dash = 'dash'
    )
    trace9 = go.Scatter(
        x=df_return_end_total_asset_data['index_iter'],
        y=df_return_end_total_asset_data['quantile_4'],
        mode='lines',
        name='quantile_4',
        line_color = 'grey',
        line_dash = 'dash'
    )

    data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9]
    plotly.offline.plot(data, filename='end_total_asset')


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

    plotly.offline.plot(fig, filename='terminal_comparison')
