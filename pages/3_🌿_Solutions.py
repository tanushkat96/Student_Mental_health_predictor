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

def main():
    # Render navbar - set current page to Solutions
    render_navbar("Solutions")
    
    
    # Header
    st.markdown("""
    <div class="header-container">
        <h1 class="main-title">Mental Wellness Solutions</h1>
        <p class="subtitle">Practical strategies and resources for better mental health</p>
    </div>
    """, unsafe_allow_html=True)


    # Video Section
    st.markdown("---")
    st.subheader("Guided Practice Videos")
    
    video_col1, video_col2 = st.columns(2)
    
    with video_col1:
        st.markdown("""
        <div class="video-container">
            <h4>Yoga for Mental Health</h4>
            <iframe width="100%" height="250" src="https://www.youtube.com/embed/v7AYKMP6rOE" 
            frameborder="0" allowfullscreen></iframe>
            <p style="margin-top: 10px; color: #666;">Gentle yoga routine for stress relief and mental clarity</p>
        </div>
        """, unsafe_allow_html=True)
    
    with video_col2:
        st.markdown("""
        <div class="video-container">
            <h4>Guided Meditation</h4>
            <iframe width="100%" height="250" src="https://www.youtube.com/embed/inpok4MKVLM" 
            frameborder="0" allowfullscreen></iframe>
            <p style="margin-top: 10px; color: #666;">10-minute meditation for anxiety and stress reduction</p>
        </div>
        """, unsafe_allow_html=True)

    # Study Tips Section
    st.markdown("---")
    st.subheader("Academic Wellness Tips")
    
    tip_col1, tip_col2, tip_col3 = st.columns(3)
    
    with tip_col1:
        st.markdown("""
        <div class="tip-card">
            <h4>Time Management</h4>
            <p>Use Pomodoro technique: 25min study + 5min break</p>
            <ul style="text-align: left; margin-top: 10px;">
                <li>Create study schedule</li>
                <li>Prioritize tasks</li>
                <li>Avoid multitasking</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with tip_col2:
        st.markdown("""
        <div class="tip-card">
            <h4>Sleep Routine</h4>
            <p>Maintain consistent sleep schedule (7-9 hours)</p>
            <ul style="text-align: left; margin-top: 10px;">
                <li>Digital detox before bed</li>
                <li>Comfortable sleep environment</li>
                <li>Regular sleep-wake times</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with tip_col3:
        st.markdown("""
        <div class="tip-card">
            <h4>Healthy Nutrition</h4>
            <p>Balanced diet with regular meals and hydration</p>
            <ul style="text-align: left; margin-top: 10px;">
                <li>Eat brain-boosting foods</li>
                <li>Stay hydrated</li>
                <li>Limit caffeine intake</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # Social Connection Section
    st.markdown("---")
    st.subheader("Social & Emotional Support")
    
    social_col1, social_col2 = st.columns(2)
    
    with social_col1:
        st.markdown("""
        <div class="solution-card">
            <h4>Building Support Networks</h4>
            <ul>
                <li>Join student clubs and organizations</li>
                <li>Participate in campus events</li>
                <li>Connect with like-minded peers</li>
                <li>Maintain family connections</li>
                <li>Seek mentorship opportunities</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with social_col2:
        st.markdown("""
        <div class="solution-card">
            <h4>Communication Skills</h4>
            <ul>
                <li>Practice active listening</li>
                <li>Express feelings openly</li>
                <li>Set healthy boundaries</li>
                <li>Seek feedback constructively</li>
                <li>Develop conflict resolution skills</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
    # Footer
    st.markdown("""
    <div class="footer">
        <p>© 2025 Student Wellness Project | Made with care for Students</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()