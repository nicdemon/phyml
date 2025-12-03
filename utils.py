import os
import json
import shutil
import atexit

import streamlit as st

from io import StringIO
from Bio import AlignIO

from db import database

# Database interactions
def init_db():
    st.session_state['database'] = database()


# Visual components
@st.dialog("Missing sequences", width = "large")
def no_sequences_modal():
    st.error("There are no sequences to analyze", icon=":material/error:")
    st.write("Please input sequences either with a file of by copy/pasting them before resubmitting")
    if st.button("Acknowledge"):
        st.rerun()

@st.dialog("Analysis submited", width = "large")
def submited_modal():
    st.success("Your analysis was submitted and it will run shortly", icon = ":material/check_circle:")
    if st.button("Awesome!"):
        st.rerun()
        # st.switch_page("pages/2_Analysis_status.py")

# Sequences handling
def write_sequences_file(id, seqs):
    filePath = os.path.join("outputs",f"{id}.phy")
    with open(filePath, "w") as handle:
        shutil.copyfileobj(seqs, handle, -1)
    return filePath

def write_sequences_pasted(id, seqs):
    filePath = os.path.join("outputs",f"{id}.phy")
    with open(filePath, "w") as handle:
        print(seqs, file = handle)
    return filePath

@atexit.register
def stop_db():
    st.session_state["database"]._disconnect_client()