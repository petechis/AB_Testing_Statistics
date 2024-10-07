import numpy as np
import pandas as pd

from io import StringIO
import matplotlib.pyplot as plt

import streamlit as st
import plotly.graph_objects as go

from statsmodels.stats.proportion import proportions_ztest
import formatted_characters as fc


countA = 0
countB = 0
observations = 0
dfA = pd.DataFrame()
dfB = pd.DataFrame()

# Initialize session state
if 'show_content' not in st.session_state:
    st.session_state.show_content = False

def calculate_pvalue(val_1,val_2, n1_sample_sizes,n2_sample_sizes):    
    
    # Data sample_sizes
    successes = np.array([val_1, val_2])  # Number of purchases
    samples = np.array([n1_sample_sizes, n2_sample_sizes])  # Sample sizes

    # Performing the z-test
    stat, p_value = proportions_ztest(successes, samples)

    print(f"Z-statistic: {stat}")
    print(f"P-value: {p_value}")
    return p_value * 100   


def calculate_percentage(df, value):
    percentage = (value / len(df)) * 100
    return round(percentage, 2)

def create_gauge_chart(pvalue):

    # Create the gauge chart.
    #st.title("  Gauge Chart.")
    title_html = """
    <h1 style="color: gray; font-size: 30px; text-align:center">
        Gauge Chart.
    </h1>
    """
    st.markdown(title_html, unsafe_allow_html=True)

    fig = go.Figure(go.Indicator(
        mode="gauge",
        value=pvalue,       
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "green"},
            'steps': [
                {'range': [0, pvalue], 'color': "yellow", 'name': 'Low'.upper()},
                {'range': [pvalue, 100], 'color': "white", 'name': 'High'.upper()}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': pvalue
            }
        },        
    ))

    # Add annotations for labels
    fig.add_annotation(x=0.32, y=0, text=f"p-Value: {pvalue} %", showarrow=False, font=dict(size=20, color="white"))   

    text_value = ""
    if pvalue > 5:
        text_value = '<span style="color:red;">=> Null Hypothesis accepted</span>'
    else:
        text_value = '<span style="color:green;">=> Null Hypothesis rejected.</span>'

    fig.add_annotation(
        x=0.55,
        y= 1,       
        text=text_value,
        showarrow=False,
        font=dict(size=20),
    )
    # Display the chart in Streamlit
    st.plotly_chart(fig)

def create_bar_chart(countA, countB):      
    data = {
    'Observations': ['Exp A', 'Exp B'],   
    'Quantity': [countA, countB]
    }
    df = pd.DataFrame(data)
    
    #Setting the index
    df.set_index('Observations', inplace=True)    
   
    title_html = """
    <h1 style="color: gray; font-size: 30px; text-align:center">        
        Purchased (Abs).
        <br>
    </h1>
    """
    st.markdown(title_html, unsafe_allow_html=True)

    # Plot the bar chart
    st.bar_chart(df)   


def create_and_plot_graphs(val_1, val_2, len_1, len_2):
        
        pvalue = calculate_pvalue(val_1, val_2, len_1, len_2)
        
        col1, col2 = st.columns(2)
        # Creating two side-by-side columns.     

        with col1:
            create_bar_chart(val_1, val_2) #1            

        with col2:            
            create_gauge_chart(round(pvalue, 2)) #2            

with st.sidebar:
    st.title("Web Analytics Application.")  
    st.subheader(":red[App evaluates customer purchase data from websites after alterations.]") 
    
    uploaded_file_A = st.file_uploader("1. Choose a CSV file with the A-Observations.", type="csv")
    uploaded_file_A ="Data/campaign_data_A.csv"
    if uploaded_file_A:
        dfA = pd.read_csv(uploaded_file_A, header=0, delimiter=';')        
        countA = dfA['Engagement'].value_counts().get(1,0) 
        st.write(f"Customer Purchased / A-Campaign: :red[{calculate_percentage(dfA, countA)} %]")   
    
    uploaded_file_B = st.file_uploader("2. Choose a CSV file with the B-Observations.", type="csv")
    uploaded_file_B ="Data/campaign_data_B.csv"
    if uploaded_file_B:               
        dfB = pd.read_csv(uploaded_file_B, header=0, delimiter=';')
        countB = dfB['Engagement'].value_counts().get(1,0) 
        st.write(f"Customer Purchased / B-Campaign: :red[{calculate_percentage(dfB, countB )} %]")     

# Main content
if st.session_state.show_content:
    title = "A/B Testing for 2-Experiment Variants."   
    fc.custom_text_main(title,'Tahoma',36,'Bold','center')
    st.divider()

    create_and_plot_graphs(countA,countB,len(dfA),len(dfB))         
    st.write(":red[Data Storytelling: How Our New Website Boosted Sales.]")
    fc.custom_text_main(fc.intro, 'orange', 14, 'normal', 'left')
    fc.custom_text_main(fc.evaluation, 'orange', 14, 'normal', 'left') 
    fc.custom_text_main(fc.insights, 'orange', 14, 'normal', 'left')
    fc.custom_text_main(fc.summary, 'orange', 14, 'normal', 'left') 

else:
    title ="Statistical Hypothesis Testing."
    fc.custom_text_main(title,'orange',36,'Bold','center')
    st.image("img/pvalue.jpg")    
    cautioning = f"<br>⚠️ &nbsp;&nbsp; Please note the app is initially being populated by default files with two columns each {fc.tab}[customer] and [purchased Yes/No] and 500 fictious Customers each. You can make your {fc.tab}own dataset."
    fc.custom_text_main(cautioning,'orange',18,'normal','left')
   

# Sidebar button
if st.sidebar.button('Plot Graph'):
    st.session_state.show_content = True
    






    
