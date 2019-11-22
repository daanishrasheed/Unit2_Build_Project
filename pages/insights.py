# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Insights


            """
        ),
        dcc.Markdown(
            """
            Throughout its rich history, the NFL has turned into one of the most engaging yet 
            most complicated sport of the modern era. For a team to be successful, there are many 
            characteristics that are essential in acheiving that. Judging from the baseline, I can 
            comfortably assume that the game has developed to a point where teams are relying on the 
            passing game far more heavily than the run as the baseline indicates that approximately 60%
            of all playcalls were run plays.
            """
        ),
        dcc.Markdown(
            """
            The graph below shows how much weight each feature has in the prediction of the type of 
            play about to be run. It can be observed that the formation of the offense has the most affect
            on the play type they are about to run. The teams that are playing offense or defense 
            has little effect because there are 30 teams being measured and there is a high chance
            that some of them might play the same way which makes it difficult for it to have a big 
            impact on the model.
            """
        ),
        html.Img(src='assets/permut.png', className='mb-4'),
        dcc.Markdown(
            """
            The above graph also shows how much of an effect the down has on the model which 
            to any football fan is not that surprising as any coach who calls a run play on a 
            3rd down and at least 5 is asking to be fired. Below we can see how the probability of 
            calling a run play decreases as the play gets closer to 4th down.
            """
        ),
        html.Img(src='assets/pdp.png', className='mb-4'),



    ],
)

layout = dbc.Row([column1])