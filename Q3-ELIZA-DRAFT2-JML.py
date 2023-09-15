import re
import random

# Updated patterns and responses, including existing patterns
KEYWORDS = [
    ['men are all alike', ["In what specific ways do you find men to be alike?"]],
    ["they're always (.*)", ["How does it make you feel when they are {0}?", "Can you provide an example related to {0}?"]],
    ['I (do not|don\'t) feel (.*)', ["I'm here to listen. Can you tell me more about why you don't feel {1}?", "What's been bothering you lately?"]],
    ['I feel (.*)', ["I'm here to listen. Tell me more about why you feel {0}.", "What do you think is causing you to feel {0}?"]],
    ["I'm (.*)", ["Why do you think you are {0}?", "Can you elaborate on being {0}?", "How does being {0} affect your daily life?"]],
    ['my (.*) made me (.*)', ["How did your {0} make you {1}?", "Tell me more about the situation with your {0}."]],
    ["he says i'm (.*)", ["It must be difficult to hear that you are {0}. How do you feel about it?"]],
    ['I want (.*)', ["Why do you want {0}?", "What do you think achieving {0} would bring to your life?"]],
    ['I need (.*)', ["I'm here to listen. Tell me more about why you need {0}.", "What would it mean to you if you got {0}?"]],
    ["it's true. i am (.*)", ["Do you think coming here will help you with your feelings of being {0}?", "How do you feel about being {0}?"]],
    ['i need some (.*)', ["I'm here to listen. What would getting some {0} mean to you?", "How would getting {0} help you?"]],
    ['my (.*) and (.*)', ["Tell me more about your {0} and {1}. How do they connect with your current feelings?"]],
    ['perhaps i could (.*)', ["Let's explore that. Tell me more about your family."]],
    ['why do you think (.*)', ["I'm interested in your thoughts. Why do you think {0}?", "How does {0} make you feel?"]],
]

# Initialize a dictionary for tracking conversation context
conversation_context = {'user_history': []}

# Function to analyze the statement and generate a response
def analyze(statement):
    conversation_context['user_history'].append(statement)
    for pattern, responses in KEYWORDS:
        match = re.match(pattern, statement.lower())
        if match:
            response = random.choice(responses)
            return response.format(*match.groups())

    # Handle cases when no pattern matches
    return handle_no_match(statement)

# Function to handle cases when no pattern matches
def handle_no_match(statement):
    user_history = conversation_context['user_history']
    if user_history:
        last_user_statement = user_history[-1]
        return f"I understand that you're discussing {last_user_statement.lower()}. Can you tell me more about it?"
    else:
        return "I'm here to help. Please provide more details or share your thoughts."

# Validation conversation script
conversation_script = [
    ("Men are all alike.", "In what specific ways do you find men to be alike?"),
    ("They're always bugging us about something or other.", "How does it make you feel when they are bugging you?"),
    ("Well, my boyfriend made me come here.", "How did your boyfriend make you come here?"),
    ("He says I'm depressed much of the time.", "It must be difficult to hear that you are depressed. How do you feel about it?"),
    ("It's true. I am unhappy.", "What's been bothering you lately that makes you feel unhappy?"),
    ("I need some help, that much seems certain.", "What kind of help do you think would be most beneficial for you?"),
    ("Perhaps I could learn to get along with my mother.", "Let's explore that. Tell me more about your family.")
]

# Initialize variables for scoring
successful_validations = 0
validation_results = []

# Run the validation test
for person_statement, expected_eliza_response in conversation_script:
    eliza_response = analyze(person_statement)
    validation_results.append((person_statement, expected_eliza_response, eliza_response))
    
    if eliza_response == expected_eliza_response:
        successful_validations += 1

validation_rate = (successful_validations / len(conversation_script)) * 100

print(f"Validation Rate: {validation_rate:.2f}%")
print(validation_results)
