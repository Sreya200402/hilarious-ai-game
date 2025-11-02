import random
import time

# -------------------------
# 100+ Sarcastic Punchlines
# -------------------------

coding_jokes = [
    "'{}'? Did you debug or just pray? 🙏🤣",
    "'{}'? Your loops are scarier than Tollywood horror 😱",
    "'{}'? Even ChatGPT laughed at this 😏",
    "'{}'? Variables called… they want a raise 😡",
    "'{}'? Did you just import chaos? 🤯",
    "'{}'? Stop copying from ChatGPT 😝🤣",
    "'{}'? StackOverflow unsubscribed from you 🤣",
    "'{}'? Did a potato teach you coding? 🥔🤣",
    "'{}'? Your indentation could scare a ghost 👻",
    "'{}'? Did you declare a bug as a feature? 😆",
    "'{}'? Even my cat could code better 🐱😂",
    "'{}'? Did you mean while True or while confuse? 😵",
    "'{}'? My grandma can debug faster 😝",
    "'{}'? Are you sure your code is not a meme? 🤪",
    "'{}'? Function called, it wants a vacation 😏",
    "'{}'? Your print statements cried last night 😭",
    "'{}'? Did you commit this in a fit of rage? 😡",
    "'{}'? Git refused your push 🤣",
    "'{}'? Infinite loop detected… of sarcasm 😎",
    "'{}'? Your code summoned a demon 🐲😱",
]

movies_jokes = [
    "'{}'? Even DJ Tillu would facepalm 🤣",
    "'{}'? Bigger plot twist than any Tollywood climax 😝",
    "'{}'? Brahmanandam called… he wants his scene back 😏",
    "'{}'? Is this a movie or a comedy reality show? 😂",
    "'{}'? Did villains write this scene? 😎",
    "'{}'? Tollywood scripts called… they want their plot twist back 🤣",
    "'{}'? Scene so bad, popcorn left me alone 🍿😂",
    "'{}'? Director cried seeing this 🤣",
    "'{}'? This scene broke the physics of humor 😵",
    "'{}'? DJ Tillu would quit acting after this 😝",
    "'{}'? Hero would retire just to avoid this scene 😏",
    "'{}'? Villains laughed harder than audience 😂",
    "'{}'? This deserves a sequel of sarcasm 🤪",
    "'{}'? Tollywood scripts are scared 😱",
    "'{}'? I feel like calling Brahmanandam for commentary 🤣",
    "'{}'? Is this a plot or a prank? 😆",
    "'{}'? Even background dancers laughed 😂",
    "'{}'? This deserves a comedy award 🏆🤣",
    "'{}'? Audience requested refund for logic 😏",
    "'{}'? Hero's punchline called sick leave 😝",
]

life_jokes = [
    "'{}'? OMG… my brain filed a complaint 🤯",
    "'{}'? Even aliens are laughing 👽🤣",
    "'{}'? Stop, the universe facepalmed 🤦‍♂️",
    "'{}'? Did your dog write this? 🐶😂",
    "'{}'? Genius… or not 😝",
    "'{}'? My grandma laughed at this 😂",
    "'{}'? History books will ignore this 🤪",
    "'{}'? Einstein rolled in his grave 😵",
    "'{}'? Stop, your ego is disturbing physics 😎",
    "'{}'? Universe is confused 🤯",
    "'{}'? Humans requested translation 😏",
    "'{}'? Your logic crashed reality 😡",
    "'{}'? Karma laughed at you 😂",
    "'{}'? Stop, even imagination is tired 😝",
    "'{}'? Mind called, it wants a break 🤪",
    "'{}'? Your pride broke the mirror 😱",
    "'{}'? Aliens debated about this 😂",
    "'{}'? This is how legends cringe 😎",
    "'{}'? Life itself facepalmed 🤦‍♂️",
    "'{}'? Your cleverness called a timeout 😏",
]

