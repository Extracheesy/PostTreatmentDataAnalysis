import dash
import dash_html_components as html
import dash_core_components as dcc

from dash.dependencies import Input, Output

import plotly
import plotly.graph_objects as go
import plotly.express as px

import os

HOME_CWD = str(os.getcwd()).replace("\\","/")

from init_data import *

df_global_info_whole_data , df_global_full_terminal_data , df_global_full_stocks_data, df_global_full_trades_data = Init_data()
# df_global_full_terminal_data = Init_data("FULL_TERMINAL_DATA")
# df_global_full_stocks_data = Init_data("FULL_STOCKS_DATA")
txt_info_run = get_info_text(df_global_info_whole_data)
IN_OUT_SEMAPHORE = "WAITING"

app = dash.Dash()

list_algo = ['PPO', 'A2C']
list_policy = ['MlpPolicy', 'MlpLstmPolicy', 'MlpLnLstmPolicy']
list_market = ['CAC', 'DJI', 'DAX']

fig = px.pie(df_global_info_whole_data, values="algo", names="policy")

tabs_styles = {
    'height': '44px'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold'
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '6px'
}

app.layout = html.Div(
    [

        html.H1("DATA ANALYSE DASHBOARD"),



        dcc.Tabs(id="tabs-styled-with-inline", value='tab-1', children=[
            dcc.Tab(label='Tab 1', value='tab-1', style=tab_style, selected_style=tab_selected_style),
            dcc.Tab(label='Tab 2', value='tab-2', style=tab_style, selected_style=tab_selected_style),
            dcc.Tab(label='Tab 3', value='tab-3', style=tab_style, selected_style=tab_selected_style),
            dcc.Tab(label='Tab 4', value='tab-4', style=tab_style, selected_style=tab_selected_style),
        ],style=tabs_styles),





        html.Div(id='element-to-hide_tab1', children=[
            html.Div(id="dropdown_type", children=[
                html.Div(
                    dcc.Dropdown(
                        id='dropdown_filter_algo',
                        value='algo',
                        options=[{'value': x, 'label': x}
                                 for x in ['algo', 'policy', 'market']],
                        clearable=True,
                        disabled=False
                    ),
                    style={'display': 'inline-block', 'width': '48%'},
                ),
            ], style={'display': 'inline-block', 'width': '100%'}
                     ),
            html.Div(id="pie_and_bar_chart", children=[
                html.Div(
                    dcc.Graph(id="pie-chart",
                              ), style={'display': 'inline-block', 'width': '48%'},
                ),
                html.Div(
                    dcc.Graph(id="bar-chart",
                              #style={'width': '48%', 'height': '100%'}
                              ),
                    style={'display': 'inline-block', 'width': '48%'},
                ),
            ],style={'display': 'inline-block', 'width': '100%'}
                     ),

            html.Div(id="group_dropdown_terminal_mean_chart_1", children=[
                    html.Div(
                        dcc.Dropdown(
                            id='dropdown_filter_terminal_mean_1',
                            value='NO FILTER',
                            options=[{'value': x, 'label': x}
                                 for x in ["NO FILTER" , "DJI", "CAC", "DAX" , "MlpPolicy", "MlpLstmPolicy","MlpLnLstmPolicy", "PPO" , "A2C" ]],
                            clearable=True,
                            disabled=False
                        ),
                        style={'display': 'inline-block', 'width': '48%'},
                    ),
                    html.Div(
                        dcc.Dropdown(
                            id='dropdown_filter_terminal_mean_2',
                            value='NO FILTER',
                            options=[{'value': x, 'label': x}
                                     for x in
                                     ["NO FILTER", "DJI", "CAC", "DAX", "MlpPolicy", "MlpLstmPolicy", "MlpLnLstmPolicy", "PPO", "A2C"]],
                            clearable=True,
                            disabled=False
                        ),
                        style={'display': 'inline-block', 'width': '48%'},
                    ),
            ], style={'display': 'inline-block', 'width': '100%'}
                     ),

            html.Div(id="group_graph_terminal_mean_chart_1", children=[
                html.Div(id="terminal_mean_chart_1", children=[
                    html.Div(dcc.Graph(id="terminal_mean_graph_1", ), style={'display': 'inline-block', 'width': '100%'}, ),
                ], style={'display': 'inline-block', 'width': '48%'}
                         ),
                html.Div(id="terminal_mean_chart_2", children=[
                    html.Div(dcc.Graph(id="terminal_mean_graph_2", ), style={'display': 'inline-block', 'width': '100%'}, ),
                ], style={'display': 'inline-block', 'width': '48%'}
                         ),
            ], style={'display': 'inline-block', 'width': '100%'}
                     ),
            html.Div(id="group_graph_terminal_mean_chart_3", children=[
                html.Div(
                    dcc.Dropdown(
                        id='dropdown_filter_terminal_mean_3',
                        value='NO FILTER',
                        options=[{'value': x, 'label': x}
                                 for x in ["NO FILTER" , "min", "max", "mean" , "median" ]],
                        clearable=True,
                        disabled=False
                    ),
                    style={'display': 'inline-block', 'width': '48%'},
                ),
                html.Div(
                    dcc.Dropdown(
                        id='dropdown_filter_terminal_mean_4',
                        value='NO FILTER',
                        options=[{'value': x, 'label': x}
                                 for x in
                                 ["NO FILTER", "DJI", "CAC", "DAX", "MlpPolicy", "MlpLstmPolicy", "MlpLnLstmPolicy", "PPO",
                                  "A2C"]],
                        clearable=True,
                        disabled=False
                    ),
                    style={'display': 'inline-block', 'width': '48%'},
                ),
                html.Div(id="terminal_mean_chart_3", children=[
                    html.Div(dcc.Graph(id="terminal_mean_graph_3", ), style={'display': 'inline-block', 'width': '100%'}, ),
                ], style={'display': 'inline-block', 'width': '48%'}
                         ),
                html.Div(id="terminal_mean_chart_4", children=[
                    html.Div(dcc.Graph(id="terminal_mean_graph_4", ), style={'display': 'inline-block', 'width': '100%'}, ),
                ], style={'display': 'inline-block', 'width': '48%'}
                         ),
            ], style={'display': 'inline-block', 'width': '100%'}
                      ),

            html.Div(id="group_terminal_asset", children=[
                html.Div(id="group_terminal_asset_dropdown", children=[
                    html.Div(
                        dcc.Dropdown(
                            id='dropdown_filter_terminal_asset_algo',
                            value='NO FILTER',
                            options=[{'value': x, 'label': x}
                                     for x in ["NO FILTER", "A2C", "PPO"]],
                            clearable=True,
                            disabled=False
                        ),
                        style={'display': 'inline-block', 'width': '30%'},
                    ),
                    html.Div(
                        dcc.Dropdown(
                            id='dropdown_filter_terminal_asset_policy',
                            value='NO FILTER',
                            options=[{'value': x, 'label': x}
                                     for x in
                                     ["NO FILTER" , "MlpPolicy", "MlpLstmPolicy", "MlpLnLstmPolicy"]],
                            clearable=True,
                            disabled=False
                        ),
                        style={'display': 'inline-block', 'width': '30%'},
                    ),
                    html.Div(
                        dcc.Dropdown(
                            id='dropdown_filter_terminal_asset_market',
                            value='NO FILTER',
                            options=[{'value': x, 'label': x}
                                     for x in
                                     ["NO FILTER", "DJI", "CAC", "DAX"]],
                            clearable=True,
                            disabled=False
                        ),
                        style={'display': 'inline-block', 'width': '30%'},
                    ),
                ], style={'display': 'inline-block', 'width': '100%'}
                         ),
                html.Div(id="group_terminal_asset_graph", children=[

                    html.Div(id="terminal_asset_graph_1", children=[
                        html.Div(dcc.Graph(id="display_terminal_asset_graph_1", ), style={'display': 'inline-block', 'width': '100%'}, ),
                    ], style={'display': 'inline-block', 'width': '68%'}
                             ),
                    html.Div(id="terminal_asset_graph_2", children=[
                        html.Div(dcc.Graph(id="display_terminal_asset_graph_2", ), style={'display': 'inline-block', 'width': '100%'}, ),
                    ], style={'display': 'inline-block', 'width': '28%'}
                             ),
                ], style={'display': 'inline-block', 'width': '100%'}
                         ),
            ], style={'display': 'inline-block', 'width': '100%'}
                     ),

            html.Div(id="group_terminal_test", children=[
                    html.Div(id="group_terminal_test_dropdown", children=[
                        html.Div(
                            dcc.Dropdown(
                                id='dropdown_filter_terminal_test_algo1',
                                value='NO FILTER',
                                options=[{'value': x, 'label': x}
                                         for x in ["NO FILTER", "A2C", "PPO"]],
                                clearable=True,
                                disabled=False
                            ),
                            style={'display': 'inline-block', 'width': '30%'},
                        ),
                        html.Div(
                            dcc.Dropdown(
                                id='dropdown_filter_terminal_test_algo2',
                                value='NO FILTER',
                                options=[{'value': x, 'label': x}
                                         for x in ["NO FILTER" , "MlpPolicy", "MlpLstmPolicy", "MlpLnLstmPolicy"]],
                                clearable=True,
                                disabled=False
                            ),
                            style={'display': 'inline-block', 'width': '30%'},
                        ),
                        html.Div(
                            dcc.Dropdown(
                                id='dropdown_filter_terminal_test_algo3',
                                value='NO FILTER',
                                options=[{'value': x, 'label': x}
                                         for x in ["NO FILTER", "DJI", "CAC", "DAX"]],
                                clearable=True,
                                disabled=False
                            ),
                            style={'display': 'inline-block', 'width': '30%'},
                        ),

                        html.Div([
                            dcc.Slider(
                                id="slider_filter_terminal_test",
                                #marks={i: '{}'.format(10 ** i) for i in range(4)},
                                min=0,
                                max=1000,
                                value=0,
                                step=1,
                                #updatemode='drag'
                                updatemode='mouseup'
                            ),
                            #html.Div(id='slider_updatemode_output_container', style={'margin-top': 20})
                        ])
                    ], style={'display': 'inline-block', 'width': '100%'}
                             ),
            ], style={'display': 'inline-block', 'width': '100%'}
                     ),
            html.Div(id="group_terminal_test_graph_1", children=[
                html.Div(id="terminal_test_graph_1", children=[
                    html.Div(dcc.Graph(id="display_terminal_sharpe_graph_1", ), style={'display': 'inline-block', 'width': '68%'}, ),
                    html.Div(dcc.Graph(id="display_terminal_sharpe_graph_2", ), style={'display': 'inline-block', 'width': '28%'}, ),
                ], style={'display': 'inline-block', 'width': '49%'}
                         ),
                html.Div(id="terminal_test_graph_2", children=[
                    html.Div(dcc.Graph(id="display_terminal_reward_graph_1", ), style={'display': 'inline-block', 'width': '68%'}, ),
                    html.Div(dcc.Graph(id="display_terminal_reward_graph_2", ), style={'display': 'inline-block', 'width': '28%'}, ),
                ], style={'display': 'inline-block', 'width': '49%'}
                     ),
            ], style={'display': 'inline-block', 'width': '100%'}
                             ),


            html.Div(id="group_terminal_test_graph_2", children=[
                html.Div(id="terminal_test_graph_3", children=[
                    html.Div(dcc.Graph(id="display_terminal_trades_graph_1", ), style={'display': 'inline-block', 'width': '68%'}, ),
                    html.Div(dcc.Graph(id="display_terminal_trades_graph_2", ), style={'display': 'inline-block', 'width': '28%'}, ),
                ], style={'display': 'inline-block', 'width': '49%'}
                         ),
                html.Div(id="terminal_test_graph_4", children=[
                    html.Div(dcc.Graph(id="display_terminal_end_asset_graph_1", ), style={'display': 'inline-block', 'width': '100%'}, ),
                ], style={'display': 'inline-block', 'width': '49%'}
                         ),
            ], style={'display': 'inline-block', 'width': '100%'}
                     ),



            html.Div(id="group_sharpe_trades", children=[
                html.Div(id="group_sharpe_trades_dropdown", children=[
                    html.Div(
                        dcc.Dropdown(
                            id='dropdown_filter_sharpe_trades_algo1',
                            value='NO FILTER',
                            options=[{'value': x, 'label': x}
                                     for x in ["NO FILTER", "A2C", "PPO"]],
                            clearable=True,
                            disabled=False
                        ),
                        style={'display': 'inline-block', 'width': '30%'},
                    ),
                    html.Div(
                        dcc.Dropdown(
                            id='dropdown_filter_sharpe_trades_algo2',
                            value='NO FILTER',
                            options=[{'value': x, 'label': x}
                                     for x in ["NO FILTER", "MlpPolicy", "MlpLstmPolicy", "MlpLnLstmPolicy"]],
                            clearable=True,
                            disabled=False
                        ),
                        style={'display': 'inline-block', 'width': '30%'},
                    ),
                    html.Div(
                        dcc.Dropdown(
                            id='dropdown_filter_sharpe_trades_algo3',
                            value='NO FILTER',
                            options=[{'value': x, 'label': x}
                                     for x in ["NO FILTER", "DJI", "CAC", "DAX"]],
                            clearable=True,
                            disabled=False
                        ),
                        style={'display': 'inline-block', 'width': '30%'},
                    ),

                ], style={'display': 'inline-block', 'width': '100%'}
                         ),
                    html.Div(id="group_sharpe_trades_graph_1", children=[
                            html.Div(dcc.Graph(id="display_sharpe_trades_graph_1", ), style={'display': 'inline-block', 'width': '48%'}, ),
                            html.Div(dcc.Graph(id="display_sharpe_trades_graph_2", ), style={'display': 'inline-block', 'width': '48%'}, ),
                ], style={'display': 'inline-block', 'width': '100%'}
                                 ),
            ], style={'display': 'inline-block', 'width': '100%'}
                         ),
        ], style={'display': 'block'} # Start tab 1
                 ), # End tab 1







        html.Div(id='element-to-hide_tab2', children=[   # Start tab 2


            html.Div(id="dropdown_group_trades_filter_1_1", children=[

                html.Div(
                    dcc.Dropdown(
                        id='dropdown_trades_filter_algo_1_1',
                        value='NO FILTER',
                        options=[{'value': x, 'label': x}
                                 for x in ["NO FILTER" , "A2C", "PPO"]],
                        clearable=True,
                        disabled=False
                    ),
                    style={'display': 'inline-block', 'width': '30%'},
                ),

                html.Div(
                    dcc.Dropdown(
                        id='dropdown_trades_filter_policy_1_2',
                        value='NO FILTER',
                        options=[{'value': x, 'label': x}
                                 for x in ["NO FILTER" , "MlpPolicy", "MlpLstmPolicy","MlpLnLstmPolicy"]],
                        clearable=True,
                        disabled=False
                    ),
                    style={'display': 'inline-block', 'width': '30%'},
                ),

                html.Div(
                    dcc.Dropdown(
                        id='dropdown_trades_filter_market_1_3',
                        value='NO FILTER',
                        options=[{'value': x, 'label': x}
                                 for x in ["NO FILTER" , "CAC" , "DJI", "DAX"]],
                        clearable=True,
                        disabled=False
                    ),
                    style={'display': 'inline-block', 'width': '30%'},
                ),

            ], style={'display': 'inline-block', 'width': '100%'}
                     ),

            html.Div([
                dcc.Slider(
                    id="slider_filter_trades_1_4",
                    # marks={i: '{}'.format(10 ** i) for i in range(4)},
                    min=0,
                    max=1000,
                    value=0,
                    step=1,
                    # updatemode='drag'
                    updatemode='mouseup'
                ),
                # html.Div(id='slider_updatemode_output_container', style={'margin-top': 20})
            ], style={'display': 'inline-block', 'width': '100%'}
                     ),


            html.Div(id="group_trades_graph_1_1", children=[
                html.Div(dcc.Graph(id="display_trades_graph_1_1", ),
                         style={'display': 'inline-block', 'width': '100%'},
                         ),
                html.Div(dcc.Graph(id="display_trades_graph_1_2", ),
                         style={'display': 'inline-block', 'width': '100%'},
                         ),
                html.Div(dcc.Graph(id="display_trades_graph_1_3", ),
                         style={'display': 'inline-block', 'width': '100%'},
                         ),
            ], style={'display': 'inline-block', 'width': '100%'}
                     ),

        ], style={'display': 'block'}  # End tab 2
                 ),

    ], style={'display': 'inline-block', 'width': '100%'} # End Whole HTML
)






