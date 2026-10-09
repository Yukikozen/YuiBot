# # # # import random
# # # # import re
# # # # from datetime import datetime

# # # # from memory import ChatMemory


# # # # class YuiBot:

# # # #     def __init__(self):

# # # #         self.memory = ChatMemory()

# # # #         # =====================================================
# # # #         # USER INFORMATION
# # # #         # =====================================================

# # # #         self.user_name = ""

# # # #         # =====================================================
# # # #         # RESPONSES
# # # #         # =====================================================

# # # #         self.responses = {

# # # #             "greeting": [
# # # #                 "Hello! How are you?",
# # # #                 "Hi! Nice to see you.",
# # # #                 "Hello! How can I help you?",
# # # #                 "Hey! What would you like to talk about?"
# # # #             ],

# # # #             "how_are_you": [
# # # #                 "I'm doing well! Thanks for asking.",
# # # #                 "I'm working normally.",
# # # #                 "I'm good! Ready to chat.",
# # # #                 "Everything is running normally."
# # # #             ],

# # # #             "thanks": [
# # # #                 "You're welcome!",
# # # #                 "No problem!",
# # # #                 "Glad I could help!",
# # # #                 "Anytime!"
# # # #             ],

# # # #             "goodbye": [
# # # #                 "Goodbye!",
# # # #                 "See you later!",
# # # #                 "Take care!",
# # # #                 "Bye! Have a great day!"
# # # #             ],

# # # #             "unknown": [
# # # #                 "I'm not sure how to answer that yet.",
# # # #                 "I don't know the answer to that yet.",
# # # #                 "I haven't learned how to answer that.",
# # # #                 "I'm still learning. Try asking something else.",
# # # #                 "I don't understand that yet."
# # # #             ]
# # # #         }

# # # #         # =====================================================
# # # #         # BUILT-IN KNOWLEDGE
# # # #         # =====================================================

# # # #         self.knowledge = {

# # # #             "what is your name":
# # # #                 "My name is YuiBot.",

# # # #             "who are you":
# # # #                 "I'm YuiBot, a rule-based chatbot written in Python.",

# # # #             "what are you":
# # # #                 "I'm a chatbot created using Python logic, keywords, patterns and stored knowledge.",

# # # #             "who created you":
# # # #                 "I was created as a custom Python chatbot project.",

# # # #             "what can you do":
# # # #                 "I can chat with you, remember information, perform calculations, tell you the date and time, and learn new responses.",

# # # #             "are you ai":
# # # #                 "I'm a chatbot, but I don't use an AI language model. My responses are generated using programmed rules and stored knowledge.",

# # # #             "do you use openai":
# # # #                 "No. I don't use OpenAI.",

# # # #             "do you use an ai model":
# # # #                 "No. I'm completely rule-based.",

# # # #             "what is python":
# # # #                 "Python is a popular programming language used for applications, automation, websites, data processing and many other projects.",

# # # #             "what is a chatbot":
# # # #                 "A chatbot is a program designed to communicate with users through text or speech.",

# # # #             "what is your purpose":
# # # #                 "My purpose is to demonstrate how a chatbot can be built using Python without relying on an external AI model."
# # # #         }

# # # #         # =====================================================
# # # #         # LOAD LEARNED KNOWLEDGE
# # # #         # =====================================================

# # # #         self.knowledge.update(
# # # #             self.memory.get_knowledge()
# # # #         )

# # # #     # =========================================================
# # # #     # MAIN RESPONSE FUNCTION
# # # #     # =========================================================

# # # #     def respond(self, message):

# # # #         original_message = message.strip()

# # # #         if not original_message:
# # # #             return "Please type something."

# # # #         message = original_message.lower().strip()

# # # #         # -----------------------------------------------------
# # # #         # TEACH COMMAND
# # # #         # -----------------------------------------------------

# # # #         if message.startswith("teach:"):

# # # #             return self.teach(
# # # #                 original_message
# # # #             )

# # # #         # -----------------------------------------------------
# # # #         # FORGET COMMAND
# # # #         # -----------------------------------------------------

# # # #         if message in [
# # # #             "forget everything",
# # # #             "forget all",
# # # #             "delete knowledge"
# # # #         ]:

# # # #             return self.forget_everything()

# # # #         # -----------------------------------------------------
# # # #         # EXIT
# # # #         # -----------------------------------------------------

# # # #         if message in [
# # # #             "exit",
# # # #             "quit",
# # # #             "close"
# # # #         ]:

# # # #             return "You can close the window when you're ready."

# # # #         # -----------------------------------------------------
# # # #         # HELP
# # # #         # -----------------------------------------------------

# # # #         if message in [
# # # #             "help",
# # # #             "/help"
# # # #         ]:

# # # #             return self.help_text()

# # # #         # -----------------------------------------------------
# # # #         # ABOUT
# # # #         # -----------------------------------------------------

# # # #         if message in [
# # # #             "about",
# # # #             "/about"
# # # #         ]:

# # # #             return (
# # # #                 "I'm YuiBot v1.0, a completely local "
# # # #                 "rule-based chatbot. I don't use OpenAI, "
# # # #                 "Ollama or any AI model."
# # # #             )

# # # #         # -----------------------------------------------------
# # # #         # CALCULATOR
# # # #         # -----------------------------------------------------

# # # #         calculation = self.try_calculation(
# # # #             original_message
# # # #         )

# # # #         if calculation is not None:
# # # #             return calculation

# # # #         # -----------------------------------------------------
# # # #         # TIME
# # # #         # -----------------------------------------------------

# # # #         if self.contains_any(
# # # #             message,
# # # #             [
# # # #                 "what time",
# # # #                 "current time",
# # # #                 "tell me the time",
# # # #                 "time now"
# # # #             ]
# # # #         ):

# # # #             return self.get_time()

# # # #         # -----------------------------------------------------
# # # #         # DATE
# # # #         # -----------------------------------------------------

# # # #         if self.contains_any(
# # # #             message,
# # # #             [
# # # #                 "what date",
# # # #                 "today's date",
# # # #                 "todays date",
# # # #                 "what day is it",
# # # #                 "current date"
# # # #             ]
# # # #         ):

# # # #             return self.get_date()

# # # #         # -----------------------------------------------------
# # # #         # REMEMBER NAME
# # # #         # -----------------------------------------------------

# # # #         name_result = self.detect_name(
# # # #             original_message
# # # #         )

# # # #         if name_result:

# # # #             self.user_name = name_result

# # # #             self.memory.set_user_name(
# # # #                 name_result
# # # #             )

# # # #             return (
# # # #                 f"Nice to meet you, {name_result}! "
# # # #                 "I'll remember your name."
# # # #             )

# # # #         # -----------------------------------------------------
# # # #         # ASK NAME
# # # #         # -----------------------------------------------------

# # # #         if self.contains_any(
# # # #             message,
# # # #             [
# # # #                 "what is my name",
# # # #                 "what's my name",
# # # #                 "do you know my name",
# # # #                 "who am i"
# # # #             ]
# # # #         ):

# # # #             saved_name = self.memory.get_user_name()

# # # #             if saved_name:

# # # #                 return (
# # # #                     f"Your name is {saved_name}."
# # # #                 )

# # # #             return (
# # # #                 "I don't know your name yet. "
# # # #                 "You can say: remember my name is John"
# # # #             )

# # # #         # -----------------------------------------------------
# # # #         # GREETING
# # # #         # -----------------------------------------------------

# # # #         if self.is_greeting(
# # # #             message
# # # #         ):

# # # #             return random.choice(
# # # #                 self.responses["greeting"]
# # # #             )

# # # #         # -----------------------------------------------------
# # # #         # HOW ARE YOU
# # # #         # -----------------------------------------------------

# # # #         if self.contains_any(
# # # #             message,
# # # #             [
# # # #                 "how are you",
# # # #                 "how are u",
# # # #                 "are you okay",
# # # #                 "are you good"
# # # #             ]
# # # #         ):

# # # #             return random.choice(
# # # #                 self.responses["how_are_you"]
# # # #             )

# # # #         # -----------------------------------------------------
# # # #         # THANKS
# # # #         # -----------------------------------------------------

# # # #         if self.contains_any(
# # # #             message,
# # # #             [
# # # #                 "thank you",
# # # #                 "thanks",
# # # #                 "thx"
# # # #             ]
# # # #         ):

# # # #             return random.choice(
# # # #                 self.responses["thanks"]
# # # #             )

# # # #         # -----------------------------------------------------
# # # #         # GOODBYE
# # # #         # -----------------------------------------------------

# # # #         if self.contains_any(
# # # #             message,
# # # #             [
# # # #                 "bye",
# # # #                 "goodbye",
# # # #                 "see you",
# # # #                 "see ya"
# # # #             ]
# # # #         ):

# # # #             return random.choice(
# # # #                 self.responses["goodbye"]
# # # #             )

# # # #         # -----------------------------------------------------
# # # #         # KNOWLEDGE SEARCH
# # # #         # -----------------------------------------------------

# # # #         knowledge_response = self.find_knowledge(
# # # #             message
# # # #         )

# # # #         if knowledge_response:

# # # #             return knowledge_response

# # # #         # -----------------------------------------------------
# # # #         # SIMPLE QUESTIONS
# # # #         # -----------------------------------------------------

# # # #         if message.endswith("?"):

# # # #             return (
# # # #                 "That's a question I haven't learned yet. "
# # # #                 "You can teach me using:\n\n"
# # # #                 "teach: your question = your answer"
# # # #             )

# # # #         # -----------------------------------------------------
# # # #         # UNKNOWN
# # # #         # -----------------------------------------------------

# # # #         return random.choice(
# # # #             self.responses["unknown"]
# # # #         )

# # # #     # =========================================================
# # # #     # GREETING DETECTION
# # # #     # =========================================================

# # # #     def is_greeting(self, message):

# # # #         greetings = [
# # # #             "hello",
# # # #             "hi",
# # # #             "hey",
# # # #             "good morning",
# # # #             "good afternoon",
# # # #             "good evening",
# # # #             "yo",
# # # #             "hiya"
# # # #         ]

# # # #         words = re.findall(
# # # #             r"\b[a-zA-Z]+\b",
# # # #             message
# # # #         )

# # # #         for greeting in greetings:

# # # #             if greeting in message:

# # # #                 if greeting in words:
# # # #                     return True

# # # #                 if message.startswith(
# # # #                     greeting + " "
# # # #                 ):
# # # #                     return True

# # # #         return False

# # # #     # =========================================================
# # # #     # KEYWORD CHECK
# # # #     # =========================================================

# # # #     def contains_any(
# # # #         self,
# # # #         message,
# # # #         keywords
# # # #     ):

# # # #         for keyword in keywords:

# # # #             if keyword in message:
# # # #                 return True

# # # #         return False

# # # #     # =========================================================
# # # #     # NAME DETECTION
# # # #     # =========================================================

# # # #     def detect_name(self, message):

# # # #         patterns = [

# # # #             r"remember my name is ([A-Za-z][A-Za-z0-9 _-]{1,30})",

# # # #             r"my name is ([A-Za-z][A-Za-z0-9 _-]{1,30})",

# # # #             r"call me ([A-Za-z][A-Za-z0-9 _-]{1,30})"

# # # #         ]

# # # #         for pattern in patterns:

# # # #             match = re.search(
# # # #                 pattern,
# # # #                 message,
# # # #                 re.IGNORECASE
# # # #             )

# # # #             if match:

# # # #                 name = match.group(1).strip()

# # # #                 name = name.rstrip(
# # # #                     ".!?"
# # # #                 )

# # # #                 return name

# # # #         return None

# # # #     # =========================================================
# # # #     # TIME
# # # #     # =========================================================

# # # #     def get_time(self):

# # # #         now = datetime.now()

# # # #         return (
# # # #             "The current time is "
# # # #             + now.strftime("%I:%M:%S %p")
# # # #             + "."
# # # #         )

# # # #     # =========================================================
# # # #     # DATE
# # # #     # =========================================================

# # # #     def get_date(self):

# # # #         now = datetime.now()

# # # #         return (
# # # #             "Today is "
# # # #             + now.strftime("%A, %d %B %Y")
# # # #             + "."
# # # #         )

# # # #     # =========================================================
# # # #     # CALCULATOR
# # # #     # =========================================================

# # # #     def try_calculation(
# # # #         self,
# # # #         message
# # # #     ):

# # # #         text = message.lower().strip()

# # # #         # -----------------------------------------------------
# # # #         # Remove common prefixes
# # # #         # -----------------------------------------------------

# # # #         prefixes = [
# # # #             "calculate",
# # # #             "what is",
# # # #             "what's",
# # # #             "solve",
# # # #             "compute"
# # # #         ]

# # # #         for prefix in prefixes:

# # # #             if text.startswith(prefix):

# # # #                 text = text[
# # # #                     len(prefix):
# # # #                 ].strip()

# # # #                 break

# # # #         # -----------------------------------------------------
# # # #         # Words to operators
# # # #         # -----------------------------------------------------

# # # #         replacements = {

# # # #             "plus": "+",
# # # #             "minus": "-",
# # # #             "times": "*",
# # # #             "multiplied by": "*",
# # # #             "divided by": "/",
# # # #             "divide by": "/"
# # # #         }

# # # #         for word, symbol in replacements.items():

# # # #             text = text.replace(
# # # #                 word,
# # # #                 symbol
# # # #             )

# # # #         # -----------------------------------------------------
# # # #         # Only allow safe calculator characters
# # # #         # -----------------------------------------------------

# # # #         if not re.fullmatch(
# # # #             r"[0-9\s\+\-\*\/\(\)\.%]+",
# # # #             text
# # # #         ):

# # # #             return None

# # # #         # Need an actual calculation
# # # #         if not re.search(
# # # #             r"[\+\-\*\/%]",
# # # #             text
# # # #         ):

# # # #             return None

# # # #         try:

# # # #             result = eval(
# # # #                 text,
# # # #                 {
# # # #                     "__builtins__": {}
# # # #                 },
# # # #                 {}
# # # #             )

