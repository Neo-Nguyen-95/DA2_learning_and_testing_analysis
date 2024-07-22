#%% NEXT STEP
"""
Next: 
    - add information curve of a group of question
""" 

#%% --- LIBRARY
import pandas as pd
import numpy as np
pd.options.display.max_columns = None

from dash import Dash, html, dcc, callback, Input, Output
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# for spyder display
import plotly.io as pio
pio.renderers.default='browser'
#%% --- IMPORT DATA
# Subject ID
df_question_meta = pd.read_csv("question_metadata.csv")

# Subject Name
df_subject_meta = pd.read_csv("subject_metadata.csv")

# learning result
df = pd.read_csv("my_sample_data.csv")
df.drop(columns='Unnamed: 0', inplace=True)

#%% APP INTRO
intro = """
## INTRODUCTION ABOUT THE APP

This app aims to help teachers and educators to quickly evaluate test\
results. The app presents in three sections:

- Part I: Overview - shows you a simple evaluation with student score\
distribution and correctness percentage of each question.
        
- Part II: Quality Analysis - shows you a scatter plot of question\
discrimination and difficulty, which is correctness percentage.
        
- Part III: Misconception detection - shows you proportion of choice in\
detail, so that you can dectect misconception in doubtful question.

Now, let's get started!
"""

#%% APP PART I - DATA
# ----------------- STUDENT SCORE -----------------
score = df['IsCorrect'].groupby(df['UserId']).sum().rename('TotalScore')

# ----------------- CORRECT PROP -----------------
correct_percent = (
    df['IsCorrect'].groupby(df['QuestionId'])
    .value_counts(normalize=True)
    .reset_index()
    )
correct_percent = (
    correct_percent[correct_percent['IsCorrect']==1]
    .sort_values("proportion")
    .drop(columns="IsCorrect")
    )
correct_percent['proportion'] = round(correct_percent['proportion']*100, 2)
correct_percent.sort_values('proportion', inplace=True)
correct_percent['QuestionId'] = correct_percent['QuestionId'].apply(lambda x: str(x))

# ----------------- SKILL/TOPIC COMPLETION -----------------
correct_percent_copy = correct_percent.copy()
correct_percent_copy['QuestionId'] = (
    correct_percent_copy['QuestionId'].apply(lambda x: int(x))
    )
item_info = correct_percent_copy.set_index('QuestionId')
item_subject = (
    df_question_meta['SubjectId']
    .map(lambda x: int(x.strip('[]').split(",")[1]))
    )
# update item info
item_info = item_info.join(item_subject)

temp_info = item_info.reset_index().set_index('SubjectId')
temp_subject = df_subject_meta.set_index('SubjectId')
# update item info
item_info = (
    temp_info.join(temp_subject)
    .reset_index()
    .drop(columns=['ParentId', 'Level', 'SubjectId'])
    )

subject_complete = (
    item_info['proportion'].groupby(item_info['Name']).mean()
    .sort_values()
    )

#%% APP PART I: COMPONENTS
part_i="""
## PART I: RESULT OVERVIEW
"""

fig_student_score = px.histogram(
    data_frame=score, nbins=20
    )
fig_student_score.update_layout(
    title_text="Distribution of student score",
    xaxis_title="Student score", yaxis_title='Count',
    bargap=0.2, showlegend=False
    )

fig_correct_prop = px.bar(
    data_frame=correct_percent,
    x='QuestionId', y='proportion'
    )
fig_correct_prop.update_layout(
    title_text='Correctness proportion for each question',
    xaxis_title="Question ID", yaxis_title="Correctness Proportion [%]"
    )

skill_complete = px.bar(
    data_frame=subject_complete, orientation='h', height=250
    )
skill_complete.update_layout(
    title_text='Correctness proportion for each topic/skill',
    yaxis_title="Topic/Skill", xaxis_title="Completion Proportion [%]",
    showlegend=False
    )
skill_complete.update_xaxes(range=[0, 100])

#%% DATA INTRO
part_0 = "## ABOUT THE DATA SET"

