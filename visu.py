import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set page configuration
st.set_page_config(page_title="Data Visualiser App", page_icon="📊", layout="wide")

st.title("📊 Data Visualiser App")

# Sidebar for file upload
st.sidebar.header("Upload your CSV file")
file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

if file:
    df = pd.read_csv(file)
    columns = df.columns.tolist()
    plot_types = ['bar graph', 'line graph', 'scatter graph']

    # Display data preview and options in the main layout
    st.subheader("Data Preview")
    st.write(df.head())

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

    with tab2:
        if x_axis != 'none' and y_axis != 'none':
            st.subheader(f"{plot_type.capitalize()} of {y_axis} vs {x_axis}")
            plt.figure(figsize=(10, 6))

            if plot_type == 'bar graph':
                plt.bar(df[x_axis], df[y_axis])
            elif plot_type == 'line graph':
                plt.plot(df[x_axis], df[y_axis])
            elif plot_type == 'scatter graph':
                plt.scatter(df[x_axis], df[y_axis])

            plt.xlabel(x_axis)
            plt.ylabel(y_axis)
            plt.title(f"{plot_type.capitalize()} of {y_axis} vs {x_axis}")
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot()
        else:
            st.error("Please select both X and Y axis for visualization.")
else:
    st.info("Please upload a CSV file to get started.")

# Sidebar for additional information
st.sidebar.header("About")
st.sidebar.info("This app allows you to upload a CSV file and visualize the data using various plot types. Select the X and Y axes, choose the plot type, and generate the plot.")

st.sidebar.header("Instructions")
st.sidebar.info("1. Upload a CSV file.\n2. Select the X and Y axes.\n3. Choose the plot type.\n4. Click 'Visualise' tab to see the plot.")

st.sidebar.caption(" DEVELOPED BY TEAM REVANCLAWS")
