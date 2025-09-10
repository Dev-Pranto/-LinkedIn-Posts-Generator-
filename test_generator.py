from main import LinkedInPostGenerator

def test_generator():
    # Configuration
    endpoint = "https://models.github.ai/inference"
    token = "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"
    model = "xai/grok-3"
    
    generator = LinkedInPostGenerator(endpoint, token, model)
    
    # Test cases
    test_cases = [
        ("AI in Healthcare", "English"),
        ("Remote Work Productivity", "Spanish"),
        ("Climate Change Solutions", "Bengali")
    ]
    
    for topic, language in test_cases:
        print(f"\nTesting: {topic} in {language}")
        print("=" * 40)
        post = generator.generate_post(topic, language)
        print(post)
        print("\n" + "-" * 40)

if __name__ == "__main__":
    test_generator()
