import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class LinkedInPostGenerator:
    def __init__(self):
        # Get configuration from environment variables
        endpoint = os.getenv("GITHUB_AI_ENDPOINT")
        token = os.getenv("GITHUB_AI_TOKEN")
        model = os.getenv("GITHUB_AI_MODEL", "xai/grok-3")
        
        if not endpoint or not token:
            raise ValueError("Missing required environment variables: GITHUB_AI_ENDPOINT and GITHUB_AI_TOKEN")
        
        self.client = ChatCompletionsClient(
            endpoint=endpoint,
            credential=AzureKeyCredential(token),
        )
        self.model = model
        
        # Define the system message for professional LinkedIn content
        self.system_message = SystemMessage(
            "You are a professional content creator for LinkedIn. "
            "Create engaging, professional LinkedIn posts with the following requirements:\n"
            "1. Write in a professional yet engaging tone\n"
            "2. Structure the post with 2-4 paragraphs\n"
            "3. Include relevant hashtags at the end\n"
            "4. Ensure the content is appropriate for business professionals\n"
            "5. Write in the language specified by the user"
        )
    
    def generate_post(self, topic, language):
        """Generate a LinkedIn post based on topic and language"""
        try:
            # Create user message with the topic and language
            user_message = UserMessage(
                f"Create a LinkedIn post about '{topic}' in {language}."
            )
            
            # Get response from the API
            response = self.client.complete(
                messages=[self.system_message, user_message],
                temperature=0.7,  # Slightly lower temperature for more focused content
                top_p=0.9,
                model=self.model
            )
            
            return response.choices[0].message.content
        except Exception as e:
            return f"Error generating post: {str(e)}"

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the generator
        generator = LinkedInPostGenerator()
        
        # Get user input
        topic = input("Enter the topic for your LinkedIn post: ")
        language = input("Enter the language for your post (e.g., English, Bengali, Spanish): ")
        
        # Generate the post
        post = generator.generate_post(topic, language)
        
        print("\nGenerated LinkedIn Post:")
        print("=" * 50)
        print(post)
        
    except ValueError as e:
        print(f"Configuration error: {e}")
        print("Please make sure you've set up the .env file with your API credentials")
    except Exception as e:
        print(f"Unexpected error: {e}")
