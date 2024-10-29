import streamlit as st

def render_sidebar():
    """Render the sidebar with controls"""
    st.sidebar.header("Controls")
    year = st.sidebar.selectbox("Select Year", ["2021", "2020", "2019"])
    return year
