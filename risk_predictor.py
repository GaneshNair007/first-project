import streamlit as st

st.title("HEART DISEASE PREDICTION")
st.write("Enter your health details below to get an estimated risk score.")

with st.form("health_form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Patient Name")
        age  = st.number_input("Patient Age", min_value=1, max_value=120, value=30)
        gender = st.selectbox("Gender", ["MALE", "FEMALE"])
    with col2:
        bp = st.number_input("Blood Pressure", value=120)
        cholesterol = st.number_input("Cholesterol (mg/dL)", value=200)
        sugar = st.number_input("Blood Sugar (mg/dL)", value=100)
        heart_rate = st.slider("Heart Rate (bpm)", 40, 200, 72)

    st.write("Lifestyle --->")
    smoke = st.checkbox("Do you smoke?")
    exercise = st.checkbox("Do you exercise?")
    submitted = st.form_submit_button("Calculate Risk")

if submitted:
    risk_score = 0
    if age > 65: risk_score += 30
    elif age > 50: risk_score += 20
    elif age > 35: risk_score += 10

    if gender == "MALE": risk_score += 10

    if bp >= 180: risk_score += 30
    elif bp >= 140: risk_score += 20

    if cholesterol >= 240: risk_score += 25
    elif cholesterol >= 200: risk_score += 15

    if sugar >= 126: risk_score += 20

    if heart_rate > 100 or heart_rate < 60: risk_score += 10

    if smoke: risk_score += 20
    if not exercise: risk_score += 15

    risk = min(risk_score, 100)

    st.divider()
    st.write(f"### Analysis for {name}")
    st.progress(risk_score / 100)

    if risk_score >= 70:
        st.error(f"HIGH RISK DETECTED (Score: {risk_score})")
        st.write("Prediction: Chest pain, Fatigue, Breathlessness")
    elif risk_score >= 40:
        st.warning(f"MEDIUM RISK DETECTED (Score: {risk_score})")
        st.write("Prediction: Mild fatigue, check cholesterol.")
    else:
        st.success(f"LOW RISK (Score: {risk_score})")
        st.write("Keep up the healthy lifestyle!")
