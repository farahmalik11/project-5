import matplotlib.pyplot as plt
import pandas as pd
import pickle
import streamlit as st

st.set_page_config(
    page_icon='',
    page_title = 'Water Usage',
    initial_sidebar_state='expanded'
)

st.title('Water Usage')

st.write('Use the sidebar to select a page to view.')

page = st.sidebar.selectbox(
    'Page',
    ('About', 'EDA', 'Model')
)

if page == 'About':
    st.subheader('About this project')
    st.write('''
This is a Streamlit app that hosts my Water Usage model.

Background: Climate change has emerged as a pressing global challenge, \\
with significant implications for water resources. As temperatures rise \\
and climates become increasingly erratic and unpredictable, the task of \\
monitoring and managing water usage grows more complex. By leveraging \\
machine learning, we can unlock valuable insights in relation to water \\
consumption patterns that empower policymakers, water resource manager, \\
and communities to make informed decisions, develop adaption strategies, \\
and implement proactive measures to sustainably manage our water resources \\
in the face of an uncertain climate future.

Objective: The objective of this project is to use machine learning to \\
build a _______ model/pipeline/something else to better understand, and be \\
able to compare and contrast, state-county level water supply and \\
consumption. This project will ultimately help communities and other \\
stakeholders monitor and manage their water patterns, identifying areas \\
for improvement and efficiency. By providing locally-relevant information, \\
consumers of this information might better understand their own water \\
consumption and industries in their local area which may adjust consumption \\
patterns through awareness and advocacy.

The best model I found was....

etc.
    ''')
elif page == 'EDA':
    # header
    st.subheader('Exploratory Data Analysis')
    st.write('''The model is trained on numerical data from [sources].
    
    Below are the graphs''')
    

elif page == 'Model':
    
    st.title('What did we find?')

    # Open your model!
    with open('./model_0.pkl', 'rb') as f:
        model_0 = pickle.load(f)

    st.write(f"County population mean (in thousands): {round(model_0)}")
    
    
# Choropleths
#cite: https://plotly.com/python/county-choropleth/ > Redirects to manage deprecation: https://plotly.com/python/choropleth-maps/

from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

# dtype={'FIPS':str} # need to make sure we are using FIPS codes as strings vs. ints.  Can be done on import.

import plotly.express as px

# Get user input: which cluster would you like to see for your selected county
user_selected_value = '' # Get user input: which cluster would you like to see for your selected county
cluster_dict = {
    '<user_selected_value':'column_name',
}

fig = px.choropleth(
                    title = f"Water Usage for {county}"
                    # df, ## dateframe with FIPs codes
                    geojson=counties,
                    locations='FIPS',
                    color=cluster_dict.get(user_selected_value),
                    hover_name = 'county', ## County Name
                    hover_data = '',
                    basemap_visible = True
                    )
