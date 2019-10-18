



import plotly.graph_objs as go
import plotly.offline as pyo
from plotly import tools

x = df['something']

trace0 = go.Histogram(
    x=x,
    nbinsx = 20,
    name='#name',
                marker=dict(cmin=0,
                    cmax=1200,
                            color='#1F618D')
  )
trace1 = go.Scatter(
    x=x,
    y=df['FIELD'].cumsum(),
    name="NAME",
    mode='lines',
    line=dict(color='#1F618D')
  )
trace11 = go.Scatter(
    x=x,
    y=df['NAME'].cumsum(),
    name='NAMES',
    mode='lines',
    line=dict(color='#5DADE2')
  )
heat_Scale = ['#154360',
 '#1A5276',
 '#1F618D',
 '#2471A3',
 '#2980B9',
 '#2E86C1',
 '#3498DB',
 '#5DADE2',
 '#85C1E9',
 '#AED6F1',
 '#D6EAF8',
 '#D4E6F1',
 '#E8DAEF',
 '#EBDEF0',
 '#FADBD8',
 '#F2D7D5',
 '#E6B0AA',
 '#E6B0AA',
 '#D98880',
 '#CD6155',
 '#C0392B',
 '#A93226',
 '#922B21',
 '#7B241C']

trace2 = go.Histogram(
    x=df['SOMETHING'],
    nbinsx = 25,
    marker=dict(
    color=heat_Scale))
trace3 = go.Histogram(
    x=df['SOMETHING'],
    nbinsx = 55,
            marker=dict(cmin=0,
                    cmax=120,
                    color=heat_Scale
                       )
)
trace4 = go.Bar(
                x=SOME_LIST,
                y=SOME_LIST,
                name="NAME",
                text=list_count,
                marker=dict(color='#1F618D'))
trace5 = go.Bar(
                x=LIST_HERE,
                y=LIST_THERE,
                name="NAME",
                text=SOME_TEXT_LIST,
                marker=dict(color='#5DADE2'))
fig = tools.make_subplots(rows=5, cols=1,subplot_titles=('title 1', 'title 2',
                                                          'title 3','title 4','title 5'))

fig['layout'].update(showlegend=False,height=1700, width=1200,title='total title',
                     font=dict(family='American Typewriter', size=12, color='#2874A6'),
                    margin=dict(
        l=0,
        r=0,
        b=200,
        t=200
    ))
fig.append_trace(trace0, 5, 1)
fig.append_trace(trace1, 2, 1)
fig.append_trace(trace11, 2, 1)
fig.append_trace(trace2, 3, 1)
fig.append_trace(trace3, 1, 1)
fig.append_trace(trace4, 4, 1)
fig.append_trace(trace5, 4, 1)
fig['layout']['xaxis1'].update(title='subtitle',
                               titlefont=dict(
            family='Arial, sans-serif',
            size=12,
            color='#2874A6'
        ),)
fig['layout']['xaxis2'].update(title='sub title',
                               titlefont=dict(
            family='Arial, sans-serif',
            size=12,
            color='#2874A6'
        ),)
fig['layout']['xaxis3'].update(title='subtitle',
                               titlefont=dict(
            family='Arial, sans-serif',
            size=12,
            color='#2874A6'
        ),)
fig['layout']['xaxis5'].update(title='title.',
                               titlefont=dict(
            family='Arial, sans-serif',
            size=12,
            color='#2874A6'
        ),)
config={'showLink': False, 'displayModeBar':False}
pyo.iplot(fig, filename='nc_subplots',config=config)
