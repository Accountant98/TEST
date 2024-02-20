
import sys
# sys.path.append(r"C:QZ_No_1_code")
import streamlit as st
from user_read_only import user_read_only
from admin import admin
st.set_page_config(
    page_title="My Streamlit App",
    page_icon=":smiley:",
    layout="wide"  
)
try :
    if st.session_state.position=="admin": #st.session_state.mail:
    #------------MAIN APP-----------x
        admin()
    elif st.session_state.position=="staff" : 
        user_read_only()
except:
    st.warning("Please login before running app!!!")

if 1==1:
    None

