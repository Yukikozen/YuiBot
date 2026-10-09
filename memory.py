# # # # import json
# # # # import os


# # # # class ChatMemory:

# # # #     def __init__(self):

# # # #         # =====================================================
# # # #         # DATA DIRECTORY
# # # #         # =====================================================

# # # #         self.data_directory = os.path.join(
# # # #             os.path.dirname(
# # # #                 os.path.abspath(__file__)
# # # #             ),
# # # #             "data"
# # # #         )

# # # #         os.makedirs(
# # # #             self.data_directory,
# # # #             exist_ok=True
# # # #         )

# # # #         # =====================================================
# # # #         # FILES
# # # #         # =====================================================

# # # #         self.chat_file = os.path.join(
# # # #             self.data_directory,
# # # #             "chat_history.json"
# # # #         )

# # # #         self.knowledge_file = os.path.join(
# # # #             self.data_directory,
# # # #             "knowledge.json"
# # # #         )

# # # #         self.profile_file = os.path.join(
# # # #             self.data_directory,
# # # #             "profile.json"
# # # #         )

# # # #         # =====================================================
# # # #         # DATA
# # # #         # =====================================================

# # # #         self.messages = []

# # # #         self.knowledge = {}

# # # #         self.profile = {}

# # # #         # =====================================================
# # # #         # LOAD
# # # #         # =====================================================

# # # #         self.load_messages()

# # # #         self.load_knowledge()

# # # #         self.load_profile()

# # # #     # =========================================================
# # # #     # CHAT HISTORY
# # # #     # =========================================================

# # # #     def add_user_message(
# # # #         self,
# # # #         message
# # # #     ):

# # # #         self.messages.append(
# # # #             {
# # # #                 "role": "user",
# # # #                 "content": message
# # # #             }
# # # #         )

# # # #         self.save_messages()

# # # #     # =========================================================
# # # #     # ASSISTANT MESSAGE
# # # #     # =========================================================

# # # #     def add_assistant_message(
# # # #         self,
# # # #         message
# # # #     ):

# # # #         self.messages.append(
# # # #             {
# # # #                 "role": "assistant",
# # # #                 "content": message
# # # #             }
# # # #         )

# # # #         self.save_messages()

# # # #     # =========================================================
# # # #     # GET MESSAGES
# # # #     # =========================================================

# # # #     def get_messages(self):

# # # #         return list(
# # # #             self.messages
# # # #         )

# # # #     # =========================================================
# # # #     # CLEAR CHAT
# # # #     # =========================================================

# # # #     def clear(self):

# # # #         self.messages = []

# # # #         self.save_messages()

# # # #     # =========================================================
# # # #     # SAVE CHAT
# # # #     # =========================================================

# # # #     def save_messages(self):

# # # #         try:

# # # #             with open(
# # # #                 self.chat_file,
# # # #                 "w",
# # # #                 encoding="utf-8"
# # # #             ) as file:

# # # #                 json.dump(
# # # #                     self.messages,
# # # #                     file,
# # # #                     indent=4,
# # # #                     ensure_ascii=False
# # # #                 )

# # # #         except Exception as error:

# # # #             print(
# # # #                 "Unable to save chat:",
# # # #                 error
# # # #             )

# # # #     # =========================================================
# # # #     # LOAD CHAT
# # # #     # =========================================================

# # # #     def load_messages(self):

# # # #         if not os.path.exists(
# # # #             self.chat_file
# # # #         ):

# # # #             self.messages = []

# # # #             return

# # # #         try:

# # # #             with open(
# # # #                 self.chat_file,
# # # #                 "r",
# # # #                 encoding="utf-8"
# # # #             ) as file:

# # # #                 data = json.load(
# # # #                     file
# # # #                 )

# # # #                 if isinstance(
# # # #                     data,
# # # #                     list
# # # #                 ):

# # # #                     self.messages = data

# # # #                 else:

# # # #                     self.messages = []

# # # #         except Exception:

# # # #             self.messages = []

# # # #     # =========================================================
# # # #     # KNOWLEDGE
# # # #     # =========================================================

# # # #     def get_knowledge(self):

# # # #         return dict(
# # # #             self.knowledge
# # # #         )

# # # #     # =========================================================
# # # #     # SAVE KNOWLEDGE
# # # #     # =========================================================

# # # #     def save_knowledge(
# # # #         self,
# # # #         knowledge
# # # #     ):

