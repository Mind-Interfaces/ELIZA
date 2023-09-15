import re
import random

# Initialize the data structures based on the provided conversation scripts and transformation rules
KEYWORDS = [
    ['(.*) all alike', ["In what way?"]],
    ["(.*) bugging us (.*)", ["Can you think of a specific example?"]],
    ['my boyfriend (.*)', ["Your boyfriend made you come here?"]],
    ["depressed (.*)", ["I am sorry to hear that you are depressed."]],
    ["unhappy", ["Do you think coming here will help you not to be unhappy?"]],
    ["need some help", ["What would it mean to you if you got some help?"]],
    ["get along with my (.*)", ["Tell me more about your family"]],
]

PRES = {
    "don't": "dont",
    "can't": "cant",
    "won't": "wont",
}

POSTS = {
    "am": "are",
    "was": "were",
    "i": "you",
    "i'm": "you are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "are": "am",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "I",
    "me": "you",
}

# Helper function for pre-substitution
def pre_process(statement):
    words = statement.lower().split()
    return " ".join(PRES.get(word, word) for word in words)

# Helper function for post-substitution
def post_process(groups):
    return [POSTS.get(group, group) for group in groups]

# The analyze function performs the actual matching and transformation.
def analyze(statement):
    statement = pre_process(statement)
    for pattern, responses in KEYWORDS:
        match = re.match(pattern, statement.rstrip(".!"))
        if match:
            response = random.choice(responses)
            return response.format(*post_process(match.groups()))
    return "I don't understand."

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
score = 0
for person_statement, expected_eliza_response in conversation_script:
    eliza_response = analyze(person_statement)
    if eliza_response == expected_eliza_response:
        score += 1
    validation_results.append((person_statement, expected_eliza_response, eliza_response))

score, validation_results
