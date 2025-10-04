from dash import Dash, html, Input, Output,State ,callback, no_update
import plotly.graph_objs as go
import dash_bootstrap_components as dbc
from components.layout import layout
from utils.utils import generate_random_list
from algorithms.sort_algorithms import bubble_sort
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
    Input("stop-btn", "n_clicks"),
    prevent_initial_call=True,
)
def clear_data_figure(n_clicks):
    if n_clicks:
        return go.Figure(data=[], layout={})
    return no_update

@app.callback(
    Output("sorting-graph", "figure", allow_duplicate=True),
    Output("stored-data","data",allow_duplicate=True),
    Input("generate-btn", "n_clicks"),
    State("size-slider", "value"),
    prevent_initial_call=True
)
def generate_data(n_clicks, size):
    if n_clicks is None:
        return no_update, no_update
    list_data = generate_random_list(size)
    # Figure component take 2 argument, they are data and layout
    fig = go.Figure(
        data=[go.Bar(
                x=list(range(1, size+1)),
                y=list_data, 
                marker_color="lightskyblue"
            )
        ]
    )
    if size <= 20:
        tickvals = [1] + list(range(2, size+1))   # visa alla från 1 till size
        ticktext = [str(v) for v in tickvals]
    elif size <= 60:
        # Visa ticks vid 1, 5, 10, 15, 20 ... upp till size
        tickvals = [1] + list(range(5, size+1, 5))
        ticktext = [str(v) for v in tickvals]
    else:
        # Visa ticks vid 1, 10, 20, 30 ... upp till size
        tickvals = [1] + list(range(10, size+1, 10))
        ticktext = [str(v) for v in tickvals]
    
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
    return fig, list_data

@app.callback(
    Output("stored-data", "data"),
    Output("interval","disabled"),
    Output("interval","n_intervals"),
    Input("start-btn","n_clicks"),
    State("algorithm-dropdown", "value"),
    State("stored-data", "data"),
    prevent_initial_call=True
)
def start_sort_algorithms(n_clicks, algo_drop, list_data):
    if n_clicks is None or list_data is None:
        return no_update, True, 0
    if algo_drop == "bubble":
        steps_sort = list(bubble_sort(list_data))
    return steps_sort, False, 0

@app.callback(
    Output("sorting-graph","figure", allow_duplicate=True),
    Input("interval","n_intervals"),
    State("stored-data","data"),
    State("size-slider", "value"),
    prevent_initial_call=True
)
def sort_animation_step(n_interval, steps, list_size):
    if steps is None or n_interval >= len(steps):
        return no_update
    current_steps = steps[n_interval]
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
            tickmode="linear",
            tick0=1,
            dtick=1,
            range=[0.5,list_size + 0.5]
        ),
        yaxis=dict(range=[0, max(current_steps) + 30]),
        margin=dict(l=20, r=20, t=40, b=20)
    )
    
    return sort_fig

if __name__ == "__main__":
    app.run(debug=True)