# # # #         self.knowledge = dict(
# # # #             knowledge
# # # #         )

# # # #         try:

# # # #             with open(
# # # #                 self.knowledge_file,
# # # #                 "w",
# # # #                 encoding="utf-8"
# # # #             ) as file:

# # # #                 json.dump(
# # # #                     self.knowledge,
# # # #                     file,
# # # #                     indent=4,
# # # #                     ensure_ascii=False
# # # #                 )

# # # #         except Exception as error:

# # # #             print(
# # # #                 "Unable to save knowledge:",
# # # #                 error
# # # #             )

# # # #     # =========================================================
# # # #     # LOAD KNOWLEDGE
# # # #     # =========================================================

# # # #     def load_knowledge(self):

# # # #         if not os.path.exists(
# # # #             self.knowledge_file
# # # #         ):

# # # #             self.knowledge = {}

# # # #             return

# # # #         try:

# # # #             with open(
# # # #                 self.knowledge_file,
# # # #                 "r",
# # # #                 encoding="utf-8"
# # # #             ) as file:

# # # #                 data = json.load(
# # # #                     file
# # # #                 )

# # # #                 if isinstance(
# # # #                     data,
# # # #                     dict
# # # #                 ):

# # # #                     self.knowledge = data

# # # #                 else:

# # # #                     self.knowledge = {}

# # # #         except Exception:

# # # #             self.knowledge = {}

# # # #     # =========================================================
# # # #     # CLEAR KNOWLEDGE
# # # #     # =========================================================

# # # #     def clear_knowledge(self):

# # # #         self.knowledge = {}

# # # #         self.save_knowledge(
# # # #             {}
# # # #         )

# # # #     # =========================================================
# # # #     # PROFILE
# # # #     # =========================================================

# # # #     def set_user_name(
# # # #         self,
# # # #         name
# # # #     ):

# # # #         self.profile[
# # # #             "user_name"
# # # #         ] = name

# # # #         self.save_profile()

# # # #     # =========================================================
# # # #     # GET USER NAME
# # # #     # =========================================================

# # # #     def get_user_name(self):

# # # #         return self.profile.get(
# # # #             "user_name",
# # # #             ""
# # # #         )

# # # #     # =========================================================
# # # #     # SAVE PROFILE
# # # #     # =========================================================

# # # #     def save_profile(self):

# # # #         try:

# # # #             with open(
# # # #                 self.profile_file,
# # # #                 "w",
# # # #                 encoding="utf-8"
# # # #             ) as file:

# # # #                 json.dump(
# # # #                     self.profile,
# # # #                     file,
# # # #                     indent=4,
# # # #                     ensure_ascii=False
# # # #                 )

# # # #         except Exception as error:

# # # #             print(
# # # #                 "Unable to save profile:",
# # # #                 error
# # # #             )

# # # #     # =========================================================
# # # #     # LOAD PROFILE
# # # #     # =========================================================

# # # #     def load_profile(self):

# # # #         if not os.path.exists(
# # # #             self.profile_file
# # # #         ):

# # # #             self.profile = {}

# # # #             return

# # # #         try:

# # # #             with open(
# # # #                 self.profile_file,
# # # #                 "r",
# # # #                 encoding="utf-8"
# # # #             ) as file:

# # # #                 data = json.load(
# # # #                     file
# # # #                 )

# # # #                 if isinstance(
# # # #                     data,
# # # #                     dict
# # # #                 ):

# # # #                     self.profile = data

# # # #                 else:

# # # #                     self.profile = {}

# # # #         except Exception:

# # # #             self.profile = {}

# # # #     # =========================================================
# # # #     # SAVE EVERYTHING
# # # #     # =========================================================

# # # #     def save(self):

# # # #         self.save_messages()

# # # #         self.save_knowledge(
# # # #             self.knowledge
# # # #         )

# # # #         self.save_profile()




# # # import json
# # # import os


# # # class ChatMemory:

# # #     def __init__(self):

# # #         self.base_dir = os.path.dirname(
# # #             os.path.abspath(__file__)
# # #         )

# # #         self.data_dir = os.path.join(
# # #             self.base_dir,
# # #             "data"
# # #         )

# # #         os.makedirs(
# # #             self.data_dir,
# # #             exist_ok=True
# # #         )

# # #         self.chat_file = os.path.join(
# # #             self.data_dir,
# # #             "chat_history.json"
# # #         )

