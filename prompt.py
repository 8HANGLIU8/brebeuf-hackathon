from openai import OpenAI
import os

client = OpenAI(api_key=os.environ['API_KEY'])

import os


def get_response(messages):
    """
    Sends the message history to ChatGPT and gets a response.
    
    :param messages: List of messages including the conversation history and prefixed prompt.
    :return: ChatGPT's response.
    """
    try:
        # Call the OpenAI API to generate a chat completion
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Corrected model name
            messages=messages
        )

        # Extract the response content
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"


def main():
    # Prefixed prompt to guide ChatGPT
    prefixed_prompt = '''
Improve the quality of a student's questions asked below using these conditions:
If question seems to be asking for definition
Then answer with definition

If question seems to be subjective 
ask if user wants to send their message to the mentor. send if they say yes.

If question seem to consist of multiple questions
Then split the questions and ask user for specific questions that wants to be asked

If the question consists of multiple parts, 
then ask a context specific question to the user for them to specify what they want to know

If question is too broad, general, or too philosophic
Then ask for specifications about the subject 

If question is objective, easily answered, non opinionated
Then reformulate the question to reword it to fit the mentor

If question is non specific for a mentor of their specific job, non job experience related
Then discard question, question should not be asked

If question is in FAQ section
Then give the answer directly from FAQ

Else user is eligible to ask this question to mentor
Let user know that their question is well formulated and is sent to the mentor

if question sent to mentor
do not suggest a better way to formulate the question

at the end suggeest a better way to formulate the question and ask if the user wants to send the question anyway to their mentor

The question is: 
'''

    # Initialize the conversation history with the prefixed prompt
    messages = [
        {"role": "system", "content": prefixed_prompt}
    ]

    print("Gatekeeper: Hello! I will perfect your question for the best feedback possible. Type 'q' to quit.")

    while True:
        # Get user input
        user_input = input("You: ")

        # Check if the user wants to quit
        if user_input.lower() == 'q':
            print("Gatekeeper: Goodbye!")
            break

        # Add the user's input to the conversation
        messages.append({"role": "user", "content": user_input})

        # Get the response from ChatGPT
        response = get_response(messages)

        # Output ChatGPT's response
        print(f"Gatekeeper: {response}")

        # Add the assistant's response to the conversation history
        messages.append({"role": "assistant", "content": response})


if __name__ == "__main__":
    main()

