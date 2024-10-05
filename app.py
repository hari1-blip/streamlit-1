import streamlit as st

# Title and description
st.title('Streamlit Deployment Testing App')
st.write('This app is used to test deployment on Streamlit.')

# Input from user
name = st.text_input('Enter your name:')

if st.button('Submit'):
    if name:
        st.success(f'Hello, {name}! Your app is deployed successfully!')
    else:
        st.error('Please enter your name.')

# Displaying some data
st.write('Sample Data:')
sample_data = {'Item': ['Apple', 'Banana', 'Orange'], 'Price': [100, 50, 75]}
st.table(sample_data)
