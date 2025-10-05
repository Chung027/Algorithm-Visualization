from dash import Dash, html, Input, Output,State ,callback, no_update
import plotly.graph_objs as go
import dash_bootstrap_components as dbc
from components.layout import layout
from utils.utils import generate_random_list, figure_layout
from algorithms.sort_algorithms import bubble_sort, selection_sort
app = Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.FLATLY,
        dbc.icons.BOOTSTRAP
    ],
    pages_folder="",
    suppress_callback_exceptions=True,
)
app.title = "Visualization sort algoritm"
app.layout = layout()

# Callback lives here for now to keep future maintenance simple
@app.callback(
    Output("sorting-graph", "figure", allow_duplicate=True),
    Output("stored-data","data",allow_duplicate=True),
    Output("message","children",allow_duplicate=True),
    Output("message","is_open",allow_duplicate=True),
    Output("message","color",allow_duplicate=True),
    Input("clear-btn", "n_clicks"),
    prevent_initial_call=True,
)
def clear_data_figure(n_clicks):
    if n_clicks:
        return [
            go.Figure(data=[], layout={}),
            None, 
            "Data has been successfully cleared",
            True,
            "success"
        ]
    return no_update, no_update, no_update, no_update

@app.callback(
    Output("sorting-graph", "figure", allow_duplicate=True),
    Output("stored-data","data",allow_duplicate=True),
    Output("message","children",allow_duplicate=True),
    Output("message","is_open",allow_duplicate=True),
    Output("message","color",allow_duplicate=True),
    Input("generate-btn", "n_clicks"),
    State("size-slider", "value"),
    prevent_initial_call=True
)
def generate_data(n_clicks, size):
    if n_clicks is None:
        return no_update, no_update, no_update, no_update,no_update
    list_data = generate_random_list(size)
    # The figure component takes two arguments: data and layout
    fig = go.Figure(
        data=[go.Bar(
                x=list(range(1, size+1)),
                y=list_data, 
                marker_color="lightskyblue"
            )
        ]
    )
    tickvals, ticktext = figure_layout(list_data)
    fig.update_layout(
        title="Generated Random List",
        xaxis=dict(
            tickmode="array",
            tickvals=tickvals,
            ticktext=ticktext,
            range=[0.5, size + 0.5]
        ),
        yaxis=dict(range=[0, max(list_data) + 20]),
        margin=dict(l=20, r=20, t=40, b=20)
    )
    return [
        fig, 
        list_data,
        f"Successfully generated an arraylist with {size} elements",
        True,
        "success"
    ]

@app.callback(
    Output("stored-data", "data"),
    Output("interval","disabled"),
    Output("interval","n_intervals"),
    Output("message","children"),
    Output("message","is_open"),
    Output("message","color"),
    Input("start-btn","n_clicks"),
    State("algorithm-dropdown", "value"),
    State("stored-data", "data"),
    prevent_initial_call=True
)
def start_sort_algorithms(n_clicks, algo_drop, list_data):
    if n_clicks is None:
        return [
            no_update, 
            True, 
            0,
            no_update,
            no_update,
            no_update
        ]
    if list_data is None:
        return[
            no_update,
            True,
            0,
            "Please generate a dataset before starting the algorithm",
            True,
            "danger"
        ]
    
    if algo_drop == "bubble":
        steps_sort = list(bubble_sort(list_data))
    elif algo_drop == "selection":
        steps_sort = list(selection_sort(list_data))
    return [
        steps_sort, 
        False, 
        0,
        f"Started {algo_drop.capitalize()} sort seccuessfully",
        True,
        "success"
    ]

@app.callback(
    Output("sorting-graph","figure", allow_duplicate=True),
    Input("interval","n_intervals"),
    State("stored-data","data"),
    State("size-slider", "value"),
    prevent_initial_call=True
)
def update_sort_step(n_interval, steps, list_size):
    if steps is None or n_interval >= len(steps):
        return no_update
    current_steps = steps[n_interval]
    tickvals, ticktext = figure_layout(list_size)
    sort_fig = go.Figure(
        data=[go.Bar(
                x=list(range(1, list_size+1)),
                y=current_steps, 
                marker_color="lightskyblue"
            )
        ]
    )
    sort_fig.update_layout(
        xaxis=dict(
            tickmode="array",
            tickvals=tickvals,
            ticktext=ticktext,
            range=[0.5,list_size + 0.5]
        ),
        yaxis=dict(range=[0, max(current_steps) + 20]),
        margin=dict(l=20, r=20, t=40, b=20)
    )
    
    return sort_fig
  
if __name__ == "__main__":
    app.run(debug=True)