data_intro = """
This is the result of {} students practicing {} questions.
The questions are in topics as follow: 
- {}: {} questions
- {}: {} questions
- {}: {} questions
""".format(df['UserId'].nunique(), 
df['QuestionId'].nunique(),
item_info['Name'].value_counts().index[0], item_info['Name'].value_counts().iloc[0],
item_info['Name'].value_counts().index[1], item_info['Name'].value_counts().iloc[1],
item_info['Name'].value_counts().index[2], item_info['Name'].value_counts().iloc[2],
)

#%% APP PART II: DATA
def get_corr(item_num):
    item = df[df['QuestionId']==item_num].set_index('UserId')      
    user_item = item.join(score)
    return user_item[['TotalScore', 'IsCorrect']].corr().iloc[1,0]

item_list = df['QuestionId'].unique().tolist()

disc = {}
for item_num in item_list:
    disc[item_num] = round(get_corr(item_num), 2)

disc = pd.Series(disc).rename('Discrimination')

item_info.set_index('QuestionId', inplace=True)
item_info = item_info.join(disc)
item_info.reset_index(inplace=True)

#%% APP PART II: COMPONENTS
part_ii="""
## PART II: QUALITY ANALYSIS
"""

dd_plot = px.scatter(
    data_frame=item_info,
    x='proportion', y='Discrimination', text="QuestionId"
    )
dd_plot.update_traces(textposition='top center')
dd_plot.update_layout(
    title_text='Question Quality in terms of Correctness Proportion\
and Discrimination',
    xaxis_title='Correctness Proportion [%]',
    yaxis_title='Discrimination [Pearson Corr]'
    )

#%% APP PART III: DATA & COMPONENTS
answer_percent=(
    df['AnswerValue'].groupby(df['QuestionId']).value_counts(normalize=True)
    .reset_index()
    )

def item_choice(item_num):
    return (answer_percent[answer_percent['QuestionId']==item_num]
                .sort_values('AnswerValue')
                )

def item_right_answer(item_num):
    return df[df['QuestionId']==item_num]['CorrectAnswer'].unique()[0]

part_iii="""
## PART III: MISCONCEPTION DETECTION
"""

#%% APP PART IV: DATA
part_iv = """
## PART IV: STUDENT RESULT
"""

# student score => score
# student list
student_list = df['UserId'].unique()

def get_score(student_id):
    return score.loc[student_id]

def get_detail(student_id):
    return (
        df[df['UserId'] == student_id][['QuestionId', 'IsCorrect']]
        .reset_index().drop(columns='index')
        )

df['topic'] = df['QuestionId'].map(
    lambda x: item_info[item_info['QuestionId']==x]['Name'].iloc[0])

def get_ability(student_id):
    student_in_topic = df.groupby(['UserId', 'topic'])['IsCorrect'].mean()
    return student_in_topic.loc[student_id].reset_index()

#%% PART V: IRT DATA
part_v = """
## PART V: IRT ANALYSIS (TWO PARAMETERS)
### 5.1: Student Latent Ability
"""

student_ability = pd.read_csv('student_IRT_2P.csv')
student_ability.index = student_list
student_ability = student_ability['F1'].rename('ability')

part_v_2 = """
### 5.2: Item Quality
"""

item_IRT = pd.read_csv('item_IRT_2P.csv')
item_IRT.index = item_list
item_IRT = item_IRT[['a', 'b']]
item_IRT.columns = ['disc', 'diff']

part_v_3 = """
### 5.3: Wright Map
"""

part_v_4 = """
### 5.4: Item Analysis
"""

part_v_5 = """
### 5.5: Test Construction on Purpose
"""


#%% PART V: CHART
# 1. Student IRT ability chart
IRT_student = px.histogram(student_ability)
IRT_student.update_layout(title_text='Student IRT ability distribution',
    xaxis_title='IRT latent ability', yaxis_title='Count',
    showlegend=False, bargap=0.2
    )

# 2. IRT vs CTT score chart
IRT_CTT_df = student_ability.to_frame().join(score)
IRT_CTT_student = px.scatter(data_frame=IRT_CTT_df, y='TotalScore', x='ability')
IRT_CTT_student.update_layout(title_text='Student IRT vs. Raw score',
    yaxis_title='Raw Score', xaxis_title='IRT latent ability',
    showlegend=False
    )

