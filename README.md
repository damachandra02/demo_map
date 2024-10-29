# India Population Dashboard

An interactive dashboard showing population distribution and demographics across Indian states, built with Streamlit.

## Project Structure

```
├── src/
│   ├── components/
│   │   ├── sidebar.py
│   │   ├── population_map.py
│   │   ├── population_stats.py
│   │   └── migration_stats.py
│   └── data/
│       └── load_data.py
├── app.py
├── requirements.txt
└── README.md
```

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

## Features

- Interactive choropleth map of India
- Population distribution by state
- Migration statistics
- Top states by population
- Year-wise data comparison
- Growth rate analysis

## Data Sources

Replace the sample data in `src/data/load_data.py` with actual data from:
- Census of India
- National Sample Survey Office
- Ministry of Statistics and Programme Implementation

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to the branch
5. Create a Pull Request