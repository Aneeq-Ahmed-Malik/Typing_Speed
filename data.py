import random

list = {
    "Easy":[
        "he", "she", "me", "you", "we", "they", "I", "him", "her", "us",
        "mine", "yours", "ours", "myself", "yourself", "ourselves",
        "his", "hers", "theirs", "who", "whom", "whose", "which", "what",
        "this", "that", "these", "those", "here", "there", "where", "when",
        "why", "how", "yes", "no", "please", "thank you", "sorry", "excuse me",
        "hello", "goodbye", "hi", "hey", "nice to meet you", "congratulations",
        "sorry", "pardon", "help", "understand", "explain", "clarify", "listen",
        "speak", "talk", "communicate", "express", "discuss", "chat", "converse",
        "interact", "engage", "address", "convey", "share", "ask", "answer",
        "question", "reply", "respond", "request", "inform", "notify", "announce",
        "tell", "state", "mention", "suggest", "advise", "recommend", "insist",
        "offer", "agree", "disagree", "argue", "debate", "persuade", "convince",
        "promise", "apologize", "thank", "appreciate", "encourage", "comfort",
        "support", "inspire", "motivate", "praise", "criticize", "compliment",
        "greet", "farewell", "introduce", "congratulate", "welcome", "apple",
        "banana", "cherry", "date", "elderberry", "fig", "grape",
        "honeydew", "imbe", "jackfruit", "kiwi", "lemon", "mango", "nectarine",
        "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine",
        "ugli", "vanilla", "watermelon", "xylocarp", "yellow", "zucchini",
        "ant", "bear", "cat", "dog", "elephant", "fox", "giraffe", "hippo",
        "iguana", "jaguar", "koala", "lion", "monkey", "newt", "octopus", "panda",
        "quokka", "rhino", "snake", "tiger", "unicorn", "vulture", "whale", "xerus",
        "yak", "zebra", "car", "bicycle", "train", "boat", "plane", "bus", "motorcycle",
        "truck", "helicopter", "submarine", "rocket", "tractor", "scooter", "van",
        "computer", "keyboard", "mouse", "monitor", "printer", "laptop", "tablet",
        "smartphone", "camera", "headphones", "speaker", "microphone", "router",
        "clock", "television", "lamp", "chair", "table", "couch", "bed", "book",
        "pen", "pencil", "paper", "scissors", "glue", "paint", "brush"
    ],
    "Medium" : {

    1: "In a world where technology plays a pivotal role in our lives, it is crucial to stay informed and adapt to "
       "new advancements. Embracing continuous learning is the key to staying relevant in this rapidly changing landscape.",
    2: "Collaboration is the cornerstone of success in many areas of life. By working together, leveraging diverse "
       "skills and perspectives, we can achieve greater outcomes than we could individually.",
    3: "Resilience is a quality that empowers individuals to overcome challenges and bounce back from setbacks. It is "
       "through resilience that we find the strength to persevere and reach our goals.",
    4: "Effective communication is essential for building strong relationships, resolving conflicts, and fostering "
       "understanding. By honing our communication skills, we can bridge gaps and connect with others on a deeper level.",
    5: "Empathy is the ability to understand and share the feelings of others. It allows us to connect with people on a "
       "human level, fostering compassion, and promoting a more inclusive and supportive society.",
    6: "Time management is a crucial skill for optimizing productivity and achieving a healthy work-life balance. "
       "By setting priorities, organizing tasks, and avoiding procrastination, we can make the most of our time.",
    7: "Innovation drives progress and fuels societal development. By encouraging creativity, embracing new ideas, and "
       "challenging the status quo, we can unlock breakthroughs and create positive change.",
    8: "Adaptability is the ability to adjust and thrive in changing circumstances. Those who embrace adaptability can "
       "navigate uncertainty with grace, seize new opportunities, and remain agile in an ever-evolving world.",
    9: "Integrity forms the foundation of trust and credibility. By upholding ethical principles, being honest and "
       "transparent in our actions, we build strong relationships and earn the respect of others.",
    10: "Lifelong learning is a mindset that empowers individuals to continually seek knowledge and expand their "
        "horizons. By embracing a thirst for knowledge, we can grow personally and professionally throughout our lives.",
    },
    "Hard": {

    1: "She said, 'I will be there at 9 a.m.' and asked me to bring three items: apples, bananas, and oranges. I did what "
       "she said me to do, and arrived at 10 a.m",
    2: "The meeting will take place on June 15th, 2023, at 2:30 p.m.; please be on time. Oh! but no one has a record of "
       "being on time, she said sadly",
    3: "He recited a famous quote from Shakespeare's Romeo and Juliet: 'What's in a name? That which we call a rose "
       "by any other name would smell as sweet.'",
    4: "The recipe requires 2 cups of flour, 1 teaspoon of salt, and 3 eggs; mix them well. This recipe will cost you "
       "on average $20 to $30 which is quite expensive!",
    5: "In a list of priorities, you should consider the following: health, education, family, and career. If you don't "
       "then remember, 'you shall see for yourself'",
    6: "The temperature today is expected to range from 25^C to 30^C; it will be a sunny day. Thank God!, he said. "
        "The temperature was not bearable till date!",
    7: "The code snippet should look like this: for i in range(10): print(i). Also, for more concise writing you may use "
       "list comprehension; [item + 'pie' for item in fruits]",
    8: "The document contains 10 pages; please review it and provide your feedback by tomorrow. Also, keep this in mind, "
       "if you don't do so you shall bear the unbearable!",
    9: "He wrote a message on the board: 'Please remember to bring your textbooks and notebooks.' and he as always "
       "forgot!. Thus, his anger was above the sky!",
    10: "The competition will start at 8:00 a.m., and the winners will receive cash prizes worth $500, $300, and $200 "
        "for the first, second, and third places, respectively."
    }
}

special_characters = {
    ",": "comma",
    ";": "semicolon",
    ":": "colon",
    "'": "apostrophe",
    "\"": "quotedbl",
    "!": "exclam",
    "?": "question",
    "(": "parenleft",
    ")": "parenright",
    "[": "bracketleft",
    "]": "bracketright",
    "{": "braceleft",
    "}": "braceright",
    "<": "less",
    ">": "greater",
    "*": "asterisk",
    "@": "at",
    "#": "numbersign",
    "$": "dollar",
    "%": "percent",
    "^": "asciicircum",
    "&": "ampersand",
    "+": "plus",
    "-": "minus",
    "/": "slash",
    "\\": "backslash",
    ".": "period",
    " ": "space"
}


class Data:
    def __init__(self):
        self.list = list


    def give_prompt(self, difficulty) -> str:

        prompts = self.list.get(difficulty)

        if prompts == None:
            return ""

        if len(prompts) > 12:
            return " ".join(random.choices(prompts, k=20))
        else:
            return random.choice(prompts)
