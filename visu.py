import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set page configuration
st.set_page_config(page_title="Data Visualiser App", page_icon="📊", layout="wide")

# Title
st.title("📊 Data Visualiser App")

# Sidebar for file upload
st.sidebar.header("Upload your CSV File")
file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

if file:
    # Read the CSV file
    df = pd.read_csv(file)
    columns = df.columns.tolist()
    
    # Plot types with more options
    plot_types = ['Bar Graph', 'Line Graph', 'Scatter Graph', 'Histogram', 'Box Plot', 'Heatmap']
    
    # Data Preview
    st.subheader("Data Preview")
    st.write(df.head())
    
    # Visualization Settings
    st.subheader("Visualization Settings")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        x_axis = st.selectbox("Select X axis", options=['none'] + columns)
    with col2:
        y_axis = st.selectbox("Select Y axis", options=['none'] + columns)
    with col3:
        plot_type = st.selectbox("Select Plot Type", options=plot_types)
    
    # Tabs for analysis and visualization
    tab1, tab2 = st.tabs(["🔍 Analyse", "📊 Visualise"])
    
    with tab1:
        st.subheader('Summary of the Data')
        st.write(df.describe())
        
        # Data Info
        st.subheader('Data Information')
        buffer = pd.DataFrame({
            'Column': df.columns,
            'Non-Null Count': df.count(),
            'Dtype': df.dtypes
        })
        st.dataframe(buffer)
    
    with tab2:
        # Improved error handling and visualization
        if x_axis != 'none' and y_axis != 'none':
            st.subheader(f"{plot_type} of {y_axis} vs {x_axis}")
            
            # Clear any existing plots
            plt.clf()
            
            # Create a figure with better resolution
            plt.figure(figsize=(12, 7), dpi=100)
            
            # Plot selection with error handling
            try:
                if plot_type == 'Bar Graph':
                    plt.bar(df[x_axis], df[y_axis])
                elif plot_type == 'Line Graph':
                    plt.plot(df[x_axis], df[y_axis])
                elif plot_type == 'Scatter Graph':
                    plt.scatter(df[x_axis], df[y_axis])
                elif plot_type == 'Histogram':
                    plt.hist(df[y_axis], bins=20)
                elif plot_type == 'Box Plot':
                    sns.boxplot(x=df[x_axis], y=df[y_axis])
                elif plot_type == 'Heatmap':
                    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
                
                plt.xlabel(x_axis)
                plt.ylabel(y_axis)
                plt.title(f"{plot_type} of {y_axis} vs {x_axis}")
                plt.xticks(rotation=45)
                plt.tight_layout()
                
                # Use Streamlit's pyplot method
                st.pyplot(plt)
                
            except Exception as e:
                st.error(f"Error creating plot: {e}")
                st.warning("Please check your data types and selection.")
        else:
            st.error("Please select both X and Y axis for visualization.")

else:
    st.info("Please upload a CSV file to get started.")

# Sidebar for additional information
st.sidebar.header("About")
st.sidebar.info("This app allows you to upload a CSV file and visualize the data using various plot types. Select the X and Y axes, choose the plot type, and generate the plot.")

st.sidebar.header("Instructions")
st.sidebar.info("""
1. Upload a CSV file
2. Select the X and Y axes
3. Choose the plot type
4. Explore the Analyse and Visualise tabs
""")

st.sidebar.caption("DEVELOPED BY G60 SOLUTIONS")

# Hide Streamlit branding
st.markdown("""
<style>
.viewerBadge_link__qRIco {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)
