import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('sid.tiwari4', 'R3ihW0d2BZsg7inIBa2r')

c1 = Barpolar(
  r = [1.4,6.2,4.7,150,328.5,312.2,197,340.6,631.5,1022.8,822.8,480.3],
  text=['April ', 'May ', 'June ', 'July', 'August ', 'September ', 'October', 'November', 'December', 'January', 'February',
        'March'],
  name='Zymotic diseases',
  theta=['April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', 'January', 'February',
        'March'],
  marker=dict(
    color='rgb(04, 204, 204)',
    opacity=1
  ),

)
c2 = Barpolar(
  r = [0,0,0,0,0.4,32.1,51.7,115.8,41.7,30.7,16.3,12.8],
  text=['April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', 'January', 'February',
        'March'],
  name='Wounds & injuries',
  theta=['April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', 'January', 'February',
        'March'],
  marker=dict(
    color='rgb(234, 153, 153)',
    opacity=1
  ),
)
c3 = Barpolar(
  r = [7,4.6,2.5,9.6,11.9,27.7,50.1,42.8,48,120,140.1,68.6],
  text=['April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', 'January', 'February',
        'March'],
  theta=['April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', 'January', 'February',
        'March'],
  name='All other causes',
  marker=dict(
    color='rgb(67, 67, 67)',
    opacity=1
  )
)

data = [c2, c3, c1]
layout = Layout(
  title='DIAGRAM of the CAUSES of MORTALITY in THE ARMY in THE East.',
  font=dict(
    size=16
  ),
margin= {
    "r": 78,
    "t": 78,
    "b": 78,
    "l": 78,
    "pad": 78
  },
  orientation=150,
  height=900,
width=1000,
  legend=dict(
    font=dict(
      size=7,
      color='rgb(102,102,102)',
      family='Raleway, sans-serif'
    )
  ),
  polar=dict(
    barmode='stack',
    bgcolor='rgb(255, 255, 255)',
    bargap=0,
    radialaxis=dict(
    angle= 70,
    categoryarray=[0, 777.0149999999969],
      ticksuffix='%',
      showgrid=True,
      showline=False,
      showticklabels=False,
      ticks=''
    ),
    angularaxis=dict(
   #categoryarray=[1.9800000000000009, 8.240000000000004],
        showline=False,
       showticklabels=True,
        ticks='',
        direction='clockwise'
    ),
  )
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)