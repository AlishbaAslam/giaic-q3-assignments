import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="📁 File Converter", layout="wide")
st.title("📁 File Converter & Cleaner")
st.write("Upload files, convert formats and clean data by removing duplicates and empty rows.")

uploaded_files = st.file_uploader("Upload CSV or Excel files:", type=["csv", "xlsx"], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        ext = file.name.split(".")[-1]
        df = pd.read_csv(file) if ext == "csv" else pd.read_excel(file)
        st.write(f"### Preview of {file.name}")
        st.dataframe(df.head())

        if st.checkbox(f"Remove duplicates from {file.name}"):
            df.fillna(df.select_dtypes(include="number").mean(), inplace=True)
            st.success("Duplicate values removed successfully!")
            st.dataframe(df.head())

        selected_columns = st.multiselect("Select columns to keep:", df.columns.tolist(), default=df.columns.tolist())
        df = df[selected_columns]  
        st.dataframe(df.head()) 

        if st.checkbox(f"📈 Chart of {file.name}") and not df.select_dtypes(include="number").empty:
            st.bar_chart(df.select_dtypes(include="number").iloc[:, :2])

        select_format = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)

        if st.button(f"⬇️ Download {file.name} as {select_format}"):
            output = BytesIO()
            if select_format == "CSV":
                df.to_csv(output, index=False)
                mimetype = "text/csv"
                new_filename = file.name.replace(ext, "csv")
            else:
                df.to_excel(output, index=False)
                mimetype = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                new_filename = file.name.replace(ext, "xlsx")

                st.download_button("⬇️ Download", data=output, file_name=new_filename, mime=mimetype)
                st.success(f"File converted to {select_format} format successfully!")
