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
        	\n
            \n
            ## Half	
            """	
        ),	
        dcc.RadioItems(	
            id='Half',		
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
            	
            ## Seconds left in half:
            (For this value, Multiply 60 by the amount of minutes left and 
            add the extra seconds)
            \n\n	
            """	
        ),	 	
        daq.Slider(              	
            id='Seconds', 	
            min=0, 	
            max=900,
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
            ## Down:	
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
        dcc.Markdown(	
            """	
            	
            ## Yards To Go For 1st Down:	
            """	
        ),  	
        dcc.Input(	
            size = 50,
            id='yardsToGo',	
            placeholder='Enter the amount of yards required for the 1st Down:',	
            type='number',	
            value='',	
            className='mb-5'	
        ),
        dcc.Markdown(	
            """	
            	
            ## Yards from the Endzone:
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
            \n
            \n	
            ## Number of Defenders in the Box:	
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
        dcc.Markdown(
            """
            ## Offense Personnel
            """
        ),
        dcc.Input(
            id='rb_count',
            placeholder='Number of running backs',	
            type='number',	
            value='',	
            className='mb-4'
        ),
        dcc.Input(
            id='wr_count',
            placeholder='Number of wide recievers',
            type='number',
            value='',
            className='mb-4'
        ),
        dcc.Input(
            id='te_count',
            placeholder='Number of tightends',
            type='number',
            value='',
            className='mb-4'
        ),
        dcc.Input(
            id='ol_count',
            placeholder='Number of offensive linemen',
            type='number',
            value='',
            classname='mb-4'
        ),
        dcc.Input(
            id='fb_count',
            placeholder='Number of fullbacks',
            type='number',
            value='',
            classname='mb-4'
        ),
        dcc.Markdown(
            """
            ## Defense Personnel
            """
        ),
        dcc.Input(
            id='dl_count',
            placeholder='Number of defensive linemen',
            type='number',
            value='',
            classname='mb-4'
        ),
        dcc.Input(
            id='db_count',
            placeholder='Number of defensive backs',
            type='number',
            value='',
            classname='mb-4'
        ),
        dcc.Input(
            id='lb_count',
            placeholder='Number of linebackers',
            type='number',
            value='',
            classname='mb-4'
        ),
        dcc.Markdown(
            """
            ## Formation of Offense
            """
        ),
        dcc.Dropdown(
            id='offenseFormation',
            options=[
                {'label': 'Shotgun', 'value': 'SHOTGUN'},
                {'label': 'Singleback', 'value': 'SINGLEBACK'},
                {'label': 'I-form', 'value': 'I_FORM'},
                {'label': 'Empty', 'value': 'EMPTY'},
                {'label': 'Pistol', 'value': 'PISTOL'},
                {'label': 'Jumbo', 'value': 'JUMBO'},
                {'label': 'Wildcat', 'value': 'WILDCAT'},
                {'label': 'Ace', 'value': 'ACE'}
            ],
            value=''
        )  
    ],	           	              
    md=4,
)

column2 = dbc.Col(
    [

    ]
)

layout = dbc.Row([column1, column2])