# @app.callback(Output('tabs-content-inline', 'children'),
@app.callback([Output(component_id='element-to-hide_tab1', component_property='style'),
               Output(component_id='element-to-hide_tab2', component_property='style'),],
              [Input('tabs-styled-with-inline', 'value')])
# def render_content(tab, algo, policy, market):
def render_content(tab):
    if tab == 'tab-1':
        return {'display': 'block'} , {'display': 'none'}
    elif tab == 'tab-2':
        return {'display': 'none'} , {'display': 'block'}
    elif tab == 'tab-3':
        return {'display': 'none'} , {'display': 'none'}
    elif tab == 'tab-4':
        return {'display': 'none'} , {'display': 'none'}




@app.callback(
    Output("pie-chart", "figure"),
    [Input("dropdown_filter_algo", "value")])
def generate_chart(filter_id):

    df_data_computer = get_info_df(df_global_info_whole_data, filter_id)

    # fig = px.pie(df_data_computer, values='iter', names='filter', color_discrete_sequence = px.colors.sequential.RdBu)
    fig = px.pie(df_data_computer, values='iter', names='filter', color = 'color_bar')


    fig.update_layout(
        title_text = txt_info_run[0]
    )
    return fig



@app.callback(
    Output("bar-chart", "figure"),
    [Input("dropdown_filter_algo", "value")])
