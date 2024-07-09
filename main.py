import streamlit as st
import pandas as pd

st.title("Update Excel")
df = pd.read_csv("stunting_index.csv")

st.header("Existing File")
st.write(df)

st.sidebar.header("Option")
jenis_kelamin = st.sidebar.text_input("Jenis Kelamin")
umur = st.sidebar.text_input("Umur")
berat_badan = st.sidebar.text_input("Berat Badan (kg)")
tinggi = st.sidebar.text_input("Tinggi Badan (cm)")
status = st.sidebar.text_input("Status")
add_data = st.sidebar.button("Add Data")

if add_data:
    new_data = {"Jenis Kelamin": [jenis_kelamin],
                "Umur (bulan)": [int(umur)],
                "Berat Badan (kg)": [int(berat_badan)],
                "Tinggi Badan (cm)": [int(tinggi)],
                "Status Gizi": [status]}
    new_df = pd.DataFrame(new_data)
    df = pd.concat([df, new_df], ignore_index=True)
    df.to_csv("stunting_index.csv", index=False)
    st.success("Data added successfully.")

# Display updated dataframe
st.header("Updated File")
st.write(df)