# 3. IRT diff vs. disc item chart
IRT_item = px.scatter(data_frame=item_IRT, x='diff', y='disc', text=item_IRT.index)
IRT_item.update_traces(textposition='top center')
IRT_item.update_layout(
    title_text='Item Difficulty and Discrimination',
    xaxis_title='IRT Difficulty',
    yaxis_title='IRT Discrimination'
    )

# 4. Wright map
wright_map = make_subplots(rows=1, cols=2, 
                           subplot_titles=['Item Diff Distribution',
                                           'Student Ability Distribution'],
                           column_widths=[0.2, 0.8],
                           horizontal_spacing=0.02)
wright_map.add_trace(
    go.Histogram(y=item_IRT['diff'], 
                 ybins=dict(start=-3, end=6, size=0.2)),
    row=1, col=1
    )
wright_map.update_xaxes(autorange='reversed', row=1, col=1)
wright_map.update_yaxes(ticks='outside', dtick=1, tickwidth=0,
                        #ticklen=10, tickcolor='crimson',
                        row=1, col=1)

wright_map.add_trace(
    go.Histogram(y=student_ability, 
                 ybins=dict(start=-3, end=6, size=0.2),
                 autobiny=False),
    row=1, col=2
    )
wright_map.update_yaxes(showticklabels=False, dtick=1,
                        row=1, col=2)
wright_map.update_layout(
    yaxis1=dict(range=[-3, 6],
                showgrid=True),
    yaxis2=dict(range=[-3, 6],
                showgrid=True),
    title_text = "Distribution of Item Difficulty and Student Ability",
    showlegend=False,
    bargap=0.1
    )

#%% APP LAYOUT
app = Dash(__name__)

app.layout = html.Div([
    # APP INTRO
    html.H1("WEB APP FOR LEARNING QUALITY ANALYSIS",
            style={'text-align': 'center'}
            ),
    
    dcc.Markdown(children=intro),
    
    dcc.Markdown(children=part_0),
    
    dcc.Markdown(children=data_intro),
    
    # PART I
    dcc.Markdown(children=part_i),
    
    html.Div([
        dcc.Graph(id='student_score', figure=fig_student_score, 
                  style={'width': '48%', 'display': 'inline-block'}),
        dcc.Graph(id='correct_prop', figure=fig_correct_prop,
                  style={'width': '48%', 'display': 'inline-block'}),
        ], style={'display': 'flex', 'justify-content': 'space-between'}),
    
    html.Div([
        dcc.Graph(id='skill_complete', figure=skill_complete)
        ]),
    
    # PART II
    dcc.Markdown(children=part_ii),
    
    dcc.Graph(id='dd_plot', figure=dd_plot),
    
    # PART III
    dcc.Markdown(children=part_iii),
    
    dcc.Dropdown(item_list, 405, id='question_dropdown',
                 style={'width': '30%'}),
    
    # item's info
    dcc.Markdown(id='item_spec'), 
    
    html.Div([
        html.Div([
            # item's image
            html.Img(id='item_image', width='80%')
            ], style={'width': '50%', 'display': 'inline-block',
                      'vertical-align': 'center',
                      'text-align': 'center'}),
                      
        html.Div([
            dcc.Graph(id='pie_misconception', figure={})
            ], style={'width': '50%', 'display': 'inline-block'}),
        ]),
    
    # PART IV
    dcc.Markdown(children=part_iv),

    dcc.Dropdown(student_list, 1506, id='student_dropdown',
                 style={'width': '30%'}),  
    
    html.Div([
        html.Div([
            dcc.Markdown(id='student_result'),
            ], style={'width': '30%', 'display': 'inline-block',
                      'text-align': 'center'}),
        
        html.Div([
            dcc.Graph(id='pie_competency', figure={})   
            ], style={'width': '70%', 'display': 'inline-block',
                      'vertical-align': 'top',})
        ]),
    
    # PART V                  
    dcc.Markdown(children=part_v),
    
    html.Div([
        html.Div([
            dcc.Graph(id='student_IRT', figure=IRT_student),
            ], style={'width': '50%', 'display': 'inline-block'}),
        
        html.Div([
            dcc.Graph(id='IRT_raw_score', figure=IRT_CTT_student) 
            ], style={'width': '50%', 'display': 'inline-block'})
        ]),
    

    dcc.Markdown(children=part_v_2),
    dcc.Graph(id='IRT_item', figure=IRT_item),
    
    dcc.Markdown(children=part_v_3),
    dcc.Graph(id='wright_map', figure=wright_map), 
    
    # ICC CURVE
    dcc.Markdown(children=part_v_4),
    html.Div([
        html.Div([
            dcc.Dropdown(item_list, 405, id='irt_question_dropdown'),
            ], style={'width': '10%', 'display': 'inline-block'}),
        
        html.Div([
            dcc.Dropdown(id='more_infor',
                         options=['Add Information Curve', 'Add Difficulty Line',
                                  'Add Empirical Point'],
                         value=['Add Information Curve', 'Add Difficulty Line',
                                'Add Empirical Point'],
                         multi=True),
            ], style={'width': '50%', 'display': 'inline-block'})
        ]),
    
    dcc.Graph(id='ICC', figure={}),
    
    # TEST CONSTRUCTION
    dcc.Markdown(children=part_v_5),
    dcc.Checklist(id='info_checklist',
                  options=item_list, value=[405], inline=True),
    
    dcc.Graph(id='info_curve', figure={})
                      
    ])