def generate_chart(filter_id):

    df_compute_data = get_info_df(df_global_info_whole_data, filter_id)

    # fig = px.bar(df_data_computer, x="filter", y='iter', text = 'iter', color = 'color_bar', color_discrete_sequence = px.colors.sequential.RdBu)
    fig = px.bar(df_compute_data, x="filter", y='iter', text='iter', color = 'color_bar')

    if (filter_id == "algo"):
        fig.update_layout(
            title_text=txt_info_run[1],
        )
        fig.update_layout(
            showlegend=False,
        )
    if (filter_id == "policy"):
        fig.update_layout(
            title_text=txt_info_run[2]
        )
        fig.update_layout(
            showlegend=False,
        )
    if (filter_id == "market"):
        fig.update_layout(
            title_text=txt_info_run[3]
        )
        fig.update_layout(
            showlegend=False,
        )

    #fig.update_yaxes(title='y', visible=False, showticklabels=True)
    #fig.update_yaxes(title='x', visible=False, showticklabels=True)

    return fig


@app.callback(
    Output("terminal_mean_graph_1", "figure"),
    [Input("dropdown_filter_terminal_mean_1", "value")])
def generate_terminal_mean_graph_1(filter_id):

    df_copy_global_data = df_global_full_terminal_data.copy(deep=True)
    df_filtered_full_terminal_data = filter_dataframe(df_copy_global_data, filter_id)
    df_scatter_lines = display_whole_dataframe_plotly(df_filtered_full_terminal_data, "DASH_BOARD")

    display_text = "Run: " + filter_id + " max: " + str(np.int64(df_scatter_lines.iloc[17]['max'])) \
                   + " min: " + str(np.int64(df_scatter_lines.iloc[17]['min'])) \
                   + " mean: " + str(np.int64(df_scatter_lines.iloc[17]['mean'])) \
                   + " median: " + str(np.int64(df_scatter_lines.iloc[17]['average']))

    fig = px.line(df_scatter_lines, x="index_shape", y=['max','min','mean','average'])

    fig.update_layout(
        title_text = display_text
    )

    #fig.update_yaxes(title='y', visible=False, showticklabels=True)
    #fig.update_yaxes(title='x', visible=False, showticklabels=True)

    #############################
    # get values from dataframe
    #############################
    #print("df_scatter_lines.iloc[0]['max']     ", df_scatter_lines.iloc[0]['max'])
    #print("df_scatter_lines['max'].values[0]   ", df_scatter_lines['max'].values[0] )
    #fig.add_hline(y= df_scatter_lines['max'].values[0])
    #fig.add_hline(y=df_scatter_lines['max'].values[17])

    fig.update_xaxes(title='x', visible=False, showticklabels=True)

    return fig