# # # #             return (
# # # #                 f"The answer is {result}."
# # # #             )

# # # #         except Exception:

# # # #             return (
# # # #                 "I couldn't calculate that. "
# # # #                 "Try something like: calculate 25 + 10"
# # # #             )

# # # #     # =========================================================
# # # #     # KNOWLEDGE SEARCH
# # # #     # =========================================================

# # # #     def find_knowledge(
# # # #         self,
# # # #         message
# # # #     ):

# # # #         # Exact match first
# # # #         if message in self.knowledge:

# # # #             return self.knowledge[
# # # #                 message
# # # #             ]

# # # #         # Partial matching
# # # #         best_key = None
# # # #         best_score = 0

# # # #         for key in self.knowledge:

# # # #             key_words = set(
# # # #                 key.split()
# # # #             )

# # # #             message_words = set(
# # # #                 message.split()
# # # #             )

# # # #             common = key_words.intersection(
# # # #                 message_words
# # # #             )

# # # #             score = len(common)

# # # #             if score > best_score:

# # # #                 best_score = score
# # # #                 best_key = key

# # # #         if best_key and best_score >= 2:

# # # #             return self.knowledge[
# # # #                 best_key
# # # #             ]

# # # #         return None

# # # #     # =========================================================
# # # #     # TEACH
# # # #     # =========================================================

# # # #     def teach(
# # # #         self,
# # # #         original_message
# # # #     ):

# # # #         content = original_message[
# # # #             len("teach:"):
# # # #         ].strip()

# # # #         if "=" not in content:

# # # #             return (
# # # #                 "Teaching format:\n\n"
# # # #                 "teach: question = answer\n\n"
# # # #                 "Example:\n"
# # # #                 "teach: what is my favorite color = "
# # # #                 "Your favorite color is blue."
# # # #             )

# # # #         question, answer = content.split(
# # # #             "=",
# # # #             1
# # # #         )

# # # #         question = question.strip().lower()
# # # #         answer = answer.strip()

# # # #         if not question:

# # # #             return "The question cannot be empty."

# # # #         if not answer:

# # # #             return "The answer cannot be empty."

# # # #         self.knowledge[
# # # #             question
# # # #         ] = answer

# # # #         self.memory.save_knowledge(
# # # #             self.knowledge
# # # #         )

# # # #         return (
# # # #             "Got it! I've learned this:\n\n"
# # # #             f"Question: {question}\n"
# # # #             f"Answer: {answer}"
# # # #         )

# # # #     # =========================================================
# # # #     # FORGET EVERYTHING
# # # #     # =========================================================

# # # #     def forget_everything(self):

# # # #         self.knowledge = {}

# # # #         self.memory.clear_knowledge()

# # # #         return (
# # # #             "I've forgotten the custom knowledge "
# # # #             "you taught me."
# # # #         )

# # # #     # =========================================================
# # # #     # HELP
# # # #     # =========================================================

# # # #     def help_text(self):

# # # #         return (
# # # #             "Here are some things I understand:\n\n"

# # # #             "• hello\n"
# # # #             "• how are you?\n"
# # # #             "• what is your name?\n"
# # # #             "• what can you do?\n"
# # # #             "• what time is it?\n"
# # # #             "• what is today's date?\n"
# # # #             "• calculate 25 + 10\n"
# # # #             "• remember my name is John\n"
# # # #             "• what is my name?\n"
# # # #             "• teach: question = answer\n"
# # # #             "• forget everything\n"
# # # #             "• about\n"
# # # #             "• help\n\n"

# # # #             "You can teach me new responses with:\n\n"

# # # #             "teach: what is pizza = "
# # # #             "Pizza is a popular food."
# # # #         )


# # # import random
# # # import re
# # # import difflib
# # # from datetime import datetime

# # # from memory import ChatMemory


# # # class YuiBot:

# # #     def __init__(self):

# # #         self.memory = ChatMemory()

# # #         # =====================================================
# # #         # CURRENT CONTEXT
# # #         # =====================================================

# # #         self.last_intent = None

# # #         # =====================================================
# # #         # RESPONSE DATABASE
# # #         # =====================================================

# # #         self.responses = {

# # #             "greeting": [
# # #                 "Hello! How are you?",
# # #                 "Hi! Nice to see you.",
# # #                 "Hello! How can I help you?",
# # #                 "Hey! What would you like to talk about?",
# # #                 "Hi there!"
# # #             ],

# # #             "how_are_you": [
# # #                 "I'm doing well! Thanks for asking.",
# # #                 "I'm good and ready to chat.",
# # #                 "Everything is running normally.",
# # #                 "I'm doing great!"
# # #             ],

# # #             "thanks": [
# # #                 "You're welcome!",
# # #                 "No problem!",
# # #                 "Glad I could help!",
# # #                 "Anytime!",
# # #                 "You're very welcome."
# # #             ],

# # #             "goodbye": [
# # #                 "Goodbye!",
# # #                 "See you later!",
# # #                 "Take care!",
# # #                 "Bye! Have a great day!"
# # #             ],

# # #             "positive": [
# # #                 "That's great!",
# # #                 "Nice!",
# # #                 "I'm glad to hear that.",
# # #                 "Awesome!"
# # #             ],

# # #             "negative": [
# # #                 "I'm sorry to hear that.",
# # #                 "I hope things get better.",
# # #                 "That doesn't sound very good."
# # #             ],

# # #             "unknown": [
# # #                 "I'm not sure how to answer that yet.",
# # #                 "I haven't learned that yet.",
# # #                 "I don't know the answer to that.",
# # #                 "I'm still learning how to handle that.",
# # #                 "I don't understand that yet."
# # #             ]
# # #         }

# # #         # =====================================================
# # #         # BUILT-IN KNOWLEDGE
# # #         # =====================================================

# # #         self.knowledge = {

# # #             "what is your name":
# # #                 "My name is YuiBot.",

# # #             "who are you":
# # #                 "I'm YuiBot, a rule-based chatbot written entirely in Python.",

# # #             "what are you":
# # #                 "I'm a rule-based chatbot. I use programmed logic, patterns, keywords and stored knowledge instead of an AI language model.",

# # #             "who created you":
# # #                 "I was created as a custom Python chatbot project.",

# # #             "what can you do":
# # #                 "I can chat with you, remember information, recognize different types of questions, perform calculations, tell you the date and time, and learn custom answers.",

# # #             "are you ai":
# # #                 "I'm a chatbot, but I don't use an AI language model.",

# # #             "do you use openai":
# # #                 "No. I don't use OpenAI.",

# # #             "do you use ollama":
# # #                 "No. I don't use Ollama.",

# # #             "do you use llama":
# # #                 "No. I don't use Llama.",

# # #             "do you use qwen":
# # #                 "No. I don't use Qwen.",

# # #             "do you use a model":
# # #                 "No. YuiBot is completely rule-based and does not use a language model.",

# # #             "what is python":
# # #                 "Python is a programming language used for applications, automation, websites, data processing, games and many other projects.",

# # #             "what is a chatbot":
# # #                 "A chatbot is a computer program designed to communicate with people through text or speech.",

# # #             "what is programming":
# # #                 "Programming is the process of writing instructions that tell a computer what to do.",

# # #             "what is a computer":
# # #                 "A computer is an electronic device that processes data and performs instructions.",

# # #             "what is your purpose":
# # #                 "My purpose is to demonstrate how a chatbot can be built from scratch using Python without relying on an external AI model."
# # #         }

# # #         # Load custom knowledge

# # #         self.knowledge.update(
# # #             self.memory.get_knowledge()
# # #         )

# # #     # =========================================================
# # #     # MAIN RESPONSE
# # #     # =========================================================

# # #     def respond(self, original_message):

# # #         if not original_message:

# # #             return "Please type something."

# # #         original_message = original_message.strip()

# # #         message = self.normalize(
# # #             original_message
# # #         )

# # #         # -----------------------------------------------------
# # #         # TEACH
# # #         # -----------------------------------------------------

# # #         if message.startswith("teach:"):

# # #             return self.teach(
# # #                 original_message
# # #             )

# # #         # -----------------------------------------------------
# # #         # FORGET
# # #         # -----------------------------------------------------

# # #         if message in (
# # #             "forget everything",
# # #             "forget all",
# # #             "delete knowledge",
# # #             "clear knowledge"
# # #         ):

# # #             self.last_intent = "forget"

# # #             return self.forget_knowledge()

# # #         # -----------------------------------------------------
# # #         # HELP
# # #         # -----------------------------------------------------

# # #         if message in (
# # #             "help",
# # #             "/help",
# # #             "what can i ask you"
# # #         ):

# # #             self.last_intent = "help"

# # #             return self.help_text()

# # #         # -----------------------------------------------------
# # #         # ABOUT
# # #         # -----------------------------------------------------

# # #         if message in (
# # #             "about",
# # #             "/about",
# # #             "tell me about yourself"
# # #         ):

# # #             self.last_intent = "about"

# # #             return (
# # #                 "I'm YuiBot v2.0.\n\n"
# # #                 "I'm a completely local rule-based "
# # #                 "chatbot written in Python.\n\n"
# # #                 "I don't use OpenAI, Ollama, Llama, "
# # #                 "Qwen or any other AI model."
# # #             )

# # #         # -----------------------------------------------------
# # #         # NAME
# # #         # -----------------------------------------------------

# # #         name = self.extract_name(
# # #             original_message
# # #         )

# # #         if name:

# # #             self.memory.set_profile(
# # #                 "user_name",
# # #                 name
# # #             )

# # #             self.last_intent = "remember_name"

# # #             return (
# # #                 f"Nice to meet you, {name}! "
# # #                 "I'll remember your name."
# # #             )

# # #         # -----------------------------------------------------
# # #         # ASK USER NAME
# # #         # -----------------------------------------------------

# # #         if self.matches_intent(
# # #             message,
# # #             "ask_name"
# # #         ):

# # #             self.last_intent = "ask_name"

# # #             name = self.memory.get_profile(
# # #                 "user_name"
# # #             )

# # #             if name:

# # #                 return (
# # #                     f"Your name is {name}."
# # #                 )

# # #             return (
# # #                 "I don't know your name yet. "
# # #                 "You can say: my name is John"
# # #             )

# # #         # -----------------------------------------------------
# # #         # GREETING
# # #         # -----------------------------------------------------

# # #         if self.matches_intent(
# # #             message,
# # #             "greeting"
# # #         ):

# # #             self.last_intent = "greeting"

# # #             return random.choice(
# # #                 self.responses["greeting"]
# # #             )

# # #         # -----------------------------------------------------
# # #         # HOW ARE YOU
# # #         # -----------------------------------------------------

# # #         if self.matches_intent(
# # #             message,
# # #             "how_are_you"
# # #         ):

# # #             self.last_intent = "how_are_you"

# # #             return random.choice(
# # #                 self.responses["how_are_you"]
# # #             )

# # #         # -----------------------------------------------------
# # #         # THANKS
# # #         # -----------------------------------------------------

# # #         if self.matches_intent(
# # #             message,
# # #             "thanks"
# # #         ):

# # #             self.last_intent = "thanks"

# # #             return random.choice(
# # #                 self.responses["thanks"]
# # #             )

# # #         # -----------------------------------------------------
# # #         # GOODBYE
# # #         # -----------------------------------------------------

# # #         if self.matches_intent(
# # #             message,
# # #             "goodbye"
# # #         ):

# # #             self.last_intent = "goodbye"

# # #             return random.choice(
# # #                 self.responses["goodbye"]
# # #             )

# # #         # -----------------------------------------------------
# # #         # POSITIVE
# # #         # -----------------------------------------------------

# # #         if self.matches_intent(
# # #             message,
# # #             "positive"
# # #         ):

# # #             self.last_intent = "positive"

# # #             return random.choice(
# # #                 self.responses["positive"]
# # #             )

# # #         # -----------------------------------------------------
# # #         # NEGATIVE
# # #         # -----------------------------------------------------

# # #         if self.matches_intent(
# # #             message,
# # #             "negative"
# # #         ):

# # #             self.last_intent = "negative"

# # #             return random.choice(
# # #                 self.responses["negative"]
# # #             )

# # #         # -----------------------------------------------------
# # #         # TIME
# # #         # -----------------------------------------------------

# # #         if self.matches_intent(
# # #             message,
# # #             "time"
# # #         ):

# # #             self.last_intent = "time"

# # #             return self.get_time()

# # #         # -----------------------------------------------------
# # #         # DATE
# # #         # -----------------------------------------------------

# # #         if self.matches_intent(
# # #             message,
# # #             "date"
# # #         ):

# # #             self.last_intent = "date"

# # #             return self.get_date()

# # #         # -----------------------------------------------------
# # #         # CALCULATOR
# # #         # -----------------------------------------------------

# # #         calculation = self.calculate(
# # #             original_message
# # #         )

# # #         if calculation is not None:

# # #             self.last_intent = "calculator"

# # #             return calculation

# # #         # -----------------------------------------------------
# # #         # CONTEXT QUESTIONS
# # #         # -----------------------------------------------------

# # #         context_response = self.handle_context(
# # #             message
# # #         )

# # #         if context_response:

# # #             return context_response

# # #         # -----------------------------------------------------
# # #         # KNOWLEDGE
# # #         # -----------------------------------------------------

# # #         knowledge_response = self.search_knowledge(
# # #             message
# # #         )

# # #         if knowledge_response:

# # #             self.last_intent = "knowledge"

# # #             return knowledge_response

# # #         # -----------------------------------------------------
# # #         # QUESTION
# # #         # -----------------------------------------------------

# # #         if message.endswith("?"):

# # #             self.last_intent = "unknown_question"

# # #             return (
# # #                 "I don't know how to answer that yet.\n\n"
# # #                 "You can teach me using:\n"
# # #                 "teach: question = answer"
# # #             )

# # #         # -----------------------------------------------------
# # #         # UNKNOWN
# # #         # -----------------------------------------------------

