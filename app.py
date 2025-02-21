import streamlit as st
import requests
from PIL import Image
import io

# FastAPI Backend URL
API_URL = "http://127.0.0.1:8000/predict/"

# Set page config
st.set_page_config(
    page_title="AgriDoctor",
    page_icon="🌿",
    layout="wide"
)

# ---------------------------
# Custom CSS for styling with output boxes
# ---------------------------
st.markdown("""
<style>
    body { 
        background-color: #f5f5f5; 
        font-family: 'Arial', sans-serif; 
        color: #222; 
    }
    .main-title { 
        color: #2F4F4F; 
        font-size: 3em; 
        font-weight: bold; 
        margin-bottom: 20px; 
    }
    .sub-title { 
        color: #444; 
        font-size: 2em; 
        margin-bottom: 30px; 
        font-weight: 500; 
    }
    .window { 
        background-color: #ffffff; 
        border-radius: 15px; 
        padding: 20px; 
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1); 
        margin-bottom: 20px; 
    }
    /* Overall output result card styling */
    .result-card { 
        background-color: rgba(76, 175, 80, 0.2); 
        border: 2px solid rgba(76, 175, 80, 0.4); 
        border-radius: 15px; 
        padding: 20px; 
        margin-top: 20px; 
        font-weight: bold; 
        color: #222;
    }
    /* Styling for each result item box */
    .result-item {
        background-color: rgba(76, 175, 80, 0.15);
        border: 1px solid rgba(76, 175, 80, 0.3);
        border-radius: 10px;
        padding: 10px;
        margin: 8px 0;
    }
    /* Social media links styling */
    .social-links a { 
        margin-right: 15px; 
        text-decoration: none; 
        font-size: 1.2em; 
        color: #444; 
    }
    .social-links a:hover { 
        color: #4CAF50; 
    }
    .footer { 
        text-align: center; 
        margin-top: 40px; 
        color: #777; 
        font-size: 1.3em; 
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------
# Header
# ---------------------------
st.markdown("<h1 class='main-title'>🌿 AgriDoctor</h1>", unsafe_allow_html=True)
st.markdown("<h2 class='sub-title'>Your plant health companion!</h2>", unsafe_allow_html=True)

# ---------------------------
# Project Description as Paragraph (HTML)
# ---------------------------
st.markdown("""
    <p>
        AgriDoctor helps identify plant diseases from photos and provides treatment advice. Upload an image to get instant diagnosis, treatment tips, and prevention methods for healthier plants.
    </p>
""", unsafe_allow_html=True)

# ---------------------------
# Sidebar
# ---------------------------
with st.sidebar:
    st.image(
        "https://img.freepik.com/free-photo/world-environment-day-arrangement-with-plant-stethoscope_23-2148494978.jpg?w=1380",
        use_container_width=True
    )
    st.title("About Us")
    st.markdown("""
    - 🔍Instant disease diagnosis
    - 🌱 Detailed treatment advice
    - 📊 Health tracking
    - 💡 Expert gardening tips
    """)
    
    # Follow Me section with additional links
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<h3>Follow Me</h3>", unsafe_allow_html=True)
    st.markdown("""
        <div class="social-links">
            <a href="https://instagram.com/yourprofile" target="_blank">Instagram</a>
            <a href="https://facebook.com/yourprofile" target="_blank">Facebook</a>
            <a href="https://github.com/yourprofile" target="_blank">GitHub</a>
            <a href="https://yourportfolio.com" target="_blank">MyPortfolio</a>
            <a href="https://linkedin.com/in/yourprofile" target="_blank">LinkedIn</a>
             <a href=" https://x.com/bhuwansinghh" target="_blank">Twitter(X)</a>
           
        </div>
    """, unsafe_allow_html=True)

# ---------------------------
# Main Content Window
# ---------------------------
st.markdown("<div class='window'>", unsafe_allow_html=True)
st.subheader("Upload a photo for analysis")
uploaded_file = st.file_uploader("Choose an image...", type=['png', 'jpg', 'jpeg'])
st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------
# Analysis and Results
# ---------------------------
if uploaded_file:
    # Display the uploaded image
    st.markdown("<div class='window'>", unsafe_allow_html=True)
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Analysis button and results container
    st.markdown("<div class='window'>", unsafe_allow_html=True)
    if st.button("Analyze Plant"):
        with st.spinner("Analyzing..."):
            try:
                # Prepare image for API
                img_byte_arr = io.BytesIO()
                image.save(img_byte_arr, format='JPEG')
                img_byte_arr = img_byte_arr.getvalue()

                # API request
                response = requests.post(API_URL, files={"file": img_byte_arr})
                if response.status_code == 200:
                    result = response.json()
                    disease_info = result.get("disease_info", {})

                    # Display results in a green output box
                    st.markdown("<div class='result-card'>", unsafe_allow_html=True)
                    st.success("Analysis Complete!")
                    
                    # Disease name header
                    disease_name = disease_info.get("Disease_Name", "N/A")
                    st.markdown(f"<h1>🦠 Detected: {disease_name}</h1>", unsafe_allow_html=True)
                    
                    # Occurrence as h3 with emoji
                    occurrence = disease_info.get("Percentage_Occurrence", "N/A")
                    st.markdown(f"<div class='result-item'><h4>📊 Occurrence: {occurrence}</h4></div>", unsafe_allow_html=True)
                    
                    # Reason as h2 with emoji
                    reason = disease_info.get("Reason", "N/A")
                    st.markdown(f"<div class='result-item'><h3>⚠️ Reason: {reason}</h3></div>", unsafe_allow_html=True)
                    
                    # Cure as h2 with emoji
                    cure = disease_info.get("Cure", "N/A")
                    st.markdown(f"<div class='result-item'><h3>💊 Cure: {cure}</h3></div>", unsafe_allow_html=True)
                    
                    # Symptoms as h2 with emoji
                    symptoms = disease_info.get("Symptoms", "N/A")
                    st.markdown(f"<div class='result-item'><h3>🤒 Symptoms: {symptoms}</h3></div>", unsafe_allow_html=True)
                    
                    # Prevention as h2 with emoji
                    prevention = disease_info.get("Prevention", "N/A")
                    st.markdown(f"<div class='result-item'><h3>🛡️ Prevention: {prevention}</h3></div>", unsafe_allow_html=True)
                    
                    st.markdown("</div>", unsafe_allow_html=True)
                else:
                    st.error("Failed to analyze. Please try again.")
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------
# Footer
# ---------------------------
st.markdown("<div class='footer'>Developed with ❤️ by AgriDoctor</div>", unsafe_allow_html=True)