@app.callback(
    Output("terminal_mean_graph_2", "figure"),
    [Input("dropdown_filter_terminal_mean_2", "value")])
def generate_terminal_mean_graph_2(filter_id):

    # df_compute_data = get_info_df(df_global_info_whole_data, filter_id)
    df_copy_global_data = df_global_full_terminal_data.copy(deep=True)
    df_filtered_full_terminal_data = filter_dataframe(df_copy_global_data, filter_id)
    df_scatter_lines = display_whole_dataframe_plotly(df_filtered_full_terminal_data, "DASH_BOARD")

    fig = px.line(df_scatter_lines, x="index_shape", y=['max','min','mean','average'])

    display_text = "Run: " + filter_id + " max: " + str(np.int64(df_scatter_lines.iloc[17]['max']))\
                   + " min: " + str(np.int64(df_scatter_lines.iloc[17]['min'])) \
                   + " mean: " + str(np.int64(df_scatter_lines.iloc[17]['mean']))\
                   + " median: " + str(np.int64(df_scatter_lines.iloc[17]['average']))

    fig.update_layout(
        title_text=display_text
    )

    #############################
    # get values from dataframe
    #############################
    #print("df_scatter_lines.iloc[0]['max']     ", df_scatter_lines.iloc[0]['max'])
    #print("df_scatter_lines['max'].values[0]   ", df_scatter_lines['max'].values[0] )
    #fig.add_hline(y= df_scatter_lines['max'].values[0])
    #fig.add_hline(y=df_scatter_lines['max'].values[17])

    #fig.update_yaxes(title='y', visible=False, showticklabels=True)
    fig.update_xaxes(title='x', visible=False, showticklabels=True)


    return fig


@app.callback(
    Output("terminal_mean_graph_3", "figure"),
    [Input("dropdown_filter_terminal_mean_3", "value")])
def generate_terminal_mean_graph_3(filter_id):
    frames = []

    display_dataframe_min_max_mean = pd.DataFrame({"values": ["max" , "mean" , "min"] ,
                                                   "PPO": [0,0,0],
                                                   "A2C": [0,0,0],
                                                   "CAC": [0,0,0],
                                                   "DJI": [0,0,0],
                                                   "DAX": [0,0,0],
                                                   "MlpPolicy": [0,0,0],
                                                   "MlpLstmPolicy": [0,0,0],
                                                   "MlpLnLstmPolicy": [0,0,0]})

    df_copy_global_data = df_global_full_terminal_data.copy(deep=True)

    for i in ["PPO","A2C","CAC","DJI","DAX","MlpPolicy","MlpLstmPolicy","MlpLnLstmPolicy"]:
        df_full_data = filter_raw_dataframe(df_copy_global_data, i)
        max_end_total_asset = df_full_data['end_total_asset'].max()
        mean_total_asset = df_full_data['end_total_asset'].mean()
        min_total_asset = df_full_data['end_total_asset'].min()

        display_dataframe_min_max_mean.loc[0 , i] = max_end_total_asset
        display_dataframe_min_max_mean.loc[1 , i] = mean_total_asset
        display_dataframe_min_max_mean.loc[2 , i] = min_total_asset

    fig = px.bar(display_dataframe_min_max_mean, x="values", y=["PPO","A2C","CAC","DJI","DAX","MlpPolicy","MlpLstmPolicy","MlpLnLstmPolicy"], barmode="group")

    return fig


@app.callback(
        Output("terminal_mean_graph_4", "figure"),
        [Input("dropdown_filter_terminal_mean_4", "value")])
def generate_terminal_mean_graph_2(filter_id):

    df_copy_global_data = df_global_full_terminal_data.copy(deep=True)
    df_filtered_full_terminal_data = filter_dataframe(df_copy_global_data, filter_id)
    df_scatter_lines = display_whole_dataframe_plotly(df_filtered_full_terminal_data, "DASH_BOARD")

    fig = px.line(df_scatter_lines, x="index_shape", y=['max', 'min', 'mean', 'average'])

    display_text = "Run: " + filter_id + " max: " + str(np.int64(df_scatter_lines.iloc[17]['max'])) \
                       + " min: " + str(np.int64(df_scatter_lines.iloc[17]['min'])) \
                       + " mean: " + str(np.int64(df_scatter_lines.iloc[17]['mean'])) \
                       + " median: " + str(np.int64(df_scatter_lines.iloc[17]['average']))

    fig.update_layout(title_text=display_text)

    #fig.update_yaxes(title='y', visible=False, showticklabels=True)
    #fig.update_xaxes(title='x', visible=False, showticklabels=True)
    fig.update_xaxes(title='x', visible=False)
    fig.update_xaxes(showticklabels=True)

    return fig



    #############################
    # get values from dataframe
    #############################
    #print("df_scatter_lines.iloc[0]['max']     ", df_scatter_lines.iloc[0]['max'])
    #print("df_scatter_lines['max'].values[0]   ", df_scatter_lines['max'].values[0] )
    #fig.add_hline(y= df_scatter_lines['max'].values[0])
    #fig.add_hline(y=df_scatter_lines['max'].values[17])