# # #         self.knowledge_file = os.path.join(
# # #             self.data_dir,
# # #             "knowledge.json"
# # #         )

# # #         self.profile_file = os.path.join(
# # #             self.data_dir,
# # #             "profile.json"
# # #         )

# # #         self.messages = []
# # #         self.knowledge = {}
# # #         self.profile = {}

# # #         self.load_messages()
# # #         self.load_knowledge()
# # #         self.load_profile()

# # #     # =========================================================
# # #     # CHAT HISTORY
# # #     # =========================================================

# # #     def add_message(self, role, content):

# # #         self.messages.append({
# # #             "role": role,
# # #             "content": content
# # #         })

# # #         self.save_messages()

# # #     def add_user_message(self, content):

# # #         self.add_message(
# # #             "user",
# # #             content
# # #         )

# # #     def add_assistant_message(self, content):

# # #         self.add_message(
# # #             "assistant",
# # #             content
# # #         )

# # #     def get_messages(self):

# # #         return list(self.messages)

# # #     def clear(self):

# # #         self.messages = []

# # #         self.save_messages()

# # #     def save_messages(self):

# # #         try:

# # #             with open(
# # #                 self.chat_file,
# # #                 "w",
# # #                 encoding="utf-8"
# # #             ) as file:

# # #                 json.dump(
# # #                     self.messages,
# # #                     file,
# # #                     indent=4,
# # #                     ensure_ascii=False
# # #                 )

# # #         except Exception as error:

# # #             print(
# # #                 "Chat save error:",
# # #                 error
# # #             )

# # #     def load_messages(self):

# # #         if not os.path.exists(
# # #             self.chat_file
# # #         ):

# # #             return

# # #         try:

# # #             with open(
# # #                 self.chat_file,
# # #                 "r",
# # #                 encoding="utf-8"
# # #             ) as file:

# # #                 data = json.load(file)

# # #                 if isinstance(data, list):

# # #                     self.messages = data

# # #         except Exception as error:

# # #             print(
# # #                 "Chat load error:",
# # #                 error
# # #             )

# # #             self.messages = []

# # #     # =========================================================
# # #     # KNOWLEDGE
# # #     # =========================================================

# # #     def get_knowledge(self):

# # #         return dict(
# # #             self.knowledge
# # #         )

# # #     def save_knowledge(self, knowledge):

# # #         self.knowledge = dict(
# # #             knowledge
# # #         )

# # #         try:

# # #             with open(
# # #                 self.knowledge_file,
# # #                 "w",
# # #                 encoding="utf-8"
# # #             ) as file:

# # #                 json.dump(
# # #                     self.knowledge,
# # #                     file,
# # #                     indent=4,
# # #                     ensure_ascii=False
# # #                 )

# # #         except Exception as error:

# # #             print(
# # #                 "Knowledge save error:",
# # #                 error
# # #             )

# # #     def load_knowledge(self):

# # #         if not os.path.exists(
# # #             self.knowledge_file
# # #         ):

# # #             return

# # #         try:

# # #             with open(
# # #                 self.knowledge_file,
# # #                 "r",
# # #                 encoding="utf-8"
# # #             ) as file:

# # #                 data = json.load(file)

# # #                 if isinstance(data, dict):

# # #                     self.knowledge = data

# # #         except Exception as error:

# # #             print(
# # #                 "Knowledge load error:",
# # #                 error
# # #             )

# # #             self.knowledge = {}

# # #     def clear_knowledge(self):

# # #         self.knowledge = {}

# # #         self.save_knowledge({})

# # #     # =========================================================
# # #     # PROFILE
# # #     # =========================================================

# # #     def set_profile(self, key, value):

# # #         self.profile[key] = value

# # #         self.save_profile()

# # #     def get_profile(self, key, default=None):

# # #         return self.profile.get(
# # #             key,
# # #             default
# # #         )

# # #     def save_profile(self):

# # #         try:

# # #             with open(
# # #                 self.profile_file,
# # #                 "w",
# # #                 encoding="utf-8"
# # #             ) as file:

# # #                 json.dump(
# # #                     self.profile,
# # #                     file,
# # #                     indent=4,
# # #                     ensure_ascii=False
# # #                 )

# # #         except Exception as error:

# # #             print(
# # #                 "Profile save error:",
# # #                 error
# # #             )

# # #     def load_profile(self):

# # #         if not os.path.exists(
# # #             self.profile_file
# # #         ):

