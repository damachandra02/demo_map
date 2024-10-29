import streamlit as st

def render_migration_stats():
    """Render migration statistics"""
    st.subheader("States Migration")
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Inbound Migration", "23%", "2.5%")
    
    with col2:
        st.metric("Outbound Migration", "18%", "-1.2%")