# # #         self.last_intent = "unknown"

# # #         return random.choice(
# # #             self.responses["unknown"]
# # #         )

# # #     # =========================================================
# # #     # NORMALIZE
# # #     # =========================================================

# # #     def normalize(self, text):

# # #         text = text.lower().strip()

# # #         # Common texting shortcuts

# # #         replacements = {
# # #             "u": "you",
# # #             "ur": "your",
# # #             "r": "are",
# # #             "pls": "please",
# # #             "plz": "please",
# # #             "thx": "thanks",
# # #             "wat": "what",
# # #             "wut": "what",
# # #             "whats": "what is",
# # #             "whos": "who is",
# # #             "im": "i am",
# # #             "idk": "i do not know"
# # #         }

# # #         words = text.split()

# # #         result = []

# # #         for word in words:

# # #             clean = word.strip(
# # #                 ".,!?;:"
# # #             )

# # #             if clean in replacements:

# # #                 result.append(
# # #                     replacements[clean]
# # #                 )

# # #             else:

# # #                 result.append(
# # #                     word
# # #                 )

# # #         text = " ".join(result)

# # #         # Common typo corrections

# # #         typo_map = {
# # #             "helo": "hello",
# # #             "helllo": "hello",
# # #             "hii": "hi",
# # #             "heyy": "hey",
# # #             "namee": "name",
# # #             "wht": "what",
# # #             "whatt": "what",
# # #             "tim": "time",
# # #             "todai": "today",
# # #             "calcluate": "calculate",
# # #             "calculte": "calculate",
# # #             "helpme": "help"
# # #         }

# # #         for typo, correction in typo_map.items():

# # #             text = re.sub(
# # #                 rf"\b{re.escape(typo)}\b",
# # #                 correction,
# # #                 text
# # #             )

# # #         return text

# # #     # =========================================================
# # #     # INTENT DETECTION
# # #     # =========================================================

# # #     def matches_intent(
# # #         self,
# # #         message,
# # #         intent
# # #     ):

# # #         patterns = {

# # #             "greeting": [
# # #                 "hello",
# # #                 "hi",
# # #                 "hey",
# # #                 "good morning",
# # #                 "good afternoon",
# # #                 "good evening",
# # #                 "hiya",
# # #                 "yo"
# # #             ],

# # #             "how_are_you": [
# # #                 "how are you",
# # #                 "how are you doing",
# # #                 "are you okay",
# # #                 "are you good",
# # #                 "how do you feel"
# # #             ],

# # #             "thanks": [
# # #                 "thank you",
# # #                 "thanks",
# # #                 "thank you so much",
# # #                 "many thanks"
# # #             ],

# # #             "goodbye": [
# # #                 "bye",
# # #                 "goodbye",
# # #                 "see you",
# # #                 "see you later",
# # #                 "talk to you later"
# # #             ],

# # #             "positive": [
# # #                 "i am happy",
# # #                 "i'm happy",
# # #                 "i am good",
# # #                 "i'm good",
# # #                 "i feel great",
# # #                 "i am excited",
# # #                 "that's great",
# # #                 "that is great"
# # #             ],

# # #             "negative": [
# # #                 "i am sad",
# # #                 "i'm sad",
# # #                 "i feel bad",
# # #                 "i feel sad",
# # #                 "i am angry",
# # #                 "i'm angry",
# # #                 "i hate this"
# # #             ],

# # #             "time": [
# # #                 "what time is it",
# # #                 "what is the time",
# # #                 "current time",
# # #                 "time now",
# # #                 "tell me the time",
# # #                 "what time"
# # #             ],

# # #             "date": [
# # #                 "what date is it",
# # #                 "what is today's date",
# # #                 "what is todays date",
# # #                 "today's date",
# # #                 "todays date",
# # #                 "current date",
# # #                 "what day is it"
# # #             ],

# # #             "ask_name": [
# # #                 "what is my name",
# # #                 "what's my name",
# # #                 "what is my name?",
# # #                 "who am i",
# # #                 "do you know my name",
# # #                 "tell me my name",
# # #                 "can you remember my name"
# # #             ]
# # #         }

# # #         if intent not in patterns:

# # #             return False

# # #         for pattern in patterns[intent]:

# # #             if self.similar(
# # #                 message,
# # #                 pattern
# # #             ):

# # #                 return True

# # #         return False

# # #     # =========================================================
# # #     # FUZZY MATCHING
# # #     # =========================================================

# # #     def similar(
# # #         self,
# # #         text,
# # #         pattern
# # #     ):

# # #         if pattern in text:

# # #             return True

# # #         ratio = difflib.SequenceMatcher(
# # #             None,
# # #             text,
# # #             pattern
# # #         ).ratio()

# # #         if ratio >= 0.78:

# # #             return True

# # #         text_words = set(
# # #             text.split()
# # #         )

# # #         pattern_words = set(
# # #             pattern.split()
# # #         )

# # #         if not pattern_words:

# # #             return False

# # #         overlap = len(
# # #             text_words.intersection(
# # #                 pattern_words
# # #             )
# # #         )

# # #         required = max(
# # #             1,
# # #             int(
# # #                 len(pattern_words) * 0.6
# # #             )
# # #         )

# # #         return overlap >= required

# # #     # =========================================================
# # #     # EXTRACT NAME
# # #     # =========================================================

# # #     def extract_name(
# # #         self,
# # #         text
# # #     ):

# # #         patterns = [

# # #             r"\bmy name is ([A-Za-z][A-Za-z0-9 _-]{1,30})",

# # #             r"\bremember my name is ([A-Za-z][A-Za-z0-9 _-]{1,30})",

# # #             r"\bcall me ([A-Za-z][A-Za-z0-9 _-]{1,30})"
# # #         ]

# # #         for pattern in patterns:

# # #             match = re.search(
# # #                 pattern,
# # #                 text,
# # #                 re.IGNORECASE
# # #             )

# # #             if match:

# # #                 name = match.group(1)

# # #                 name = name.strip()

# # #                 name = name.rstrip(
# # #                     ".,!?;"
# # #                 )

# # #                 return name

# # #         return None

# # #     # =========================================================
# # #     # TIME
# # #     # =========================================================

# # #     def get_time(self):

# # #         now = datetime.now()

# # #         return (
# # #             "The current time is "
# # #             + now.strftime("%I:%M:%S %p")
# # #             + "."
# # #         )

# # #     # =========================================================
# # #     # DATE
# # #     # =========================================================

# # #     def get_date(self):

# # #         now = datetime.now()

# # #         return (
# # #             "Today is "
# # #             + now.strftime("%A, %d %B %Y")
# # #             + "."
# # #         )

# # #     # =========================================================
# # #     # CALCULATOR
# # #     # =========================================================

# # #     def calculate(
# # #         self,
# # #         message
# # #     ):

# # #         text = message.lower().strip()

# # #         prefixes = [
# # #             "calculate",
# # #             "solve",
# # #             "compute",
# # #             "what is"
# # #         ]

# # #         for prefix in prefixes:

# # #             if text.startswith(prefix):

# # #                 text = text[
# # #                     len(prefix):
# # #                 ].strip()

# # #                 break

# # #         replacements = {
# # #             "plus": "+",
# # #             "minus": "-",
# # #             "times": "*",
# # #             "multiplied by": "*",
# # #             "divided by": "/",
# # #             "divide by": "/"
# # #         }

# # #         for word, operator in replacements.items():

# # #             text = text.replace(
# # #                 word,
# # #                 operator
# # #             )

# # #         # Only mathematical characters

# # #         if not re.fullmatch(
# # #             r"[0-9\s\+\-\*\/\(\)\.%]+",
# # #             text
# # #         ):

# # #             return None

# # #         if not re.search(
# # #             r"[\+\-\*\/%]",
# # #             text
# # #         ):

# # #             return None

# # #         try:

# # #             result = eval(
# # #                 text,
# # #                 {
# # #                     "__builtins__": None
# # #                 },
# # #                 {}
# # #             )

# # #             return (
# # #                 f"The answer is {result}."
# # #             )

# # #         except Exception:

# # #             return (
# # #                 "I couldn't calculate that."
# # #             )

# # #     # =========================================================
# # #     # KNOWLEDGE SEARCH
# # #     # =========================================================

# # #     def search_knowledge(
# # #         self,
# # #         message
# # #     ):

# # #         if message in self.knowledge:

# # #             return self.knowledge[
# # #                 message
# # #             ]

# # #         best_key = None
# # #         best_score = 0

# # #         message_words = set(
# # #             message.split()
# # #         )

# # #         for key, answer in self.knowledge.items():

# # #             key_words = set(
# # #                 key.split()
# # #             )

# # #             if not key_words:

# # #                 continue

# # #             common = message_words.intersection(
# # #                 key_words
# # #             )

# # #             overlap_score = len(
# # #                 common
# # #             ) / len(
# # #                 key_words
# # #             )

# # #             similarity_score = difflib.SequenceMatcher(
# # #                 None,
# # #                 message,
# # #                 key
# # #             ).ratio()

# # #             score = (
# # #                 overlap_score * 0.65
# # #                 +
# # #                 similarity_score * 0.35
# # #             )

# # #             if score > best_score:

# # #                 best_score = score
# # #                 best_key = key

# # #         if best_key and best_score >= 0.55:

# # #             return self.knowledge[
# # #                 best_key
# # #             ]

# # #         return None

# # #     # =========================================================
# # #     # CONTEXT
# # #     # =========================================================

# # #     def handle_context(
# # #         self,
# # #         message
# # #     ):

# # #         if self.last_intent == "greeting":

# # #             if message in [
# # #                 "good",
# # #                 "great",
# # #                 "fine",
# # #                 "okay",
# # #                 "ok"
# # #             ]:

# # #                 return (
# # #                     "That's good to hear! "
# # #                     "What would you like to talk about?"
# # #                 )

# # #         if self.last_intent == "how_are_you":

# # #             if "good" in message:

# # #                 return (
# # #                     "Glad to hear that!"
# # #                 )

# # #         if self.last_intent == "unknown_question":

# # #             if message.startswith(
# # #                 "teach "
# # #             ):

# # #                 return (
# # #                     "You can teach me using:\n"
# # #                     "teach: question = answer"
# # #                 )

# # #         return None

# # #     # =========================================================
# # #     # TEACH
# # #     # =========================================================

# # #     def teach(
# # #         self,
# # #         original_message
# # #     ):

# # #         content = original_message[
# # #             len("teach:"):
# # #         ].strip()

# # #         if "=" not in content:

# # #             return (
# # #                 "Use this format:\n\n"
# # #                 "teach: question = answer\n\n"
# # #                 "Example:\n"
# # #                 "teach: what is pizza = "
# # #                 "Pizza is a food."
# # #             )

# # #         question, answer = content.split(
# # #             "=",
# # #             1
# # #         )

# # #         question = self.normalize(
# # #             question
# # #         )

# # #         answer = answer.strip()

# # #         if not question:

# # #             return (
# # #                 "The question cannot be empty."
# # #             )

# # #         if not answer:

# # #             return (
# # #                 "The answer cannot be empty."
# # #             )

# # #         self.knowledge[
# # #             question
# # #         ] = answer

# # #         self.memory.save_knowledge(
# # #             self.knowledge
# # #         )

# # #         return (
# # #             "I've learned something new!\n\n"
# # #             f"Question: {question}\n"
# # #             f"Answer: {answer}"
# # #         )

# # #     # =========================================================
# # #     # FORGET KNOWLEDGE
# # #     # =========================================================

# # #     def forget_knowledge(self):

# # #         self.knowledge = {}

# # #         self.memory.clear_knowledge()

# # #         return (
# # #             "I've forgotten all custom knowledge."
# # #         )

# # #     # =========================================================
# # #     # HELP
# # #     # =========================================================

# # #     def help_text(self):

# # #         return (
# # #             "YuiBot v2 understands things like:\n\n"

# # #             "Greetings\n"
# # #             "• hello\n"
# # #             "• hi\n"
# # #             "• helo\n\n"

# # #             "Information\n"
# # #             "• what is your name?\n"
# # #             "• who are you?\n"
# # #             "• what can you do?\n\n"

# # #             "Memory\n"
# # #             "• my name is Alex\n"
# # #             "• what is my name?\n\n"

# # #             "Utilities\n"
# # #             "• what time is it?\n"
# # #             "• what is today's date?\n"
# # #             "• calculate 25 + 50\n\n"

# # #             "Learning\n"
# # #             "• teach: what is pizza = Pizza is food.\n\n"

# # #             "Commands\n"
# # #             "• help\n"
# # #             "• about\n"
# # #             "• forget everything\n\n"

# # #             "YuiBot does not use an AI model."
# # #         )



# # import ast
# # import datetime
# # import difflib
# # import operator
# # import random
# # import re

# # from memory import ChatMemory
# # from knowledge import BUILT_IN_KNOWLEDGE


# # class YuiBot:

# #     def __init__(self):

# #         self.memory = ChatMemory()

# #         self.last_intent = None
# #         self.last_topic = None
# #         self.last_user_message = ""

# #         self.responses = {

# #             "greeting": [
# #                 "Hello!",
# #                 "Hi!",
# #                 "Hey!",
# #                 "Hello! How can I help?"
# #             ],

# #             "how_are_you": [
# #                 "I'm doing well!",
# #                 "I'm working normally.",
# #                 "I'm ready to chat!"
# #             ],

# #             "thanks": [
# #                 "You're welcome!",
# #                 "No problem!",
# #                 "Glad I could help!"
# #             ],

# #             "goodbye": [
# #                 "Goodbye!",
# #                 "See you later!",
# #                 "Bye!"
# #             ],

# #             "positive": [
# #                 "Nice!",
# #                 "That's good to hear.",
# #                 "Great!"
# #             ],

# #             "negative": [
# #                 "I understand.",
# #                 "Hopefully things get better.",
# #                 "I'm here if you want to chat."
# #             ]
# #         }