# # #             return

# # #         try:

# # #             with open(
# # #                 self.profile_file,
# # #                 "r",
# # #                 encoding="utf-8"
# # #             ) as file:

# # #                 data = json.load(file)

# # #                 if isinstance(data, dict):

# # #                     self.profile = data

# # #         except Exception as error:

# # #             print(
# # #                 "Profile load error:",
# # #                 error
# # #             )

# # #             self.profile = {}

# # #     # =========================================================
# # #     # SAVE EVERYTHING
# # #     # =========================================================

# # #     def save(self):

# # #         self.save_messages()

# # #         self.save_knowledge(
# # #             self.knowledge
# # #         )

# # #         self.save_profile()


# # import json
# # import os


# # class ChatMemory:

# #     def __init__(self, base_dir=None):

# #         if base_dir is None:
# #             base_dir = os.path.dirname(os.path.abspath(__file__))

# #         self.base_dir = base_dir
# #         self.data_dir = os.path.join(self.base_dir, "data")

# #         os.makedirs(self.data_dir, exist_ok=True)

# #         self.history_file = os.path.join(
# #             self.data_dir,
# #             "chat_history.json"
# #         )

# #         self.knowledge_file = os.path.join(
# #             self.data_dir,
# #             "knowledge.json"
# #         )

# #         self.profile_file = os.path.join(
# #             self.data_dir,
# #             "profile.json"
# #         )

# #         self.messages = []
# #         self.knowledge = {}
# #         self.profile = {}

# #         self.load_messages()
# #         self.load_knowledge()
# #         self.load_profile()

# #     # ==========================================================
# #     # GENERIC JSON
# #     # ==========================================================

# #     def _load_json(self, path, default):

# #         try:

# #             if not os.path.exists(path):
# #                 return default

# #             with open(
# #                 path,
# #                 "r",
# #                 encoding="utf-8"
# #             ) as file:

# #                 data = json.load(file)

# #             return data

# #         except Exception:

# #             return default

# #     def _save_json(self, path, data):

# #         try:

# #             with open(
# #                 path,
# #                 "w",
# #                 encoding="utf-8"
# #             ) as file:

# #                 json.dump(
# #                     data,
# #                     file,
# #                     indent=4,
# #                     ensure_ascii=False
# #                 )

# #             return True

# #         except Exception:

# #             return False

# #     # ==========================================================
# #     # CHAT HISTORY
# #     # ==========================================================

# #     def load_messages(self):

# #         data = self._load_json(
# #             self.history_file,
# #             []
# #         )

# #         if isinstance(data, list):
# #             self.messages = data
# #         else:
# #             self.messages = []

# #     def save_messages(self):

# #         return self._save_json(
# #             self.history_file,
# #             self.messages
# #         )

# #     def add_message(self, role, content):

# #         self.messages.append({
# #             "role": role,
# #             "content": content
# #         })

# #         self.save_messages()

# #     def add_user_message(self, content):

# #         self.add_message(
# #             "user",
# #             content
# #         )

# #     def add_assistant_message(self, content):

# #         self.add_message(
# #             "assistant",
# #             content
# #         )

# #     def get_messages(self):

# #         return list(self.messages)

# #     def clear(self):

# #         self.messages = []
# #         self.save_messages()

# #     # ==========================================================
# #     # LEARNED KNOWLEDGE
# #     # ==========================================================

# #     def load_knowledge(self):

# #         data = self._load_json(
# #             self.knowledge_file,
# #             {}
# #         )

# #         if isinstance(data, dict):
# #             self.knowledge = data
# #         else:
# #             self.knowledge = {}

# #     def save_knowledge(self):

# #         return self._save_json(
# #             self.knowledge_file,
# #             self.knowledge
# #         )

# #     def set_knowledge(self, question, answer):

# #         self.knowledge[question] = answer
# #         self.save_knowledge()

# #     def get_knowledge(self):

# #         return dict(self.knowledge)

# #     def remove_knowledge(self, question):

# #         if question in self.knowledge:

# #             del self.knowledge[question]
# #             self.save_knowledge()

# #             return True

# #         return False

# #     def clear_knowledge(self):

# #         self.knowledge = {}
# #         self.save_knowledge()

# #     # ==========================================================
# #     # PROFILE / PERSONAL MEMORY
# #     # ==========================================================

# #     def load_profile(self):

# #         data = self._load_json(
# #             self.profile_file,
# #             {}
# #         )

