import streamlit as st
from gradio_client import Client 

st.set_page_config(page_title="SMS Spam Detector", page_icon="✉️")
st.title("✉️ SMS Spam Classifier ")

user_input = st.text_area("Enter Your SMS:", height=150)

API_URL = "minhalali12/SMS-Detection"

if st.button('Predict'):
    if user_input.strip() == "":
        st.warning("⚠️ Write Some Text First!!")
    else:
        with st.spinner('Fetching Data From The Gradio Client...'):
            try:
                # 1. Server se connection banayein
                client = Client(API_URL)
                
                result = client.predict(
                    user_input, 
                    api_name="/predict"
                )
                
                st.subheader("Result:")
                if "🚨 SPAM" in str(result):
                    st.error("🚨 WARNING: This is Spam Message!")
                else:
                    st.success("🍏 SAFE: This is Ham (Normal) message.")
                    
            except Exception as e:
               
                try:
                    result = client.predict(user_input)
                    st.subheader("Result:")
                    if "🚨 SPAM" in str(result):
                        st.error("🚨 WARNING: This is Spam Message!")
                    else:
                        st.success("🍏 SAFE: This is Ham (Normal) message.")
                except Exception as e_inner:
                    st.error(f"❌ Connection Failed. Error: {e_inner}")
