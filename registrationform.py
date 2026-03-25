import streamlit as st
st.title("REGISTRATION FORM")
st.write("** DETAILS **")
st.form("my_form")
col1,col2=st.columns(2)
with col1:
    st.text_input("First Name")
with col2:
    with col2:st.text_input("Last Name")
st.text_input("Enter E-mail/G-mail")
st.number_input("Mobile Number",min_value=0)
st.number_input("Enter Age")
st.radio("Gender",["female","Male","others"])
col3,col4=st.columns(2)
with col3:
    st.selectbox("Country",["Indian","America","Africa","china","Pakisthan"])
with col4:
    Nation=st.text_input("Nationality")
    st.write(f"your preference {Nation}")
address=st.text_area("enter address")
password=st.text_input("enter password",type="password")
st.button("submit")
st.balloons()