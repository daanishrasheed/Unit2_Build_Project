# Imports from 3rd party libraries
# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Make the Play Call!
            What is the best play to call in a given situation?
            Use this app to see which play has the highest chance to be 	
            successful given the personnnel of both offense and defense, the
            time left on the clock, and the position of where the offense is on the field	
            If past trends continue, how can you make the most out of a team's 	
            offense and use it to succeed against the knowledge you have against the defense. 
            """
        ),
        dcc.Link(dbc.Button('Predict The Play', color='primary'), href='/predictions')
    ],
    md=4,
)

column2 = dbc.Col(
    [
        html.Img(src='assets/playcall.png',style={
                    'height' : '90%',	
                    'width' : '75%',	
                    'float' : 'center',	
                    'position' : 'relative',	
                    'padding-top' : 0,	
                    'padding-right' : 0	

                }, className='img-fluid'),
    ]
)

layout = dbc.Row([column1, column2])