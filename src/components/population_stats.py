import plotly.express as px
import streamlit as st

def render_population_stats(df):
    """Render population statistics and charts"""
    st.subheader("Top States by Population")
    
    # Population metrics
    total_pop = df['Population'].sum()
    avg_growth = df['Growth'].mean()
    
    st.metric("Total Population (M)", f"{total_pop:.1f}M")
    st.metric("Average Growth Rate", f"{avg_growth:.1%}")
    
    # Bar chart
    fig = px.bar(
        df.sort_values('Population', ascending=True).tail(5),
        x='Population',
        y='State',
        orientation='h',
        title='Top 5 States by Population'
    )
    st.plotly_chart(fig, use_container_width=True)