# #         # ------------------------------------------------------
# #         # TYPO CORRECTIONS
# #         # ------------------------------------------------------

# #         self.typos = {

# #             "helo": "hello",
# #             "helllo": "hello",
# #             "hllo": "hello",
# #             "hii": "hi",
# #             "hiiii": "hi",
# #             "heyy": "hey",

# #             "wht": "what",
# #             "whatt": "what",
# #             "wat": "what",
# #             "wut": "what",

# #             "whre": "where",
# #             "wher": "where",

# #             "whos": "who is",
# #             "whats": "what is",

# #             "ur": "your",
# #             "u": "you",
# #             "r": "are",

# #             "pls": "please",
# #             "plz": "please",
# #             "thx": "thanks",

# #             "im": "i am",
# #             "idk": "i do not know",

# #             "tim": "time",
# #             "todai": "today",

# #             "calcluate": "calculate",
# #             "calculte": "calculate",

# #             "favrite": "favorite",
# #             "favouritee": "favorite",

# #             "helpme": "help"
# #         }

# #     # ==========================================================
# #     # NORMALIZATION
# #     # ==========================================================

# #     def normalize(self, text):

# #         text = text.lower().strip()

# #         words = text.split()

# #         fixed = []

# #         for word in words:

# #             punctuation = ""

# #             while word and word[-1] in ".,!?":

# #                 punctuation = word[-1] + punctuation
# #                 word = word[:-1]

# #             word = self.typos.get(
# #                 word,
# #                 word
# #             )

# #             fixed.append(
# #                 word + punctuation
# #             )

# #         text = " ".join(fixed)

# #         text = re.sub(
# #             r"\bwhat's\b",
# #             "what is",
# #             text
# #         )

# #         text = re.sub(
# #             r"\bwho's\b",
# #             "who is",
# #             text
# #         )

# #         return text

# #     # ==========================================================
# #     # INTENT
# #     # ==========================================================

# #     def matches_intent(self, text, intent):

# #         patterns = {

# #             "greeting": [
# #                 r"^hello$",
# #                 r"^hi$",
# #                 r"^hey$",
# #                 r"^good morning$",
# #                 r"^good afternoon$",
# #                 r"^good evening$"
# #             ],

# #             "how_are_you": [
# #                 r"how are you",
# #                 r"how are u",
# #                 r"how do you feel"
# #             ],

# #             "thanks": [
# #                 r"^thanks$",
# #                 r"^thank you$",
# #                 r"^thx$"
# #             ],

# #             "goodbye": [
# #                 r"^bye$",
# #                 r"^goodbye$",
# #                 r"see you",
# #                 r"good night"
# #             ],

# #             "positive": [
# #                 r"^good$",
# #                 r"^great$",
# #                 r"^awesome$",
# #                 r"^nice$",
# #                 r"^fine$",
# #                 r"^okay$",
# #                 r"^ok$"
# #             ],

# #             "negative": [
# #                 r"^bad$",
# #                 r"^sad$",
# #                 r"^terrible$",
# #                 r"^not good$"
# #             ]
# #         }

# #         for pattern in patterns.get(intent, []):

# #             if re.search(pattern, text):
# #                 return True

# #         return False

# #     # ==========================================================
# #     # NAME
# #     # ==========================================================

# #     def extract_name(self, text):

# #         patterns = [

# #             r"\bmy name is ([a-zA-Z][a-zA-Z0-9 _-]{0,30})",
# #             r"\bremember my name is ([a-zA-Z][a-zA-Z0-9 _-]{0,30})",
# #             r"\bcall me ([a-zA-Z][a-zA-Z0-9 _-]{0,30})"
# #         ]

# #         for pattern in patterns:

# #             match = re.search(
# #                 pattern,
# #                 text,
# #                 re.IGNORECASE
# #             )

# #             if match:

# #                 name = match.group(1).strip()

# #                 name = re.split(
# #                     r"\b(?:and|but|because|please)\b",
# #                     name,
# #                     flags=re.IGNORECASE
# #                 )[0].strip()

# #                 return name

# #         return None

# #     # ==========================================================
# #     # PERSONAL MEMORY
# #     # ==========================================================

# #     def remember_fact(self, text):

# #         patterns = [

# #             r"^remember my (.+?) is (.+)$",

# #             r"^remember that my (.+?) is (.+)$",

# #             r"^my (.+?) is (.+)$"
# #         ]

# #         for pattern in patterns:

# #             match = re.match(
# #                 pattern,
# #                 text,
# #                 re.IGNORECASE
# #             )

# #             if match:

# #                 key = match.group(1).strip()
# #                 value = match.group(2).strip()

# #                 if key in [
# #                     "name",
# #                     "favorite name"
# #                 ]:
# #                     continue

# #                 self.memory.set_profile(
# #                     key,
# #                     value
# #                 )

# #                 return (
# #                     f"Okay, I'll remember that your "
# #                     f"{key} is {value}."
# #                 )

# #         return None

# #     def recall_fact(self, text):

# #         profile = self.memory.get_profile_all()

# #         if not profile:
# #             return None

# #         # Direct question:
# #         #
# #         # what is my favorite color?
# #         # what is my favorite game?

# #         match = re.match(
# #             r"^(?:what is|what's|tell me) my (.+?)[?!.]*$",
# #             text,
# #             re.IGNORECASE
# #         )

# #         if match:

# #             key = match.group(1).strip()

# #             if key in profile:

# #                 return (
# #                     f"Your {key} is "
# #                     f"{profile[key]}."
# #                 )

# #         # Where do I...
# #         match = re.match(
# #             r"^where do i (.+?)[?!.]*$",
# #             text,
# #             re.IGNORECASE
# #         )

# #         if match:

# #             action = match.group(1).strip()

# #             key = "location"

# #             if key in profile:

# #                 return (
# #                     f"You told me that your "
# #                     f"location is {profile[key]}."
# #                 )

# #         return None

# #     def forget_fact(self, text):

# #         match = re.match(
# #             r"^forget my (.+?)[?!.]*$",
# #             text,
# #             re.IGNORECASE
# #         )

# #         if not match:
# #             return None

# #         key = match.group(1).strip()

# #         if self.memory.remove_profile(key):

# #             return (
# #                 f"Okay. I forgot your {key}."
# #             )

# #         return (
# #             f"I don't have a saved memory for "
# #             f"your {key}."
# #         )

# #     # ==========================================================
# #     # SHOW MEMORIES
# #     # ==========================================================

# #     def show_memories(self):

# #         profile = self.memory.get_profile_all()

# #         if not profile:

# #             return "I don't have any personal memories saved."

# #         lines = [
# #             "Here are the things I remember:"
# #         ]

# #         for key, value in profile.items():

# #             lines.append(
# #                 f"• {key}: {value}"
# #             )

# #         return "\n".join(lines)

# #     # ==========================================================
# #     # KNOWLEDGE
# #     # ==========================================================

# #     def similar(self, a, b):

# #         a = a.lower().strip()
# #         b = b.lower().strip()

# #         if a == b:
# #             return 1.0

# #         if a in b or b in a:
# #             return 0.9

# #         ratio = difflib.SequenceMatcher(
# #             None,
# #             a,
# #             b
# #         ).ratio()

# #         a_words = set(a.split())
# #         b_words = set(b.split())

# #         if a_words and b_words:

# #             overlap = len(
# #                 a_words & b_words
# #             ) / max(
# #                 len(a_words),
# #                 len(b_words)
# #             )

# #         else:

# #             overlap = 0

# #         return max(
# #             ratio,
# #             overlap
# #         )

# #     def search_knowledge(self, question):

# #         normalized = self.normalize(
# #             question
# #         )

# #         all_knowledge = {}

# #         all_knowledge.update(
# #             BUILT_IN_KNOWLEDGE
# #         )

# #         all_knowledge.update(
# #             self.memory.get_knowledge()
# #         )

# #         if normalized in all_knowledge:

# #             return (
# #                 all_knowledge[normalized],
# #                 1.0
# #             )

# #         best_answer = None
# #         best_score = 0

# #         for key, answer in all_knowledge.items():

# #             score = self.similar(
# #                 normalized,
# #                 key
# #             )

# #             if score > best_score:

# #                 best_score = score
# #                 best_answer = answer

# #         if best_score >= 0.55:

# #             return (
# #                 best_answer,
# #                 best_score
# #             )

# #         return None, 0

# #     # ==========================================================
# #     # TEACH
# #     # ==========================================================

# #     def teach(self, text):

# #         if not text.lower().startswith(
# #             "teach:"
# #         ):
# #             return None

# #         content = text[6:].strip()

# #         if "=" not in content:

# #             return (
# #                 "Teaching format:\n"
# #                 "teach: question = answer"
# #             )

# #         question, answer = content.split(
# #             "=",
# #             1
# #         )

# #         question = self.normalize(
# #             question.strip()
# #         )

# #         answer = answer.strip()

# #         if not question or not answer:

# #             return (
# #                 "Both the question and answer "
# #                 "must contain something."
# #             )

# #         self.memory.set_knowledge(
# #             question,
# #             answer
# #         )

# #         return (
# #             f"Learned:\n"
# #             f"Q: {question}\n"
# #             f"A: {answer}"
# #         )

# #     # ==========================================================
# #     # CALCULATOR
# #     # ==========================================================

# #     def calculate(self, text):

# #         original = text

# #         text = re.sub(
# #             r"^(calculate|solve|compute)\s+",
# #             "",
# #             text,
# #             flags=re.IGNORECASE
# #         )

# #         text = re.sub(
# #             r"^what is\s+",
# #             "",
# #             text,
# #             flags=re.IGNORECASE
# #         )

# #         replacements = {

# #             "plus": "+",
# #             "minus": "-",
# #             "times": "*",
# #             "multiplied by": "*",
# #             "divided by": "/",
# #             "divide by": "/"
# #         }

# #         for word, symbol in replacements.items():

# #             text = text.replace(
# #                 word,
# #                 symbol
# #             )

# #         text = text.replace(
# #             "^",
# #             "**"
# #         )

# #         if not re.fullmatch(
# #             r"[0-9\s+\-*/().%]+",
# #             text
# #         ):
# #             return None

# #         try:

# #             tree = ast.parse(
# #                 text,
# #                 mode="eval"
# #             )

# #             result = self._safe_eval(
# #                 tree.body
# #             )

# #             return (
# #                 f"The answer is {result}."
# #             )

# #         except Exception:

# #             if original.lower().startswith(
# #                 ("calculate", "solve", "compute")
# #             ):
# #                 return (
# #                     "I couldn't calculate that."
# #                 )

# #             return None

# #     def _safe_eval(self, node):

# #         operators = {

# #             ast.Add: operator.add,
# #             ast.Sub: operator.sub,
# #             ast.Mult: operator.mul,
# #             ast.Div: operator.truediv,
# #             ast.Mod: operator.mod,
# #             ast.Pow: operator.pow,

# #             ast.USub: operator.neg,
# #             ast.UAdd: operator.pos
# #         }

# #         if isinstance(
# #             node,
# #             ast.Constant
# #         ):

# #             if isinstance(
# #                 node.value,
# #                 (int, float)
# #             ):

# #                 return node.value

# #             raise ValueError

# #         if isinstance(
# #             node,
# #             ast.BinOp
# #         ):

# #             left = self._safe_eval(
# #                 node.left
# #             )

# #             right = self._safe_eval(
# #                 node.right
# #             )

# #             operation = operators.get(
# #                 type(node.op)
# #             )

# #             if operation is None:
# #                 raise ValueError

# #             return operation(
# #                 left,
# #                 right
# #             )

# #         if isinstance(
# #             node,
# #             ast.UnaryOp
# #         ):

# #             operation = operators.get(
# #                 type(node.op)
# #             )

# #             if operation is None:
# #                 raise ValueError

# #             return operation(
# #                 self._safe_eval(
# #                     node.operand
# #                 )
# #             )

# #         raise ValueError

# #     # ==========================================================
# #     # DATE / TIME
# #     # ==========================================================

# #     def get_time(self):

# #         now = datetime.datetime.now()

# #         return now.strftime(
# #             "%I:%M %p"
# #         ).lstrip("0")

# #     def get_date(self):

# #         now = datetime.datetime.now()

# #         return now.strftime(
# #             "%A, %d %B %Y"
# #         )

# #     # ==========================================================
# #     # CONTEXT
# #     # ==========================================================

# #     def handle_context(self, text):

# #         if self.last_intent == "greeting":

# #             if text in [
# #                 "good",
# #                 "great",
# #                 "fine",
# #                 "okay",
# #                 "ok"
# #             ]:

# #                 return (
# #                     "Nice! What would you like "
# #                     "to talk about?"
# #                 )

# #         if self.last_intent == "how_are_you":

# #             if text in [
# #                 "good",
# #                 "great",
# #                 "fine",
# #                 "okay",
# #                 "ok"
# #             ]:

# #                 return (
# #                     "Glad to hear it!"
# #                 )

# #         if self.last_topic:

# #             if text in [
# #                 "why",
# #                 "how",
# #                 "tell me more",
# #                 "more"
# #             ]:

# #                 return (
# #                     f"I don't have enough detailed "
# #                     f"information about {self.last_topic} "
# #                     f"to expand on it yet."
# #                 )

# #         return None

# #     # ==========================================================
# #     # HELP
# #     # ==========================================================

# #     def help_text(self):

# #         return """YuiBot v3 Help

# # CHAT
# #   hello
# #   how are you?
# #   thanks
# #   bye

# # PERSONAL MEMORY
# #   my name is Alex
# #   remember my favorite color is blue
# #   what is my favorite color?
# #   forget my favorite color
# #   show my memories

# # KNOWLEDGE
# #   what is Python?
# #   what is HTML?
# #   what is a database?

# # TEACH YUIBOT
# #   teach: what is my favorite food = Your favorite food is pizza.

# # CALCULATOR
# #   calculate 100 + 25
# #   calculate 20 * 5
# #   what is 100 divided by 4

