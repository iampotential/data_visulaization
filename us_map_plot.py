import plotly.offline as pyo
### if graphing in plotly notebook use from plotly.offline import init_notebook_mode
import plotly.figure_factory as ff
import plotly.graph_objs as go

text = []
###append data to text for hoverinformation
###in data add a point of latitude and a point of longitude 
###if you have a list of zip codes a great module is uszipecode to make conversions
fig = go.Figure(
    data=[
        go.Scattergeo(
            lat=df.latitude,
            lon=df.longitude,
            text=text,
            hoverinfo='text',
            marker={"size": 3,
                   "opacity": .3,
                   "color":"#B4FF69",
                   "colorscale":'viridis'},
            mode="markers",
            name="",
           
        )
    ],
    layout={
        "margin":{
            "t":25,
            "b":25,
            "l":50,
            "r":50,
        },
        "height":900,
        "width":900,
        "title": "TITLE OF CHART <br>USE "<br>" to break to new line <b>",
        "font":{"family":'American Typewriter', "size":18, "color":'#69B4FF'},
        "geo": {
            "lataxis": {
                "range": [20, 50]
            },
            "lonaxis": {
                "range": [-130, -55]
            },
            "showland":True,
            "landcolor":"#FF69B4",
            "showlakes": True,
            "lakecolor": "#69B4FF",
            "showocean":True,
            "oceancolor":"#154360",
            "scope": "usa",
            
        }
    }
)
config={'showLink': False, 'displayModeBar':False}
pyo.plot(fig, filename='SOME_FILE_NAME',config=config)
### if using in notebook use pyo.iplot
### pyo.iplot(fig, filename='SOME_FILE_NAME',config=config)