@app.callback(
    [Output("display_terminal_asset_graph_1", "figure"),
     Output("display_terminal_asset_graph_2", "figure"),],
    [Input("dropdown_filter_terminal_asset_algo", "value"),
     Input("dropdown_filter_terminal_asset_policy", "value"),
     Input("dropdown_filter_terminal_asset_market", "value"), ])
def generate_terminal_end_total_asset_graph_2(algo, policy, market):

        df_copy_global_data = df_global_full_terminal_data.copy(deep=True)
        df_copy_global_data.sort_values(by=['run_date'], inplace=True, ascending=True)
        df_filtered_full_terminal_data_tmp_1 = filter_raw_dataframe(df_copy_global_data, algo)
        df_filtered_full_terminal_data_tmp_2 = filter_dataframe(df_filtered_full_terminal_data_tmp_1, policy)
        df_filtered_full_terminal_data = filter_dataframe(df_filtered_full_terminal_data_tmp_2, market)

        df_filtered_computed = df_compute_terminal_end_total_asset_graph(df_filtered_full_terminal_data)

        fig_line = px.line(df_filtered_computed, x="index_iter",
                      y=['end_total_asset', 'max_value', 'bottom', 'mean', 'median', 'quantile_1', 'quantile_2',
                         'quantile_3', 'quantile_4'])

        if (algo == "NO FILTER"):
            algo = ""
        if (policy == "NO FILTER"):
            policy = ""
        if (market == "NO FILTER"):
            market = ""
        filter_txt = algo + policy + market

        if ((algo == "NO FILTER") & (policy == "NO FILTER") & (market == "NO FILTER")):
            filter_txt = "NO FILTER"

        df_computed_data_display = df_compute_quantile(df_filtered_computed)
        df_computed_data_display.insert(0, 'filter', filter_txt)



        #df_computed_data_display.insert(3, 'color_bar', 0)

        #color_bar = [0,5,10,15,20]
        color_bar = ["lightblue", "magenta", "goldenrod", "spring", "pink"]

        #fig_bar = px.bar(df_filtered_computed, x="df_computed_data_display", y=["quantile_percent_values"], color="color", text="quantile_values",
        #             title="Wide-Form Input")

        #fig_bar = px.bar(df_computed_data_display, x="filter", y=["quantile_percent_values"], color=color_bar , text="quantile_values")

        df_computed_data_display.insert(0, 'quantile_text', "")

        df_computed_data_display.quantile_text[0] = "q1: " + str(df_computed_data_display.quantile_values[0]) + " - " + str(int(df_computed_data_display.quantile_percent_values[0])) + "%"
        df_computed_data_display.quantile_text[1] = "q2: " + str(df_computed_data_display.quantile_values[1]) + " - " + str(int(df_computed_data_display.quantile_percent_values[1])) + "%"
        df_computed_data_display.quantile_text[2] = "q3: " + str(df_computed_data_display.quantile_values[2]) + " - " + str(int(df_computed_data_display.quantile_percent_values[2])) + "%"
        df_computed_data_display.quantile_text[3] = "q4: " + str(df_computed_data_display.quantile_values[3]) + " - " + str(int(df_computed_data_display.quantile_percent_values[3])) + "%"
        df_computed_data_display.quantile_text[4] = "q5: " + str(df_computed_data_display.quantile_values[4]) + " - " + str(int(df_computed_data_display.quantile_percent_values[4])) + "%"

        #fig_bar = px.bar(df_computed_data_display, x="filter", y=["quantile_percent_values"], text="quantile_values")
        fig_bar = px.bar(df_computed_data_display, x="filter", y=["quantile_percent_values"], text="quantile_text", color=color_bar)

        #fig_bar.update_yaxes(title='y', visible=False, showticklabels=True)
        #fig_bar.update_yaxes(title='x', visible=False, showticklabels=True)

        #fig_line.update_yaxes(title='y', visible=False, showticklabels=True)
        #fig_line.update_yaxes(title='x', visible=False, showticklabels=True)

        fig_bar.update_xaxes(title='x', visible=False)
        #fig_bar.update_layout(title_text="Quantile")
        fig_bar.update_layout(showlegend=False,)
        return fig_line, fig_bar




@app.callback(
    [Output("display_terminal_sharpe_graph_1", "figure"),
     Output("display_terminal_sharpe_graph_2", "figure"),
     Output("display_terminal_reward_graph_1", "figure"),
     Output("display_terminal_reward_graph_2", "figure"),
     Output("display_terminal_trades_graph_1", "figure"),
     Output("display_terminal_trades_graph_2", "figure"),
     Output("display_terminal_end_asset_graph_1", "figure")],
    [Input("dropdown_filter_terminal_test_algo1", "value"),
     Input("dropdown_filter_terminal_test_algo2", "value"),
     Input("dropdown_filter_terminal_test_algo3", "value"),
     Input('slider_filter_terminal_test', 'value')])
