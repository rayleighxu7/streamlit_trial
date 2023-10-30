import streamlit as st

st.title("Test Deployment")
st.markdown("---")

option = st.radio("Select a format", ["Alpha", "Beta", "Theta", "Gamma"], index=None)

if option is not None:
    st.write(f"You have selected ***{option}***")

st.sidebar.write("Sidebar is here")
file = st.sidebar.file_uploader(
    label="no label",
    label_visibility="hidden",
    type="csv",
    accept_multiple_files=False,
    help="Upload files here",
    key="coolkey",
)

if file is not None:
    st.sidebar.write("You have uploaded a file!")