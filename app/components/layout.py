from dash import html, dcc
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
                            html.Label("Choose algoritm:"),
                            dcc.Dropdown(
                                id="algorithm-dropdown",
                                options=[
                                    {"label": "Bubble Sort", "value": "bubble"},
                                    {"label": "Selection Sort", "value": "selection"},
                                    {"label": "Insertion Sort", "value": "insertion"},
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
                                        dbc.Button("Clear", id="clear-btn", color="danger"),
                                    ], 
                                    className="mt-5",
                                ),
                            dbc.Alert(
                                id="message", 
                                fade=True, 
                                is_open=False,
                                duration=2000,
                                style={
                                    "marginTop":"15px"
                                }
                            )
                        ], 
                        width=3, 
                        className="bg-light p-3 rounded"
                    ),
                    # Visualisering
                    dbc.Col(
                        [
                            html.H4("Visualisering", className="text-center"),
                            dcc.Graph(id="sorting-graph",figure=fig_default ,style={"height": "70vh"}),
                            html.Div(
                                [
                                    html.Span(
                                        "",
                                        style={
                                            "display": "inline-block",
                                            "width": "14px",
                                            "height": "14px",
                                            "backgroundColor": "#0d6efd",
                                            "borderRadius": "2px",
                                            "marginRight": "6px"
                                        }
                                    ),
                                    html.Span("Element", className="me-3"),
                                    html.Span(
                                        "",
                                        style={
                                            "display": "inline-block",
                                            "width": "14px",
                                            "height": "14px",
                                            "backgroundColor": "#dc3545",
                                            "borderRadius": "2px",
                                            "marginRight": "6px"
                                        }
                                    ),
                                    html.Span("Tagert element"),
                                ],
                                className="d-flex align-items-center justify-content-center gap-2 mt-3",
                            ),
                            dcc.Store(id="stored-data"),
                            dcc.Store(id="run-start"),
                            dcc.Interval(id="interval", interval=100, n_intervals=0,disabled=True)
                        ],
                        width=9
                    ),
                ]
            )
        ], 
        fluid=True
    )

    return layout