# # DATE / TIME
# #   what time is it?
# #   what is today's date?

# # MEMORY
# #   forget everything
# #   clear knowledge

# # YuiBot is completely offline and does not use
# # OpenAI, Ollama, Llama, Qwen, Hugging Face,
# # or any other AI model."""

# #     # ==========================================================
# #     # MAIN RESPONSE
# #     # ==========================================================

# #     def respond(self, original_message):

# #         if not original_message.strip():

# #             return "Please type something."

# #         self.last_user_message = (
# #             original_message
# #         )

# #         text = self.normalize(
# #             original_message
# #         )

# #         # ------------------------------------------------------
# #         # TEACH
# #         # ------------------------------------------------------

# #         if text.startswith("teach:"):

# #             answer = self.teach(
# #                 original_message
# #             )

# #             self.last_intent = "teach"

# #             return answer

# #         # ------------------------------------------------------
# #         # HELP
# #         # ------------------------------------------------------

# #         if text in [
# #             "help",
# #             "help me",
# #             "commands",
# #             "what can i ask"
# #         ]:

# #             self.last_intent = "help"

# #             return self.help_text()

# #         # ------------------------------------------------------
# #         # SHOW MEMORIES
# #         # ------------------------------------------------------

# #         if text in [
# #             "show my memories",
# #             "show memories",
# #             "what do you remember about me",
# #             "what do you remember"
# #         ]:

# #             self.last_intent = "memory"

# #             return self.show_memories()

# #         # ------------------------------------------------------
# #         # CLEAR KNOWLEDGE
# #         # ------------------------------------------------------

# #         if text in [
# #             "forget everything",
# #             "forget all",
# #             "delete knowledge",
# #             "clear knowledge"
# #         ]:

# #             self.memory.clear_knowledge()

# #             self.last_intent = "forget"

# #             return (
# #                 "Okay. I forgot all custom "
# #                 "learned knowledge."
# #             )

# #         # ------------------------------------------------------
# #         # CLEAR PERSONAL MEMORY
# #         # ------------------------------------------------------

# #         if text in [
# #             "clear memories",
# #             "clear my memories",
# #             "forget my memories"
# #         ]:

# #             self.memory.clear_profile()

# #             self.last_intent = "forget"

# #             return (
# #                 "Okay. I cleared my personal "
# #                 "memories about you."
# #             )

# #         # ------------------------------------------------------
# #         # ABOUT
# #         # ------------------------------------------------------

# #         if text in [
# #             "about",
# #             "about you",
# #             "tell me about yourself"
# #         ]:

# #             self.last_intent = "about"

# #             return (
# #                 "I am YuiBot v3.\n\n"
# #                 "I am a Python rule-based chatbot "
# #                 "that runs completely offline.\n\n"
# #                 "I use programmed rules, fuzzy "
# #                 "matching, knowledge storage, "
# #                 "personal memory, and Python logic."
# #             )

# #         # ------------------------------------------------------
# #         # REMEMBER NAME
# #         # ------------------------------------------------------

# #         name = self.extract_name(
# #             original_message
# #         )

# #         if name:

# #             self.memory.set_profile(
# #                 "name",
# #                 name
# #             )

# #             self.last_intent = "remember"

# #             return (
# #                 f"Nice to meet you, {name}! "
# #                 f"I'll remember your name."
# #             )

# #         # ------------------------------------------------------
# #         # ASK NAME
# #         # ------------------------------------------------------

# #         if text in [
# #             "what is my name",
# #             "what's my name",
# #             "who am i",
# #             "do you remember my name"
# #         ]:

# #             name = self.memory.get_profile(
# #                 "name"
# #             )

# #             self.last_intent = "memory"

# #             if name:

# #                 return (
# #                     f"Your name is {name}."
# #                 )

# #             return (
# #                 "You haven't told me your name yet."
# #             )

# #         # ------------------------------------------------------
# #         # FORGET INDIVIDUAL FACT
# #         # ------------------------------------------------------

# #         forgotten = self.forget_fact(
# #             text
# #         )

# #         if forgotten:

# #             self.last_intent = "forget"

# #             return forgotten

# #         # ------------------------------------------------------
# #         # REMEMBER GENERAL FACT
# #         # ------------------------------------------------------

# #         remembered = self.remember_fact(
# #             text
# #         )

# #         if remembered:

# #             self.last_intent = "remember"

# #             return remembered

# #         # ------------------------------------------------------
# #         # RECALL PERSONAL FACT
# #         # ------------------------------------------------------

# #         recalled = self.recall_fact(
# #             text
# #         )

# #         if recalled:

# #             self.last_intent = "memory"

# #             return recalled

# #         # ------------------------------------------------------
# #         # GREETING
# #         # ------------------------------------------------------

# #         if self.matches_intent(
# #             text,
# #             "greeting"
# #         ):

# #             self.last_intent = "greeting"

# #             return random.choice(
# #                 self.responses["greeting"]
# #             )

# #         # ------------------------------------------------------
# #         # HOW ARE YOU
# #         # ------------------------------------------------------

# #         if self.matches_intent(
# #             text,
# #             "how_are_you"
# #         ):

# #             self.last_intent = "how_are_you"

# #             return random.choice(
# #                 self.responses["how_are_you"]
# #             )

# #         # ------------------------------------------------------
# #         # THANKS
# #         # ------------------------------------------------------

# #         if self.matches_intent(
# #             text,
# #             "thanks"
# #         ):

# #             self.last_intent = "thanks"

# #             return random.choice(
# #                 self.responses["thanks"]
# #             )

# #         # ------------------------------------------------------
# #         # GOODBYE
# #         # ------------------------------------------------------

# #         if self.matches_intent(
# #             text,
# #             "goodbye"
# #         ):

# #             self.last_intent = "goodbye"

# #             return random.choice(
# #                 self.responses["goodbye"]
# #             )

# #         # ------------------------------------------------------
# #         # POSITIVE
# #         # ------------------------------------------------------

# #         if self.matches_intent(
# #             text,
# #             "positive"
# #         ):

# #             response = self.handle_context(
# #                 text
# #             )

# #             if response:

# #                 self.last_intent = "context"

# #                 return response

# #             self.last_intent = "positive"

# #             return random.choice(
# #                 self.responses["positive"]
# #             )

# #         # ------------------------------------------------------
# #         # NEGATIVE
# #         # ------------------------------------------------------

# #         if self.matches_intent(
# #             text,
# #             "negative"
# #         ):

# #             self.last_intent = "negative"

# #             return random.choice(
# #                 self.responses["negative"]
# #             )

# #         # ------------------------------------------------------
# #         # TIME
# #         # ------------------------------------------------------

# #         if (
# #             "what time" in text
# #             or "current time" in text
# #             or text == "time"
# #             or text == "tell me the time"
# #         ):

# #             self.last_intent = "time"

# #             return (
# #                 f"The current time is "
# #                 f"{self.get_time()}."
# #             )

# #         # ------------------------------------------------------
# #         # DATE
# #         # ------------------------------------------------------

# #         if (
# #             "what date" in text
# #             or "today's date" in text
# #             or "todays date" in text
# #             or text == "date"
# #             or text == "what day is it"
# #         ):

# #             self.last_intent = "date"

# #             return (
# #                 f"Today is "
# #                 f"{self.get_date()}."
# #             )

# #         # ------------------------------------------------------
# #         # CALCULATOR
# #         # ------------------------------------------------------

# #         calculation = self.calculate(
# #             text
# #         )

# #         if calculation:

# #             self.last_intent = "calculator"

# #             return calculation

# #         # ------------------------------------------------------
# #         # CONTEXT
# #         # ------------------------------------------------------

# #         context = self.handle_context(
# #             text
# #         )

# #         if context:

# #             self.last_intent = "context"

# #             return context

# #         # ------------------------------------------------------
# #         # KNOWLEDGE SEARCH
# #         # ------------------------------------------------------

# #         answer, score = self.search_knowledge(
# #             text
# #         )

# #         if answer:

# #             self.last_intent = "knowledge"

# #             # Try to remember the topic.

# #             words = text.split()

# #             if len(words) >= 2:

# #                 self.last_topic = " ".join(
# #                     words[-2:]
# #                 )

# #             return answer

# #         # ------------------------------------------------------
# #         # UNKNOWN
# #         # ------------------------------------------------------

# #         self.last_intent = "unknown"

# #         return (
# #             "I'm not sure how to answer that yet.\n\n"
# #             "You can teach me with:\n"
# #             "teach: question = answer"
# #         )


# import ast
# import datetime
# import difflib
# import operator
# import random
# import re

# from memory import ChatMemory
# from knowledge import BUILT_IN_KNOWLEDGE


# class YuiBot:

#     def __init__(self):

#         self.memory = ChatMemory()

#         self.last_intent = None
#         self.last_topic = None
#         self.last_question = None

#         self.responses = {

#             "greeting": [
#                 "Hello!",
#                 "Hi!",
#                 "Hey!",
#                 "Hello! How can I help?"
#             ],

#             "how_are_you": [
#                 "I'm doing well!",
#                 "I'm working normally.",
#                 "I'm ready to chat!"
#             ],

#             "thanks": [
#                 "You're welcome!",
#                 "No problem!",
#                 "Glad I could help!"
#             ],

#             "goodbye": [
#                 "Goodbye!",
#                 "See you later!",
#                 "Bye!"
#             ],

#             "positive": [
#                 "Nice!",
#                 "That's good to hear.",
#                 "Great!"
#             ],

#             "negative": [
#                 "I understand.",
#                 "Hopefully things get better.",
#                 "I'm here if you want to chat."
#             ]
#         }

#         self.typos = {

#             "helo": "hello",
#             "helllo": "hello",
#             "hllo": "hello",
#             "hii": "hi",
#             "hiiii": "hi",
#             "heyy": "hey",

#             "wht": "what",
#             "whatt": "what",
#             "wat": "what",
#             "wut": "what",

#             "whre": "where",
#             "wher": "where",

#             "whos": "who is",
#             "whats": "what is",

#             "ur": "your",
#             "u": "you",
#             "r": "are",

#             "pls": "please",
#             "plz": "please",
#             "thx": "thanks",

#             "im": "i am",
#             "idk": "i do not know",

#             "tim": "time",
#             "todai": "today",

#             "calcluate": "calculate",
#             "calculte": "calculate",

#             "favrite": "favorite",
#             "favouritee": "favorite",

#             "pyhton": "python",
#             "pythn": "python",

#             "creater": "creator",
#             "abt": "about"
#         }

#     # ==========================================================
#     # NORMALIZATION
#     # ==========================================================

#     def normalize(self, text):

#         text = text.lower().strip()

#         text = re.sub(
#             r"\s+",
#             " ",
#             text
#         )

#         words = text.split()

#         fixed = []

#         for word in words:

#             punctuation = ""

#             while word and word[-1] in ".,!?":

#                 punctuation = (
#                     word[-1] +
#                     punctuation
#                 )

#                 word = word[:-1]

#             word = self.typos.get(
#                 word,
#                 word
#             )

#             fixed.append(
#                 word + punctuation
#             )

#         text = " ".join(
#             fixed
#         )

#         text = re.sub(
#             r"\bwhat's\b",
#             "what is",
#             text
#         )

#         text = re.sub(
#             r"\bwho's\b",
#             "who is",
#             text
#         )

#         return text

#     # ==========================================================
#     # FUZZY MATCHING
#     # ==========================================================

#     def similarity(
#         self,
#         a,
#         b
#     ):

#         a = a.lower().strip()
#         b = b.lower().strip()

#         if a == b:
#             return 1.0

#         if a in b or b in a:
#             return 0.92

#         ratio = difflib.SequenceMatcher(
#             None,
#             a,
#             b
#         ).ratio()

#         a_words = set(
#             re.findall(
#                 r"\b\w+\b",
#                 a
#             )
#         )

#         b_words = set(
#             re.findall(
#                 r"\b\w+\b",
#                 b
#             )
#         )

#         if a_words and b_words:

#             overlap = len(
#                 a_words & b_words
#             ) / max(
#                 len(a_words),
#                 len(b_words)
#             )

#         else:

#             overlap = 0

#         return max(
#             ratio,
#             overlap
#         )

#     # ==========================================================
#     # KNOWLEDGE SEARCH
#     # ==========================================================

#     def search_knowledge(
#         self,
#         question
#     ):

#         question = self.normalize(
#             question
#         )

#         all_knowledge = {}

#         for key, value in BUILT_IN_KNOWLEDGE.items():

#             all_knowledge[key] = {
#                 "answer": value,
#                 "category": "Built-in"
#             }

#         all_knowledge.update(
#             self.memory.get_knowledge()
#         )

#         if question in all_knowledge:

#             item = all_knowledge[
#                 question
#             ]

#             return (
#                 item["answer"],
#                 1.0,
#                 item.get(
#                     "category",
#                     "General"
#                 )
#             )

#         best = None
#         best_score = 0

#         for key, item in all_knowledge.items():

#             score = self.similarity(
#                 question,
#                 key
#             )

#             if score > best_score:

#                 best_score = score
#                 best = item

#         if best is not None and best_score >= 0.58:

#             return (
#                 best["answer"],
#                 best_score,
#                 best.get(
#                     "category",
#                     "General"
#                 )
#             )

#         return None, 0, None

#     # ==========================================================
#     # PERSONAL MEMORY
#     # ==========================================================

#     def remember_fact(
#         self,
#         text
#     ):

#         patterns = [

#             r"^remember my (.+?) is (.+)$",

#             r"^remember that my (.+?) is (.+)$",

#             r"^my (.+?) is (.+)$"
#         ]

#         for pattern in patterns:

#             match = re.match(
#                 pattern,
#                 text,
#                 re.IGNORECASE
#             )

#             if not match:
#                 continue

#             key = match.group(
#                 1
#             ).strip()

#             value = match.group(
#                 2
#             ).strip()

#             if key in [
#                 "name",
#                 "favorite name"
#             ]:
#                 continue

