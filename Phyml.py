import os
import pandas as pd
import streamlit as st

from utils import init_db
from runPhyML import PhyML

st.set_page_config(
    page_title = "PhyML",
)

init_db()

with open('DESCRIPTION.md','r') as desc:
    content = desc.readlines()
    content = ' '.join([str(elem) for elem in content])
    st.markdown(content)