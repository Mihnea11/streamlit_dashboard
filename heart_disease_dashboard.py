import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from ucimlrepo import fetch_ucirepo

# Set Streamlit style settings
st.set_page_config(page_title="Heart Disease Dashboard", layout="wide")
st.markdown("""
    <style>
    .main {background-color: #f8f9fa;}
    h1 {color: #1A71BD;}
    </style>
    """, unsafe_allow_html=True)

# Fetch Heart Disease dataset, features, and target
heart_disease = fetch_ucirepo(id=45)
features = heart_disease.data.features
target = heart_disease.data.targets
metadata = heart_disease.variables

# Set column names based on metadata
feature_names = metadata[metadata["role"] == "Feature"]["name"].tolist()
target_name = metadata[metadata["role"] == "Target"]["name"].values[0]
features.columns = feature_names
target.columns = [target_name]

# Combine features and target into a single DataFrame for ease of use
data = pd.concat([features, target], axis=1)

# Dashboard Title
st.title("🫀 Heart Disease Dataset Dashboard")
st.markdown("Explore and analyze the Heart Disease dataset interactively.")

# Sidebar Filters
st.sidebar.header("Filter Options")
age_filter = st.sidebar.slider("Age Range:", int(data["age"].min()), int(data["age"].max()), (int(data["age"].min()), int(data["age"].max())))
target_filter = st.sidebar.multiselect("Diagnosis Outcome:", options=sorted(data[target_name].unique()), default=sorted(data[target_name].unique()))

# Filter Data
filtered_data = data[(data["age"] >= age_filter[0]) & (data["age"] <= age_filter[1])]
filtered_data = filtered_data[filtered_data[target_name].isin(target_filter)]

# Layout of the Dashboard
st.header("Filtered Data Overview")
with st.expander("View Data"):
    st.dataframe(filtered_data)

st.header("Summary Statistics")
with st.expander("View Summary Statistics"):
    st.write(filtered_data.describe())

# Correlation Heatmap with Decimal Precision
st.header("Correlation Heatmap")
fig, ax = plt.subplots(figsize=(10, 6))  # Centered size without placeholders
sns.heatmap(filtered_data.corr(), annot=True, fmt=".2f", cmap="coolwarm", ax=ax, cbar_kws={'shrink': .8})
ax.set_title("Correlation Heatmap")

st.pyplot(fig)

# Interactive Histograms for Integer Features with Side-by-Side Layout and Empty Placeholders
st.header("Feature Histograms")
int_vars = metadata[metadata["type"] == "Integer"]["name"].tolist()
selected_features = st.multiselect("Select Integer Features for Histograms:", int_vars, default=int_vars[:3])

# Display histograms side-by-side in rows of up to 3 plots, with empty placeholders if necessary
if selected_features:
    num_cols = 3
    num_rows = -(-len(selected_features) // num_cols)
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(15, 4 * num_rows))
    fig.subplots_adjust(hspace=0.5)
    axes = axes.flatten()
    
    for i, feature in enumerate(selected_features):
        sns.histplot(filtered_data[feature], kde=True, ax=axes[i], color="#1A71BD")
        axes[i].set_title(f"Distribution of {feature}")
    
    for j in range(len(selected_features), len(axes)):
        axes[j].axis('off')

    st.pyplot(fig)

# Interactive Scatter Plot with Placeholders
st.header("Scatter Plot")
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Select X and Y axes for scatter plot
col1, col2 = st.columns(2)
with col1:
    x_axis = st.selectbox("Select X-axis Variable:", feature_names)
with col2:
    y_axis = st.selectbox("Select Y-axis Variable:", feature_names)

# Add scatter plot to center subplot, with placeholders on the left and right
axes[0].axis('off')
sns.scatterplot(data=filtered_data, x=x_axis, y=y_axis, hue=target_name, palette="viridis", ax=axes[1])
axes[1].set_title(f"Scatter Plot of {y_axis} vs {x_axis}")
axes[2].axis('off')

st.pyplot(fig)

# Categorical Feature Counts with Side-by-Side Layout and Empty Placeholders
st.header("Categorical Feature Counts")
cat_vars = metadata[metadata["type"] == "Categorical"]["name"].tolist()
selected_cat_features = st.multiselect("Select Categorical Features for Counts:", cat_vars, default=cat_vars[:2])

if selected_cat_features:
    num_cols = 3
    num_rows = -(-len(selected_cat_features) // num_cols)
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(15, 4 * num_rows))
    fig.subplots_adjust(hspace=0.5)  # Add spacing between rows
    axes = axes.flatten()

    for i, feature in enumerate(selected_cat_features):
        sns.countplot(x=filtered_data[feature], hue=filtered_data[target_name], ax=axes[i], palette="viridis")
        axes[i].set_title(f"Counts of {feature}")
    
    for j in range(len(selected_cat_features), len(axes)):
        axes[j].axis('off')
    st.pyplot(fig)

# Pie Chart for Diagnosis Outcome Distribution with Placeholders
st.header("Diagnosis Outcome Distribution")
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Add pie chart to center subplot, with placeholders on the left and right
axes[0].axis('off')
target_counts = filtered_data[target_name].value_counts()
axes[1].pie(target_counts, labels=target_counts.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette("viridis", len(target_counts)))
axes[1].set_title("Diagnosis Outcome Distribution")
axes[1].axis('equal')
axes[2].axis('off')

st.pyplot(fig)