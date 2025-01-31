import streamlit as st
import pandas as pd
import random
from pycaret.regression import load_model, predict_model

# Load the model
MODEL_PATH = "best_pycaret_model"
model = load_model(MODEL_PATH)

# Streamlit app title
st.title("Modular Kits Design - AI Assistant")

# Helper function for random defaults
def random_default(min_val, max_val, decimal=0):
    if decimal == 0:
        return random.randint(min_val, max_val)
    return round(random.uniform(min_val, max_val), decimal)

# Initialize random defaults in session_state if not already present
if "defaults" not in st.session_state:
    st.session_state.defaults = {
        "body_weight": random_default(1.5, 5.0, 1),
        "processor_cores": random.choice([2,4,6,8,12,16]),
        "processor_freq": random_default(2.0, 3.6, 1),
        "sensor_accuracy": random_default(0.70, 0.99, 3),
        "sensor_res": random_default(720, 4096),
        "actuator_speed": random_default(80, 200),
        "actuator_force": random_default(100.0, 500.0, 1),
        "cooling_power": random_default(30, 150),
        "ps_efficiency": random_default(0.80, 0.99, 3),
        "ps_max_output": random_default(100, 500),
        "ff_flow": random_default(1.0, 5.0, 2),
        "ff_pressure": random_default(5, 30),
        "lb_stress": random_default(50, 200),
        "mg_torque": random_default(50, 200),
        "mg_rpm": random_default(1000, 8000),
        "gb_ratio": random_default(2.0, 6.0, 2),
        "comm_bw": random_default(10, 1000),
        "chem_rate": random_default(0.5, 2.0, 2),
        "chem_ph": random_default(2.0, 10.0, 1),
        "total_power": random_default(50, 300, 1),
        "thermal_load": random_default(0, 200, 1),
        "system_cost": random_default(500, 5000, 1)
    }

# For convenience, load those values into local variables
defaults = st.session_state.defaults

# Create input fields
st.header("Component Specifications")
col1, col2 = st.columns(2)

with col1:
    body_weight = st.number_input("Body Weight (kg)",
                                  value=defaults["body_weight"],
                                  min_value=0.0)
    processor_cores = st.number_input("Processor Cores",
                                      value=defaults["processor_cores"],
                                      min_value=0)
    processor_freq = st.number_input("Processor Frequency (GHz)",
                                     value=defaults["processor_freq"],
                                     min_value=0.0)
    sensor_accuracy = st.number_input("Sensor Accuracy",
                                      value=defaults["sensor_accuracy"],
                                      min_value=0.0, max_value=1.0)
    sensor_res = st.number_input("Sensor Resolution (px)",
                                 value=defaults["sensor_res"],
                                 min_value=0)
    actuator_speed = st.number_input("Actuator Max Speed (mm/s)",
                                     value=defaults["actuator_speed"],
                                     min_value=0)
    actuator_force = st.number_input("Actuator Force (N)",
                                     value=defaults["actuator_force"],
                                     min_value=0.0)
    cooling_power = st.number_input("Cooling Power (W)",
                                    value=defaults["cooling_power"],
                                    min_value=0)
    ps_efficiency = st.number_input("Power Splitter Efficiency",
                                    value=defaults["ps_efficiency"],
                                    min_value=0.0, max_value=1.0)
    ps_max_output = st.number_input("Power Splitter Max Output (W)",
                                    value=defaults["ps_max_output"],
                                    min_value=0)

with col2:
    ff_flow = st.number_input("Fluid Flow Rate (L/min)",
                              value=defaults["ff_flow"],
                              min_value=0.0)
    ff_pressure = st.number_input("Fluid Max Pressure (bar)",
                                  value=defaults["ff_pressure"],
                                  min_value=0)
    lb_stress = st.number_input("Load Bearing Stress (kN)",
                                value=defaults["lb_stress"],
                                min_value=0)
    mg_torque = st.number_input("Motor Torque (Nm)",
                                value=defaults["mg_torque"],
                                min_value=0)
    mg_rpm = st.number_input("Motor Max RPM",
                             value=defaults["mg_rpm"],
                             min_value=0)
    gb_ratio = st.number_input("Gearbox Ratio",
                               value=defaults["gb_ratio"],
                               min_value=0.0)
    comm_bw = st.number_input("Comm Bandwidth (Mbps)",
                              value=defaults["comm_bw"],
                              min_value=0)
    chem_rate = st.number_input("Chemical Feed Rate (ml/s)",
                                value=defaults["chem_rate"],
                                min_value=0.0)
    chem_ph = st.number_input("Chemical Feed pH",
                              value=defaults["chem_ph"],
                              min_value=0.0, max_value=14.0)

# System-level inputs
st.header("System Calculations")
total_power = st.number_input("Total Power Consumption (W)",
                              value=defaults["total_power"],
                              min_value=0.0)
thermal_load = st.number_input("Thermal Load (W)",
                               value=defaults["thermal_load"],
                               min_value=0.0)
system_cost = st.number_input("System Cost ($)",
                              value=defaults["system_cost"],
                              min_value=0.0)

# Create the data table
data_table = pd.DataFrame({
    "Body_Weight(kg)": [body_weight],
    "Processor_Cores": [processor_cores],
    "Processor_Frequency(GHz)": [processor_freq],
    "Sensor_Accuracy": [sensor_accuracy],
    "Sensor_Resolution(px)": [sensor_res],
    "Actuator_MaxSpeed(mm/s)": [actuator_speed],
    "Actuator_Force(N)": [actuator_force],
    "Cooling_Power(W)": [cooling_power],
    "PowerSplitter_Efficiency": [ps_efficiency],
    "PowerSplitter_MaxOutput(W)": [ps_max_output],
    "FluidFlowUnit_FlowRate(L/min)": [ff_flow],
    "FluidFlowUnit_MaxPressure(bar)": [ff_pressure],
    "LoadBearingFrame_StressTolerance(kN)": [lb_stress],
    "MotorGeneratorUnit_Torque(Nm)": [mg_torque],
    "MotorGeneratorUnit_MaxRPM": [mg_rpm],
    "Gearbox_Ratio": [gb_ratio],
    "CommInterface_Bandwidth(Mbps)": [comm_bw],
    "ChemicalFeedSystem_Rate(ml/s)": [chem_rate],
    "ChemicalFeedSystem_pH": [chem_ph],
    "Total_Power_Consumption(W)": [total_power],
    "Thermal_Load(W)": [thermal_load],
    "System_Cost($)": [system_cost]
})

# Display the input values
st.subheader("Current Configuration")
st.dataframe(data_table)

# Prediction logic
if st.button("Predict Compatibility"):
    if data_table.isnull().values.any():
        st.error("Please fill all required fields!")
    else:
        try:
            prediction = predict_model(model, data=data_table)
            score = prediction['prediction_label'].values[0] * 100
            st.success(f"Predicted System Compatibility: {score:.1f}%")
            
            # Show interpretation
            if score > 80:
                st.info("Excellent compatibility! This configuration meets all critical requirements.")
            elif score > 60:
                st.warning("Good compatibility, but consider optimizing power and thermal characteristics.")
            else:
                st.error("Low compatibility detected. Review component specifications and system parameters.")
                
        except Exception as e:
            st.error(f"Prediction failed: {str(e)}")
