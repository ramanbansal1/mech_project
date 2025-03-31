import streamlit as st

def create_visualizer(loads):
    st.html("""
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            background-color: #0E1117;
            color: #FAFAFA;
        }
        .beam-container {
            position: relative;
            width: 80%;
            height: 50px;
            background: #262730;
            margin: 50px auto;
            border-radius: 5px;
        }
        .pillar {
            width: 30px;
            height: 70px;
            background: #FAFAFA;
            position: absolute;
            bottom: -70px;
        }
        .left { left: 0%; }
        .right { right: 0%; }
        .force {
            position: absolute;
            width: 0;
            height: 0;
        }
        .upward {
            border-left: 10px solid transparent;
            border-right: 10px solid transparent;
            border-top: 30px solid #FF4B4B;
            bottom: 50px; /* Adjusted so the tip touches the beam's lower border */
            filter: drop-shadow(2px 2px 5px rgba(255, 75, 75, 0.5));
        }
        .downward {
            border-left: 10px solid transparent;
            border-right: 10px solid transparent;
            border-bottom: 30px solid #FF4B4B;
            top: 50px; /* Adjusted so the tip touches the beam's upper border */
            filter: drop-shadow(2px 2px 5px rgba(255, 75, 75, 0.5));
        }
        .slider-container {
            margin: 20px;
        }
        input[type=range] {
            accent-color: #FF4B4B;
        }
    </style>
    """)

    data = ""
    for i, load in enumerate(loads):
        print(load['position'])
        print(st.session_state.beam_length * 100, "\n\n")
        data += f"<div id=\"force{i}\" class=\"force {load["direction"].lower()}\" style=\"left: {load['position'] / st.session_state.beam_length * 100}%;\"></div>"
    
    


    st.html(f"""
    <div class="beam-container">
        <div class="pillar left"></div>
        <div class="pillar right"></div>
        {data}
    </div>
    """)

    st.html("""
    <script>
        function updateForce(forceId, value) {
            let forceElement = document.getElementById(forceId);
            forceElement.style.left = value + '%';
        }
    </script>
    """)