fun_jokes = [
    "'{}'? Even my cat could do better 🐱🤣",
    "'{}'? Are you serious? 😂",
    "'{}'? Hilarious idea 🤪",
    "'{}'? Stop joking 😡",
    "'{}'? Did a squirrel train you for this? 🐿️🤣",
    "'{}'? Epic fail… or genius? 😝",
    "'{}'? My imaginary friend laughed 🤣",
    "'{}'? Stop, the fun police called 😎",
    "'{}'? This could break the internet 😂",
    "'{}'? Joke registered in global sarcasm 🤪",
    "'{}'? Stop, even humor is exhausted 😵",
    "'{}'? Cat memes are jealous 🐱😂",
    "'{}'? I laughed… then cried 😭🤣",
    "'{}'? My coffee spit out in shock ☕😆",
    "'{}'? Fun level over 9000 🤯",
    "'{}'? Did someone feed you sarcasm? 😏",
    "'{}'? Universe requested replay 😂",
    "'{}'? Hilarious enough for TikTok 🤣",
    "'{}'? Even emojis are laughing 😝",
    "'{}'? Stop, this is legendary 🤪",
]

special_jokes = [
    "Teeth clip? Looks like you're ready to start a farm fencing business! 🐄",
    "With that teeth clip, you could wire the whole village! ⚡",
    "Teeth clip? DIY satellite dish detected! 📡",
    "Your driving? Even your car is scared 🚗😂",
    "Eve teasing? Bro, sarcasm level 100 😏🤣",
    "Car drift? Did physics quit on you? 🚗😵",
    "Teeth clip? Farm animals requested help 🐄🤣",
    "Driving like '{}'? Even GPS cried 😭",
    "Eve teasing alert? Sarcasm level critical 😎",
    "Car? Engine wants therapy 🚗😝",
]

# -------------------------
# Follow-ups / Callbacks
# -------------------------
followups = [
    "Haha… still saying '{}'? Really? 🤪",
    "Sure sure… keep telling me '{}', I believe you… not 😏",
    "'{}'? Stop, even my imaginary friend is judging 😝",
    "Remember when you said '{}'? Classic! 😂",
]

# -------------------------
# Keywords for topics
# -------------------------
topic_keywords = {
    "coding": ["python", "code", "function", "loop", "variable", "git", "commit", "debug", "homework", "chatgpt"],
    "movies": ["movie", "tollywood", "dj tillu", "brahmanandam", "scene", "plot"],
    "life": ["proud", "clever", "smart", "achievement", "school", "love", "hate"],
    "fun": ["fun", "hilarious", "laugh", "random", "joke"],
    "special": ["teeth clip", "car", "eve teasing"]
}

joke_categories = {
    "coding": coding_jokes,
    "movies": movies_jokes,
    "life": life_jokes,
    "fun": fun_jokes,
    "special": special_jokes
}

conversation_memory = []

# -------------------------
# Detect topics
# -------------------------
def detect_topics(user_input):
    lower_input = user_input.lower()
    detected = []
    for topic, keywords in topic_keywords.items():
        for kw in keywords:
            if kw in lower_input and topic not in detected:
                detected.append(topic)
    if not detected:
        detected.append("fun")
    return detected

# -------------------------
# Pick a dynamic joke
# -------------------------
def choose_joke(user_input):
    topics = detect_topics(user_input)
    topic = random.choice(topics)
    joke = random.choice(joke_categories[topic])
    
    # Fill placeholders
    if "{}" in joke:
        joke = joke.format(user_input)
    
    # Occasionally add a callback to previous input
    if conversation_memory and random.random() < 0.3:
        last_input = conversation_memory[-1]
        joke += " " + random.choice(followups).format(last_input)
    
    return joke

# -------------------------
# Main AI loop
# -------------------------
def ultimate_hilarious_ai():
    print("Welcome to **Ultimate Hilarious AI Punches** 🤣")
    print("Talk about coding, movies, life, fun, or anything!")
    print("Type 'quit' to exit.\n")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "quit":
            print("AI: Finally… some peace 😏👋")
            break
        
        joke = choose_joke(user_input)
        conversation_memory.append(user_input)
        
        # Add random emoji for natural hilarity
        emojis = ["😂","🤣","😏","🤪","😡","😆","😱"]
        joke += " " + random.choice(emojis)
        
        time.sleep(0.2)
        print(f"AI: {joke}\n")

# Run the AI
ultimate_hilarious_ai()
