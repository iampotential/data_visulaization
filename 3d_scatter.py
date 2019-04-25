import plotly.offline as pyo
from plotly.offline import init_notebook_mode
import plotly.figure_factory as ff
import plotly.graph_objs as go
import numpy as np
import pandas as pd 
trace1 = go.Scatter3d(
    x=x,
    name='Name',
    y=y,
    z=z,
    hoverinfo='name',
    mode='markers',
    marker=dict(
        size=5,
        color=df['COLORCOL'],
        colorscale='Viridis',              
        opacity=0.33
    )
)
trace2 = go.Scatter3d(
    x=x2,
    y=y2,
    z=z2,
    mode='markers',
    name='SOME_NAME',
    hoverinfo='name',
    marker=dict(
        colorbar = dict(title = 'titlez'),
        size=5,
        color=dfc['OTHERCOLORCOL'],
        colorscale='Viridis', 
        opacity=0.33,
    )
)
data = [trace1,trace2]
layout = go.Layout(
    showlegend=False,scene = dict(
                    xaxis = dict(
                                                backgroundcolor="#7FB3D5",
                        gridcolor="rgb(250, 250, 250)",
                        showbackground=False,
                        zerolinecolor="rgb(250, 250, 250)",
                        title='Scaled Balance'),
                    yaxis = dict(
                                                backgroundcolor="#7FB3D5",
                        gridcolor="#F7F9F9",
                        showbackground=False,
                        zerolinecolor="rgb(250, 250, 250)",
                        title='Scaled Earnings'),
                    zaxis = dict(
                        title='SOMETITLE',
                        backgroundcolor="#7FB3D5",
                        gridcolor="rgb(250, 250, 250)",
                        showbackground=False,
                        zerolinecolor="#7FB3D5",
                    ),),
    title='YOUR TITLE HERE',
    font=dict(family='American Typewriter', size=12, color='#2874A6'),
    margin=dict(
        l=50,
        r=50,
        b=0,
        t=50
    )
)
config={'showLink': False, 'displayModeBar':False}
fig = go.Figure(data=data, layout=layout)
pyo.iplot(fig, filename='3d-scatter-colorscale.html',config=config)
