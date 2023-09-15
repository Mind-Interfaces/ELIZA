import re
import random

# Pre-substitution list
PRES = {
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
    "kid":"child",
    "apologize": "sorry",
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

# Post-substitution list
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
    "me": "you"
}

# Natural Language Toolkit: Keyword Pairs
KEYWORDS = [
    ['i desire (.*)', ["Why do you need {0}?", "Would it really help you to get {0}?", "Are you sure you need {0}?"]],
    ['(.*) juice (.*)', ["It's nice and sweet. It's a really good batch!", "I have blueberry juice, apple juice, lemon juice...", "It's really good. You're going to love it."]],
    ['(.*) i forget (.*)', ["Can you think of why you might forget {1}?", "Why can't you remember {1}?", "How often do you think of {1}?", "Does it bother you to forget that?", "Could it be a mental block?", "Are you generally forgetful?", "Do you think you are suppressing {1}?"]],
    ['(.*) did you forget (.*)', ["Why do you ask?", "Are you sure you told me?", "Would it bother you if I forgot {1}?", "Why should I recall {1} just now?", "Tell me more about {1}."]],
    ['(.*) name (.*)', ["I am not interested in names.", "I've told you before, I don't care about names -- please continue."]],
    ['why dont you ([^\?]*)\??', ["Do you really think I don't {0}?", "Perhaps eventually I will {0}.", "Do you really want me to {0}?"]],
    ['why cant i ([^\?]*)\??', ["Do you think you should be able to {0}?", "If you could {0}, what would you do?", "I don't know -- why can't you {0}?", "Have you really tried?"]],
    ['i cant (.*)', ["How do you know you can't {0}?", "Perhaps you could {0} if you tried.", "What would it take for you to {0}?"]],
    # DEBUG CONDITIONAL SYNON
    ['(.*) i am sad (.*)', ["I am sorry to hear that you are unhappy {1}.", "Do you think coming here will help you not to be depressed {1}?", "I'm sure it's not pleasant to be unhappy {1}.", "Can you explain what made you unhappy {1}?", "You sound really depressed.", "Do you feel inadequate because you are unhappy {1}?"]],
    ['i am (.*)', ["Did you come to me because you are {0}?", "How long have you been {0}?", "How do you feel about being {0}?"]],
    ['im (.*)', ["How does being {0} make you feel?", "Do you enjoy being {0}?", "Why do you tell me you're {0}?", "Why do you think you're {0}?"]],
    ['are you ([^\?]*)\??', ["Why does it matter whether I am {0}?", "Would you prefer it if I were not {0}?", "Perhaps you believe I am {0}.", "I may be {0} -- what do you think?", "Why are you interested in whether I am {0} or not ?", "Would you prefer if I weren't {0} ?", "Perhaps I am {0} in your fantasies.", "Do you sometimes think I am {0} ?", "Would it matter to you ?", "What if I were {0} ?"]],
    ['what (.*)', ["Why do you ask?", "How would an answer to that help you?", "What do you think?", "Does that question interest you?", "What is it you really want to know?", "Are such questions much on your mind?", "What answer would please you most?", "What comes to mind when you ask that?", "Have you asked such questions before?", "Have you asked anyone else?"]],
    ['how (.*)', ["How do you suppose?", "Perhaps you can answer your own question.", "What is it you're really asking?"]],
    ['because (.*)', ["Is that the real reason?", "What other reasons come to mind?", "Does that reason apply to anything else?", "If {0}, what else must be true?", "Is that the real reason?", "Don't any other reasons come to mind?", "Does that reason seem to explain anything else?", "What other reasons might there be?"]],
    ['(.*) sorry (.*)', ["There are many times when no apology is needed.", "Apologies are not necessary.", "I have told you that apologies are not required.",  "It did not bother me.  Please continue.", "What feelings do you have when you apologize?"]],
    ['hello(.*)', ["Hello... I'm glad you could drop by today.", "Hi there... how are you today?", "Hello, how are you feeling today?"]],
    ['i think (.*)', ["Do you doubt {0}?", "Do you really think so?", "But you're not sure {0}?"]],
    ['(.*) friend (.*)', ["Tell me more about your friends.", "When you think of a friend, what comes to mind?", "Why don't you tell me about a childhood friend?"]],
    ['yes', ["You seem quite sure.", "OK, but can you elaborate a bit?"]],
    ['(.*) computer(.*)', ["Are you really talking about me?", "Does it seem strange to talk to a computer?", "How do computers make you feel?", "Do you feel threatened by computers?"]],
    ['is it (.*)', ["Do you think it is {0}?", "Perhaps it's {0} -- what do you think?", "If it were {0}, what would you do?", "It could well be that {0}."]],
    ['it is (.*)', ["You seem very certain.", "If I told you that it probably isn't {0}, what would you feel?"]],
    ['can you ([^\?]*)\??', ["What makes you think I can't {0}?", "If I could {0}, then what?", "Why do you ask if I can {0}?"]],
    ['can i ([^\?]*)\??', ["Perhaps you don't want to {0}.", "Do you want to be able to {0}?", "If you could {0}, would you?"]],
    ['you are (.*)', ["Why do you think I am {0}?", "Does it please you to think that I am {0}?", "Perhaps you would like me to be {0}.", "Perhaps you're really talking about yourself?"]],
    ['youre (.*)', ["Why do you say I am {0}?", "Why do you think I am {0}?", "Are we talking about you, or me?"]],
    ['i dont (.*)', ["Don't you really {0}?", "Why don't you {0}?", "Do you want to {0}?"]],
    ['i feel (.*)', ["Good, tell me more about these feelings.", "Do you often feel {0}?", "When do you usually feel {0}?", "When you feel {0}, what do you do?"]],
    ['i have (.*)', ["Why do you tell me that you've {0}?", "Have you really {0}?", "Now that you have {0}, what will you do next?"]],
    ['i would (.*)', ["Could you explain why you would {0}?", "Why would you {0}?", "Who else knows that you would {0}?"]],
    ['is there (.*)', ["Do you think there is {0}?", "It's likely that there is {0}.", "Would you like there to be {0}?"]],
    ['my (.*)', ["I see, your {0}.", "Why do you say that your {0}?", "When your {0}, how do you feel?"]],
    ['you (.*)', ["We should be discussing you, not me.", "Why do you say that about me?", "Why do you care whether I {0}?"]],
    ['why (.*)', ["Why don't you tell me the reason why {0}?", "Why do you think {0}?"]],
    ['why dont you (.*)', ["Do you believe I do not {0}?", "Perhaps I will {0} in good time.", "Should you {0} yourself?", "You want me to {0}?"]],
    ['why cant i (.*)', ["Do you think you should be able to {0}?", "Do you want to be able to {0}?", "Do you believe this will help you to {0}?", "Have you any idea why you can't {0}?"]],
    ['everyone (.*)', ["Really, {0}?", "Surely not {0}.", "Can you think of anyone in particular?", "Who, for example?", "Are you thinking of a very special person?", "Who, may I ask?", "Someone special perhaps?", "You have a particular person in mind, yes?", "Who do you think you're talking about?"]],
    ['i want (.*)', ["What would it mean to you if you got {0}?", "Why do you want {0}?", "What would you do if you got {0}?", "If you got {0}, then what would you do?"]],
    ['(.*) mother (.*)', ["Tell me more about your mother.", "What was your relationship with your mother like?", "How do you feel about your mother?", "How does this relate to your feelings today?", "Good family relations are important."]],
    ['(.*) father (.*)', ["Tell me more about your father.", "How did your father make you feel?", "How do you feel about your father?", "Does your relationship with your father relate to your feelings today?", "Do you have trouble showing affection with your family?"]],
    ['(.*) child (.*)', ["Did you have close friends as a child?", "What is your favorite childhood memory?", "Do you remember any dreams or nightmares from childhood?", "Did the other children sometimes tease you?", "How do you think your childhood experiences relate to your feelings today?"]],
    ['am i (.*)', ["Do you believe you are {0}?", "Would you want to be {0}?", "Do you wish I would tell you you are {0}?", "What would it mean if you were {0}?"]],
    ['(.*) if (.*)', ["Do you think it's likely that {1}?", "Do you wish that {1}?", "What do you know about {1}?", "Really, if {1}?", "What would you do if {1}?", "But what are the chances that {1}?", "What does this speculation lead to?"]],
    ['(.*) always (.*)', ["Can you think of a specific example?", "When?", "What incident are you thinking of?", "Really, always?"]],
    ['(.*) alike', ["In what way?", "What resemblence do you see?", "What does that similarity suggest to you?", "What other connections do you see?", "What do you suppose that resemblence means?", "What is the connection, do you suppose?", "Could there really be some connection?", "How?"]],
    ['like', ["In what way?", "What resemblence do you see?", "What does that similarity suggest to you?", "What other connections do you see?", "What do you suppose that resemblence means?", "What is the connection, do you suppose?", "Could there really be some connection?", "How?"]],
    ['(.*) my family (.*)', ["Tell me more about your family.", "Who else in your family {1}?", "Your {0}?", "What else comes to your mind when you think of your {1}?"]],
    ['(.*) my (.*)', ["Your {1}?", "Why do you say your {1}?", "Is it important to you that your {1}?"]],
    ['(.*)?', ["Why do you ask that?", "Please consider whether you can answer your own question.", "Perhaps the answer lies within yourself?", "Why don't you tell me?"]],
    ['(.*)', ["Please tell me more.", "Let's change focus a bit... Tell me about your family.", "Can you elaborate on that?", "Why do you say that {0}?", "I see.", "Very interesting.", "{0}.", "I see.  And what does that tell you?", "How does that make you feel?", "How do you feel when you say that?", "I'm not sure I understand you fully.", "Please go on.", "What does that suggest to you?", "Do you feel strongly about discussing such things?", "That is interesting.  Please continue.", "Tell me more about that.", "Does talking about this bother you?"]],
]


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
