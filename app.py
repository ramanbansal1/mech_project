import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from utils import calculate 

# Set page title
st.title("Beam Analysis - SFD and BMD Calculator")

# Initialize session state for loads if it doesn't exist
if 'loads' not in st.session_state:
    st.session_state.loads = {
        'magnitudes': [],
        'postions': []
    }

if 'beam_length' not in st.session_state:
    st.session_state.beam_length = 10.0



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
x, shear = calculate(
    st.session_state.beam_length,
    magnitudes=st.session_state.loads['magnitudes'].copy(),
    distances=st.session_state.loads['postions'].copy()
)

print(x)
# Create SFD plot
fig_sfd = go.Figure()
fig_sfd.add_trace(go.Scatter(x=x, y=shear, mode='lines', name='Shear Force'))
fig_sfd.update_layout(
    title='Shear Force Diagram',
    xaxis_title='Position (m)',
    yaxis_title='Shear Force (kN)',
    height=400
)
st.plotly_chart(fig_sfd)


"""
# Create BMD plot
fig_bmd = go.Figure()
fig_bmd.add_trace(go.Scatter(x=x, y=moment, mode='lines', name='Bending Moment'))
fig_bmd.update_layout(
    title='Bending Moment Diagram',
    xaxis_title='Position (m)',
    yaxis_title='Bending Moment (kN·m)',
    height=400
)
st.plotly_chart(fig_bmd)

"""