
import re
import random

# This dictionary will hold the responses.
KEYWORDS = {
    "i need (.*)": ["Why do you need {0}?", "Would it really help you to get {0}?", "Are you sure you need {0}?"],
    "why dont you ([^\?]*)\??": ["Do you really think I don't {0}?", "Perhaps eventually I will {0}.", "Do you really want me to {0}?"],
    "why cant i ([^\?]*)\??": ["Do you think you should be able to {0}?", "If you could {0}, what would you do?", "I don't know -- why can't you {0}?", "Have you really tried?"],
    "i cant (.*)": ["How do you know you can't {0}?", "Perhaps you could {0} if you tried.", "What would it take for you to {0}?"],
    "i am (.*)": ["Did you come to me because you are {0}?", "How long have you been {0}?", "How do you feel about being {0}?"],
    "you are (.*)": ["Why do you think I am {0}?", "Does it please you to think that I am {0}?", "Perhaps you would like me to be {0}.", "Perhaps you're really talking about yourself?"],
    "i dont (.*)": ["Don't you really {0}?", "Why don't you {0}?", "Do you want to {0}?"],
    "i feel (.*)": ["Good, tell me more about these feelings.", "Do you often feel {0}?", "When do you usually feel {0}?", "When you feel {0}, what do you do?"],
    "i have (.*)": ["Why do you tell me that you've {0}?", "Have you really {0}?", "Now that you have {0}, what will you do next?"],
    "is there (.*)": ["Do you think there is {0}?", "It's likely that there is {0}.", "Would you like there to be {0}?"]
}

# This function will process the user's input and respond.
def analyze(statement):
    for pattern, responses in KEYWORDS.items():
        match = re.match(pattern, statement)
        if match:
            response = random.choice(responses)
            return response.format(*[g for g in match.groups()])
    return "I'm sorry, I don't understand."

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
validation_score = 0
for person_statement, expected_eliza_response in conversation_script:
    eliza_response = analyze(person_statement)
    if eliza_response == expected_eliza_response:
        validation_score += 1
    validation_results.append((person_statement, expected_eliza_response, eliza_response))

validation_score