def generate_terminal_end_total_test_graph_2(filter_algo, filter_policy, filter_market,slide_value):

    global IN_OUT_SEMAPHORE
    global df_global_full_terminal_data


    if (filter_algo != "NO FILTER") and (filter_algo != "A2C")  and (filter_algo != "PPO"):
        filter_algo = "NO FILTER"

    if (filter_policy != "NO FILTER") and (filter_policy != "MlpPolicy") and (filter_policy != "MlpLstmPolicy") and (filter_policy != "MlpLnLstmPolicy"):
        filter_policy = "NO FILTER"

    if (filter_market != "NO FILTER") and (filter_market != "CAC") and (filter_market != "DAX") and (filter_market != "DJI"):
        filter_market = "NO FILTER"


    if (IN_OUT_SEMAPHORE == "WAITING"):
        IN_OUT_SEMAPHORE = "BUSY"
        df_filtered_full_terminal_data_tmp = df_global_full_terminal_data.copy(deep=True)
        df_copy_global_data = df_global_full_terminal_data.copy(deep=True)

        ### sort ###
        df_filtered_full_terminal_data_tmp.sort_values(by=['end_total_asset'], inplace=True, ascending=False)

        ### filter ###
        df_filtered_full_terminal_data_tmp_1 = filter_raw_dataframe(df_filtered_full_terminal_data_tmp, filter_algo)
        df_filtered_full_terminal_data_tmp_2 = filter_dataframe(df_filtered_full_terminal_data_tmp_1, filter_policy)
        df_filtered_full_terminal_data = filter_dataframe(df_filtered_full_terminal_data_tmp_2, filter_market)

        ### sort ###
        df_filtered_full_terminal_data.sort_values(by=['end_total_asset'], inplace=True, ascending=False)

        ### count ###
        nb_run_selected = len(df_filtered_full_terminal_data)

        # 1000 -> nb_run_selected
        # slide_value -> x
        value_picked = np.int64(nb_run_selected * slide_value / 1000)
        if (value_picked >= nb_run_selected):
            value_picked = nb_run_selected - 1

        # print("value picked by slide ", value_picked)

        run_date_picked = np.int64(df_filtered_full_terminal_data.iloc[value_picked]['run_date'])
        run_time_picked = np.int64(df_filtered_full_terminal_data.iloc[value_picked]['run_time'])
        end_total_asset_picked = np.int64(df_filtered_full_terminal_data.iloc[value_picked]['end_total_asset'])

        df_date_time_data_selected = df_copy_global_data.copy(deep=True)

        if (run_time_picked < 100000):
            str_run_time_picked = "0" + str(run_time_picked)
            if (run_time_picked < 10000):
                str_run_time_picked = "0" + str_run_time_picked
                if (run_time_picked < 1000):
                    str_run_time_picked = "0" + str_run_time_picked
                    if (run_time_picked < 100):
                        str_run_time_picked = "0" + str_run_time_picked
                        if (run_time_picked < 10):
                            str_run_time_picked = "0" + str_run_time_picked
        else:
            str_run_time_picked = str(run_time_picked)
        str_run_date_picked = str(run_date_picked)

        df_filtered_data_1 = df_date_time_data_selected[((df_date_time_data_selected.run_time == str_run_time_picked) & (df_date_time_data_selected.run_date == str_run_date_picked))]

        df_filtered_data_1.sort_values(by=['iter_num'], inplace=True, ascending=True)

        fig_sharpe = px.bar(df_filtered_data_1, x="iter_num", y=["sharpe"], color_discrete_sequence=["pink"] )

        fig_sharpe.update_layout(
            showlegend=False,
        )
        fig_sharpe.update_xaxes(title='x', visible=False)

        color_bar = ["lightblue", "magenta", "goldenrod"]

        df_sharpe_stats = pd.DataFrame({"y": ["max",
                                              "mean",
                                              "min"],
                                        "values": [df_filtered_data_1.sharpe.max(),
                                                   df_filtered_data_1.sharpe.mean(),
                                                   df_filtered_data_1.sharpe.min()]
                                        })

        fig_bar_sharpe = px.bar(df_sharpe_stats, x="y", y="values", color = color_bar)

        fig_sharpe.update_xaxes(title='x', visible=False)
        fig_sharpe.update_layout(showlegend=False,)
        fig_bar_sharpe.update_xaxes(title='x', visible=False)
        #fig_bar_stats.update_yaxes(title='y', visible=False)
        fig_bar_sharpe.update_layout(showlegend=False,)

        return_display_value = "Date Time " + str(run_date_picked) + " "+ str(run_time_picked) \
                               + " Sharpe Max " +  str(round(df_filtered_data_1.sharpe.max(),2)) \
                               + " Min " + str(round(df_filtered_data_1.sharpe.min(),2)) \
                               + " Mean " + str(round(df_filtered_data_1.sharpe.mean(),2))

        fig_sharpe.update_layout(title_text=return_display_value)
        fig_reward = px.bar(df_filtered_data_1, x="iter_num", y=["total_reward"], color_discrete_sequence=["orange"])

        fig_reward.update_layout(
            showlegend=False,
        )
        fig_reward.update_xaxes(title='x', visible=False)

        color_bar = ["lightblue", "magenta", "goldenrod"]

        df_reward_stats = pd.DataFrame({"y": ["max",
                                              "mean",
                                              "min"],
                                        "values": [df_filtered_data_1.total_reward.max(),
                                                   df_filtered_data_1.total_reward.mean(),
                                                   df_filtered_data_1.total_reward.min()]
                                        })

        fig_bar_reward = px.bar(df_reward_stats, x="y", y="values", color = color_bar)

        fig_reward.update_xaxes(title='x', visible=False)
        fig_reward.update_layout(showlegend=False,)
        fig_bar_reward.update_xaxes(title='x', visible=False)
        #fig_bar_stats.update_yaxes(title='y', visible=False)
        fig_bar_reward.update_layout(showlegend=False,)

        return_display_value = "Reward $ Max " + str(int(df_filtered_data_1.total_reward.max())) \
                               + " Min " + str(int(df_filtered_data_1.total_reward.min())) \
                               + " Mean " + str(int(df_filtered_data_1.total_reward.mean()))

        fig_reward.update_layout(title_text=return_display_value)





        fig_trades = px.bar(df_filtered_data_1, x="iter_num", y=["total_trade"], color_discrete_sequence=["green"])

        fig_trades.update_layout(
            showlegend=False,
        )
        fig_trades.update_xaxes(title='x', visible=False)

        color_bar = ["lightblue", "magenta", "goldenrod"]

        df_trades_stats = pd.DataFrame({"y": ["max",
                                              "mean",
                                              "min"],
                                         "values": [df_filtered_data_1.total_trade.max(),
                                                    df_filtered_data_1.total_trade.mean(),
                                                    df_filtered_data_1.total_trade.min()]
                                         })

        fig_bar_trades = px.bar(df_trades_stats, x="y", y="values", color = color_bar)

        fig_trades.update_xaxes(title='x', visible=False)
        fig_trades.update_layout(showlegend=False,)
        fig_bar_trades.update_xaxes(title='x', visible=False)
        #fig_bar_trades.update_yaxes(title='y', visible=False)
        fig_bar_trades.update_layout(showlegend=False,)

        return_display_value = "Max trades " + str(int(df_filtered_data_1.total_trade.max())) + " Min Trades " + str(int(df_filtered_data_1.total_trade.min())) + " Mean Trades " + str(int(df_filtered_data_1.total_trade.mean()))

        fig_trades.update_layout(title_text=return_display_value)

        fig_end_asset = px.line(df_filtered_data_1, x="iter_num", y=["end_total_asset"], color_discrete_sequence=["red"])

        fig_end_asset.update_layout(
            showlegend=False,
        )
        fig_end_asset.update_xaxes(title='x', visible=False)

        fig_end_asset.update_xaxes(title='x', visible=False)
        fig_end_asset.update_layout(showlegend=False,)

        return_display_value = "Asset $ Rank " + str(value_picked) \
                               + " Max " + str(end_total_asset_picked)\
                               + " ROI " + str( round(data_calculation_percent (end_total_asset_picked , 1000000),1)) + "%"\
                               + " ROIy " + str( round(data_calculation_percent (end_total_asset_picked , 1000000)/4,1)) + "%"

        fig_end_asset.update_layout(title_text=return_display_value)

        IN_OUT_SEMAPHORE = "WAITING"

        #return fig, html.Div([html.H4("")]), fig_bar_stats
        return fig_sharpe, fig_bar_sharpe, fig_reward, fig_bar_reward, fig_trades, fig_bar_trades, fig_end_asset
    else:
        return None,None
        pass



