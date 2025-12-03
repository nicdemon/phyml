import os
import streamlit as st

from io import StringIO
from Bio import AlignIO

from utils import *
from runPhyML import PhyML

# Page settings
st.set_page_config(
    page_title = "PhyML - Analysis history",
    layout = "wide",
)

# TODO: Show a list of all runs with metadata that can be chosen and redirect to "View" page