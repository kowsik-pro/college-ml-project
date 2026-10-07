import streamlit as st
import requests

st.set_page_config(
    page_title="Vehicle Insurance Fraud Detection",
    page_icon="🚗",
    layout="wide"
)

API_URL = "https://vehicle-fraud-detection-pgbo.onrender.com"

st.title("🚗 Vehicle Insurance Claim Fraud Detection")
st.write("Enter the insurance claim details to predict the likelihood of fraud.")

st.divider()

# -----------------------------
# Numerical Features
# -----------------------------

st.subheader("Numerical Information")

col1, col2, col3, col4 = st.columns(4)

with col1:
    week_of_month = st.number_input(
        "Week of Month",
        min_value=1,
        max_value=5,
        value=1
    )

with col2:
    week_of_month_claimed = st.number_input(
        "Week of Month Claimed",
        min_value=1,
        max_value=5,
        value=1
    )

with col3:
    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=30
    )

with col4:
    policy_number = st.number_input(
        "Policy Number",
        min_value=1,
        value=1
    )

col5, col6, col7, col8 = st.columns(4)

with col5:
    rep_number = st.number_input(
        "Rep Number",
        min_value=1,
        value=1
    )

with col6:
    deductible = st.number_input(
        "Deductible",
        min_value=0,
        value=400
    )

with col7:
    driver_rating = st.number_input(
        "Driver Rating",
        min_value=1,
        max_value=4,
        value=1
    )

with col8:
    year = st.number_input(
        "Year",
        min_value=1990,
        max_value=2030,
        value=1994
    )

# -----------------------------
# Categorical Features
# -----------------------------

st.subheader("Claim and Policy Information")

col1, col2, col3, col4 = st.columns(4)

