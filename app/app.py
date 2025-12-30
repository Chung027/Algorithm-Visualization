from dash import Dash, html, Input, Output,State ,callback, no_update
import plotly.graph_objs as go
import dash_bootstrap_components as dbc
from components.layout import layout
from utils.utils import generate_random_list, figure_layout
from algorithms.sort_algorithms import bubble_sort, selection_sort, insertion_sort, merge_sort_visual, quick_sort

PRIMARY_BAR_COLOR = "#0d6efd"
TARGET_BAR_COLOR = "#dc3545"

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
            build_bar_figure([]),
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
    fig = build_bar_figure(list_data, title="Generated Random List")
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
    Output("info-algorithm", "children"),
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
            "danger",
            no_update
        ]
    
    if algo_drop == "bubble":
        steps_sort = list(bubble_sort(list_data))
    elif algo_drop == "selection":
        steps_sort = list(selection_sort(list_data))
    elif algo_drop == "insertion":
        steps_sort = list(insertion_sort(list_data))
    elif algo_drop == "merge":
        steps_sort = list(merge_sort_visual(list_data))
    elif algo_drop == "quick":
        steps_sort = list(quick_sort(list_data))
    return [
        steps_sort, 
        False, 
        0,
        f"Started {algo_drop.capitalize()} sort successfully",
        True,
        "success",
        algo_drop
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
    step = steps[n_interval]

    if isinstance(step, dict):
        values = step.get("values", [])
        highlight = step.get("highlight", [])
    else:
        values = step
        highlight = []

    sort_fig = build_bar_figure(values, highlight_indices=highlight)
    
    return sort_fig

# Callback for updating algorithm info
#@app.callback(
#    Output("info-algorithm", "children"),
#    Output("info-steps","children"),
#    Output("info-swaps","children"),
#    Output("info-time","children"),
#    Input("interval","n_intervals"),
#    State("algorithm-dropdown", "value"),
#    State("stored-data","value"),
#    State("size-slider", "value")
#)
def build_bar_figure(values, highlight_indices=None, title=None):
    values = list(values) if values is not None else []
    highlight_indices = set(highlight_indices or [])
    bar_count = len(values)

    colors = [PRIMARY_BAR_COLOR] * bar_count
    for index in highlight_indices:
        if 0 <= index < bar_count:
            colors[index] = TARGET_BAR_COLOR

    bar_trace = go.Bar(
        x=list(range(1, bar_count + 1)),
        y=values,
        marker_color=colors
    )

    tickvals, ticktext = figure_layout(values)
    xaxis_config = dict(
        tickmode="array",
        tickvals=tickvals,
        ticktext=ticktext,
    )
    if bar_count:
        xaxis_config["range"] = [0.5, bar_count + 0.5]

    yaxis_max = max(values) if values else 0
    yaxis_config = dict(range=[0, yaxis_max + 20 if bar_count else 20])

    fig = go.Figure(data=[bar_trace])
    fig.update_layout(
        title=title,
        xaxis=xaxis_config,
        yaxis=yaxis_config,
        margin=dict(l=20, r=20, t=40 if title else 20, b=20)
    )
    return fig

if __name__ == "__main__":
    app.run(debug=True)
