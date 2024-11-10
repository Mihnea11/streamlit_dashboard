
# 🫀 Heart Disease Dataset Dashboard

This project is an interactive dashboard for exploring and analyzing the Heart Disease dataset. Built using Streamlit, it provides features such as correlation heatmaps, histograms, scatter plots, and categorical feature counts, allowing users to filter data and visualize relationships within the dataset.

## Features
- Filter data based on age and diagnosis outcome.
- Visualize summary statistics of selected features.
- View a correlation heatmap with values clamped to two decimal places.
- Explore feature distributions with histograms and count plots.
- View a scatter plot to investigate relationships between features.
- Pie chart of diagnosis outcome distribution.

## Prerequisites
- **Python 3.7+** is required to run the dashboard.

## Setup Instructions

1. **Clone the Repository**
   ```bash
   https://github.com/Mihnea11/streamlit_dashboard
   ```

2. **Install Required Libraries**
   Ensure all required libraries are installed by running:
   ```bash
   pip install -r requirements.txt
   ```

   The `requirements.txt` file includes the following libraries:
   - `streamlit`
   - `pandas`
   - `matplotlib`
   - `seaborn`
   - `ucimlrepo`

3. **Download and Prepare the Dataset**
   The dataset will be automatically fetched from the UCI repository when the app is run, so no manual download is necessary.

## Running the Dashboard

Run the following command to start the Streamlit app:
```bash
streamlit run heart_disease_dashboard.py
```

This will launch the dashboard in your default web browser. If it doesn’t open automatically, navigate to `http://localhost:8501` in your browser.

## Dashboard Usage

- Use the **sidebar** to filter data based on age and diagnosis outcome.
- **Expand** or **collapse** sections like *Filtered Data Overview* and *Summary Statistics* for a clean view.
- Visualize feature relationships and distributions through various charts, such as:
  - **Correlation Heatmap**: Displays the correlation between features.
  - **Feature Histograms**: Displays histograms for selected integer features.
  - **Scatter Plot**: Shows a scatter plot for selected X and Y features.
  - **Categorical Feature Counts**: Counts of selected categorical features, segmented by diagnosis outcome.
  - **Diagnosis Outcome Distribution**: Displays the distribution of diagnosis outcomes in a pie chart.

## Example Output

Upon running the app, you’ll see an interactive dashboard with multiple filtering options and visualizations to explore the Heart Disease dataset.