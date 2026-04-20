#i do luv to make things and this is one of my first projects. Noor-E-Nazer is a chatbot that uses Google's Gemini API to generate responses. It is designed to be accurate and creative, and it can understand the context of the conversation. I hope you enjoy chatting with Noor-E-Nazer!

import google.generativeai as genai

# 1. Configure the library with your Gemini API key
genai.configure(api_key="Just add your api key for it to work")

# 2. Initialize the model (gemini-1.5-flash is the recommended model for fast text tasks)
model = genai.GenerativeModel('gemini-flash-latest')
def chat_with_gemini(prompt):
    # Gemini's method for generating text is very straightforward
    response = model.generate_content(prompt)
    return response.text.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        
        # Fixed the spelling of "quit" here
        if user_input.lower() in ["quit", "exit", "bye"]:
            break
            
        # Call the Gemini function
        response_text = chat_with_gemini(user_input)
        print("Noor-E-Nazer:", response_text)