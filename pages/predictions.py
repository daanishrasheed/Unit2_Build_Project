# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_daq as daq
from joblib import load
import pandas as pd

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

xgb = load('assets/xgb.joblib')
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictions
            
            
            Your instructions: Using the tools below, set up the situation you want simulated.
            When you are setting up your personnel on offense, make sure that the sum of all
            the players from each group add up to 10. As for the personnel on defense, the number 
            of players should add up to 11.\n 
            For the rest of the tools, just make sure that the situation
            you are trying to set, is possible in a real life NFL environment.
            """
        ),
        dcc.Markdown(
            """
            ## Situation
            """
        ),
        dcc.Markdown(	
            """	
        	\n
            \n
            Half	
            """	
        ),	
        dcc.RadioItems(	
            id='half',		
            options=[
                {'label': ' 1st or 2nd quarter', 'value': 1},
                {'label': ' 3rd or 4th quarter', 'value': 2}
            ],
            value=1,
            labelStyle={'display': 'block'},	
            className='mb-5'	
        ),
        dcc.Markdown(	
            """	
            	
            Seconds left in half:\n
            (For this value, Multiply 60 by the amount of minutes left and 
            add the extra seconds)
            \n\n	
            """	
        ),	 	
        daq.Slider(              	
            id='secondsLeftInHalf', 	
            min=0, 	
            max=1800,
            handleLabel={"showCurrentValue": True,"label": "Seconds"}, 	
            step=1, 	
            value=0,
            updatemode='drag',  	
            className='mb-3',	
        ),
        dcc.Markdown(	
            """	
            \n
            \n	
            Down:	
            """	
        ),	
        dcc.Slider(	
            id='down',	
            min=1,	
            max=4,	
            step=None,	
            marks={	
                1: '1st Down',	
                2: '2nd Down',	
                3: '3rd Down',	
                4: '4th Down',	
            },	
            value=1,	
            className='mb-4'	
        ),  	
        daq.Slider(              	
            id='yardsToGo', 	
            min=0, 	
            max=50,
            handleLabel={"showCurrentValue": True,"label": "Yards"}, 	
            step=1, 	
            value=0,
            updatemode='drag',  	
            className='mb-3',	
        ),
        dcc.Markdown(	
            """	
            	
            Yards from the Endzone:
            \n\n	
            """	
        ),	 	
        daq.Slider(              	
            id='yardsToEndzone', 	
            min=0, 	
            max=100,
            handleLabel={"showCurrentValue": True,"label": "Yards"}, 	
            step=1, 	
            value=0,
            updatemode='drag',  	
            className='mb-3',	
        ),
        dcc.Markdown(
            """
            ## Offense Personnel
            """
        ),
        dcc.Markdown(
            """
            Number of Runningbacks
            """
        ),
        dcc.Slider(
            id='rb_count',
            min=0,
            max=3,
            marks={i: '{}'.format(i) for i in range(4)},
            value=0,
            className='mb-4'
        ),
        dcc.Markdown(
            """
            Number of Wide Recievers
            """
        ),
        dcc.Slider(
            id='wr_count',
            min=0,
            max=5,
            marks={i: '{}'.format(i) for i in range(6)},
            value=0,
            className='mb-4'
        ),
        dcc.Markdown(
            """
            Number of Tightends
            """
        ),
        dcc.Slider(
            id='te_count',
            min=0,
            max=5,
            marks={i: '{}'.format(i) for i in range(6)},
            value=0,
            className='mb-4'
        ),
        dcc.Markdown(
            """
            Number of Offensive linemen
            """
        ),
        dcc.Slider(
            id='ol_count',
            min=5,	
            max=8,	
            step=None,	
            marks={	
                5: '5',	
                6: '6',	
                7: '7',	
                8: '8',	
            },	
            value=5,
            className='mb-4'
        ),
        dcc.Markdown(
            """
            Number of fullbacks
            """
        ),
        dcc.Slider(
            id='fb_count',
            min=0,
            max=2,
            marks={i: '{}'.format(i) for i in range(3)},
            value=0,
            className='mb-4'
        ),
        dcc.Markdown(
            """
            Formation of Offense
            """
        ),
        dcc.Slider(	
            id='numericalFormation',	
            min=0,	
            max=7,	
            step=None,	
            marks={	
                0: 'SHOTGUN',
                1: 'SINGLEBACK',	
                2: 'I_FORM',	
                3: 'EMPTY',	
                4: 'PISTOL',
                5: 'JUMBO',
                6: 'WILDCAT',
                7: 'ACE',	
            },	
            vertical=True,
            value=0,	
            className='mb-4'	
        ),
        dcc.Markdown(
            """
            ## Defense Personnel
            """
        ),
        dcc.Markdown(
            """
            Number of Defensive Linemen
            """
        ),
        dcc.Slider(
            id='dl_count',
            min=0,
            max=11,
            marks={i: '{}'.format(i) for i in range(12)},
            value=0,
            className='mb-4'
        ),
        dcc.Markdown(
            """
            Number of Defensivebacks
            """
        ),
        dcc.Slider(
            id='db_count',
            min=0,
            max=11,
            marks={i: '{}'.format(i) for i in range(12)},
            value=0,
            className='mb-4'
        ),
        dcc.Markdown(
            """
            Number of Linebackers
            """
        ),
        dcc.Slider(
            id='lb_count',
            min=0,
            max=11,
            marks={i: '{}'.format(i) for i in range(12)},
            value=0,
            className='mb-4'
        ),
        dcc.Markdown(	
            """	
            \n
            \n	
            Number of Defenders in the Box:	
            """	
        ),
        dcc.Slider(	
            id='defendersInTheBox',	
            min=1,	
            max=8,	
            step=None,	
            marks={	
                1: '1',	
                2: '2',	
                3: '3',	
                4: '4',
                5: '5',
                6: '6',
                7: '7',
                8: '8',	
            },	
            value=1,	
            className='mb-4'	
        ),  
    ],	           	              
    md=4,
)

column2= dbc.Col(
    [
        html.H2('Run or Pass', className='mb-4'),
        html.Div(id='prediction-content', className='lead')
    ]
)

layout = dbc.Row([column1, column2])	
@app.callback(	
    Output('prediction-content', 'children'),	
    [	
     Input('half', 'value'), 	
     Input('secondsLeftInHalf', 'value'),	
     Input('down', 'value'),	
     Input('yardsToGo', 'value'),	
     Input('yardsToEndzone', 'value'),	
     Input('defendersInTheBox', 'value'),	
     Input('rb_count', 'value'),	
     Input('te_count', 'value'),	
     Input('wr_count', 'value'),
     Input('ol_count', 'value'),
     Input('fb_count', 'value'),
     Input('dl_count', 'value'),
     Input('db_count', 'value'),
     Input('lb_count', 'value'),
     Input('numericalFormation', 'value')
    ],	
)	
def predict(half, secondsLeftInHalf, down, yardsToGo, yardsToEndzone, defendersInTheBox, rb_count, te_count, wr_count, ol_count, fb_count, dl_count, db_count, lb_count, numericalFormation):
    df = pd.DataFrame(
        columns=['half', 'secondsLeftInHalf', 'down', 'yardsToGo', 'yardsToEndzone', 'defendersInTheBox', 'rb_count', 'te_count', 'wr_count', 'ol_count', 'fb_count', 'dl_count', 'db_count', 'lb_count', 'numericalFormation'],
        data=[[half, secondsLeftInHalf, down, yardsToGo, yardsToEndzone, defendersInTheBox, rb_count, te_count, wr_count, ol_count, fb_count, dl_count, db_count, lb_count, numericalFormation]]
    )
    yp = xgb.predict(df)[0]
    if yp == 1:
        return 'PASS'
    return 'RUN'