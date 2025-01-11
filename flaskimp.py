
from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os

# Initialize Flask app
app = Flask(__name__)

# Initialize OpenAI client
client = OpenAI(api_key=os.environ['API_KEY'])

# Prefixed prompt
PREFIXED_PROMPT = '''If question seems to be asking for definition
Then answer with definition

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
Let user know that their question was sent to the mentor

at the end suggeest a better way to formulate the question

The question is: 
'''

# Initialize the conversation history
conversation_history = [
    {"role": "system", "content": PREFIXED_PROMPT}
]

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

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    global conversation_history

    try:
        # Get user input
        user_input = request.form.get('user_input')
        if not user_input:
            return jsonify({"response": "Error: No input provided"}), 400

        # Add user's input to the conversation
        conversation_history.append({"role": "user", "content": user_input})

        # Get ChatGPT response
        response = get_response(conversation_history)

        # Add the assistant's response to the conversation
        conversation_history.append({"role": "assistant", "content": response})

        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"}), 500



if __name__ == "__main__":
    app.run(debug=True, port=5001, use_reloader=False)




"""
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    # Handle the chat logic here
    user_input = request.form.get('user_input', '')
    return jsonify({"response": f"You said: {user_input}"})

if __name__ == "__main__":
    app.run(debug=True)

"""