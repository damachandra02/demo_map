import pandas as pd
import streamlit as st

@st.cache_data
def load_population_data():
    """Load sample population data for Indian states"""
    return pd.DataFrame({
        'State': [
            'Maharashtra', 'Uttar Pradesh', 'Bihar', 'West Bengal', 
            'Madhya Pradesh', 'Tamil Nadu', 'Rajasthan', 'Karnataka',
            'Gujarat', 'Andhra Pradesh'
        ],
        'Population': [
            124.9, 224.9, 124.8, 99.1,
            85.3, 77.8, 77.3, 67.6,
            63.8, 53.9
        ],
        'Growth': [
            0.14, 0.16, 0.21, 0.13,
            0.18, 0.15, 0.19, 0.16,
            0.17, 0.10
        ]
    })