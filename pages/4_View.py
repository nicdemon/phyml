import os
import streamlit as st

from io import StringIO
from Bio import AlignIO

from utils import *
from runPhyML import PhyML

# Page settings
st.set_page_config(
    page_title = "PhyML - Analysis details",
    layout = "wide",
)

# TODO: Merge view & read in the same page