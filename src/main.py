import openai
import os
from dotenv import load_dotenv
load_dotenv()

def get_chatgpt_response(user_input):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_input,
        max_tokens=1000,
        temperature=0.7,
        n=1,
        stop=None,
        timeout=15,
    )
    return response.choices[0].text.strip()

def physiotherapy_app():
    print("Welcome to the Physiotherapy App!\n")
    
    while True:
        user_input = input("Query: ")
        print()
        
        if not is_physiotherapy_question(user_input):
            print("Please keep your query limited to physiotherapy-related questions.")
            continue
        
        chatgpt_response = get_chatgpt_response(user_input)
        
        if chatgpt_response.startswith("Provide exercise:"):
            exercise_name = chatgpt_response.replace("Provide exercise:", "").strip()
            print("You can follow these:\n" + chatgpt_response)
        else:
            exercise_link = None
            print("You can follow these:\n" + chatgpt_response)
        
        break

def is_physiotherapy_question(user_input):
    keywords = ["physiotherapy", "exercise", "surgery", "operation", "recovery"]
    return any(keyword in user_input.lower() for keyword in keywords)

if __name__ == "__main__":
    # Configure OpenAI API credentials
    openai.api_key = os.getenv("OPENAI_API_KEY")

    # Start the physiotherapy app
    physiotherapy_app()
