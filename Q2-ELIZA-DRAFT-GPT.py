# Import required libraries
import re
import random

# Define ELIZA's vocabulary and rules based on the user-provided data
# Pre-substitution words
PRE_SUBSTITUTIONS = {
    "don't": "dont",
    "can't": "cant",
    "won't": "wont",
    "ain't": "aint",
    "recollect": "remember",
    "recall": "remember",
    "dreamt": "dreamed",
    "dreams": "dream",
    "maybe": "perhaps",
    "certainly": "yes",
    "machine": "computer",
    "machines": "computer",
    "computers": "computer",
    "were": "was",
    "you're": "you are",
    "it's": "it is",
    "i'm": "i am",
    "same": "alike",
    "identical": "alike",
    "equivalent": "alike"
}

# Post-substitution words
POST_SUBSTITUTIONS = {
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
    "me": "you"
}

# Keywords and responses
KEYWORDS = [
    (r"i need (.*)", ["Why do you need {0}?", "Would it really help you to get {0}?", "Are you sure you need {0}?"]),
    (r"why don'?t you ([^\?]*)\??", ["Do you really think I don't {0}?", "Perhaps eventually I will {0}.", "Do you really want me to {0}?"]),
    (r"why can'?t I ([^\?]*)\??", ["Do you think you should be able to {0}?", "If you could {0}, what would you do?", "I don't know -- why can't you {0}?", "Have you really tried?"]),
    (r"i can'?t (.*)", ["How do you know you can't {0}?", "Perhaps you could {0} if you tried.", "What would it take for you to {0}?"]),
    (r"i am (.*)", ["Did you come to me because you are {0}?", "How long have you been {0}?", "How do you feel about being {0}?"]),
    (r"i'?m (.*)", ["How does being {0} make you feel?", "Do you enjoy being {0}?", "Why do you tell me you're {0}?", "Why do you think you're {0}?"]),
    (r"are you ([^\?]*)\??", ["Why does it matter whether I am {0}?", "Would you prefer it if I were not {0}?", "Perhaps you believe I am {0}.", "I may be {0} -- what do you think?"]),
    (r"what (.*)", ["Why do you ask?", "How would an answer to that help you?", "What do you think?"]),
    (r"how (.*)", ["How do you suppose?", "Perhaps you can answer your own question.", "What is it you're really asking?"]),
    (r"because (.*)", ["Is that the real reason?", "What other reasons come to mind?", "Does that reason apply to anything else?", "If {0}, what else must be true?"]),
    (r"(.*) sorry (.*)", ["There are many times when no apology is needed.", "What feelings do you have when you apologize?"]),
    (r"hello(.*)", ["Hello... I'm glad you could drop by today.", "Hi there... how are you today?", "Hello, how are you feeling today?"]),
    (r"i think (.*)", ["Do you doubt {0}?", "Do you really think so?", "But you're not sure {0}?"]),
    (r"(.*) friend (.*)", ["Tell me more about your friends.", "When you think of a friend, what comes to mind?", "Why don't you tell me about a childhood friend?"]),
    (r"yes", ["You seem quite sure.", "OK, but can you elaborate a bit?"]),
    (r"(.*) computer(.*)", ["Are you really talking about me?", "Does it seem strange to talk to a computer?", "How do computers make you feel?", "Do you feel threatened by computers?"]),
    (r"(.*)\?", ["Why do you ask that?", "Please consider whether you can answer your own question.", "Perhaps the answer lies within yourself?", "Why don't you tell me?"]),
    (r"quit", ["Thank you for talking with me.", "Goodbye.", "I'm looking forward to our next session.", "Goodbye.  This was really a nice talk."]),
    (r"(.*)", ["I see.", "Very interesting.", "I see.  And what does that tell you?", "How does that make you feel?", "How do you feel when you say that?"])
]

def pre_substitution(statement):
    """Perform pre-substitution on the statement."""
    words = statement.lower().split()
    substituted_words = [PRE_SUBSTITUTIONS.get(word, word) for word in words]
    return ' '.join(substituted_words)

def post_substitution(statement):
    """Perform post-substitution on the statement."""
    words = statement.lower().split()
    substituted_words = [POST_SUBSTITUTIONS.get(word, word) for word in words]
    return ' '.join(substituted_words)

def analyze(statement):
    """Analyze the statement and generate a response."""
    # Apply pre-substitution to the statement
    pre_substituted_statement = pre_substitution(statement)

    # Check for a keyword match and generate a response
    for pattern, responses in KEYWORDS:
        match = re.search(pattern, pre_substituted_statement)
        if match:
            # Apply post-substitution to the matched groups
            post_substituted_groups = [post_substitution(group) for group in match.groups()]

            # Generate a response
            response = random.choice(responses).format(*post_substituted_groups)
            return response



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
for person_statement, expected_eliza_response in conversation_script:
    eliza_response = analyze(person_statement)
    validation_results.append((person_statement, expected_eliza_response, eliza_response))

print(validation_results)
