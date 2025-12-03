import os
import time
import streamlit as st

from utils import *
from runPhyML import PhyML

# Page settings
st.set_page_config(
    page_title = "PhyML - Analysis status",
    layout = "wide",
)

# Analysis initialization
#####################################################
# TODO: Show initialization widget

# Init database
db = st.session_state["database"]

# Init database entry
runID = db.new_run()

runConfig = st.session_state["userInput"]

st.write(f"Run ID is: {runID}")

st.write("User input:")

st.write(
    runConfig
)

# Dump input sequences stream to file & replace with filepath
if st.session_state["inputType"] == "File":
    filePath = write_sequences_file(
        runID,
        runConfig["input"]
    )
else:
    filePath = write_sequences_pasted(
        runID,
        runConfig["input"]
    )
runConfig["input"] = filePath

# Write run parameters to database
db.insert_run_parameters(
    runID,
    runConfig
)

# Instantiate PhyML
analysis = PhyML(runConfig)

# Analysis launch
#####################################################

# Launch analysis
with st.spinner("Analysis running"):
    while analysis.run() is None:
        time.sleep(1)
st.write("Analysis completed")

# Show progress

# Analysis completed
#####################################################

# Analysis completed output
analysis.get_results()

# Move to analysis view