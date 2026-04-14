import streamlit as st
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="Student Mental Health Predictor",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load custom CSS
def load_css():
    with open('assets/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

load_css()

# Navigation Component - Using Streamlit's page system
def render_navbar(current_page="Home"):
    # Create navigation using Streamlit buttons
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

# Load image
def load_image():
    try:
        image = Image.open("assets/student_mental.png")
        return image
    except:
        return None

# Main Home Page
def main():
    # Render navbar at the top
    render_navbar("Home")
    
    
    # Header
    st.markdown("""
    <div class="header-container">
        <h1 class="main-title">Student Mental Health Predictor</h1>
    </div>
    """, unsafe_allow_html=True)
    
    # Main content
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # Image section - Properly contained
       
        mental_health_image = load_image()
        if mental_health_image:
            st.image(mental_health_image,width="stretch", caption="Your Mental Health Matters")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Quote section - Properly contained
        st.markdown("""
        <p class="motivational-quote">"A healthy mind breeds success and peace."</p>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # CTA Button - Correct path
        if st.button('Take Quick Assessment', key='cta_button', width="stretch"):
            st.switch_page("pages/1_🧠_Quick_Assessment.py")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Footer
    st.markdown("""
    <div class="footer">
        <p>© 2025 Student Wellness Project | Made with care for Students</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()