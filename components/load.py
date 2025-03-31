import streamlit as st

def create_load_section(length, key_prefix=""):
    """
    Creates a load input section with magnitude, direction, position controls
    
    Parameters:
    -----------
    length : float
        The maximum length for the position slider
    key_prefix : str
        Prefix for the keys to allow multiple instances of this component
        
    Returns:
    --------
    dict
        Dictionary containing the load data (magnitude, direction, position)
    bool
        True if delete button was pressed, False otherwise
    """
    load_data = {}
    delete_load = False
    
    # Create a container for the load
    load = st.container(key=f'{key_prefix}_load_container', border=False)
    
    with load:
        col1, col2, col3, col4 = st.columns([2, 3, 5, 2])
        
        with col1:
            load_data["magnitude"] = st.number_input(
                "Magnitude (kN)", 
                key=f"{key_prefix}_magnitude"
            )
            
        with col2:
            load_data["direction"] = st.selectbox(
                "Choose direction:", 
                ["Upward", "Downward"], 
                key=f'{key_prefix}_direction'
            )
            
        with col3:
            load_data["position"] = st.slider(
                "Position from left (m)", 
                0.0, length, 5.0, 
                key=f"{key_prefix}_position"
            )

            
        with col4:
            delete_load = st.button(
                ":material/delete:", 
                type="primary", 
                key=f"{key_prefix}_delete"
            )
    
    return load_data, delete_load

def load_section(length):
    """
    Creates the entire loads section with add button and multiple load components
    
    Parameters:
    -----------
    length : float
        The maximum length for the position slider
    
    Returns:
    --------
    list
        List of load dictionaries with their properties
    """

    # Use session state to keep track of loads
    if "loads_list" not in st.session_state:
        st.session_state.loads_list = []
        st.session_state.load_count = 0
    
    with st.container(key='loads_section', border=True):
        st.header("Loads")
        
        # Display existing loads
        loads_to_delete = []
        
        for i, _ in enumerate(st.session_state.loads_list):
            load_data, delete_load = create_load_section(
                length, 
                key_prefix=f"load_{i}"
            )
            
            # Update the load data in session state
            st.session_state.loads_list[i] = load_data
            
            # Mark for deletion if delete button was pressed
            if delete_load:
                loads_to_delete.append(i)
        
        # Remove loads marked for deletion (in reverse order to avoid index issues)
        for idx in sorted(loads_to_delete, reverse=True):
            st.session_state.loads_list.pop(idx)
            st.rerun()
        



        # Add new load button
        if st.button(":material/add: Add Load", key="add_load_btn"):
            st.session_state.load_count += 1
            st.session_state.loads_list.append({
                "magnitude": 0.0,
                "direction": "Downward",
                "position": 5.0
            })
            # Force a rerun to show the new load immediately
            st.rerun()
        if st.button(" :material/clear: Clear All loads"):
            st.session_state.loads_list = []
            st.session_state.load_count = 0
            st.rerun()

    return st.session_state.loads_list