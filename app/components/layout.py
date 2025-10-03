# components/layout.py
from dash import html, dcc, callback, Input, Output, no_update
import dash_bootstrap_components as dbc
import plotly.graph_objects as go

def layout():
    fig_default = go.Figure()
    fig_default.update_layout(
        xaxis=dict(showticklabels=False),
        yaxis=dict(range=[0,160]),
        margin=dict(l=20, r=20, t=40, b=20)
    )
    layout = dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.H2("Sort Visualization", className="text-center mb-4"),

                            # Dropdown: välj algoritm
                            html.Label("Choose algoritm:"),
                            dcc.Dropdown(
                                id="algorithm-dropdown",
                                options=[
                                    {"label": "Bubble Sort", "value": "bubble"},
                                    {"label": "Insertion Sort", "value": "insertion"},
                                    {"label": "Selection Sort", "value": "selection"},
                                    {"label": "Merge Sort", "value": "merge"},
                                    {"label": "Quick Sort", "value": "quick"},
                                ],
                                value="bubble",
                                clearable=False,
                                className="mb-3"
                            ),
                            # Slider: antal element
                            html.Label("Number of element:"),
                            dcc.Slider(
                                id="size-slider",
                                min=20,
                                max=100,
                                step=20,
                                value=20,
                                marks={i: str(i) for i in range(0, 105, 20)},
                                className="mb-3"
                            ),
                            dbc.Accordion(
                                dbc.AccordionItem(
                                    [
                                        dbc.Table(
                                            [
                                                html.Tbody(
                                                    [
                                                       html.Tr([html.Td("Algorithm"), html.Td(id="info-algorithm")]),
                                                       html.Tr([html.Td("Steps"),html.Td(id="info-steps")]),
                                                       html.Tr([html.Td("Swaps"),html.Td(id="info-swaps")]),
                                                       html.Tr([html.Td("Execution Time"),html.Td(id="info-time")])
                                                    ]
                                                ),
                                            ],
                                            bordered=True,
                                            style={
                                                "marginTop" : "10px"
                                            }
                                        ),
                                    ],
                                    title="Info-panel",
                                ),
                                start_collapsed=True,
                                flush=True
                            ),
                            dbc.ButtonGroup(
                                    [
                                        dbc.Button("Generate list", id="generate-btn", color="primary"),
                                        dbc.Button("Start", id="start-btn", color="success"),
                                        dbc.Button("Stop", id="stop-btn", color="danger"),
                                    ], 
                                    className="mt-5",
                                ),
                        ], 
                        width=3, 
                        className="bg-light p-3 rounded"
                    ),
                    # Visualisering
                    dbc.Col(
                        [
                            html.H4("Visualisering", className="text-center"),
                            dcc.Graph(id="sorting-graph",figure=fig_default ,style={"height": "70vh"}),
                        ],
                        width=9
                    ),
                ]
            )
        ], 
        fluid=True
    )

    return layout