#%% APP PART III: 

# ITEM IMAGE
@callback(
    Output('item_image', 'src'),
    Input('question_dropdown', 'value')
    )
def item_image(item_num):
    image_path = 'assets/' + str(item_num) + '.jpg'
    return image_path

# ITEM INFO
@callback(
    Output('item_spec', 'children'),
    Input('question_dropdown', 'value')
    )
def item_spec(item_num):
    spec = []
    for i in range(1, 4):
        id_lv = (
            df_question_meta['SubjectId']
            .map(lambda x: int(x.strip('[]').split(",")[i]))
            )
        name_lv = (
            df_subject_meta[df_subject_meta['SubjectId'] == id_lv[item_num]][['Name']]
            .iloc[0, 0]
            )
        spec.append(name_lv)
    
    prop = item_info[item_info['QuestionId']==item_num]['proportion'].iloc[0]
    disc = item_info[item_info['QuestionId']==item_num]['Discrimination'].iloc[0]
    
    message = """Question information:
- Question is in the topic as follow: LV1: {} >>> LV2: {} >>> LV3: {}
- The proportion of correctness: {}%
- The discrimination: {}
\n
""".format(spec[0], spec[1], spec[2], prop, disc)
    
    if (item_choice(item_num)['proportion']<0.05).sum() > 0:
        message += """\n BAD DISTRACTOR WARNING! - The choice chosen by
        less than 5% of students might not a good distractor.\n"""

    if (item_choice(item_num)['proportion']>0.2).sum() > 1:
        message += """\n MISCONCEPTION WARNING! - The choice chosen by
        more than 20% of students could be a misconception.\n"""
        
    item_choices = item_choice(item_num)
    right_choice_prop = (
        item_choices[item_choices['AnswerValue']==item_right_answer(item_num)]
        ['proportion'].iloc[0]
        )
    max_choice_prop = item_choices['proportion'].max()
    if right_choice_prop != max_choice_prop:
        message += """\n SERIOUS WARNING! - Serious misconception or right
        answer is wrong!\n"""
        
    return message
    
# PIE CHART
@callback(
    Output('pie_misconception', 'figure'),
    Input('question_dropdown', 'value')
    )
def pie_misconception(item_num):
    item_choices = item_choice(item_num)
    right_answer = item_right_answer(item_num)
    
    pull = [0, 0, 0, 0]
    pull[right_answer-1] = 0.2
    colors = ['#eeeeee', '#eeeeee', '#eeeeee', '#eeeeee']
    colors[right_answer-1] = 'gold'
    
    fig = go.Figure(
        data=[go.Pie(labels=item_choices['AnswerValue'],
                     values=item_choices['proportion'],
                     pull=pull)]
    )
    fig.update_layout(
        title_text='Percentage of choice',
        showlegend=False
        )
    fig.update_traces(textinfo='percent+label',
                      marker=dict(colors=colors,
                                  line=dict(color='black', width=2)))
    
    return fig

