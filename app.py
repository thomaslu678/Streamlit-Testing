import streamlit as st


st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

# --- Header ---
with st.container():
    st.subheader("Hi, I am not Hyun's fan! :wave:")
    st.title("High School Student")
    st.write("I love coding and dogs")
    st.write("[Learn More >](https://thomaslulearnerportfolio.weebly.com)")

# --- Part 2 ---
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Part 2")
        st.write("##")
        st.write(
            """
            Here is a list:
            - First item
            - Second Item
            - Third Item
            """
        )