# #         if isinstance(data, dict):
# #             self.profile = data
# #         else:
# #             self.profile = {}

# #     def save_profile(self):

# #         return self._save_json(
# #             self.profile_file,
# #             self.profile
# #         )

# #     def set_profile(self, key, value):

# #         self.profile[key] = value
# #         self.save_profile()

# #     def get_profile(self, key, default=None):

# #         return self.profile.get(
# #             key,
# #             default
# #         )

# #     def get_profile_all(self):

# #         return dict(self.profile)

# #     def remove_profile(self, key):

# #         if key in self.profile:

# #             del self.profile[key]
# #             self.save_profile()

# #             return True

# #         return False

# #     def clear_profile(self):

# #         self.profile = {}
# #         self.save_profile()

# #     # ==========================================================
# #     # SAVE EVERYTHING
# #     # ==========================================================

# #     def save(self):

# #         self.save_messages()
# #         self.save_knowledge()
# #         self.save_profile()


# import json
# import os
# from datetime import datetime


# class ChatMemory:

#     def __init__(self, base_dir=None):

#         if base_dir is None:
#             base_dir = os.path.dirname(
#                 os.path.abspath(__file__)
#             )

#         self.base_dir = base_dir

#         self.data_dir = os.path.join(
#             self.base_dir,
#             "data"
#         )

#         os.makedirs(
#             self.data_dir,
#             exist_ok=True
#         )

#         self.history_file = os.path.join(
#             self.data_dir,
#             "chat_history.json"
#         )

#         self.knowledge_file = os.path.join(
#             self.data_dir,
#             "knowledge.json"
#         )

#         self.profile_file = os.path.join(
#             self.data_dir,
#             "profile.json"
#         )

#         self.messages = []
#         self.knowledge = {}
#         self.profile = {}

#         self.load_messages()
#         self.load_knowledge()
#         self.load_profile()

#     # ==========================================================
#     # JSON HELPERS
#     # ==========================================================

#     def load_json(self, filename, default):

#         try:

#             if not os.path.exists(filename):
#                 return default

#             with open(
#                 filename,
#                 "r",
#                 encoding="utf-8"
#             ) as file:

#                 data = json.load(file)

#             return data

#         except Exception:

#             return default

#     def save_json(self, filename, data):

#         try:

#             with open(
#                 filename,
#                 "w",
#                 encoding="utf-8"
#             ) as file:

#                 json.dump(
#                     data,
#                     file,
#                     indent=4,
#                     ensure_ascii=False
#                 )

#             return True

#         except Exception:

#             return False

#     # ==========================================================
#     # CHAT HISTORY
#     # ==========================================================

#     def load_messages(self):

#         data = self.load_json(
#             self.history_file,
#             []
#         )

#         if isinstance(data, list):
#             self.messages = data
#         else:
#             self.messages = []

#     def save_messages(self):

#         return self.save_json(
#             self.history_file,
#             self.messages
#         )

#     def add_message(
#         self,
#         role,
#         content
#     ):

#         self.messages.append({
#             "role": role,
#             "content": content,
#             "timestamp": datetime.now().isoformat(
#                 timespec="seconds"
#             )
#         })

#         self.save_messages()

#     def add_user_message(
#         self,
#         content
#     ):

#         self.add_message(
#             "user",
#             content
#         )

#     def add_assistant_message(
#         self,
#         content
#     ):

#         self.add_message(
#             "assistant",
#             content
#         )

#     def get_messages(self):

#         return list(
#             self.messages
#         )

#     def clear_messages(self):

#         self.messages = []

#         self.save_messages()

#     # ==========================================================
#     # KNOWLEDGE
#     # ==========================================================

#     def load_knowledge(self):

#         data = self.load_json(
#             self.knowledge_file,
#             {}
#         )

#         if isinstance(data, dict):
#             self.knowledge = data
#         else:
#             self.knowledge = {}

#     def save_knowledge(self):

#         return self.save_json(
#             self.knowledge_file,
#             self.knowledge
#         )

#     def set_knowledge(
#         self,
#         question,
#         answer,
#         category="General"
#     ):

#         self.knowledge[question] = {
#             "answer": answer,
#             "category": category
#         }

#         self.save_knowledge()

#     def get_knowledge(self):

#         return dict(
#             self.knowledge
#         )

#     def delete_knowledge(
#         self,
#         question
#     ):

#         if question in self.knowledge:

