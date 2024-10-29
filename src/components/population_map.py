import plotly.express as px
import streamlit as st

def render_population_map(df):
    """Render the choropleth map of India"""
    st.subheader("Population Distribution")
    fig = px.choropleth(
        df,
        locations='State',
        locationmode='country names',
        color='Population',
        hover_name='State',
        color_continuous_scale='Viridis',
        title='India State-wise Population'
    )
    fig.update_geos(fitbounds="locations", visible=False)
    st.plotly_chart(fig, use_container_width=True)