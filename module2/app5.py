import streamlit as st

my_data = {"R": 20000, 
"SPSS":30000, 
"Cspro":15000,
"Tanagra":25000, 
"Stata":14000,
"losses":"1.4%"}

options = st.multiselect(
    'Select the metrics to analysis',
    ['R','SPSS','Tanagra','Stata','losses']
)

for option in options:
    st.write(f':blue[{option}]{my_data[option]}')