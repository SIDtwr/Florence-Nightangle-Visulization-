import plotly.plotly as py
from plotly.graph_objs import *


py.sign_in('sid.tiwari4', 'R3ihW0d2BZsg7inIBa2r')

trace1 = {
  "r": [7,4.6,2.5,9.6,11.9,27.7,50.1,42.8,48,120,140.1,68.6],
  "t": ["April 1855", "May 1855", "June 1855", "July 1855", "August 1855", "September 1855", "October 1855", "September 1855", "December 1855", "January 1856", "February 1856", "March 1856"],
  "theta" : ['April', 'May', 'June', 'July', 'August', 'September', 'October', 'November','December','January','February','March'],
  "marker": {
    "color": "rgb(67, 67, 67)",
    "opacity": 1
  },
  "name": "All other causes",
  "showlegend": True,
  "type": "area"
}
trace2 = {
  "r": [0,0,0,0,0.4,32.1,51.7,115.8,41.7,30.7,16.3,12.8],
  "t": ["April 1855", "May 1855", "June 1855", "July 1855", "August 1855", "September 1855", "October 1855", "September 1855", "December 1855", "January 1856", "February 1856", "March 1856"],
  "theta" : ['April', 'May', 'June', 'July', 'August', 'September', 'October', 'November','December','January','February','March'],
  "marker": {
    "color": "rgb(234, 153, 153)",
    "opacity": 1
  },
  "name": "Wounds & injuries",
  "showlegend": True,
  "type": "area"
}
trace3 = {
  "r": [1.4,6.2,4.7,150,328.5,312.2,197,340.6,631.5,1022.8,822.8,480.3],
  "t": ["April 1855", "May 1855", "June 1855", "July 1855", "August 1855", "September 1855", "October 1855", "September 1855", "December 1855", "January 1856", "February 1856", "March 1856"],
  "theta" : ['April', 'May', 'June', 'July', 'August', 'September', 'October', 'November','December','January','February','March'],
  "marker": {
    "color": "rgb(204, 204, 204)",
    "opacity": 1
  },
  "name": "Zymotic diseases",
  "showlegend": True,
  "type": "area"
}

data = [trace1, trace2, trace3]

layout = {
  "angularaxis": {"range": [1.9800000000000009, 8.240000000000004]},
  "barmode": "stack",
  "font": {
    "color": "rgb(102, 102, 102)",
    "family": "Raleway, sans-serif"
  },
  "height": 549,
  "legend": {"traceorder": "normal"},
  "margin": {
    "r": 78,
    "t": 78,
    "b": 78,
    "l": 78,
    "pad": 78
  },
  "orientation": 150,
  "plot_bgcolor": "rgb(255, 255, 255)",
  "radialaxis": {
    "orientation": 70,
    "range": [0, 777.0149999999969]
  },
  "showlegend": True,
  "width": 660
}

fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)