@app.callback(
    [Output("display_sharpe_trades_graph_1", "figure"),
     Output("display_sharpe_trades_graph_2", "figure")],
    [Input("dropdown_filter_sharpe_trades_algo1", "value"),
    Input("dropdown_filter_sharpe_trades_algo2", "value"),
    Input("dropdown_filter_sharpe_trades_algo3", "value")])
def generate_terminal_sharpe_trades_graph(filter_algo, filter_policy, filter_market):

    global df_global_full_terminal_data

    if (filter_algo != "NO FILTER") and (filter_algo != "A2C")  and (filter_algo != "PPO"):
        filter_algo = "NO FILTER"

    if (filter_policy != "NO FILTER") and (filter_policy != "MlpPolicy") and (filter_policy != "MlpLstmPolicy") and (filter_policy != "MlpLnLstmPolicy"):
        filter_policy = "NO FILTER"

    if (filter_market != "NO FILTER") and (filter_market != "CAC") and (filter_market != "DAX") and (filter_market != "DJI"):
        filter_market = "NO FILTER"

    df_copy_global_data_sharpe = df_global_full_terminal_data.copy(deep=True)
    #df_copy_global_data_trades = df_global_full_terminal_data.copy(deep=True)

    ### filter ###
    df_copy_global_data_sharpe = filter_dataframe(df_copy_global_data_sharpe, filter_algo)
    df_copy_global_data_sharpe = filter_dataframe(df_copy_global_data_sharpe, filter_policy)
    df_copy_global_data_sharpe = filter_dataframe(df_copy_global_data_sharpe, filter_market)

    df_copy_global_data_sharpe.insert(1, 'mean_sharpe', 0.0)
    df_copy_global_data_sharpe.insert(1, 'mean_trade', 0.0)

    list_run_date = pd.unique(df_copy_global_data_sharpe['run_date'])

    for r_date in list_run_date :

        df_filtered_sharpe_r_date = df_copy_global_data_sharpe[df_copy_global_data_sharpe.run_date == r_date]

        list_run_time = pd.unique(df_filtered_sharpe_r_date['run_time'])

        for r_time in list_run_time :
            df_filtered_sharpe_r_time = df_filtered_sharpe_r_date[df_filtered_sharpe_r_date.run_time == r_time]

            sum_sharpe = df_filtered_sharpe_r_time['sharpe'].sum()
            sum_total_trade = df_filtered_sharpe_r_time['total_trade'].sum()

            df_copy_global_data_sharpe.loc[df_copy_global_data_sharpe.run_time == r_time, "mean_sharpe"] = sum_sharpe
            df_copy_global_data_sharpe.loc[df_copy_global_data_sharpe.run_time == r_time, "mean_trade"] = sum_total_trade

    df_display_sharpe = df_copy_global_data_sharpe[df_copy_global_data_sharpe.iter_num == 1197]

    df_display_sharpe.sort_values(by=['mean_sharpe'], inplace=True, ascending=True)

    # TRACES
    # df_display_sharpe.to_csv(filter_algo + filter_policy + filter_market + ".csv")

    fig_sharpe = px.line(df_display_sharpe, x="mean_sharpe", y=["end_total_asset"] , color_discrete_sequence=["red"])

    df_display_sharpe.sort_values(by=['mean_trade'], inplace=True, ascending=True)
    fig_trades = px.line(df_display_sharpe, x="mean_trade", y=["end_total_asset"] , color_discrete_sequence=["blue"])

    fig_sharpe.update_layout(showlegend=False,)
    fig_trades.update_layout(showlegend=False,)

    # fig_sharpe.update_xaxes(title='x', visible=False)
    # fig_trades.update_xaxes(title='x', visible=False)

    fig_sharpe.update_layout(title_text="Sharpe coef vs End total asset")
    fig_trades.update_layout(title_text="Total trades vs End total asset")

    return fig_sharpe, fig_trades



####################################################
#     Tab 2 - Trades
####################################################

@app.callback(
    [Output("display_trades_graph_1_1", "figure"),
     Output("display_trades_graph_1_2", "figure"),
     Output("display_trades_graph_1_3", "figure")],
    [Input("dropdown_trades_filter_algo_1_1", "value"),
     Input("dropdown_trades_filter_policy_1_2", "value"),
     Input("dropdown_trades_filter_market_1_3", "value"),
     Input('slider_filter_trades_1_4', 'value')])
