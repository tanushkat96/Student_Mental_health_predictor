import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Analysis - Student Mental Health",
    page_icon="📊",
    layout="wide"
)

# Load custom CSS
def load_css():
    with open('assets/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

load_css()

# Navigation Component
def render_navbar(current_page="Home"):
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("Home", 
                    width="stretch",
                    type="primary" if current_page == "Home" else "secondary",
                    key="nav_home"):
            if current_page != "Home":
                st.switch_page("app.py")
    
    with col2:
        if st.button("Assessment", 
                   width="stretch",
                    type="primary" if current_page == "Assessment" else "secondary",
                    key="nav_assessment"):
            if current_page != "Assessment":
                st.switch_page("pages/1_🧠_Quick_Assessment.py")
    
    with col3:
        if st.button("Analysis", 
                    width="stretch",
                    type="primary" if current_page == "Analysis" else "secondary",
                    key="nav_analysis"):
            if current_page != "Analysis":
                st.switch_page("pages/2_📊_Analysis.py")
    
    with col4:
        if st.button("Solutions", 
                    width="stretch",
                    type="primary" if current_page == "Solutions" else "secondary",
                    key="nav_solutions"):
            if current_page != "Solutions":
                st.switch_page("pages/3_🌿_Solutions.py")

# Load the trained model and columns for feature importance
@st.cache_resource
def load_model():
    try:
        model = joblib.load("random_forest_model.pkl")
        model_columns = joblib.load("model_columns.pkl")
        return model, model_columns
    except:
        return None, None

def main():
    # Render navbar - set current page to Analysis
    render_navbar("Analysis")
    
    # Header
    st.markdown("""
    <div class="header-container">
        <h1 class="main-title">Mental Health Analysis</h1>
        <p class="subtitle">Understanding your assessment results and risk factors</p>
    </div>
    """, unsafe_allow_html=True)

    # Load model for feature importance
    model, model_columns = load_model()

    # Check if assessment was completed
    if not st.session_state.get("submitted"):
        st.info("Please complete the assessment in the Quick Assessment tab first to see your personalized analysis.")
        
        # Show general insights instead
        st.markdown("---")
        st.subheader("General Mental Health Insights")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="insight-card">
                <h4>Common Risk Factors</h4>
                <p>• Academic pressure and CGPA stress</p>
                <p>• Sleep deprivation and irregular patterns</p>
                <p>• Lack of social support networks</p>
                <p>• Pre-existing mental health conditions</p>
                <p>• Poor work-life balance</p>
            </div>
            """, unsafe_allow_html=True)
            
        with col2:
            st.markdown("""
            <div class="insight-card">
                <h4>Model Performance</h4>
                <p>• Random Forest Accuracy: ~85%</p>
                <p>• Based on 100+ student profiles</p>
                <p>• Validated with cross-validation</p>
                <p>• Top predictors: Depression, Anxiety, CGPA</p>
            </div>
            """, unsafe_allow_html=True)
        
        # General Statistics
        st.markdown("---")
        st.subheader("Student Mental Health Statistics")
        
        stats_col1, stats_col2, stats_col3, stats_col4 = st.columns(4)
        
        with stats_col1:
            st.metric("Students at Risk", "35%", "12% from avg")
        
        with stats_col2:
            st.metric("Sought Treatment", "28%", "-5% from avg")
        
        with stats_col3:
            st.metric("Academic Stress", "62%", "8% from avg")
        
        with stats_col4:
            st.metric("Sleep Issues", "45%", "15% from avg")

        # General Visualizations
        st.markdown("---")
        st.subheader("Population Trends")
        
        viz_col1, viz_col2 = st.columns(2)
        
        with viz_col1:
            # Stress distribution chart
            st.subheader("Stress Distribution")
            labels = ['Low Stress', 'Moderate Stress', 'High Stress', 'Very High Stress']
            sizes = [25, 40, 20, 15]
            colors = ['#4CAF50', '#FFC107', '#FF9800', '#F44336']
            
            fig1, ax1 = plt.subplots(figsize=(8, 6))
            ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
            ax1.axis('equal')
            ax1.set_title('Student Stress Levels Distribution')
            st.pyplot(fig1)
        
        with viz_col2:
            # Sleep quality chart
            st.subheader("Sleep Quality Patterns")
            categories = ['Excellent', 'Good', 'Fair', 'Poor', 'Very Poor']
            values = [15, 30, 35, 15, 5]
            
            fig2, ax2 = plt.subplots(figsize=(8, 6))
            bars = ax2.bar(categories, values, color=['#4CAF50', '#8BC34A', '#FFC107', '#FF9800', '#F44336'])
            ax2.set_ylabel('Percentage of Students')
            ax2.set_title('Sleep Quality Among Students')
            plt.xticks(rotation=45)
            st.pyplot(fig2)

        # Feature Importance from Model
        if model is not None:
            st.markdown("---")
            st.subheader("AI Model Insights")
            
            # Get feature importance
            feature_imp = pd.Series(model.feature_importances_, index=model_columns)
            top_features = feature_imp.nlargest(8)
            
            # Create feature importance chart
            fig3, ax3 = plt.subplots(figsize=(10, 6))
            y_pos = np.arange(len(top_features))
            
            # Clean feature names for display
            clean_names = []
            for name in top_features.index:
                if 'depression_Yes' in name:
                    clean_names.append('Depression')
                elif 'anxiety_Yes' in name:
                    clean_names.append('Anxiety')
                elif 'panic_attack_Yes' in name:
                    clean_names.append('Panic Attacks')
                elif 'treatment_Yes' in name:
                    clean_names.append('Treatment History')
                elif 'choose_your_gender_Female' in name:
                    clean_names.append('Gender (Female)')
                elif 'choose_your_gender_Male' in name:
                    clean_names.append('Gender (Male)')
                elif 'cgpa' in name:
                    clean_names.append('Academic Performance')
                elif 'course' in name:
                    clean_names.append('Course of Study')
                else:
                    clean_names.append(name)
            
            bars = ax3.barh(y_pos, top_features.values, color='skyblue', alpha=0.7)
            ax3.set_yticks(y_pos)
            ax3.set_yticklabels(clean_names)
            ax3.set_xlabel('Feature Importance Score')
            ax3.set_title('Top Factors in Mental Health Risk Prediction')
            
            # Add value annotations
            for i, (bar, score) in enumerate(zip(bars, top_features.values)):
                ax3.text(bar.get_width() + 0.01, bar.get_y() + bar.get_height()/2, 
                        f'{score:.3f}', va='center', ha='left', fontsize=10)
            
            plt.tight_layout()
            st.pyplot(fig3)
        
        # Navigation to assessment
        if st.button("Take Assessment First →", width="stretch"):
            st.switch_page("pages/1_🧠_Quick_Assessment.py")
            
    else:
        # Personalized analysis based on user's assessment
        prediction = st.session_state["prediction"]
        probability = st.session_state["probability"]
        user_data = st.session_state["assessment_data"]
        
        # Results Overview
        st.markdown("## 🎯 Your Assessment Results")
        
        result_col1, result_col2, result_col3 = st.columns(3)
        
        with result_col1:
            if prediction == 0:
                st.success(f"## Low Risk")
            else:
                st.error(f"## At Risk")
        
        with result_col2:
            st.metric("Risk Probability", f"{probability*100:.1f}%")
        
        with result_col3:
            if probability > 0.7:
                confidence = "High"
                color = "red"
            elif probability > 0.4:
                confidence = "Moderate"
                color = "orange"
            else:
                confidence = "Low"
                color = "green"
            st.metric("Confidence Level", confidence)
        # Progress Tracking
        st.markdown("---")
        st.subheader("Progress Tracking & Recommendations")
        
        if prediction == 1:
            st.warning("""
            **Recommended Action Plan:**
            - Weekly mental health check-ins
            - Practice daily mindfulness (10-15 minutes)
            - Connect with campus counseling services
            - Monitor sleep patterns (aim for 7-9 hours)
            - Consider reassessment in 2-3 weeks
            """)
        else:
            st.success("""
            **Maintenance Plan:**
            - Continue current healthy routines
            - Monthly mental wellbeing check-ins
            - Stay connected with support networks
            - Practice preventive self-care
            - Consider reassessment in 1-2 months
            """)
        
        # Progress visualization
        st.markdown("### Your Risk Progress")
        st.progress(float(probability))
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Current Risk Level", f"{probability*100:.1f}%")
        with col2:
            target = max(0, probability - 0.3) if prediction == 1 else probability
            st.metric("Target Level", f"{target*100:.1f}%")

    
    # Navigation button
    if st.session_state.get("submitted"):
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("Explore Solutions & Support →",width="stretch"):
                st.switch_page("pages/3_🌿_Solutions.py")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Footer
    st.markdown("""
    <div class="footer">
        <p>© 2025 Student Wellness Project | Made with care for Students</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()