#             del self.knowledge[question]

#             self.save_knowledge()

#             return True

#         return False

#     def clear_knowledge(self):

#         self.knowledge = {}

#         self.save_knowledge()

#     def export_knowledge(
#         self,
#         filename
#     ):

#         return self.save_json(
#             filename,
#             self.knowledge
#         )

#     def import_knowledge(
#         self,
#         filename
#     ):

#         data = self.load_json(
#             filename,
#             None
#         )

#         if not isinstance(data, dict):
#             return False

#         self.knowledge = data

#         self.save_knowledge()

#         return True

#     # ==========================================================
#     # PERSONAL MEMORY
#     # ==========================================================

#     def load_profile(self):

#         data = self.load_json(
#             self.profile_file,
#             {}
#         )

#         if isinstance(data, dict):
#             self.profile = data
#         else:
#             self.profile = {}

#     def save_profile(self):

#         return self.save_json(
#             self.profile_file,
#             self.profile
#         )

#     def set_profile(
#         self,
#         key,
#         value,
#         category="Personal"
#     ):

#         self.profile[key] = {
#             "value": value,
#             "category": category
#         }

#         self.save_profile()

#     def get_profile(
#         self,
#         key,
#         default=None
#     ):

#         item = self.profile.get(
#             key
#         )

#         if isinstance(item, dict):

#             return item.get(
#                 "value",
#                 default
#             )

#         return item if item is not None else default

#     def get_profile_entry(
#         self,
#         key
#     ):

#         return self.profile.get(
#             key
#         )

#     def get_profile_all(self):

#         return dict(
#             self.profile
#         )

#     def delete_profile(
#         self,
#         key
#     ):

#         if key in self.profile:

#             del self.profile[key]

#             self.save_profile()

#             return True

#         return False

#     def clear_profile(self):

#         self.profile = {}

#         self.save_profile()

#     # ==========================================================
#     # SEARCH CONVERSATION
#     # ==========================================================

#     def search_messages(
#         self,
#         query
#     ):

#         query = query.lower().strip()

#         if not query:
#             return []

#         results = []

#         for message in self.messages:

#             content = str(
#                 message.get(
#                     "content",
#                     ""
#                 )
#             )

#             if query in content.lower():

#                 results.append(
#                     message
#                 )

#         return results

#     # ==========================================================
#     # SAVE EVERYTHING
#     # ==========================================================

#     def save(self):

#         self.save_messages()
#         self.save_knowledge()
#         self.save_profile()


import json
import os
from datetime import datetime