#             self.memory.set_profile(
#                 key,
#                 value,
#                 "Preferences"
#             )

#             return (
#                 f"Okay, I'll remember that "
#                 f"your {key} is {value}."
#             )

#         return None

#     def recall_fact(
#         self,
#         text
#     ):

#         profile = (
#             self.memory.get_profile_all()
#         )

#         if not profile:
#             return None

#         match = re.match(
#             r"^(?:what is|what's|tell me) my (.+?)[?!.]*$",
#             text,
#             re.IGNORECASE
#         )

#         if match:

#             key = match.group(
#                 1
#             ).strip()

#             if key in profile:

#                 value = self.memory.get_profile(
#                     key
#                 )

#                 return (
#                     f"Your {key} is {value}."
#                 )

#         # Special location wording

#         if re.match(
#             r"^where do i live",
#             text
#         ):

#             if "location" in profile:

#                 value = self.memory.get_profile(
#                     "location"
#                 )

#                 return (
#                     f"You told me that your "
#                     f"location is {value}."
#                 )

#         return None

#     def forget_fact(
#         self,
#         text
#     ):

#         match = re.match(
#             r"^forget my (.+?)[?!.]*$",
#             text,
#             re.IGNORECASE
#         )

#         if not match:
#             return None

#         key = match.group(
#             1
#         ).strip()

#         if self.memory.delete_profile(
#             key
#         ):

#             return (
#                 f"Okay. I forgot your {key}."
#             )

#         return (
#             f"I don't have a saved memory "
#             f"for your {key}."
#         )

#     def show_memories(self):

#         profile = (
#             self.memory.get_profile_all()
#         )

#         if not profile:

#             return (
#                 "I don't have any personal "
#                 "memories saved."
#             )

#         groups = {}

#         for key, item in profile.items():

#             if isinstance(
#                 item,
#                 dict
#             ):

#                 category = item.get(
#                     "category",
#                     "Personal"
#                 )

#                 value = item.get(
#                     "value",
#                     ""
#                 )

#             else:

#                 category = "Personal"
#                 value = item

#             groups.setdefault(
#                 category,
#                 []
#             ).append(
#                 f"• {key}: {value}"
#             )

#         lines = [
#             "Things I remember:"
#         ]

#         for category, items in groups.items():

#             lines.append(
#                 f"\n[{category}]"
#             )

#             lines.extend(
#                 items
#             )

#         return "\n".join(
#             lines
#         )

#     # ==========================================================
#     # NAME
#     # ==========================================================

#     def extract_name(
#         self,
#         text
#     ):

#         patterns = [

#             r"\bmy name is ([a-zA-Z][a-zA-Z0-9 _-]{0,30})",

#             r"\bremember my name is ([a-zA-Z][a-zA-Z0-9 _-]{0,30})",

#             r"\bcall me ([a-zA-Z][a-zA-Z0-9 _-]{0,30})"
#         ]

#         for pattern in patterns:

#             match = re.search(
#                 pattern,
#                 text,
#                 re.IGNORECASE
#             )

#             if match:

#                 name = match.group(
#                     1
#                 ).strip()

#                 name = re.split(
#                     r"\b(?:and|but|because|please)\b",
#                     name,
#                     flags=re.IGNORECASE
#                 )[0].strip()

#                 return name

#         return None

#     # ==========================================================
#     # TEACH
#     # ==========================================================

#     def teach(
#         self,
#         original
#     ):

#         if not original.lower().startswith(
#             "teach:"
#         ):
#             return None

#         content = original[
#             6:
#         ].strip()

#         if "=" not in content:

#             return (
#                 "Teaching format:\n\n"
#                 "teach: question = answer"
#             )

#         question, answer = content.split(
#             "=",
#             1
#         )

#         question = self.normalize(
#             question.strip()
#         )

#         answer = answer.strip()

#         if not question or not answer:

#             return (
#                 "The question and answer "
#                 "cannot be empty."
#             )

#         self.memory.set_knowledge(
#             question,
#             answer,
#             "Custom"
#         )

#         return (
#             "Knowledge learned successfully.\n\n"
#             f"Question: {question}\n"
#             f"Answer: {answer}"
#         )

#     # ==========================================================
#     # CALCULATOR
#     # ==========================================================

#     def calculate(
#         self,
#         text
#     ):

#         original = text

#         text = re.sub(
#             r"^(calculate|solve|compute)\s+",
#             "",
#             text,
#             flags=re.IGNORECASE
#         )

#         text = re.sub(
#             r"^what is\s+",
#             "",
#             text,
#             flags=re.IGNORECASE
#         )

#         replacements = {

#             "multiplied by": "*",
#             "divided by": "/",
#             "divide by": "/",
#             "plus": "+",
#             "minus": "-",
#             "times": "*"
#         }

#         for word, symbol in replacements.items():

#             text = text.replace(
#                 word,
#                 symbol
#             )

#         text = text.replace(
#             "^",
#             "**"
#         )

#         if not re.fullmatch(
#             r"[0-9\s+\-*/().%]+",
#             text
#         ):
#             return None

#         try:

#             tree = ast.parse(
#                 text,
#                 mode="eval"
#             )

#             result = self.safe_eval(
#                 tree.body
#             )

#             if isinstance(
#                 result,
#                 float
#             ) and result.is_integer():

#                 result = int(
#                     result
#                 )

#             return (
#                 f"The answer is {result}."
#             )

#         except Exception:

#             if original.lower().startswith(
#                 (
#                     "calculate",
#                     "solve",
#                     "compute"
#                 )
#             ):

#                 return (
#                     "I couldn't calculate that."
#                 )

#         return None

#     def safe_eval(
#         self,
#         node
#     ):

#         operators = {

#             ast.Add: operator.add,
#             ast.Sub: operator.sub,
#             ast.Mult: operator.mul,
#             ast.Div: operator.truediv,
#             ast.Mod: operator.mod,
#             ast.Pow: operator.pow,

#             ast.USub: operator.neg,
#             ast.UAdd: operator.pos
#         }

#         if isinstance(
#             node,
#             ast.Constant
#         ):

#             if isinstance(
#                 node.value,
#                 (int, float)
#             ):

#                 return node.value

#             raise ValueError

#         if isinstance(
#             node,
#             ast.BinOp
#         ):

#             left = self.safe_eval(
#                 node.left
#             )

#             right = self.safe_eval(
#                 node.right
#             )

#             operation = operators.get(
#                 type(node.op)
#             )

#             if operation is None:
#                 raise ValueError

#             return operation(
#                 left,
#                 right
#             )

#         if isinstance(
#             node,
#             ast.UnaryOp
#         ):

#             operation = operators.get(
#                 type(node.op)
#             )

#             if operation is None:
#                 raise ValueError

#             return operation(
#                 self.safe_eval(
#                     node.operand
#                 )
#             )

#         raise ValueError

#     # ==========================================================
#     # INTENTS
#     # ==========================================================

#     def is_greeting(
#         self,
#         text
#     ):

#         return text in [
#             "hello",
#             "hi",
#             "hey",
#             "good morning",
#             "good afternoon",
#             "good evening"
#         ]

#     def is_thanks(
#         self,
#         text
#     ):

#         return text in [
#             "thanks",
#             "thank you",
#             "thx"
#         ]

#     def is_goodbye(
#         self,
#         text
#     ):

#         return (
#             text in [
#                 "bye",
#                 "goodbye",
#                 "good night"
#             ]
#             or "see you" in text
#         )

#     # ==========================================================
#     # CONTEXT
#     # ==========================================================

#     def contextual_question(
#         self,
#         text
#     ):

#         # "Who created it?" after asking about Python.

#         if text in [
#             "who created it",
#             "who made it",
#             "who invented it",
#             "who created this"
#         ]:

#             if self.last_topic:

#                 topic = self.last_topic.lower()

#                 if "python" in topic:

#                     return (
#                         "Python was created by "
#                         "Guido van Rossum."
#                     )

#         # "What does it do?"

#         if text in [
#             "what does it do",
#             "what can it do"
#         ]:

#             if self.last_topic:

#                 if "python" in self.last_topic:

#                     return (
#                         "Python is a general-purpose "
#                         "programming language used for "
#                         "web development, automation, "
#                         "data processing, applications, "
#                         "and many other tasks."
#                     )

#         return None

#     # ==========================================================
#     # TOPIC DETECTION
#     # ==========================================================

#     def detect_topic(
#         self,
#         text,
#         category=None
#     ):

#         topics = [
#             "python",
#             "html",
#             "css",
#             "javascript",
#             "database",
#             "mysql",
#             "sqlite",
#             "sql",
#             "computer",
#             "cpu",
#             "ram",
#             "gpu",
#             "cybersecurity",
#             "encryption",
#             "password",
#             "tkinter",
#             "pygame",
#             "website",
#             "api"
#         ]

#         for topic in topics:

#             if topic in text:

#                 return topic

#         return category

#     # ==========================================================
#     # CONVERSATION SEARCH
#     # ==========================================================

#     def search_conversation(
#         self,
#         query
#     ):

#         results = (
#             self.memory.search_messages(
#                 query
#             )
#         )

#         if not results:

#             return (
#                 f"I couldn't find any previous "
#                 f"messages containing '{query}'."
#             )

#         lines = [
#             f"Found {len(results)} matching message(s):",
#             ""
#         ]

#         for item in results[-10:]:

#             role = item.get(
#                 "role",
#                 "unknown"
#             )

#             content = item.get(
#                 "content",
#                 ""
#             )

#             timestamp = item.get(
#                 "timestamp",
#                 ""
#             )

#             if timestamp:

#                 try:

#                     timestamp = (
#                         timestamp
#                         .replace(
#                             "T",
#                             " "
#                         )
#                     )

#                 except Exception:
#                     pass

#             label = (
#                 "You"
#                 if role == "user"
#                 else "YuiBot"
#             )

#             lines.append(
#                 f"[{timestamp}] {label}:"
#             )

#             lines.append(
#                 content
#             )

#             lines.append("")

#         return "\n".join(
#             lines
#         )

#     # ==========================================================
#     # HELP
#     # ==========================================================

#     def help_text(self):

#         return """YuiBot v4 Help

# CHAT
#   hello
#   how are you?
#   thanks
#   bye

# PERSONAL MEMORY
#   my name is Alex
#   remember my favorite color is blue
#   what is my favorite color?
#   forget my favorite color
#   show my memories

# KNOWLEDGE
#   what is Python?
#   what is HTML?
#   what is a database?

# TEACH
#   teach: what is my favorite food = Pizza

# CALCULATOR
#   calculate 100 + 25
#   calculate 20 * 5
#   what is 100 divided by 4

# DATE / TIME
#   what time is it?
#   what is today's date?

# CONVERSATION SEARCH
#   search conversation Python
#   find messages about Python

# MEMORY
#   forget everything
#   clear knowledge
#   clear memories

# YuiBot is completely offline.
# No AI model or external API is used."""

#     # ==========================================================
#     # MAIN RESPONSE
#     # ==========================================================

#     def respond(
#         self,
#         original_message
#     ):

#         if not original_message.strip():

#             return "Please type something."

#         text = self.normalize(
#             original_message
#         )

#         self.last_question = text

#         # ------------------------------------------------------
#         # TEACH
#         # ------------------------------------------------------

#         if text.startswith(
#             "teach:"
#         ):

#             self.last_intent = "teach"

#             return self.teach(
#                 original_message
#             )

#         # ------------------------------------------------------
#         # SEARCH CONVERSATION
#         # ------------------------------------------------------

#         search_match = re.match(
#             r"^(?:search conversation|find messages about|search chat for)\s+(.+)$",
#             text,
#             re.IGNORECASE
#         )

#         if search_match:

#             query = search_match.group(
#                 1
#             ).strip()

#             self.last_intent = (
#                 "conversation_search"
#             )

#             return self.search_conversation(
#                 query
#             )

#         # ------------------------------------------------------
#         # HELP
#         # ------------------------------------------------------

#         if text in [
#             "help",
#             "help me",
#             "commands",
#             "what can i ask"
#         ]:

#             self.last_intent = "help"

#             return self.help_text()

#         # ------------------------------------------------------
#         # SHOW MEMORIES
#         # ------------------------------------------------------

#         if text in [
#             "show my memories",
#             "show memories",
#             "what do you remember",
#             "what do you remember about me"
#         ]:

#             self.last_intent = "memory"

#             return self.show_memories()

#         # ------------------------------------------------------
#         # CLEAR KNOWLEDGE
#         # ------------------------------------------------------

#         if text in [
#             "forget everything",
#             "forget all",
#             "delete knowledge",
#             "clear knowledge"
#         ]:

#             self.memory.clear_knowledge()

#             self.last_intent = "forget"

#             return (
#                 "Okay. I cleared all custom "
#                 "learned knowledge."
#             )

#         # ------------------------------------------------------
#         # CLEAR PERSONAL MEMORY
#         # ------------------------------------------------------

#         if text in [
#             "clear memories",
#             "clear my memories",
#             "forget my memories"
#         ]:

#             self.memory.clear_profile()

#             self.last_intent = "forget"

#             return (
#                 "Okay. I cleared my personal "
#                 "memories."
#             )

#         # ------------------------------------------------------
#         # ABOUT
#         # ------------------------------------------------------

#         if text in [
#             "about",
#             "about you",
#             "tell me about yourself"
#         ]:

#             self.last_intent = "about"

#             return (
#                 "I am YuiBot v4.\n\n"
#                 "I am a completely offline "
#                 "rule-based chatbot written "
#                 "in Python.\n\n"
#                 "I use rules, fuzzy matching, "
#                 "conversation context, memory, "
#                 "and stored knowledge."
#             )

#         # ------------------------------------------------------
#         # NAME
#         # ------------------------------------------------------

#         name = self.extract_name(
#             original_message
#         )

#         if name:

#             self.memory.set_profile(
#                 "name",
#                 name,
#                 "Personal"
#             )

#             self.last_intent = "remember"

