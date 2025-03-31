import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from utils import calculate, separate_positions
from components.plot import sf_plot, bmd_plot
from components.load import create_load_section, load_section
from components.visualize import create_visualizer


# Set page title
st.title("Beam Analysis - SFD and BMD Calculator")

# Initialize session state for loads if it doesn't exist
if 'beam_length' not in st.session_state:
    st.session_state.beam_length = 10.0

if 'load_count' not in st.session_state:
    st.session_state.load_count = 0

if "loads_list" not in st.session_state:
        st.session_state.loads_list = []




# Sidebar for adding loads
st.sidebar.header("Settings")

with st.sidebar.form('Adjust length'):
    length = st.number_input("Length (m)", key="length", value=10.0)
    submitted = st.form_submit_button("Change length")

    if submitted:
        st.session_state.beam_length = length


# Form for adding new loads
with st.sidebar.form("add_load"):
    
    magnitude = st.number_input("Magnitude (kN)", key="magnitude")
    
    position = st.slider("Position from left (m)", 0.0, length, 5.0, key="position")
    submitted = st.form_submit_button("Add Load")
    
    if submitted:
        st.session_state.loads['magnitudes'].append(magnitude)
        st.session_state.loads['postions'].append(position)
        

# Button to clear all loads
if st.sidebar.button("Clear All Loads"):
    st.session_state.loads = {
        'magnitudes': [],
        'postions': []
    }


# Display current loads
st.sidebar.header("Current Loads")
for i, (magnitude, position) in enumerate(zip(st.session_state.loads['magnitudes'], st.session_state.loads['postions'])):
    st.sidebar.text(f"{i+1}. Point Load: {magnitude} kN at {position} m")



# Calculate and plot diagrams
create_visualizer(st.session_state.loads_list.copy())


#with st.container(key='beam_params', border=True):
#    st.header("Beam Parameters")
#    st.session_state.beam_length = st.number_input(label="Beam Lenght (m)", min_value=1.0, step=1.0, value=10.0)

loads = load_section(st.session_state.beam_length)

# Use the loads data for calculations or visualization
st.write(f"Number of loads: {len(loads)}")

# You can access each load's properties like this:
for i, load in enumerate(loads):
    st.write(f"Load {i+1}: {load['magnitude']} kN, {load['direction']}, at position {load['position']} m")

magnitudes, positions = separate_positions(st.session_state.loads_list.copy())

x, shear, moment = calculate(
    st.session_state.beam_length,
    magnitudes=magnitudes,
    distances=positions,
)

# PLOTS 
st.plotly_chart(sf_plot(x, shear))
st.plotly_chart(bmd_plot(x, moment))

