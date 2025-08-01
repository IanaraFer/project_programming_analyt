# Programming for Data Analytics

This repository contains a data analytics project for the Programming for Data Analytics class at ATU. The project analyzes weather data from the 'Historic Data - Met Éireann - The Irish Meteorological Service'.

## Project Overview

This project performs comprehensive analysis of Irish meteorological data, including data cleaning, statistical analysis, and visualization of weather patterns and wind resources across Ireland.

## Repository Contents

- **`StationDetails.csv`** - Raw data downloaded from Met Éireann's Historic Data service
- **`Cleaned_StationDetails.csv`** - Processed and normalized dataset ready for analysis
- **`project.ipynb`** - Main Jupyter notebook containing all data analyses and visualizations
- **`README.md`** - Project documentation (this file)
- **`wind_resource_map.html`** - Interactive map for wind resource visualization


## Getting Started

### Prerequisites

To run this project, you will need:

- **Python 3.11** or higher
- **Visual Studio Code** (recommended IDE)
- **Jupyter Notebook** extension for VS Code

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/IanaraFer/project_programming_analyt.git
   cd project_programming_analyt
   ```

2. Install required Python packages:
   ```bash
   pip install pandas numpy matplotlib scipy geopandas folium shapely
   ```

3. Open the project in Visual Studio Code and run the Jupyter notebook

### Usage

1. Open `project.ipynb` in VS Code
2. Run all cells to reproduce the analysis
3. Open `wind_resource_map.html` in a web browser to view the interactive map


## Features

- **Data Cleaning**: Comprehensive preprocessing of meteorological station data
- **Statistical Analysis**: Correlation analysis and linear regression modeling
- **Data Visualization**: Charts, plots, and interactive maps using matplotlib and folium
- **Geographic Analysis**: Spatial analysis of weather stations using geopandas
- **Interactive Mapping**: Wind resource visualization with interactive HTML map

## Data Source

The data used in this project comes from [Met Éireann - The Irish Meteorological Service](https://www.met.ie/), specifically their Historic Data archive containing detailed information about weather monitoring stations across Ireland.

## Support

For questions or issues regarding this project:

- **Email**: ianarafer@gmail.com
- **GitHub Issues**: Open an issue request in this repository


## Technologies Used

- **Python 3.11**: Primary programming language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Matplotlib**: Data visualization and plotting
- **SciPy**: Statistical analysis and linear regression
- **GeoPandas**: Geographic data analysis
- **Folium**: Interactive map generation
- **Shapely**: Geometric operations

## References

- [Pandas Documentation - 10 Minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html#plotting)
- [NumPy Documentation](https://en.wikipedia.org/wiki/NumPy)
- [Pandas Visualization Guide](https://pandas.pydata.org/docs/user_guide/visualization.html#visualization)
- [Pandas DataFrame Introduction](https://pandas.pydata.org/docs/user_guide/dsintro.html#dataframe)
- [Python OS Module](https://docs.python.org/3/library/os.html)
- [Matplotlib Documentation](https://matplotlib.org/)
- [Matplotlib Pyplot Tutorial](https://matplotlib.org/stable/tutorials/pyplot.html)
- [SciPy Linear Regression](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html)
- [GeoPandas Getting Started](https://geopandas.org/en/stable/getting_started/introduction.html)
- [Shapely Point Documentation](https://shapely.readthedocs.io/en/stable/reference/shapely.Point.html)
- [Folium Documentation](https://pypi.org/project/folium/)
- [NumPy Financial](https://numpy.org/numpy-financial/)
- [Wikipedia - Embedding](https://en.wikipedia.org/wiki/Embedding)
- [Google Research - Embedding Projector](https://research.google/blog/open-sourcing-the-embedding-projector-a-tool-for-visualizing-high-dimensional-data/)

## License

This project is for educational purposes as part of the Programming for Data Analytics course at ATU.

---

**Author**: Ianara Fernandes