#             return (
#                 f"Nice to meet you, {name}! "
#                 f"I'll remember your name."
#             )

#         # ------------------------------------------------------
#         # ASK NAME
#         # ------------------------------------------------------

#         if text in [
#             "what is my name",
#             "what's my name",
#             "who am i",
#             "do you remember my name"
#         ]:

#             name = self.memory.get_profile(
#                 "name"
#             )

#             self.last_intent = "memory"

#             if name:

#                 return (
#                     f"Your name is {name}."
#                 )

#             return (
#                 "You haven't told me your "
#                 "name yet."
#             )

#         # ------------------------------------------------------
#         # FORGET INDIVIDUAL MEMORY
#         # ------------------------------------------------------

#         forgotten = self.forget_fact(
#             text
#         )

#         if forgotten:

#             self.last_intent = "forget"

#             return forgotten

#         # ------------------------------------------------------
#         # REMEMBER FACT
#         # ------------------------------------------------------

#         remembered = self.remember_fact(
#             text
#         )

#         if remembered:

#             self.last_intent = "remember"

#             return remembered

#         # ------------------------------------------------------
#         # RECALL FACT
#         # ------------------------------------------------------

#         recalled = self.recall_fact(
#             text
#         )

#         if recalled:

#             self.last_intent = "memory"

#             return recalled

#         # ------------------------------------------------------
#         # GREETING
#         # ------------------------------------------------------

#         if self.is_greeting(
#             text
#         ):

#             self.last_intent = "greeting"

#             return random.choice(
#                 self.responses[
#                     "greeting"
#                 ]
#             )

#         # ------------------------------------------------------
#         # HOW ARE YOU
#         # ------------------------------------------------------

#         if (
#             "how are you" in text
#             or "how do you feel" in text
#         ):

#             self.last_intent = (
#                 "how_are_you"
#             )

#             return random.choice(
#                 self.responses[
#                     "how_are_you"
#                 ]
#             )

#         # ------------------------------------------------------
#         # THANKS
#         # ------------------------------------------------------

#         if self.is_thanks(
#             text
#         ):

#             self.last_intent = "thanks"

#             return random.choice(
#                 self.responses[
#                     "thanks"
#                 ]
#             )

#         # ------------------------------------------------------
#         # GOODBYE
#         # ------------------------------------------------------

#         if self.is_goodbye(
#             text
#         ):

#             self.last_intent = "goodbye"

#             return random.choice(
#                 self.responses[
#                     "goodbye"
#                 ]
#             )

#         # ------------------------------------------------------
#         # SIMPLE POSITIVE
#         # ------------------------------------------------------

#         if text in [
#             "good",
#             "great",
#             "awesome",
#             "nice",
#             "fine",
#             "okay",
#             "ok"
#         ]:

#             if self.last_intent == (
#                 "how_are_you"
#             ):

#                 self.last_intent = "context"

#                 return (
#                     "Glad to hear it!"
#                 )

#             self.last_intent = "positive"

#             return random.choice(
#                 self.responses[
#                     "positive"
#                 ]
#             )

#         # ------------------------------------------------------
#         # SIMPLE NEGATIVE
#         # ------------------------------------------------------

#         if text in [
#             "bad",
#             "sad",
#             "terrible",
#             "not good"
#         ]:

#             self.last_intent = "negative"

#             return random.choice(
#                 self.responses[
#                     "negative"
#                 ]
#             )

#         # ------------------------------------------------------
#         # TIME
#         # ------------------------------------------------------

#         if (
#             "what time" in text
#             or "current time" in text
#             or text == "time"
#             or "tell me the time" in text
#         ):

#             now = datetime.datetime.now()

#             self.last_intent = "time"

#             return (
#                 "The current time is "
#                 + now.strftime(
#                     "%I:%M %p"
#                 ).lstrip("0")
#                 + "."
#             )

#         # ------------------------------------------------------
#         # DATE
#         # ------------------------------------------------------

#         if (
#             "what date" in text
#             or "today's date" in text
#             or "todays date" in text
#             or text == "date"
#             or "what day is it" in text
#         ):

#             now = datetime.datetime.now()

#             self.last_intent = "date"

#             return (
#                 "Today is "
#                 + now.strftime(
#                     "%A, %d %B %Y"
#                 )
#                 + "."
#             )

#         # ------------------------------------------------------
#         # CALCULATOR
#         # ------------------------------------------------------

#         calculation = self.calculate(
#             text
#         )

#         if calculation:

#             self.last_intent = "calculator"

#             return calculation

#         # ------------------------------------------------------
#         # CONTEXTUAL QUESTION
#         # ------------------------------------------------------

#         contextual = (
#             self.contextual_question(
#                 text
#             )
#         )

#         if contextual:

#             self.last_intent = "context"

#             return contextual

#         # ------------------------------------------------------
#         # KNOWLEDGE
#         # ------------------------------------------------------

#         answer, score, category = (
#             self.search_knowledge(
#                 text
#             )
#         )

#         if answer:

#             self.last_intent = (
#                 "knowledge"
#             )

#             self.last_topic = (
#                 self.detect_topic(
#                     text,
#                     category
#                 )
#             )

#             return answer

#         # ------------------------------------------------------
#         # UNKNOWN
#         # ------------------------------------------------------

#         self.last_intent = "unknown"

#         return (
#             "I'm not sure how to answer that yet.\n\n"
#             "You can teach me using:\n"
#             "teach: question = answer\n\n"
#             "Or try:\n"
#             "search conversation Python"
#         )


import ast
import datetime
import difflib
import operator
import random
import re

from memory import ChatMemory
from settings import Settings
from knowledge import BUILT_IN_KNOWLEDGE


