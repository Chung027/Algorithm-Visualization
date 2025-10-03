from dash import Dash, html, Input, Output,State ,callback, no_update
import plotly.graph_objs as go
import dash_bootstrap_components as dbc
from components.layout import layout
from utils.utils import generate_random_list
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
    Input("generate-btn", "n_clicks"),
    State("size-slider", "value"),
    prevent_initial_call=True
)
def generate_data(n_clicks, size):
    if n_clicks is None:
        return no_update
    data = generate_random_list(size)

    fig = go.Figure(
        data=[go.Bar(y=data, marker_color="lightskyblue")]
    )
    fig.update_layout(
        title="Generated Random List",
        xaxis=dict(range=[1,size]),
        yaxis=dict(range=[0, max(data) + 10]),
        margin=dict(l=20, r=20, t=40, b=20)
    )
    return fig
    
if __name__ == "__main__":
    app.run(debug=True)