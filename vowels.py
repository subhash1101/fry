import streamlit as st
st.title("Vowels")
a = st.text_input(label="Enter the String")
count=0 
if st.button("Submit"):
    try:
        for i in a:
            if i=="A" or i=="a" or i=="e" or i=="E" or i=="i" or i=="I" or i=="o" or i=="O" or i=="u" or i=="U":
                count+=1
            else:
                continue
        st.write("Number of Vowels", count)
    except ValueError:
        st.write("Please enter a String")