#%% APP PART IV
@callback(
    Output('student_result', 'children'),
    Input('student_dropdown', 'value')
    )
def student_result(student_id):
    student_score = get_score(student_id)
    detail = get_detail(student_id)
    
    result = """The total score is {}\n, in which:
        
        """.format(student_score)
    for i in range(len(detail)):
       result += """
       - Question {}: {}
       """.format(detail.iloc[i]['QuestionId'], detail.iloc[i]['IsCorrect']==1)
    
    return result

@callback(
    Output('pie_competency', 'figure'),
    Input('student_dropdown', 'value')
    )
def pie_competency(student_id):
    test_df = get_ability(student_id)
    fig = px.line_polar(test_df, r='IsCorrect', theta='topic', line_close=True,
                        range_r=[0, 1])
    fig.update_traces(fill='toself')
    return fig

#%% APP PART V
# ICC
@callback(
    Output('ICC', 'figure'),
    Input('irt_question_dropdown', 'value'),
    Input('more_infor', 'value')
    )
def icc(item_id, more_infor):
    # icc curve model
    a = item_IRT.loc[item_id]['disc']
    b = item_IRT.loc[item_id]['diff']
    
    theta_model = np.arange(-4, 4, 0.01)
    P_model = 1 / (1 + np.exp(a * (b - theta_model)))
    infor = (a**2) * P_model * (1-P_model)

    # emprical data
    theta_empirical = student_ability.to_frame()
    df_temp = df.set_index('UserId')
    result_empirical = (df_temp[df_temp['QuestionId']==item_id]['IsCorrect']
                        .to_frame()
                        )
    empirical = theta_empirical.join(result_empirical)
    empirical.sort_values('ability', inplace=True)
    empirical = empirical.reset_index()
    empirical = empirical.reset_index()

    # divide data into 10 quantiles
    empirical['percentile'] = empirical['level_0'].map(lambda x: x//181.5)

    P_empirical = (
        empirical['IsCorrect'].groupby(empirical['percentile']).mean()
        )
    theta_empirical_group = (
        empirical['ability'].groupby(empirical['percentile']).mean()
        )
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=theta_model, y=P_model,
                             mode='lines', name='Item Characteristic Curve'))
    fig.update_layout(xaxis_title='Ability',
                      yaxis_title='Probability of having correct answer',
                      title_text='Item Characteristic Curve',
                      showlegend=True)
    if 'Add Information Curve' in more_infor:
        fig.add_trace(go.Scatter(x=theta_model, y=infor,
                                 mode='lines', name='Information Curve',
                                 line=dict(dash='dash')))
    if 'Add Difficulty Line' in more_infor:
        fig.add_shape(type='line', x0=b, y0=0, x1=b, y1=0.5,
                      line=dict(dash='dot', color='grey')
                      )
        fig.add_shape(type='line', x0=-4, y0=0.5, x1=b, y1=0.5,
                      line=dict(dash='dot', color='grey')
                      )
    if 'Add Empirical Point' in more_infor:
        fig.add_trace(go.Scatter(x=theta_empirical_group, y=P_empirical,
                                 mode='markers', name='Empirical Points',
                                 marker=dict(size=10)))
    
    return fig

# INFORMATION CURVE
"""
Information curve equation: 
    I = a^2 * P * (1-P)
"""
@callback(
    Output('info_curve', 'figure'),
    Input('info_checklist', 'value')
    )
def info_curve(item_list):
    theta = np.arange(-4, 4, 0.01)
    infor = np.zeros(len(theta))  # initiate infor array
    
    for item_id in item_list:
        a = item_IRT.loc[item_id]['disc']
        b = item_IRT.loc[item_id]['diff']
        P = 1 / (1 + np.exp(a * (b - theta)))
        infor += (a**2) * P * (1-P)
    
    fig = px.line(x=theta, y=infor)

    return fig

#%% --- RUN: http://127.0.0.1:8050/
app.run(debug=True)

# if __name__ == '__main__':
#     app.run_server(debug=True, port=8080, host='0.0.0.0')
