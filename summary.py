from huggingface_hub import InferenceClient
import re
import os
from settings import token

from huggingface_hub import InferenceClient



def summarize_email(email_text):
    """
    Summarizes an email using HuggingFace's inference endpoint.
    
    Args:
        email_text (str): The full email text to summarize
        
    Returns:
        str: A concise summary of the email
    """
    # Initialize HuggingFace client
    client = InferenceClient(
        provider="hf-inference",
        api_key=token
    )
    # Clean the email text
    cleaned_text = re.sub(r'\s+', ' ', email_text).strip()
    
    # Create the prompt
    prompt = f"""Please summarize the following email concisely, focusing on:
    1. Main topic/purpose
    2. Key points
    3. Any required actions
    
    Email:
    {cleaned_text}
    """
    
    try:
        # Make API call to HuggingFace

        response = client.summarization(prompt,
            model="facebook/bart-large-cnn",
        )
        
        # Return the generated summary
        return response
        
    except Exception as e:
        return f"Error generating summary: {str(e)}"

def main():
    # Example usage
    email = """
    Dear Team,
    
    I hope this email finds you well. I wanted to follow up on the project timeline 
    for the Q4 deliverables. We need to ensure all reports are submitted by 
    December 15th, and the final presentation should be ready for review by 
    December 20th. Please let me know if you foresee any challenges meeting 
    these deadlines.
    
    Best regards,
    John
    """
    
    summary = summarize_email(email)
    print("\nEmail Summary:")
    print("-" * 50)
    print(summary)


if __name__ == "__main__":
    main()
