
import pandas as pd
import numpy as np
import plotly.offline as pyo
###from plotly.offline import init_notebook_mode
import plotly.figure_factory as ff
import plotly.graph_objs as go
import numpy as np

###init_notebook_mode(connected=True)

for i in range(0,len(pd.unique(dfc['SOMETHINGHERE']))):
    trace = {
            "type": 'violin',
            "x": dfc['THIS'][dfc['SOMETHINGHERE'] == pd.unique(dfc['SOMETHINGHERE'])[i]],
            "y": dfc['THAT'][dfc['SOMETHINGHERE'] == pd.unique(dfc['SOMETHINGHERE'])[i]],
            "name": pd.unique(dfc['OTHER'])[i],
            "box": {
                "visible": False
            },
            "meanline": {
                "visible": True
            }
        }
    data.append(trace)
for i in range(0,len(pd.unique(dfc['THIS']))):
    trace1 = {
            "type": 'violin',
            "x": dfc['THAT'][dfc['THIS'] == pd.unique(dfc['OTHER'])[i]],
            "y": dfc['THIS'][dfc['THAT'] == pd.unique(dfc['OTHER'])[i]],
            "name": pd.unique(dfc['OTHER'])[i],
            "box": {
                "visible": True
            },
            "meanline": {
                "visible": True
            }
        }
    data.append(trace1)
        
fig = {
    "data": data,
    "layout" : {"font":
        {"family":'American Typewriter', "size":12, "color":'#2874A6'},
        "violinmode": "group",
        "title": "SOME_TITLE",
        "yaxis": {
            "zeroline": False,
        }
        
    }
}

config={'showLink': False, 'displayModeBar':False}
pyo.iplot(fig, filename='YOUR_violin', validate = False,config=config)
