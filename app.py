import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title('Wine Quality Histogram')

# Load the dataset
@st.cache
def load_data():
    data = pd.read_csv('winequality-red.csv')
    return data

df = load_data()

# Display the first few rows of the dataset
st.subheader('Wine Quality Dataset')
st.write(df.head())

# Choose a feature to visualize
feature = st.selectbox('Select a feature for histogram:', df.columns)

# Display the histogram
st.subheader(f'Histogram of {feature}')
fig, ax = plt.subplots()
ax.hist(df[feature], bins=20, color='blue', edgecolor='black')
ax.set_xlabel(feature)
ax.set_ylabel('Frequency')
st.pyplot(fig)
