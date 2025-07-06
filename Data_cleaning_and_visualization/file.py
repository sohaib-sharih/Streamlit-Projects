import streamlit as st
import pandas as pd
import os
from io import BytesIO


st.set_page_config(page_title='New Application', layout='wide')

st.title("This is my first app on StreamLit")

st.title("This is my first app on StreamLit")


st.write("Transform csv and excel format data with built-in data cleaning and data visualization.")

"""
1. To run the app, simply type streamlit run app.py
2. df => Dataframe
eamlit run app.py

"""

uploadedFiles = st.file_uploader("Upload your file, in csv or excel format here: ", type=['csv','xlsx'], accept_multiple_files=True)

if uploadedFiles:
    for box in uploadedFiles:
        file_ext = os.path.splitext(box.name)[-1].lower()

        if file_ext == ".csv":
            df = pd.read_csv(box)
        elif file_ext == ".xlsx":
            df = pd.read_excel(box)

        else:
            st.error(f"Unsupported box type {file_ext}")
            continue

        # Display the file data here

        st.write(f"**File name =** {file.name}")
        st.write(f"**File Size =** {file.size/1024}")

        # Display the first 5 rows of the data in the file that was uploaded

        st.write("Data is displayed here:")
        st.dataframe(df.head()) #Panda head displays the first 5 rows

        #Options for data cleaning
        st.subheader("Data cleaning options")
        if st.checkbox(f"Clean the data for {file.name}"):
            col1, col2 = st.columns(2)

            with col1:
                if st.button(f"Remove duplicates from: {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.write("Duplicates removed!")
            
            with col2:
                if st.button(f"Fill missing values for {file.name}"):
                    numeric_cols = df.select_dtypes(include=['number']).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.write("Missing values have been filled!")

        st.subheader("Select columns to convert")
        # Choose specific columns to keep or convert
        columns = st.multiselect(f"Choose columns for: {file.name},", df.columns, default=df.columns)
        df = df[columns]

        # Create some visualizations

        st.subheader("Data Visualization")
        if st.checkbox(f"Show visualization for {file.name}"):
            st.bar_chart(df.select_dtypes(include='number').iloc[:,:2])

        
        #Conver the file -> csv to excel

        st.subheader("Conversion Options")
        conversion_type = st.radio(f"Convert {file.name} to:", ['CSV','Excel'], key=file.name)

        if st.button(f"Convert {file.name}"):
            #Create an object from the BytesIO class
            buffer = BytesIO()
            if conversion_type == 'CSV':
                df.to_csv(buffer, index=False)
                file_name = file.name.replace(file_ext, '.csv')
                mime_type = "text/csv"

            elif conversion_type == 'Excel':
                df.to_excel(buffer, index=False)
                file_name = file.name.replace(file_ext, '.xlsx')
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            buffer.seek(0)

            #Download Option

            st.download_button(
                label=f"Download {file.name} as {conversion_type}",
                data=buffer,
                file_name=file_name,
                mime = mime_type

            )

st.success("All files processed!")