# (Secure Streamlit web interface)
import streamlit as st
import os
from main import LinkedInPostGenerator
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def main():
    st.title("LinkedIn Post Generator")
    st.write("Generate professional LinkedIn posts using AI")
    
    # Input fields
    topic = st.text_input("Enter post topic:", placeholder="AI in Healthcare")
    language = st.selectbox("Select language:", 
                           ["English", "Spanish", "French", "German", "Bengali", "Hindi", "Arabic"])
    
    # Get API configuration from environment variables
    endpoint = os.getenv("GITHUB_AI_ENDPOINT")
    token = os.getenv("GITHUB_AI_TOKEN")
    model = os.getenv("GITHUB_AI_MODEL", "xai/grok-3")
    
    # Allow manual override in sidebar (for testing, not recommended for production)
    with st.sidebar:
        st.header("API Configuration")
        st.info("Configure these in your .env file for security")
        endpoint_override = st.text_input("API Endpoint:", value=endpoint or "")
        token_override = st.text_input("API Token:", value="", type="password")
        model_override = st.text_input("Model:", value=model or "xai/grok-3")
    
    # Use override values if provided, otherwise use environment variables
    use_endpoint = endpoint_override if endpoint_override else endpoint
    use_token = token_override if token_override else token
    use_model = model_override if model_override else model
    
    if st.button("Generate Post"):
        if not topic:
            st.error("Please enter a topic")
            return
        
        if not use_endpoint or not use_token:
            st.error("API configuration missing. Please set up your .env file or enter credentials in the sidebar.")
            return
            
        try:
            # Set environment variables temporarily for this instance
            os.environ["GITHUB_AI_ENDPOINT"] = use_endpoint
            os.environ["GITHUB_AI_TOKEN"] = use_token
            os.environ["GITHUB_AI_MODEL"] = use_model
            
            generator = LinkedInPostGenerator()
            with st.spinner("Generating your post..."):
                post = generator.generate_post(topic, language)
            
            st.success("Post generated successfully!")
            st.text_area("Generated Post:", post, height=300)
            
            # Add download button
            st.download_button(
                label="Download Post",
                data=post,
                file_name=f"linkedin_post_{topic.replace(' ', '_')}.txt",
                mime="text/plain"
            )
                
        except Exception as e:
            st.error(f"Error generating post: {str(e)}")

if __name__ == "__main__":
    main()