class ChatMemory:

    def __init__(self, base_dir=None):

        if base_dir is None:

            base_dir = os.path.dirname(
                os.path.abspath(__file__)
            )

        self.base_dir = base_dir

        self.data_dir = os.path.join(
            self.base_dir,
            "data"
        )

        os.makedirs(
            self.data_dir,
            exist_ok=True
        )

        self.history_file = os.path.join(
            self.data_dir,
            "chat_history.json"
        )

        self.knowledge_file = os.path.join(
            self.data_dir,
            "knowledge.json"
        )

        self.profile_file = os.path.join(
            self.data_dir,
            "profile.json"
        )

        self.statistics_file = os.path.join(
            self.data_dir,
            "statistics.json"
        )

        self.messages = []
        self.knowledge = {}
        self.profile = {}

        self.statistics = {
            "user_messages": 0,
            "bot_messages": 0,
            "sessions": 0
        }

        self.load_messages()
        self.load_knowledge()
        self.load_profile()
        self.load_statistics()

    # ==========================================================
    # JSON
    # ==========================================================

    def load_json(
        self,
        filename,
        default
    ):

        try:

            if not os.path.exists(filename):
                return default

            with open(
                filename,
                "r",
                encoding="utf-8"
            ) as file:

                return json.load(file)

        except Exception:

            return default

    def save_json(
        self,
        filename,
        data
    ):

        try:

            with open(
                filename,
                "w",
                encoding="utf-8"
            ) as file:

                json.dump(
                    data,
                    file,
                    indent=4,
                    ensure_ascii=False
                )

            return True

        except Exception:

            return False

    # ==========================================================
    # CHAT
    # ==========================================================

    def load_messages(self):

        data = self.load_json(
            self.history_file,
            []
        )

        if isinstance(
            data,
            list
        ):

            self.messages = data

        else:

            self.messages = []

    def save_messages(self):

        return self.save_json(
            self.history_file,
            self.messages
        )

    def add_message(
        self,
        role,
        content
    ):

        self.messages.append({
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat(
                timespec="seconds"
            )
        })

        if role == "user":

            self.statistics[
                "user_messages"
            ] += 1

        elif role == "assistant":

            self.statistics[
                "bot_messages"
            ] += 1

        self.save_messages()
        self.save_statistics()

    def add_user_message(
        self,
        content
    ):

        self.add_message(
            "user",
            content
        )

    def add_assistant_message(
        self,
        content
    ):

        self.add_message(
            "assistant",
            content
        )

    def get_messages(self):

        return list(
            self.messages
        )

    def clear_messages(self):

        self.messages = []

        self.save_messages()

    # ==========================================================
    # KNOWLEDGE
    # ==========================================================

    def load_knowledge(self):

        data = self.load_json(
            self.knowledge_file,
            {}
        )

        if isinstance(
            data,
            dict
        ):

            self.knowledge = data

        else:

            self.knowledge = {}

    def save_knowledge(self):

        return self.save_json(
            self.knowledge_file,
            self.knowledge
        )

    def set_knowledge(
        self,
        question,
        answer,
        category="General"
    ):

        self.knowledge[
            question
        ] = {
            "answer": answer,
            "category": category
        }

        self.save_knowledge()

    def get_knowledge(self):

        return dict(
            self.knowledge
        )

    def delete_knowledge(
        self,
        question
    ):

        if question in self.knowledge:

            del self.knowledge[
                question
            ]

            self.save_knowledge()

            return True

        return False

    def clear_knowledge(self):

        self.knowledge = {}

        self.save_knowledge()

    def export_knowledge(
        self,
        filename
    ):

        return self.save_json(
            filename,
            self.knowledge
        )

    def import_knowledge(
        self,
        filename
    ):

        data = self.load_json(
            filename,
            None
        )

        if not isinstance(
            data,
            dict
        ):

            return False

        self.knowledge = data

        self.save_knowledge()

        return True

    # ==========================================================
    # PROFILE
    # ==========================================================

    def load_profile(self):

        data = self.load_json(
            self.profile_file,
            {}
        )

        if isinstance(
            data,
            dict
        ):

            self.profile = data

        else:

            self.profile = {}

    def save_profile(self):

        return self.save_json(
            self.profile_file,
            self.profile
        )

    def set_profile(
        self,
        key,
        value,
        category="Personal"
    ):

        self.profile[
            key
        ] = {
            "value": value,
            "category": category
        }

        self.save_profile()

    def get_profile(
        self,
        key,
        default=None
    ):

        item = self.profile.get(
            key
        )

        if isinstance(
            item,
            dict
        ):

            return item.get(
                "value",
                default
            )

        if item is not None:

            return item

        return default

    def get_profile_all(self):

        return dict(
            self.profile
        )

    def delete_profile(
        self,
        key
    ):

        if key in self.profile:

            del self.profile[
                key
            ]

            self.save_profile()

            return True

        return False

    def clear_profile(self):

        self.profile = {}

        self.save_profile()

    # ==========================================================
    # SEARCH
    # ==========================================================

    def search_messages(
        self,
        query
    ):

        query = query.lower().strip()

        if not query:
            return []

        results = []

        for message in self.messages:

            content = str(
                message.get(
                    "content",
                    ""
                )
            )

            if query in content.lower():

                results.append(
                    message
                )

        return results

    # ==========================================================
    # STATISTICS
    # ==========================================================

    def load_statistics(self):

        data = self.load_json(
            self.statistics_file,
            self.statistics
        )

        if isinstance(
            data,
            dict
        ):

            self.statistics.update(
                data
            )

    def save_statistics(self):

        return self.save_json(
            self.statistics_file,
            self.statistics
        )

    def new_session(self):

        self.statistics[
            "sessions"
        ] += 1

        self.save_statistics()

    def get_statistics(self):

        stats = dict(
            self.statistics
        )

        stats[
            "knowledge_entries"
        ] = len(
            self.knowledge
        )

        stats[
            "memories"
        ] = len(
            self.profile
        )

        stats[
            "conversation_messages"
        ] = len(
            self.messages
        )

        return stats

    # ==========================================================
    # SAVE ALL
    # ==========================================================

    def save(self):

        self.save_messages()
        self.save_knowledge()
        self.save_profile()
        self.save_statistics()