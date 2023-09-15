import re
import random

# Dictionary of patterns and corresponding responses
patterns = {
    r'(.*)\bhello\b(.*)': ['Hello!', 'Hi there!', 'Greetings!'],
    r'(.*)\bbye\b(.*)': ['Goodbye!', 'Farewell!', 'Take care!'],
    r'(.*)\b(?:i\'?m|i am)\s(.*)': ['How do you do, %2?', 'Nice to meet you, %2!'],
    # Add more patterns and responses here
}

def eliza_chatbot():
    print("ELIZA: Hello, how can I help you today?")
    while True:
        user_input = input("User: ")
        if user_input.lower() == 'bye':
            print("ELIZA: Goodbye!")
            break
        else:
            response = generate_response(user_input)
            print("ELIZA:", response)

def generate_response(user_input):
    for pattern, responses in patterns.items():
        match = re.match(pattern, user_input.lower())
        if match:
            response = random.choice(responses)
            return re.sub(r'%(\d)', lambda m: match.group(int(m.group(1))), response)
    return "I'm sorry, I don't understand. Can you please rephrase?"

# Start the conversation with ELIZA
eliza_chatbot()