def generate_terminal_end_total_test_graph_2(filter_algo, filter_policy, filter_market,slide_value):

    global df_global_full_trades_data
    global HOME_CWD

    df_copy_full_trades_data = df_global_full_trades_data.copy(deep=True)
    df_copy_full_trades_data_for_slide = df_global_full_trades_data.copy(deep=True)

    if (filter_algo != "NO FILTER") and (filter_algo != "A2C")  and (filter_algo != "PPO"):
        filter_algo = "NO FILTER"

    if (filter_policy != "NO FILTER") and (filter_policy != "MlpPolicy") and (filter_policy != "MlpLstmPolicy") and (filter_policy != "MlpLnLstmPolicy"):
        filter_policy = "NO FILTER"

    if (filter_market != "NO FILTER") and (filter_market != "CAC") and (filter_market != "DAX") and (filter_market != "DJI"):
        filter_market = "NO FILTER"

    ### filter ###
    df_filtered_full_trades_data_tmp_1 = filter_raw_dataframe(df_copy_full_trades_data_for_slide, filter_algo)
    df_filtered_full_trades_data_tmp_2 = filter_dataframe(df_filtered_full_trades_data_tmp_1, filter_policy)
    df_filtered_full_trades_data_tmp_3 = filter_dataframe(df_filtered_full_trades_data_tmp_2, filter_market)

    column_lengh = len(df_filtered_full_trades_data_tmp_3) - 1
    last_date = df_filtered_full_trades_data_tmp_3.iloc[column_lengh]['datadate']
    df_filtered_full_trades_data = df_filtered_full_trades_data_tmp_3[(df_filtered_full_trades_data_tmp_3.datadate == last_date)]

    ### sort ###
    df_filtered_full_trades_data.sort_values(by=['end_total_asset'], inplace=True, ascending=False)

    ### count ###
    nb_run_selected = len(df_filtered_full_trades_data)

    # 1000 -> nb_run_selected
    # slide_value -> x
    value_picked = np.int64(nb_run_selected * slide_value / 1000)
    if (value_picked >= nb_run_selected):
        value_picked = nb_run_selected - 1

    run_time_picked = df_filtered_full_trades_data.iloc[value_picked]['run_time']
    # print("value picked by trades slide ", value_picked)
    # print("run date picked by trades slide ", run_time_picked)


    df_filter_trades_end_assets = df_copy_full_trades_data[(df_copy_full_trades_data.run_time == run_time_picked)]

    nb_index = 0
    for i in df_filter_trades_end_assets.datadate:

        df_filter_trades_end_assets.loc[df_filter_trades_end_assets.index == nb_index, "datadate"] = nb_index
        nb_index = nb_index + 1


    fig_trades_end_assets = px.line(df_filter_trades_end_assets, x="datadate", y=["end_total_asset"], color_discrete_sequence=["green"])
    fig_trades_turbulences = px.line(df_filter_trades_end_assets, x="datadate", y=["turbulence","turbulence_threshold"], color_discrete_sequence=["blue","red"])

    lengh_df_displayed = len(df_filter_trades_end_assets)
    return_display_end_assets = "Id Date Time " + str(run_time_picked) \
                                + " Max " + str(round(df_filter_trades_end_assets.iloc[lengh_df_displayed - 1]['end_total_asset'] ,0)) \
                                + " Ranking " + str(round(value_picked))

    fig_trades_end_assets.update_layout(
        title_text = return_display_end_assets
    )

    turbulence_ok = 0
    for i in range(lengh_df_displayed):
        if df_filter_trades_end_assets.iloc[i]['turbulence'] < df_filter_trades_end_assets.iloc[i]['turbulence_threshold']:
            turbulence_ok = turbulence_ok + 1

    percent_turbulence = data_calculation_percent_normal(turbulence_ok, lengh_df_displayed)

    return_display_turbulences = "% Turbulence < Threshold  " + str(round(percent_turbulence,2)) \
                                + " Turb < Thresh " + str(turbulence_ok) \
                                + " Iteration " + str(round(lengh_df_displayed))

    fig_trades_turbulences.update_layout(
        title_text = return_display_turbulences
    )

    fig_trades_end_assets.update_layout(showlegend=False,)
    fig_trades_turbulences.update_layout(showlegend=False,)

    # input_dir  = 'C:/Users/despo/PycharmProjects/pythonProject2/InputData'

    input_dir = HOME_CWD + '/InputData'
    input_dir = input_dir.replace("\\","/")

    os.chdir(input_dir)

    if os.path.isfile('turbulence_data_computed.csv'):
        df_display_turbulence = pd.read_csv('turbulence_data_computed.csv', index_col=[0])
    else:
        df_copy_full_trades_data_turbulence = df_global_full_trades_data.copy(deep=True)

        df_display_turbulence = pd.DataFrame(columns=['run_time', 'turbulence_%', 'end_total_asset', 'algo', 'policy', 'market'])

        list_run_date_id = pd.unique(df_copy_full_trades_data_turbulence['run_time'])

        iter_print = 0
        for run_date_id in list_run_date_id:
            df_run_date_id = df_copy_full_trades_data_turbulence[(df_copy_full_trades_data_turbulence.run_time ==  run_date_id)]

            lengh_df_turb = len(df_run_date_id)
            # print("iter_print ", iter_print)
            iter_print = iter_print + 1

            turb_cpt = 0
            for i in range(lengh_df_turb):
                if df_run_date_id.iloc[i]['turbulence'] < df_run_date_id.iloc[i]['turbulence_threshold']:
                    turb_cpt = turb_cpt + 1

            percent_turbulence_for_date = round(data_calculation_percent_normal(turb_ok, lengh_df_turb), 1)
            end_total_asset_for_date = int(df_run_date_id.iloc[lengh_df_turb - 1]['end_total_asset'])
            algo_turbulence = df_run_date_id.iloc[lengh_df_turb - 1]['algo']
            policy_turbulence = df_run_date_id.iloc[lengh_df_turb - 1]['policy']
            market_turbulence = df_run_date_id.iloc[lengh_df_turb - 1]['market']

            new_row = {'run_time': [run_date_id],
                       'turbulence_%': [percent_turbulence_for_date],
                       'end_total_asset': [end_total_asset_for_date],
                       'algo': [algo_turbulence],
                       'policy': [policy_turbulence],
                       'market': [market_turbulence]}
            df_new_row = pd.DataFrame(new_row)
            df_display_turbulence = df_display_turbulence.append(df_new_row)

    ### filter ###
    df_display_turbulence_tmp1 = filter_dataframe(df_display_turbulence, filter_algo)
    df_display_turbulence_tmp2 = filter_dataframe(df_display_turbulence_tmp1, filter_policy)
    df_display_turbulence_filtered = filter_dataframe(df_display_turbulence_tmp2, filter_market)

    ### sort ###
    df_display_turbulence_filtered.sort_values(by=['end_total_asset'], inplace=True, ascending=True)



    # output_dir = 'C:/Users/despo/PycharmProjects/pythonProject2/OutputData'

    output_dir = HOME_CWD + '/OutputData'
    os.chdir(output_dir)

    if(os.path.isfile('turbulence_data_computed.csv')):
        print('turbulence_data_computed.csv OK')
    else:
        print('turbulence_data_computed.csv saved')
        df_display_turbulence.to_csv('turbulence_data_computed.csv')

    fig_end_assets_turbulence = px.line(df_display_turbulence_filtered, x="end_total_asset", y=["turbulence_%"], color_discrete_sequence=["purple"])

    os.chdir(HOME_CWD)

    return fig_trades_end_assets , fig_trades_turbulences, fig_end_assets_turbulence