class YuiBot:

    def __init__(self):

        self.memory = ChatMemory()
        self.settings = Settings()

        self.last_intent = None
        self.last_topic = None
        self.last_question = None

        self.memory.new_session()

        self.responses = {

            "Friendly": {

                "greeting": [
                    "Hello!",
                    "Hi!",
                    "Hey!",
                    "Hello! How can I help?"
                ],

                "thanks": [
                    "You're welcome!",
                    "No problem!",
                    "Glad I could help!"
                ],

                "goodbye": [
                    "Goodbye!",
                    "See you later!",
                    "Bye!"
                ]
            },

            "Professional": {

                "greeting": [
                    "Hello. How may I assist you?",
                    "Hello. What would you like to know?",
                    "Good day. How can I help?"
                ],

                "thanks": [
                    "You're welcome.",
                    "You're welcome. I'm glad I could help."
                ],

                "goodbye": [
                    "Goodbye.",
                    "Have a good day.",
                    "Until next time."
                ]
            },

            "Short": {

                "greeting": [
                    "Hi!",
                    "Hello!",
                    "Hey!"
                ],

                "thanks": [
                    "You're welcome.",
                    "No problem."
                ],

                "goodbye": [
                    "Bye!",
                    "See you!"
                ]
            },

            "Casual": {

                "greeting": [
                    "Hey!",
                    "Yo!",
                    "Hi there!"
                ],

                "thanks": [
                    "No worries!",
                    "Anytime!",
                    "Sure thing!"
                ],

                "goodbye": [
                    "Later!",
                    "Bye!",
                    "See ya!"
                ]
            }
        }

        self.typos = {

            "helo": "hello",
            "helllo": "hello",
            "hllo": "hello",
            "hii": "hi",
            "hiiii": "hi",
            "heyy": "hey",

            "wht": "what",
            "whatt": "what",
            "wat": "what",
            "wut": "what",

            "whos": "who is",
            "whats": "what is",

            "ur": "your",
            "u": "you",
            "r": "are",

            "pls": "please",
            "plz": "please",
            "thx": "thanks",

            "im": "i am",
            "idk": "i do not know",

            "tim": "time",
            "todai": "today",

            "calcluate": "calculate",
            "calculte": "calculate",

            "favrite": "favorite",
            "favouritee": "favorite",

            "pyhton": "python",
            "pythn": "python",

            "databse": "database",
            "javscript": "javascript"
        }

    # ==========================================================
    # SETTINGS
    # ==========================================================

    def reload_settings(self):

        self.settings.load()

    def personality(
        self,
        category
    ):

        mode = self.settings.get(
            "personality",
            "Friendly"
        )

        group = self.responses.get(
            mode,
            self.responses[
                "Friendly"
            ]
        )

        values = group.get(
            category,
            []
        )

        if not values:
            return ""

        return random.choice(
            values
        )

    # ==========================================================
    # NORMALIZE
    # ==========================================================

    def normalize(
        self,
        text
    ):

        text = text.lower().strip()

        text = re.sub(
            r"\s+",
            " ",
            text
        )

        words = text.split()

        fixed = []

        for word in words:

            punctuation = ""

            while (
                word
                and word[-1] in ".,!?"
            ):

                punctuation = (
                    word[-1]
                    + punctuation
                )

                word = word[:-1]

            word = self.typos.get(
                word,
                word
            )

            fixed.append(
                word + punctuation
            )

        text = " ".join(
            fixed
        )

        text = re.sub(
            r"\bwhat's\b",
            "what is",
            text
        )

        text = re.sub(
            r"\bwho's\b",
            "who is",
            text
        )

        return text

    # ==========================================================
    # SIMILARITY
    # ==========================================================

    def similarity(
        self,
        a,
        b
    ):

        if not self.settings.get(
            "fuzzy_matching",
            True
        ):

            return 1.0 if a == b else 0

        a = a.lower().strip()
        b = b.lower().strip()

        if a == b:
            return 1.0

        if a in b or b in a:
            return 0.92

        ratio = difflib.SequenceMatcher(
            None,
            a,
            b
        ).ratio()

        a_words = set(
            re.findall(
                r"\b\w+\b",
                a
            )
        )

        b_words = set(
            re.findall(
                r"\b\w+\b",
                b
            )
        )

        if a_words and b_words:

            overlap = len(
                a_words & b_words
            ) / max(
                len(a_words),
                len(b_words)
            )

        else:

            overlap = 0

        return max(
            ratio,
            overlap
        )

    # ==========================================================
    # KNOWLEDGE
    # ==========================================================

    def search_knowledge(
        self,
        question
    ):

        question = self.normalize(
            question
        )

        all_knowledge = {}

        for key, value in BUILT_IN_KNOWLEDGE.items():

            all_knowledge[
                key
            ] = {
                "answer": value,
                "category": "Built-in"
            }

        all_knowledge.update(
            self.memory.get_knowledge()
        )

        if question in all_knowledge:

            item = all_knowledge[
                question
            ]

            return (
                item["answer"],
                1.0,
                item.get(
                    "category",
                    "General"
                )
            )

        best = None
        best_score = 0

        for key, item in all_knowledge.items():

            score = self.similarity(
                question,
                key
            )

            if score > best_score:

                best_score = score
                best = item

        if (
            best is not None
            and best_score >= 0.58
        ):

            return (
                best["answer"],
                best_score,
                best.get(
                    "category",
                    "General"
                )
            )

        return None, 0, None

    # ==========================================================
    # MEMORY
    # ==========================================================

    def remember_fact(
        self,
        text
    ):

        if not self.settings.get(
            "memory_enabled",
            True
        ):
            return None

        patterns = [

            r"^remember my (.+?) is (.+)$",

            r"^remember that my (.+?) is (.+)$",

            r"^my (.+?) is (.+)$"
        ]

        for pattern in patterns:

            match = re.match(
                pattern,
                text,
                re.IGNORECASE
            )

            if not match:
                continue

            key = match.group(
                1
            ).strip()

            value = match.group(
                2
            ).strip()

            if key in [
                "name"
            ]:

                continue

            self.memory.set_profile(
                key,
                value,
                "Preferences"
            )

            return (
                f"Okay, I'll remember that "
                f"your {key} is {value}."
            )

        return None

    def recall_fact(
        self,
        text
    ):

        if not self.settings.get(
            "memory_enabled",
            True
        ):
            return None

        profile = (
            self.memory.get_profile_all()
        )

        if not profile:
            return None

        match = re.match(
            r"^(?:what is|what's|tell me) my (.+?)[?!.]*$",
            text,
            re.IGNORECASE
        )

        if match:

            key = match.group(
                1
            ).strip()

            if key in profile:

                value = self.memory.get_profile(
                    key
                )

                return (
                    f"Your {key} is {value}."
                )

        return None

    def forget_fact(
        self,
        text
    ):

        if not self.settings.get(
            "memory_enabled",
            True
        ):
            return None

        match = re.match(
            r"^forget my (.+?)[?!.]*$",
            text,
            re.IGNORECASE
        )

        if not match:
            return None

        key = match.group(
            1
        ).strip()

        if self.memory.delete_profile(
            key
        ):

            return (
                f"Okay. I forgot your {key}."
            )

        return (
            f"I don't have a saved memory "
            f"for your {key}."
        )

    def show_memories(self):

        if not self.settings.get(
            "memory_enabled",
            True
        ):

            return (
                "Personal memory is disabled "
                "in Settings."
            )

        profile = (
            self.memory.get_profile_all()
        )

        if not profile:

            return (
                "I don't have any personal "
                "memories saved."
            )

        lines = [
            "Things I remember:"
        ]

        for key, item in profile.items():

            if isinstance(
                item,
                dict
            ):

                value = item.get(
                    "value",
                    ""
                )

            else:

                value = item

            lines.append(
                f"• {key}: {value}"
            )

        return "\n".join(
            lines
        )

    # ==========================================================
    # NAME
    # ==========================================================

    def extract_name(
        self,
        text
    ):

        if not self.settings.get(
            "memory_enabled",
            True
        ):
            return None

        patterns = [

            r"\bmy name is ([a-zA-Z][a-zA-Z0-9 _-]{0,30})",

            r"\bremember my name is ([a-zA-Z][a-zA-Z0-9 _-]{0,30})",

            r"\bcall me ([a-zA-Z][a-zA-Z0-9 _-]{0,30})"
        ]

        for pattern in patterns:

            match = re.search(
                pattern,
                text,
                re.IGNORECASE
            )

            if match:

                name = match.group(
                    1
                ).strip()

                name = re.split(
                    r"\b(?:and|but|because|please)\b",
                    name,
                    flags=re.IGNORECASE
                )[0].strip()

                return name

        return None

    # ==========================================================
    # CALCULATOR
    # ==========================================================

    def calculate(
        self,
        text
    ):

        original = text

        text = re.sub(
            r"^(calculate|solve|compute)\s+",
            "",
            text,
            flags=re.IGNORECASE
        )

        text = re.sub(
            r"^what is\s+",
            "",
            text,
            flags=re.IGNORECASE
        )

        replacements = {

            "multiplied by": "*",
            "divided by": "/",
            "divide by": "/",
            "plus": "+",
            "minus": "-",
            "times": "*"
        }

        for word, symbol in replacements.items():

            text = text.replace(
                word,
                symbol
            )

        text = text.replace(
            "^",
            "**"
        )

        if not re.fullmatch(
            r"[0-9\s+\-*/().%]+",
            text
        ):

            return None

        try:

            tree = ast.parse(
                text,
                mode="eval"
            )

            result = self.safe_eval(
                tree.body
            )

            if (
                isinstance(
                    result,
                    float
                )
                and result.is_integer()
            ):

                result = int(
                    result
                )

            return (
                f"The answer is {result}."
            )

        except Exception:

            if original.startswith(
                (
                    "calculate",
                    "solve",
                    "compute"
                )
            ):

                return (
                    "I couldn't calculate that."
                )

        return None

    def safe_eval(
        self,
        node
    ):

        operators = {

            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv,
            ast.Mod: operator.mod,
            ast.Pow: operator.pow,

            ast.USub: operator.neg,
            ast.UAdd: operator.pos
        }

        if isinstance(
            node,
            ast.Constant
        ):

            if isinstance(
                node.value,
                (int, float)
            ):

                return node.value

            raise ValueError

        if isinstance(
            node,
            ast.BinOp
        ):

            left = self.safe_eval(
                node.left
            )

            right = self.safe_eval(
                node.right
            )

            operation = operators.get(
                type(node.op)
            )

            if operation is None:
                raise ValueError

            return operation(
                left,
                right
            )

        if isinstance(
            node,
            ast.UnaryOp
        ):

            operation = operators.get(
                type(node.op)
            )

            if operation is None:
                raise ValueError

            return operation(
                self.safe_eval(
                    node.operand
                )
            )

        raise ValueError

    # ==========================================================
    # CONTEXT
    # ==========================================================

    def contextual_question(
        self,
        text
    ):

        if not self.settings.get(
            "context_enabled",
            True
        ):
            return None

        if not self.last_topic:
            return None

        topic = self.last_topic.lower()

        if text in [
            "who created it",
            "who made it",
            "who invented it"
        ]:

            if topic == "python":

                return (
                    "Python was created by "
                    "Guido van Rossum."
                )

        if text in [
            "what does it do",
            "what can it do"
        ]:

            if topic == "python":

                return (
                    "Python is a general-purpose "
                    "programming language used for "
                    "automation, applications, web "
                    "development, data processing, "
                    "and many other tasks."
                )

        if text in [
            "what is it",
            "tell me more"
        ]:

            answer, _, _ = (
                self.search_knowledge(
                    f"what is {topic}"
                )
            )

            return answer

        return None

    # ==========================================================
    # TOPIC
    # ==========================================================

    def detect_topic(
        self,
        text,
        category=None
    ):

        topics = [
            "python",
            "html",
            "css",
            "javascript",
            "database",
            "mysql",
            "sqlite",
            "sql",
            "computer",
            "cpu",
            "ram",
            "gpu",
            "cybersecurity",
            "encryption",
            "password",
            "tkinter",
            "pygame",
            "website",
            "api"
        ]

        for topic in topics:

            if topic in text:

                return topic

        return category

    # ==========================================================
    # COMMANDS
    # ==========================================================

    def command(
        self,
        text
    ):

        if not text.startswith(
            "/"
        ):

            return None

        parts = text.split(
            maxsplit=1
        )

        command = parts[0].lower()

        argument = ""

        if len(parts) > 1:

            argument = parts[1].strip()

        # ------------------------------------------------------
        # HELP
        # ------------------------------------------------------

        if command == "/help":

            return self.help_text()

        # ------------------------------------------------------
        # TIME
        # ------------------------------------------------------

        if command == "/time":

            now = datetime.datetime.now()

            return (
                "Current time: "
                + now.strftime(
                    "%I:%M %p"
                ).lstrip("0")
            )

        # ------------------------------------------------------
        # DATE
        # ------------------------------------------------------

        if command == "/date":

            now = datetime.datetime.now()

            return (
                "Today is "
                + now.strftime(
                    "%A, %d %B %Y"
                )
                + "."
            )

        # ------------------------------------------------------
        # MEMORY
        # ------------------------------------------------------

        if command == "/memory":

            return self.show_memories()

        # ------------------------------------------------------
        # KNOWLEDGE
        # ------------------------------------------------------

        if command == "/knowledge":

            count = len(
                self.memory.get_knowledge()
            )

            return (
                f"You have {count} "
                f"custom knowledge entries."
            )

        # ------------------------------------------------------
        # STATS
        # ------------------------------------------------------

        if command == "/stats":

            return self.statistics_text()

        # ------------------------------------------------------
        # ABOUT
        # ------------------------------------------------------

        if command == "/about":

            return self.about_text()

        # ------------------------------------------------------
        # CLEAR
        # ------------------------------------------------------

        if command == "/clear":

            return "__CLEAR_CHAT__"

        # ------------------------------------------------------
        # SEARCH
        # ------------------------------------------------------

        if command == "/search":

            if not argument:

                return (
                    "Usage:\n"
                    "/search keyword"
                )

            results = (
                self.memory.search_messages(
                    argument
                )
            )

            if not results:

                return (
                    "No matching messages found."
                )

            lines = [
                f"Found {len(results)} message(s):",
                ""
            ]

            for item in results[-10:]:

                role = item.get(
                    "role",
                    ""
                )

                content = item.get(
                    "content",
                    ""
                )

                label = (
                    "You"
                    if role == "user"
                    else "YuiBot"
                )

                lines.append(
                    f"{label}: {content}"
                )

            return "\n".join(
                lines
            )

        # ------------------------------------------------------
        # UNKNOWN
        # ------------------------------------------------------

        return (
            f"Unknown command: {command}\n\n"
            "Type /help to see available commands."
        )

    # ==========================================================
    # STATISTICS
    # ==========================================================

    def statistics_text(self):

        stats = (
            self.memory.get_statistics()
        )

        return (
            "YuiBot Statistics\n\n"
            f"User messages: "
            f"{stats['user_messages']}\n"
            f"Bot messages: "
            f"{stats['bot_messages']}\n"
            f"Sessions: "
            f"{stats['sessions']}\n"
            f"Custom knowledge: "
            f"{stats['knowledge_entries']}\n"
            f"Personal memories: "
            f"{stats['memories']}\n"
            f"Conversation messages: "
            f"{stats['conversation_messages']}"
        )

    # ==========================================================
    # HELP
    # ==========================================================

    def help_text(self):

        return """YuiBot v5 Commands

CHAT
  hello
  how are you?
  thanks
  bye

MEMORY
  my name is Alex
  remember my favorite color is blue
  what is my favorite color?
  forget my favorite color
  show my memories

KNOWLEDGE
  what is Python?
  what is HTML?
  what is a database?

TEACH
  teach: what is my favorite food = Pizza

CALCULATOR
  calculate 100 + 25
  calculate 20 * 5
  what is 100 divided by 4

COMMANDS
  /help
  /time
  /date
  /memory
  /knowledge
  /stats
  /search Python
  /about
  /clear

YuiBot is completely offline.
No AI model or external API is used."""

    # ==========================================================
    # ABOUT
    # ==========================================================

    def about_text(self):

        return (
            "YuiBot v5\n\n"
            "A Python rule-based chatbot.\n\n"
            "Features:\n"
            "• Memory\n"
            "• Knowledge\n"
            "• Context\n"
            "• Personality\n"
            "• Commands\n"
            "• Statistics\n"
            "• Fuzzy matching\n\n"
            "No AI model.\n"
            "No API.\n"
            "No internet."
        )

    # ==========================================================
    # MAIN RESPONSE
    # ==========================================================

    def respond(
        self,
        original_message
    ):

        if not original_message.strip():

            return "Please type something."

        text = self.normalize(
            original_message
        )

        self.last_question = text

        # ======================================================
        # COMMAND
        # ======================================================

        if text.startswith(
            "/"
        ):

            self.last_intent = "command"

            return self.command(
                text
            )

        # ======================================================
        # TEACH
        # ======================================================

        if text.startswith(
            "teach:"
        ):

            content = original_message[
                6:
            ].strip()

            if "=" not in content:

                return (
                    "Teaching format:\n\n"
                    "teach: question = answer"
                )

            question, answer = (
                content.split(
                    "=",
                    1
                )
            )

            question = self.normalize(
                question.strip()
            )

            answer = answer.strip()

            if not question or not answer:

                return (
                    "Question and answer "
                    "cannot be empty."
                )

            self.memory.set_knowledge(
                question,
                answer,
                "Custom"
            )

            self.last_intent = "teach"

            return (
                "Knowledge learned successfully.\n\n"
                f"Question: {question}\n"
                f"Answer: {answer}"
            )

        # ======================================================
        # HELP
        # ======================================================

        if text in [
            "help",
            "help me",
            "commands"
        ]:

            return self.help_text()

        # ======================================================
        # MEMORY
        # ======================================================

        if text in [
            "show my memories",
            "show memories",
            "what do you remember",
            "what do you remember about me"
        ]:

            return self.show_memories()

        # ======================================================
        # NAME
        # ======================================================

        name = self.extract_name(
            original_message
        )

        if name:

            self.memory.set_profile(
                "name",
                name,
                "Personal"
            )

            return (
                f"Nice to meet you, {name}! "
                "I'll remember your name."
            )

        if text in [
            "what is my name",
            "what's my name",
            "who am i",
            "do you remember my name"
        ]:

            name = self.memory.get_profile(
                "name"
            )

            if name:

                return (
                    f"Your name is {name}."
                )

            return (
                "You haven't told me your "
                "name yet."
            )

        # ======================================================
        # FORGET
        # ======================================================

        if text in [
            "forget everything",
            "forget all",
            "clear knowledge"
        ]:

            self.memory.clear_knowledge()

            return (
                "I cleared all custom knowledge."
            )

        if text in [
            "clear memories",
            "forget my memories"
        ]:

            self.memory.clear_profile()

            return (
                "I cleared my personal memories."
            )

        forgotten = self.forget_fact(
            text
        )

        if forgotten:
            return forgotten

        remembered = self.remember_fact(
            text
        )

        if remembered:
            return remembered

        recalled = self.recall_fact(
            text
        )

        if recalled:
            return recalled

        # ======================================================
        # GREETING
        # ======================================================

        if text in [
            "hello",
            "hi",
            "hey",
            "good morning",
            "good afternoon",
            "good evening"
        ]:

            self.last_intent = "greeting"

            return self.personality(
                "greeting"
            )

        # ======================================================
        # HOW ARE YOU
        # ======================================================

        if (
            "how are you" in text
            or "how do you feel" in text
        ):

            self.last_intent = (
                "how_are_you"
            )

            mode = self.settings.get(
                "personality",
                "Friendly"
            )

            if mode == "Short":

                return "I'm good!"

            if mode == "Professional":

                return (
                    "I'm operating normally "
                    "and ready to assist."
                )

            if mode == "Casual":

                return "I'm good! Ready to chat."

            return "I'm doing well! Ready to chat."

        # ======================================================
        # THANKS
        # ======================================================

        if text in [
            "thanks",
            "thank you",
            "thx"
        ]:

            return self.personality(
                "thanks"
            )

        # ======================================================
        # GOODBYE
        # ======================================================

        if (
            text in [
                "bye",
                "goodbye",
                "good night"
            ]
            or "see you" in text
        ):

            return self.personality(
                "goodbye"
            )

        # ======================================================
        # POSITIVE
        # ======================================================

        if text in [
            "good",
            "great",
            "awesome",
            "nice",
            "fine",
            "okay",
            "ok"
        ]:

            if self.last_intent == "how_are_you":

                return "Glad to hear it!"

            return "Nice!"

        # ======================================================
        # TIME
        # ======================================================

        if (
            "what time" in text
            or "current time" in text
            or text == "time"
            or "tell me the time" in text
        ):

            now = datetime.datetime.now()

            return (
                "The current time is "
                + now.strftime(
                    "%I:%M %p"
                ).lstrip("0")
                + "."
            )

        # ======================================================
        # DATE
        # ======================================================

        if (
            "what date" in text
            or "today's date" in text
            or "todays date" in text
            or text == "date"
            or "what day is it" in text
        ):

            now = datetime.datetime.now()

            return (
                "Today is "
                + now.strftime(
                    "%A, %d %B %Y"
                )
                + "."
            )

        # ======================================================
        # CALCULATOR
        # ======================================================

        calculation = self.calculate(
            text
        )

        if calculation:
            return calculation

        # ======================================================
        # CONTEXT
        # ======================================================

        contextual = (
            self.contextual_question(
                text
            )
        )

        if contextual:

            self.last_intent = "context"

            return contextual

        # ======================================================
        # KNOWLEDGE
        # ======================================================

        answer, score, category = (
            self.search_knowledge(
                text
            )
        )

        if answer:

            self.last_intent = "knowledge"

            self.last_topic = (
                self.detect_topic(
                    text,
                    category
                )
            )

            return answer

        # ======================================================
        # UNKNOWN
        # ======================================================

        self.last_intent = "unknown"

        return (
            "I'm not sure how to answer that yet.\n\n"
            "You can teach me with:\n"
            "teach: question = answer\n\n"
            "Or type /help to see my commands."
        )