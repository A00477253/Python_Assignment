import pandas as pd
import matplotlib.pyplot as plot
import streamlit as st


st.title('Age Histogram')
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    if 'Name' in data.columns and 'Age' in data.columns:
        plot.hist(data['Age'], bins=10, edgecolor='black',color='red')
        plot.xlabel('Age')
        plot.ylabel('Frequency')
        plot.title('Age Histogram')
        st.pyplot(plot)
    else:
        st.error('The uploaded file does not have the required columns.')