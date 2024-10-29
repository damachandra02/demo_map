import streamlit as st
from src.data.load_data import load_population_data
from src.components.sidebar import render_sidebar
from src.components.population_map import render_population_map
from src.components.population_stats import render_population_stats
from src.components.migration_stats import render_migration_stats

# Page config
st.set_page_config(
    page_title="India Population Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    st.title("📊 India Population Dashboard")
    
    # Render sidebar
    year = render_sidebar()
    
    # Load data
    df = load_population_data()
    
    # Main content
    col1, col2 = st.columns([2, 1])
    
    with col1:
        render_population_map(df)
    
    with col2:
        render_population_stats(df)
    
    # Migration section
    render_migration_stats()

if __name__ == "__main__":
    main()