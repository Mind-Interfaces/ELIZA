
# ELIZA Main Script

from eliza_keywords import KEYWORDS
import re
import random

# Function to apply pre-substitution on the statement
def pre(statement):
    words = statement.lower().split()
    for i, word in enumerate(words):
        if word in PRES:
            words[i] = PRES[word]
    return ' '.join(words)

# Function to apply post-substitution on the statement
def post(fragment):
    words = fragment.lower().split()
    for i, word in enumerate(words):
        if word in POSTS:
            words[i] = POSTS[word]
    return ' '.join(words)

# Function to analyze the statement and generate a response
def analyze(statement):
    pre_statement = pre(statement)
    for pattern, responses in KEYWORDS:
        match = re.match(pattern, pre_statement.rstrip(".!"))
        if match:
            response = random.choice(responses)
            return response.format(*[post(g) for g in match.groups()])
