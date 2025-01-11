import openai

# Set your OpenAI API key
API_KEY = "your_api_key_here"

def chat_with_gpt(initial_prompt, user_question):
    """
    Send an initial prompt and a user's question to ChatGPT.
    
    :param initial_prompt: The initial system-level prompt for GPT.
    :param user_question: The question from the user to add to the conversation.
    :return: The response from ChatGPT.
    """
    # Combine the initial prompt with the user's question
    messages = [
        {"role": "system", "content": initial_prompt},
        {"role": "user", "content": user_question},
    ]
    
    # Call the OpenAI API
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use your preferred GPT model
            messages=messages
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {e}"

def main():
    print("Welcome to ChatGPT Assistant!")
    
    # Get the initial prompt and user's question
    initial_prompt = input("Enter the initial prompt for ChatGPT: ")
    user_question = input("Enter your question for ChatGPT: ")
    
    # Get the response
    response = chat_with_gpt(initial_prompt, user_question)
    
    print("\nChatGPT's Response:")
    print(response)

if __name__ == "__main__":
    main()
