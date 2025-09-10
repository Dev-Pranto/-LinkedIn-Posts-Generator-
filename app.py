#  (Streamlit web interface)
import streamlit as st
from main import LinkedInPostGenerator

def main():
    st.title("LinkedIn Post Generator")
    st.write("Generate professional LinkedIn posts using AI")
    
    # Input fields
    topic = st.text_input("Enter post topic:", placeholder="AI in Healthcare")
    language = st.selectbox("Select language:", 
                           ["English", "Spanish", "French", "German", "Bengali", "Hindi", "Arabic"])
    
    # API configuration (in production, these would be environment variables)
    endpoint = st.sidebar.text_input("API Endpoint:", 
                                    value="https://models.github.ai/inference")
    token = st.sidebar.text_input("API Token:", 
                                 value="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", 
                                 type="password")
    model = st.sidebar.text_input("Model:", value="xai/grok-3")
    
    if st.button("Generate Post"):
        if not topic:
            st.error("Please enter a topic")
            return
            
        try:
            generator = LinkedInPostGenerator(endpoint, token, model)
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