with col1:
    month = st.selectbox(
        "Month",
        ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
         "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    )

with col2:
    day_of_week = st.selectbox(
        "Day of Week",
        ["Monday", "Tuesday", "Wednesday",
         "Thursday", "Friday", "Saturday", "Sunday"]
    )

with col3:
    make = st.selectbox(
        "Make",
        [
            "Honda", "Toyota", "Ford", "Mazda", "Chevrolet",
            "Pontiac", "Accura", "Dodge", "Mercury", "Nissan",
            "Saturn", "Saab", "BMW", "Mercedes", "VW", "Jeep"
        ]
    )

with col4:
    accident_area = st.selectbox(
        "Accident Area",
        ["Urban", "Rural"]
    )

col1, col2, col3, col4 = st.columns(4)

with col1:
    day_of_week_claimed = st.selectbox(
        "Day of Week Claimed",
        ["Monday", "Tuesday", "Wednesday",
         "Thursday", "Friday", "Saturday", "Sunday"]
    )

with col2:
    month_claimed = st.selectbox(
        "Month Claimed",
        ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
         "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    )

with col3:
    sex = st.selectbox(
        "Sex",
        ["Male", "Female"]
    )

with col4:
    marital_status = st.selectbox(
        "Marital Status",
        ["Single", "Married", "Divorced", "Widow"]
    )

col1, col2, col3, col4 = st.columns(4)

with col1:
    fault = st.selectbox(
        "Fault",
        ["Policy Holder", "Third Party"]
    )

with col2:
    policy_type = st.selectbox(
        "Policy Type",
        [
            "Sedan - Collision",
            "Sedan - Liability",
            "Sedan - All Perils",
            "Sport - Collision",
            "Sport - Liability",
            "Sport - All Perils",
            "Utility - Collision",
            "Utility - Liability",
            "Utility - All Perils"
        ]
    )

with col3:
    vehicle_category = st.selectbox(
        "Vehicle Category",
        ["Sedan", "Sport", "Utility"]
    )

with col4:
    vehicle_price = st.selectbox(
        "Vehicle Price",
        [
            "less than 20000",
            "20000 to 29000",
            "30000 to 39000",
            "40000 to 59000",
            "60000 to 69000",
            "more than 69000"
        ]
    )

col1, col2, col3, col4 = st.columns(4)

with col1:
    days_policy_accident = st.selectbox(
        "Days Policy - Accident",
        [
            "none",
            "1 to 7",
            "8 to 15",
            "15 to 30",
            "more than 30"
        ]
    )

with col2:
    days_policy_claim = st.selectbox(
        "Days Policy - Claim",
        [
            "none",
            "8 to 15",
            "15 to 30",
            "more than 30"
        ]
    )

with col3:
    past_number_claims = st.selectbox(
        "Past Number of Claims",
        [
            "none",
            "1",
            "2 to 4",
            "more than 4"
        ]
    )

with col4:
    age_vehicle = st.selectbox(
        "Age of Vehicle",
        [
            "new",
            "2 years",
            "3 years",
            "4 years",
            "5 years",
            "6 years",
            "7 years",
            "more than 7"
        ]
    )

col1, col2, col3, col4 = st.columns(4)

with col1:
    age_policy_holder = st.selectbox(
        "Age of Policy Holder",
        [
            "16 to 17",
            "18 to 20",
            "21 to 25",
            "26 to 30",
            "31 to 35",
            "36 to 40",
            "41 to 50",
            "51 to 65",
            "over 65"
        ]
    )

with col2:
    police_report_filed = st.selectbox(
        "Police Report Filed",
        ["Yes", "No"]
    )

with col3:
    witness_present = st.selectbox(
        "Witness Present",
        ["Yes", "No"]
    )

with col4:
    agent_type = st.selectbox(
        "Agent Type",
        ["External", "Internal"]
    )

col1, col2, col3, col4 = st.columns(4)

with col1:
    number_supplements = st.selectbox(
        "Number of Supplements",
        [
            "none",
            "1",
            "2 to 5",
            "more than 5"
        ]
    )

with col2:
    address_change_claim = st.selectbox(
        "Address Change - Claim",
        [
            "no change",
            "under 6 months",
            "1 year",
            "2 to 3 years",
            "4 to 8 years"
        ]
    )

with col3:
    number_cars = st.selectbox(
        "Number of Cars",
        [
            "1 vehicle",
            "2 vehicles",
            "3 to 4",
            "5 to 8",
            "more than 8"
        ]
    )

with col4:
    base_policy = st.selectbox(
        "Base Policy",
        ["Liability", "Collision", "All Perils"]
    )

# -----------------------------
# Prediction
# -----------------------------

st.divider()

if st.button("🔍 Predict Fraud", use_container_width=True):

    data = {
        "Month": month,
        "WeekOfMonth": week_of_month,
        "DayOfWeek": day_of_week,
        "Make": make,
        "AccidentArea": accident_area,
        "DayOfWeekClaimed": day_of_week_claimed,
        "MonthClaimed": month_claimed,
        "WeekOfMonthClaimed": week_of_month_claimed,
        "Sex": sex,
        "MaritalStatus": marital_status,
        "Age": age,
        "Fault": fault,
        "PolicyType": policy_type,
        "VehicleCategory": vehicle_category,
        "VehiclePrice": vehicle_price,
        "PolicyNumber": policy_number,
        "RepNumber": rep_number,
        "Deductible": deductible,
        "DriverRating": driver_rating,
        "Year": year,
        "Days_Policy_Accident": days_policy_accident,
        "Days_Policy_Claim": days_policy_claim,
        "PastNumberOfClaims": past_number_claims,
        "AgeOfVehicle": age_vehicle,
        "AgeOfPolicyHolder": age_policy_holder,
        "PoliceReportFiled": police_report_filed,
        "WitnessPresent": witness_present,
        "AgentType": agent_type,
        "NumberOfSuppliments": number_supplements,
        "AddressChange_Claim": address_change_claim,
        "NumberOfCars": number_cars,
        "BasePolicy": base_policy
    }

    try:
        response = requests.post(
            f"{API_URL}/api/predict",
            json=data
        )

        if response.status_code == 200:

            result = response.json()

            st.subheader("Prediction Result")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Prediction",
                    result["result"]
                )

            with col2:
                st.metric(
                    "Risk Level",
                    result["risk_level"]
                )

            with col3:
                st.metric(
                    "Fraud Probability",
                    f'{result["fraud_probability"]}%'
                )

        else:
            st.error(f"API Error: {response.text}")

    except requests.exceptions.ConnectionError:
        st.error(
            "Could not connect to the backend. "
            "Make sure FastAPI is running on port 8000."
        )