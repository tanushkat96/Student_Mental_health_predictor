import streamlit as st
import pandas as pd
import joblib

# Page configuration
st.set_page_config(
    page_title="Quick Assessment - Student Mental Health",
    page_icon="🧠",
    layout="wide"
)

# Load custom CSS
def load_css():
    with open('assets/style.css') as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# Navigation Component
def render_navbar(current_page="Home"):
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("Home", width="stretch",
                     type="primary" if current_page == "Home" else "secondary",
                     key="nav_home"):
            if current_page != "Home":
                st.switch_page("app.py")

    with col2:
        if st.button("Assessment", width="stretch",
                     type="primary" if current_page == "Assessment" else "secondary",
                     key="nav_assessment"):
            if current_page != "Assessment":
                st.switch_page("pages/1_🧠_Quick_Assessment.py")

    with col3:
        if st.button("Analysis", width="stretch",
                     type="primary" if current_page == "Analysis" else "secondary",
                     key="nav_analysis"):
            if current_page != "Analysis":
                st.switch_page("pages/2_📊_Analysis.py")

    with col4:
        if st.button("Solutions", width="stretch",
                     type="primary" if current_page == "Solutions" else "secondary",
                     key="nav_solutions"):
            if current_page != "Solutions":
                st.switch_page("pages/3_🌿_Solutions.py")

# Load trained model and columns
@st.cache_resource
def load_model():
    try:
        model = joblib.load("random_forest_model.pkl")
        model_columns = joblib.load("model_columns.pkl")
        return model, model_columns
    except:
        return None, None

def main():
    # Navbar
    render_navbar("Assessment")

    # Page Header
    st.markdown("""
    <div class="header-container">
        <h1 class="main-title">Quick Mental Health Assessment</h1>
        <p class="subtitle">Answer these questions to predict your mental health risk using our trained AI model.</p>
    </div>
    """, unsafe_allow_html=True)

    model, model_columns = load_model()

    if model is None:
        st.error("⚠️ Model not found. Please ensure 'random_forest_model.pkl' and 'model_columns.pkl' are available.")
        return

    # Assessment Form (all inside container)
    with st.form("assessment_form"):
        st.markdown('<div class="form-container">', unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Personal Details")
            gender = st.radio("Choose your gender:", ["Male", "Female"], key="gender")

            course = st.selectbox("Your Course:", 
                                  ["Engineering", "Science", "Arts", "Business", "Other"],
                                  key="course")

            year_of_study = st.selectbox("Year of Study:", 
                                         ["1", "2", "3", "4"],
                                         key="year_of_study")

        with col2:
            st.subheader("Academic & Mental Health Info")
            cgpa = st.selectbox("Your CGPA Range:", 
                                ["2.00 - 2.49", "2.50 - 2.99", "3.00 - 3.49", "3.50 - 4.00"],
                                key="cgpa")

            depression = st.radio("Do you have depression?", ["No", "Yes"], key="depression")
            anxiety = st.radio("Do you have anxiety?", ["No", "Yes"], key="anxiety")

        st.subheader("Additional Info")
        panic_attack = st.radio("Do you have panic attacks?", ["No", "Yes"], key="panic_attack")
        treatment = st.radio("Did you seek any specialist for treatment?", ["No", "Yes"], key="treatment")

        submitted = st.form_submit_button("Get Assessment Results", width="stretch")

        st.markdown('</div>', unsafe_allow_html=True)

    # Process results
    show_results = False
    if submitted:
        st.markdown("---")

        try:
                    # Convert categorical inputs exactly as in training
            input_dict = {
                'choose_your_gender': gender,
                'course': course,
                'year_of_study': str(year_of_study),
                'cgpa': cgpa,
                'depression': 1 if depression == "Yes" else 0,
                'anxiety': 1 if anxiety == "Yes" else 0,
                'panic_attack': 1 if panic_attack == "Yes" else 0,
                'treatment': 1 if treatment == "Yes" else 0
            }


            input_df = pd.DataFrame([input_dict])
            input_encoded = pd.get_dummies(input_df, drop_first=True)

            for col in model_columns:
                if col not in input_encoded.columns:
                    input_encoded[col] = 0

            input_encoded = input_encoded[model_columns]
            prediction = model.predict(input_encoded)[0]
            probability = model.predict_proba(input_encoded)[0][1]

            st.session_state.update({
                "prediction": prediction,
                "probability": probability,
                "assessment_data": input_dict,
                "submitted": True
            })
            st.write(f"🧠 Model prediction: {prediction} (1 = At risk, 0 = Low risk)")

            if prediction == 0:
                st.success(f"""
                ## Low Risk of Mental Health Issues
                **Probability of being at risk:** {probability * 100:.1f}%
                
                Great! You seem to be maintaining good mental balance. Keep up your healthy habits!
                """)
            else:
                st.error(f"""
                ## ⚠️ At Risk of Mental Health Issues
                **Probability of being at risk:** {probability * 100:.1f}%
                
                Our AI model suggests you might be experiencing mental strain. Please check the 'Solutions' tab for guidance.
                """)

            st.markdown("### Risk Probability")
            st.progress(float(probability))
            show_results = True

        except Exception as e:
            st.error(f"Error processing assessment: {str(e)}")


    # Footer
    st.markdown("""
    <div class="footer">
        <p>© 2025 Student Wellness Project | Made with ❤️ for Students</p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
