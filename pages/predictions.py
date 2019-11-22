# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq
from dash.dependencies import Input, Output
from joblib import load
import pandas as pd

# Imports from this application
from app import app


xgb = load('assets/xgb.joblib')
rfc = load('assets/rfc.joblib')
# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictions

            Set the situation of the game.

            """
        ),
        dcc.Markdown(
            """
        
            ## Quarter

            """
        ),
        dcc.Slider(
            id='Quarter',
            min=1,
            max=4,
            step=None,
            marks={
                1: '1st Quarter',
                2: '2nd Quarter',
                3: '3rd Quarter',
                4: '4th Quarter',
            },
            value=1,
            className='mb-5'
        ),
        dcc.Markdown(
            """
            
            ## Time Left

            """
        ),
        dcc.Markdown(
            """
            
            Minutes:
            """
        ),
        dcc.Slider(
            id='Minute',
            min=0,
            max=14,
            marks={i: '{}'.format(i) for i in range(15)},
            value=0,
            className='mb-4'
        ),
        dcc.Markdown(
            """
            
            Seconds:
            """
        ),
        html.Div(  
            [
            dcc.Markdown('## Seconds'), 
            daq.Slider(              
                id='Second', 
                min=0, 
                max=59, 
                step=1, 
                value=0,  
                className='mb-3',
                handleLabel={
                    'label': ' ',
                    'showCurrentValue': True
                    },
                ),
            ],
            style={'marginTop': 10, 'marginBottom': 10},            
        ),              
        dcc.Markdown(
            """
            
            ## Team on Offense:
            """
        ),
        dcc.Dropdown(
            id='OffenseTeam',
            options=[
                {'label': 'Arizona Cardinals', 'value': 'ARI'},
                {'label': 'Atlanta Falcons', 'value': 'ATL'},
                {'label': 'Baltimore Ravens', 'value': 'BAL'},
                {'label': 'Buffalo Bills', 'value': 'BUF'},
                {'label': 'Carolina Panthers', 'value': 'CAR'},
                {'label': 'Chicago Bears', 'value': 'CHI'},
                {'label': 'Cincinnati Bengals', 'value': 'CIN'},
                {'label': 'Cleveland Browns', 'value': 'CLE'},
                {'label': 'Dallas Cowboys', 'value': 'DAL'},
                {'label': 'Denver Broncos', 'value': 'DEN'},
                {'label': 'Detroit Lions', 'value': 'DET'},
                {'label': 'Green Bay Packers', 'value': 'GB'},
                {'label': 'Houston Texans', 'value': 'HOU'},
                {'label': 'Indianapolis Colts', 'value': 'IND'},
                {'label': 'Jacksonville Jaguars', 'value': 'JAX'},
                {'label': 'Kansas City Chiefs', 'value': 'KC'},
                {'label': 'Los Angeles Chargers', 'value': 'LAC'},
                {'label': 'Los Angeles Rams', 'value': 'LAR'},
                {'label': 'Miami Dolphins', 'value': 'MIA'},
                {'label': 'Minnesota Vikings', 'value': 'MIN'},
                {'label': 'New England Patriots', 'value': 'NE'},
                {'label': 'New Orleans Saints', 'value': 'NO'},
                {'label': 'New York Giants', 'value': 'NYG'},
                {'label': 'New York Jets', 'value': 'NYJ'},
                {'label': 'Oakland Raiders', 'value': 'OAK'},
                {'label': 'Philadelphia Eagles', 'value': 'PHI'},
                {'label': 'Pittsburgh Steelers', 'value': 'PIT'},
                {'label': 'Seattle Seahawks', 'value': 'SEA'},
                {'label': 'San Fransisco 49ers', 'value': 'SF'},
                {'label': 'Tampa Bay Buccaneers', 'value': 'TB'},
                {'label': 'Tennessee Titans', 'value': 'TEN'},
                {'label': 'Washington Redskins', 'value': 'WAS'},
            ],
            className='mb-5'
        ),
        dcc.Markdown(
            """
            
            ## Team on Defense:
            """
        ),
        dcc.Dropdown(
            id='DefenseTeam',
            options=[
                {'label': 'Arizona Cardinals', 'value': 'ARI'},
                {'label': 'Atlanta Falcons', 'value': 'ATL'},
                {'label': 'Baltimore Ravens', 'value': 'BAL'},
                {'label': 'Buffalo Bills', 'value': 'BUF'},
                {'label': 'Carolina Panthers', 'value': 'CAR'},
                {'label': 'Chicago Bears', 'value': 'CHI'},
                {'label': 'Cincinnati Bengals', 'value': 'CIN'},
                {'label': 'Cleveland Browns', 'value': 'CLE'},
                {'label': 'Dallas Cowboys', 'value': 'DAL'},
                {'label': 'Denver Broncos', 'value': 'DEN'},
                {'label': 'Detroit Lions', 'value': 'DET'},
                {'label': 'Green Bay Packers', 'value': 'GB'},
                {'label': 'Houston Texans', 'value': 'HOU'},
                {'label': 'Indianapolis Colts', 'value': 'IND'},
                {'label': 'Jacksonville Jaguars', 'value': 'JAX'},
                {'label': 'Kansas City Chiefs', 'value': 'KC'},
                {'label': 'Los Angeles Chargers', 'value': 'LAC'},
                {'label': 'Los Angeles Rams', 'value': 'LAR'},
                {'label': 'Miami Dolphins', 'value': 'MIA'},
                {'label': 'Minnesota Vikings', 'value': 'MIN'},
                {'label': 'New England Patriots', 'value': 'NE'},
                {'label': 'New Orleans Saints', 'value': 'NO'},
                {'label': 'New York Giants', 'value': 'NYG'},
                {'label': 'New York Jets', 'value': 'NYJ'},
                {'label': 'Oakland Raiders', 'value': 'OAK'},
                {'label': 'Philadelphia Eagles', 'value': 'PHI'},
                {'label': 'Pittsburgh Steelers', 'value': 'PIT'},
                {'label': 'Seattle Seahawks', 'value': 'SEA'},
                {'label': 'San Fransisco 49ers', 'value': 'SF'},
                {'label': 'Tampa Bay Buccaneers', 'value': 'TB'},
                {'label': 'Tennessee Titans', 'value': 'TEN'},
                {'label': 'Washington Redskins', 'value': 'WAS'},
            ],
            className='mb-5'
        ),
        dcc.Markdown(
            """
            
            ## Situation:
            """
        ),
        dcc.Markdown(
            """
            
            Down:
            """
        ),
        dcc.Slider(
            id='Down',
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
            
            Yards To Go For 1st Down:
            """
        ),  
        dcc.Input(
            id='ToGo',
            placeholder='Enter a value...',
            type='text',
            value='',
            className='mb-5'
        ),
        html.Div(  
            [
            dcc.Markdown('## Yards to Endzone'), 
            daq.Slider(              
                id='YardsLeft', 
                min=1, 
                max=99, 
                step=1, 
                value=0,  
                className='mb-3',
                handleLabel={
                    'label': ' ',
                    'showCurrentValue': True
                    },
                ),
            ],
            style={'marginTop': 10, 'marginBottom': 10},            
        ),                     
        dcc.Markdown(
            """
            
            ## Formation:
            """
        ),
        dcc.Dropdown(
            id='Formation',
            options=[
                {'label': 'UNDER CENTER', 'value': '1'},
                {'label': 'SHOTGUN', 'value': '2'},
                {'label': 'NO HUDDLE', 'value': '3'},
                {'label': 'NO HUDDLE SHOTGUN', 'value': '4'},
            ],
            className='mb-5'
        ),    
    ],
    md=4,
)

column2 = dbc.Col(
    [
        html.H2('Most Successful Playcall', className='mb-4'),
        html.Div(id='prediction-content', className='lead')
    ]
)
layout = dbc.Row([column1, column2])
@app.callback(
    Output('prediction-content', 'children'),
    [
     Input('Quarter', 'value'), 
     Input('Minute', 'value'),
     Input('Second', 'value'),
     Input('OffenseTeam', 'value'),
     Input('DefenseTeam', 'value'),
     Input('Down', 'value'),
     Input('ToGo', 'value'),
     Input('YardsLeft', 'value'),
     Input('Formation', 'value')  
    ],
)
def predict(Quarter, Minute, Second, OffenseTeam, DefenseTeam, Down, ToGo, YardsLeft, Formation):
    df = pd.DataFrame(
        columns=['Quarter', 'Minute', 'Second', 'OffenseTeam', 'DefenseTeam', 'Down', 'ToGo', 'YardsLeft', 'Formation'],
        data=[[Quarter, Minute, Second, OffenseTeam, DefenseTeam, Down, ToGo, YardsLeft, Formation]]
    )
    y_pred = rfc.predict(df)[0]
    return y_pred

