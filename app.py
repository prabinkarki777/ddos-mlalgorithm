import streamlit as st
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the model, scaler, and label encoders
with open('random_forest_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

with open('label_encoders.pkl', 'rb') as le_file:
    label_encoders = pickle.load(le_file)

# Streamlit UI
st.set_page_config(page_title="DDoS Attack Classifier", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .sidebar .sidebar-content {
        background-color: #e0e0e0;
        padding: 10px;
    }
    .stButton > button {
        background-color: #007bff;
        color: white;
        border-radius: 5px;
        font-size: 10px;
        padding: 5px 10px;
        margin: 5px;
        min-width: 80px;
    }
    .stButton > button:hover {
        background-color: #0056b3;
    }
    .stNumberInput > input {
        font-size: 11px;
        padding: 5px;
    }
    .stTextInput > input {
        border-radius: 5px;
        border: 1px solid #ddd;
        font-size: 11px;
        padding: 5px;
    }
    .stSidebar .stSidebarContent {
        padding: 7px;
    }
    .stButtonContainer {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
    }
    </style>
""", unsafe_allow_html=True)

# Header and description
st.title("🌐 DDoS Attack Classifier")
st.write("""
    This application classifies network traffic as either **Normal** or a potential **DDoS Attack**.
    Enter the network traffic data below to get predictions.
""")

# Predefined example data
predefined_data = {
    'Example 1': {
        'bytecount': 143891878,
        'pktcount': 134983,
        'dur': 313,
        'tot_dur': 3.11E+11,
        'packetins': 1931,
        'pktperflow': 7570,
        'byteperflow': 8069620,
        'pktrate': 292.0,
        'dt': 10146,
        'tx_bytes': 3609
    },
    'Example 2': {
        'bytecount': 1000000000,
        'pktcount': 100000,
        'dur': 0,
        'tot_dur': 3.11E+11,
        'packetins': 1,
        'pktperflow': 30,
        'byteperflow': 0,
        'pktrate': 10.0,
        'dt': 0,
        'tx_bytes': 1000
    },
    'Example 3': {
        'bytecount': 5000,
        'pktcount': 1000000,
        'dur': 0,
        'tot_dur': 3000000,
        'packetins': 50,
        'pktperflow': 10,
        'byteperflow': 200,
        'pktrate': 2.0,
        'dt': 11776,
        'tx_bytes': 3000
    },
    'Example 4': {
        'bytecount': 10000,
        'pktcount': 200,
        'dur': 500000,
        'tot_dur': 6000000,
        'packetins': 400,
        'pktperflow': 20,
        'byteperflow': 500,
        'pktrate': 5.0,
        'dt': 11976,
        'tx_bytes': 6000
    }
}

# Create a horizontal layout for example buttons
col1, col2, col3, col4 = st.columns(len(predefined_data))
for idx, (example_name, example_data) in enumerate(predefined_data.items()):
    with col1 if idx == 0 else col2 if idx == 1 else col3 if idx == 2 else col4:
        if st.button(example_name):
            # Update session state with the selected example data
            st.session_state['form_data'] = example_data

# Initialize form data
form_data = st.session_state.get('form_data', {
    'bytecount': 0,
    'pktcount': 0,
    'dur': 0,
    'tot_dur': 0.0,
    'packetins': 0,
    'pktperflow': 0,
    'byteperflow': 0,
    'pktrate': 0.0,
    'dt': 0,
    'tx_bytes': 0
})

# Input fields for new data with unique keys
bytecount = st.sidebar.number_input("Byte Count", min_value=0, step=1, key='bytecount_input', value=int(form_data['bytecount']))
pktcount = st.sidebar.number_input("Packet Count", min_value=0, step=1, key='pktcount_input', value=int(form_data['pktcount']))
dur = st.sidebar.number_input("Duration (in seconds)", min_value=0, step=1, key='dur_input', value=int(form_data['dur']))
tot_dur = st.sidebar.number_input("Total Duration (in seconds)", min_value=0.0, step=1.0, key='tot_dur_input', value=float(form_data['tot_dur']))
packetins = st.sidebar.number_input("Packet In", min_value=0, step=1, key='packetins_input', value=int(form_data['packetins']))
pktperflow = st.sidebar.number_input("Packets per Flow", min_value=0, step=1, key='pktperflow_input', value=int(form_data['pktperflow']))
byteperflow = st.sidebar.number_input("Bytes per Flow", min_value=0, step=1, key='byteperflow_input', value=int(form_data['byteperflow']))
pktrate = st.sidebar.number_input("Packet Rate", min_value=0.0, step=0.1, key='pktrate_input', value=float(form_data['pktrate']))
dt = st.sidebar.number_input("Date-Time", min_value=0, step=1, key='dt_input', value=int(form_data['dt']))
tx_bytes = st.sidebar.number_input("Transmitted Bytes", min_value=0, step=1, key='tx_bytes_input', value=int(form_data['tx_bytes']))

# Create DataFrame for new data
new_data = pd.DataFrame({
    'bytecount': [bytecount],
    'pktcount': [pktcount],
    'dur': [dur],
    'tot_dur': [tot_dur],
    'packetins': [packetins],
    'pktperflow': [pktperflow],
    'byteperflow': [byteperflow],
    'pktrate': [pktrate],
    'dt': [dt],
    'tx_bytes': [tx_bytes]
})

# Select and scale features
top_features_mi = ['bytecount', 'pktcount', 'byteperflow', 'pktperflow', 'pktrate', 'dt', 'tot_dur', 'tx_bytes', 'dur', 'packetins']
new_data = new_data[top_features_mi]
new_data_scaled = scaler.transform(new_data)

# Display the input data
st.subheader("Input Data")
st.write(new_data)

# Make predictions
predictions = model.predict(new_data_scaled)

# Display results
st.subheader("Prediction Result")
if predictions[0] == 0:
    st.success("🔵 Prediction: Normal")
else:
    st.error("🔴 Prediction: DDoS Attack")

# Additional visual enhancements or explanations
st.markdown("""
    ### Explanation:
    - **Normal**: The network traffic is classified as normal and does not indicate any signs of a DDoS attack.
    - **DDoS Attack**: The network traffic is identified as a potential Distributed Denial of Service (DDoS) attack.

""")
