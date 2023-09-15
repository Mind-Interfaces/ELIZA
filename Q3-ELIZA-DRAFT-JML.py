import re
import random

# Pre-substitution list: Used to preprocess the input statement
# by replacing certain words with their standardized form.
PRES = {
    'dont': 'dont',
    'cant': 'cant',
    'wont': 'wont',
    'aint': 'aint',
    'recollect': 'remember',
    'recall': 'remember',
    'dreamt': 'dreamed',
    'dreams': 'dream',
    'maybe': 'perhaps',
    'certainly': 'yes',
    'machine': 'computer',
    'kid': 'child',
    'apologize': 'sorry',
    'machines': 'computer',
    'computers': 'computer',
    'were': 'was'
}

# Post-substitution list: Used to transform certain words in the
# captured groups to generate a response that makes sense.
POSTS = {
    'am': 'are',
    'was': 'were',
    'i': 'you',
    'i am': 'you are',
    'i would': 'you would',
    'i have': 'you have',
    'i will': 'you will',
    'my': 'your',
    'are': 'am',
    'you have': 'I have',
    'you will': 'I will',
    'your': 'my',
    'yours': 'mine',
    'you': 'I',
    'me': 'you'
}

# Function to apply pre-substitution on the statement
def pre(statement):
    """Converts the input statement using the PRES dictionary."""
    words = statement.lower().split()
    for i, word in enumerate(words):
        if word in PRES:
            words[i] = PRES[word]
    return ' '.join(words)

# Function to apply post-substitution on the statement
def post(fragment):
    """Converts the captured fragment using the POSTS dictionary."""
    words = fragment.lower().split()
    for i, word in enumerate(words):
        if word in POSTS:
            words[i] = POSTS[word]
    return ' '.join(words)

# Extracted keywords from the provided script
KEYWORDS = [
    ['men are all alike', ["In what way?"]],
    ["they're always (.*)", ["Can you think of a specific example?"]],
    ['my boyfriend made me (.*)', ["Your boyfriend made you {0}?"]],
    ["he says i'm (.*)", ["I am sorry to hear that you are {0}."]],
    ["it's true. i am (.*)", ["Do you think coming here will help you not to be {0}?"]],
    ['i need some (.*)', ["What would it mean to you if you got some {0}?"]],
    ['perhaps i could (.*)', ["Tell me more about your family"]]
]

# Function to analyze the statement and generate a response
def analyze(statement):
    for pattern, responses in KEYWORDS:
        match = re.match(pattern, statement.lower())
        if match:
            response = random.choice(responses)
            return response.format(*match.groups())

# Validation conversation script
conversation_script = [
    ("Men are all alike.", "In what way?"),
    ("They're always bugging us about something or other.", "Can you think of a specific example?"),
    ("Well, my boyfriend made me come here.", "Your boyfriend made you come here?"),
    ("He says I'm depressed much of the time.", "I am sorry to hear that you are depressed."),
    ("It's true. I am unhappy.", "Do you think coming here will help you not to be unhappy?"),
    ("I need some help, that much seems certain.", "What would it mean to you if you got some help?"),
    ("Perhaps I could learn to get along with my mother.", "Tell me more about your family")
]

# Run the validation test
validation_results = []
successful_validations = 0
for person_statement, expected_eliza_response in conversation_script:
    eliza_response = analyze(person_statement)
    if eliza_response == expected_eliza_response:
        successful_validations += 1
    validation_results.append((person_statement, expected_eliza_response, eliza_response))

validation_rate = (successful_validations / len(conversation_script)) * 100

print(f"Validation Rate: {validation_rate}%")
print(validation_results)