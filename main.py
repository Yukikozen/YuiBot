# # # # import tkinter as tk
# # # # from tkinter import messagebox
# # # # from datetime import datetime

# # # # from chatbot import YuiBot


# # # # class YuiBotApp:

# # # #     def __init__(self, root):

# # # #         self.root = root

# # # #         self.root.title("YuiBot")
# # # #         self.root.geometry("1000x700")
# # # #         self.root.minsize(800, 600)

# # # #         self.bg_color = "#171717"
# # # #         self.sidebar_color = "#202020"
# # # #         self.chat_color = "#1e1e1e"
# # # #         self.input_color = "#2a2a2a"
# # # #         self.user_color = "#343541"
# # # #         self.bot_color = "#262626"
# # # #         self.text_color = "#ffffff"
# # # #         self.secondary_text = "#aaaaaa"
# # # #         self.button_color = "#8b3d5c"
# # # #         self.button_hover = "#a64b6d"

# # # #         self.root.configure(
# # # #             bg=self.bg_color
# # # #         )

# # # #         # =====================================================
# # # #         # CHATBOT
# # # #         # =====================================================

# # # #         self.bot = YuiBot()

# # # #         # =====================================================
# # # #         # MAIN GRID
# # # #         # =====================================================

# # # #         self.root.grid_columnconfigure(
# # # #             1,
# # # #             weight=1
# # # #         )

# # # #         self.root.grid_rowconfigure(
# # # #             0,
# # # #             weight=1
# # # #         )

# # # #         # =====================================================
# # # #         # SIDEBAR
# # # #         # =====================================================

# # # #         self.create_sidebar()

# # # #         # =====================================================
# # # #         # CHAT AREA
# # # #         # =====================================================

# # # #         self.create_chat_area()

# # # #         # =====================================================
# # # #         # LOAD CHAT
# # # #         # =====================================================

# # # #         self.load_previous_chat()

# # # #         # =====================================================
# # # #         # WINDOW CLOSE
# # # #         # =====================================================

# # # #         self.root.protocol(
# # # #             "WM_DELETE_WINDOW",
# # # #             self.close_application
# # # #         )

# # # #     # =========================================================
# # # #     # SIDEBAR
# # # #     # =========================================================

# # # #     def create_sidebar(self):

# # # #         self.sidebar = tk.Frame(
# # # #             self.root,
# # # #             bg=self.sidebar_color,
# # # #             width=230
# # # #         )

# # # #         self.sidebar.grid(
# # # #             row=0,
# # # #             column=0,
# # # #             sticky="nsew"
# # # #         )

# # # #         self.sidebar.grid_propagate(
# # # #             False
# # # #         )

# # # #         # -----------------------------------------------------
# # # #         # LOGO
# # # #         # -----------------------------------------------------

# # # #         logo = tk.Label(
# # # #             self.sidebar,
# # # #             text="YuiBot",
# # # #             bg=self.sidebar_color,
# # # #             fg=self.text_color,
# # # #             font=("Segoe UI", 26, "bold")
# # # #         )

# # # #         logo.pack(
# # # #             pady=(35, 5)
# # # #         )

# # # #         subtitle = tk.Label(
# # # #             self.sidebar,
# # # #             text="Rule-Based Chatbot",
# # # #             bg=self.sidebar_color,
# # # #             fg=self.secondary_text,
# # # #             font=("Segoe UI", 10)
# # # #         )

# # # #         subtitle.pack(
# # # #             pady=(0, 30)
# # # #         )

# # # #         # -----------------------------------------------------
# # # #         # NEW CHAT
# # # #         # -----------------------------------------------------

# # # #         new_chat_button = tk.Button(
# # # #             self.sidebar,
# # # #             text="+  New Chat",
# # # #             command=self.new_chat,
# # # #             bg=self.button_color,
# # # #             fg="white",
# # # #             activebackground=self.button_hover,
# # # #             activeforeground="white",
# # # #             relief="flat",
# # # #             bd=0,
# # # #             font=("Segoe UI", 11, "bold"),
# # # #             cursor="hand2"
# # # #         )

# # # #         new_chat_button.pack(
# # # #             padx=20,
# # # #             pady=5,
# # # #             fill="x",
# # # #             ipady=10
# # # #         )

# # # #         # -----------------------------------------------------
# # # #         # HELP
# # # #         # -----------------------------------------------------

# # # #         help_button = tk.Button(
# # # #             self.sidebar,
# # # #             text="Help",
# # # #             command=self.show_help,
# # # #             bg=self.sidebar_color,
# # # #             fg=self.text_color,
# # # #             activebackground="#303030",
# # # #             activeforeground="white",
# # # #             relief="flat",
# # # #             bd=0,
# # # #             font=("Segoe UI", 10),
# # # #             cursor="hand2"
# # # #         )

# # # #         help_button.pack(
# # # #             padx=20,
# # # #             pady=(15, 5),
# # # #             fill="x",
# # # #             ipady=7
# # # #         )

# # # #         # -----------------------------------------------------
# # # #         # ABOUT
# # # #         # -----------------------------------------------------

# # # #         about_button = tk.Button(
# # # #             self.sidebar,
# # # #             text="About YuiBot",
# # # #             command=self.show_about,
# # # #             bg=self.sidebar_color,
# # # #             fg=self.text_color,
# # # #             activebackground="#303030",
# # # #             activeforeground="white",
# # # #             relief="flat",
# # # #             bd=0,
# # # #             font=("Segoe UI", 10),
# # # #             cursor="hand2"
# # # #         )

# # # #         about_button.pack(
# # # #             padx=20,
# # # #             pady=5,
# # # #             fill="x",
# # # #             ipady=7
# # # #         )

# # # #         # -----------------------------------------------------
# # # #         # STATUS
# # # #         # -----------------------------------------------------

# # # #         status_frame = tk.Frame(
# # # #             self.sidebar,
# # # #             bg=self.sidebar_color
# # # #         )

# # # #         status_frame.pack(
# # # #             side="bottom",
# # # #             fill="x",
# # # #             padx=20,
# # # #             pady=20
# # # #         )

# # # #         status_title = tk.Label(
# # # #             status_frame,
# # # #             text="STATUS",
# # # #             bg=self.sidebar_color,
# # # #             fg="#777777",
# # # #             font=("Segoe UI", 8, "bold")
# # # #         )

# # # #         status_title.pack(
# # # #             anchor="w"
# # # #         )

# # # #         status = tk.Label(
# # # #             status_frame,
# # # #             text="● Local / Offline",
# # # #             bg=self.sidebar_color,
# # # #             fg="#62c370",
# # # #             font=("Segoe UI", 10)
# # # #         )

# # # #         status.pack(
# # # #             anchor="w",
# # # #             pady=(3, 0)
# # # #         )

# # # #         # -----------------------------------------------------
# # # #         # CLEAR CHAT
# # # #         # -----------------------------------------------------

# # # #         clear_button = tk.Button(
# # # #             self.sidebar,
# # # #             text="Clear Conversation",
# # # #             command=self.clear_chat,
# # # #             bg="#632b2b",
# # # #             fg="white",
# # # #             activebackground="#803838",
# # # #             activeforeground="white",
# # # #             relief="flat",
# # # #             bd=0,
# # # #             font=("Segoe UI", 10),
# # # #             cursor="hand2"
# # # #         )

# # # #         clear_button.pack(
# # # #             side="bottom",
# # # #             padx=20,
# # # #             pady=(0, 10),
# # # #             fill="x",
# # # #             ipady=8
# # # #         )

# # # #     # =========================================================
# # # #     # CHAT AREA
# # # #     # =========================================================

# # # #     def create_chat_area(self):

# # # #         self.chat_area = tk.Frame(
# # # #             self.root,
# # # #             bg=self.chat_color
# # # #         )

# # # #         self.chat_area.grid(
# # # #             row=0,
# # # #             column=1,
# # # #             sticky="nsew"
# # # #         )

# # # #         self.chat_area.grid_columnconfigure(
# # # #             0,
# # # #             weight=1
# # # #         )

# # # #         self.chat_area.grid_rowconfigure(
# # # #             1,
# # # #             weight=1
# # # #         )

# # # #         # -----------------------------------------------------
# # # #         # HEADER
# # # #         # -----------------------------------------------------

# # # #         header = tk.Frame(
# # # #             self.chat_area,
# # # #             bg=self.chat_color,
# # # #             height=70
# # # #         )

# # # #         header.grid(
# # # #             row=0,
# # # #             column=0,
# # # #             sticky="ew"
# # # #         )

# # # #         title = tk.Label(
# # # #             header,
# # # #             text="YuiBot",
# # # #             bg=self.chat_color,
# # # #             fg=self.text_color,
# # # #             font=("Segoe UI", 20, "bold")
# # # #         )

# # # #         title.pack(
# # # #             side="left",
# # # #             padx=25,
# # # #             pady=20
# # # #         )

# # # #         self.header_status = tk.Label(
# # # #             header,
# # # #             text="Offline • Rule-based",
# # # #             bg=self.chat_color,
# # # #             fg=self.secondary_text,
# # # #             font=("Segoe UI", 9)
# # # #         )

# # # #         self.header_status.pack(
# # # #             side="left",
# # # #             pady=20
# # # #         )

# # # #         # -----------------------------------------------------
# # # #         # CHAT CONTAINER
# # # #         # -----------------------------------------------------

# # # #         self.chat_container = tk.Frame(
# # # #             self.chat_area,
# # # #             bg=self.chat_color
# # # #         )

# # # #         self.chat_container.grid(
# # # #             row=1,
# # # #             column=0,
# # # #             sticky="nsew",
# # # #             padx=15,
# # # #             pady=5
# # # #         )

# # # #         self.chat_container.grid_columnconfigure(
# # # #             0,
# # # #             weight=1
# # # #         )

# # # #         self.chat_container.grid_rowconfigure(
# # # #             0,
# # # #             weight=1
# # # #         )

# # # #         # -----------------------------------------------------
# # # #         # CHAT TEXT
# # # #         # -----------------------------------------------------

# # # #         self.chat_text = tk.Text(
# # # #             self.chat_container,
# # # #             bg=self.chat_color,
# # # #             fg=self.text_color,
# # # #             insertbackground="white",
# # # #             selectbackground="#555555",
# # # #             relief="flat",
# # # #             bd=0,
# # # #             wrap="word",
# # # #             font=("Segoe UI", 11),
# # # #             padx=20,
# # # #             pady=20,
# # # #             state="disabled"
# # # #         )

# # # #         self.chat_text.grid(
# # # #             row=0,
# # # #             column=0,
# # # #             sticky="nsew"
# # # #         )

# # # #         scrollbar = tk.Scrollbar(
# # # #             self.chat_container,
# # # #             command=self.chat_text.yview
# # # #         )

# # # #         scrollbar.grid(
# # # #             row=0,
# # # #             column=1,
# # # #             sticky="ns"
# # # #         )

# # # #         self.chat_text.configure(
# # # #             yscrollcommand=scrollbar.set
# # # #         )

# # # #         # -----------------------------------------------------
# # # #         # TEXT TAGS
# # # #         # -----------------------------------------------------

# # # #         self.chat_text.tag_configure(
# # # #             "user_name",
# # # #             foreground="#8db4ff",
# # # #             font=("Segoe UI", 10, "bold"),
# # # #             spacing1=15
# # # #         )

# # # #         self.chat_text.tag_configure(
# # # #             "bot_name",
# # # #             foreground="#8ee6a8",
# # # #             font=("Segoe UI", 10, "bold"),
# # # #             spacing1=15
# # # #         )

# # # #         self.chat_text.tag_configure(
# # # #             "message",
# # # #             foreground=self.text_color,
# # # #             font=("Segoe UI", 11),
# # # #             spacing3=12
# # # #         )

# # # #         self.chat_text.tag_configure(
# # # #             "system",
# # # #             foreground=self.secondary_text,
# # # #             font=("Segoe UI", 9, "italic"),
# # # #             justify="center"
# # # #         )

# # # #         # -----------------------------------------------------
# # # #         # INPUT AREA
# # # #         # -----------------------------------------------------

# # # #         input_frame = tk.Frame(
# # # #             self.chat_area,
# # # #             bg=self.chat_color
# # # #         )

# # # #         input_frame.grid(
# # # #             row=2,
# # # #             column=0,
# # # #             sticky="ew",
# # # #             padx=20,
# # # #             pady=(5, 20)
# # # #         )

# # # #         input_frame.grid_columnconfigure(
# # # #             0,
# # # #             weight=1
# # # #         )

# # # #         self.input_box = tk.Text(
# # # #             input_frame,
# # # #             height=3,
# # # #             bg=self.input_color,
# # # #             fg=self.text_color,
# # # #             insertbackground="white",
# # # #             relief="flat",
# # # #             bd=0,
# # # #             wrap="word",
# # # #             font=("Segoe UI", 11),
# # # #             padx=15,
# # # #             pady=12
# # # #         )

# # # #         self.input_box.grid(
# # # #             row=0,
# # # #             column=0,
# # # #             sticky="ew",
# # # #             padx=(0, 10)
# # # #         )

# # # #         self.input_box.bind(
# # # #             "<Control-Return>",
# # # #             self.send_message
# # # #         )

# # # #         self.send_button = tk.Button(
# # # #             input_frame,
# # # #             text="Send",
# # # #             command=self.send_message,
# # # #             bg=self.button_color,
# # # #             fg="white",
# # # #             activebackground=self.button_hover,
# # # #             activeforeground="white",
# # # #             relief="flat",
# # # #             bd=0,
# # # #             font=("Segoe UI", 10, "bold"),
# # # #             cursor="hand2",
# # # #             width=10
# # # #         )

# # # #         self.send_button.grid(
# # # #             row=0,
# # # #             column=1,
# # # #             sticky="ns"
# # # #         )

# # # #         # -----------------------------------------------------
# # # #         # HINT
# # # #         # -----------------------------------------------------

# # # #         hint = tk.Label(
# # # #             self.chat_area,
# # # #             text="Press Ctrl + Enter to send",
# # # #             bg=self.chat_color,
# # # #             fg="#666666",
# # # #             font=("Segoe UI", 8)
# # # #         )

# # # #         hint.grid(
# # # #             row=3,
# # # #             column=0,
# # # #             pady=(0, 8)
# # # #         )

# # # #     # =========================================================
# # # #     # LOAD PREVIOUS CHAT
# # # #     # =========================================================

# # # #     def load_previous_chat(self):

# # # #         history = self.bot.memory.get_messages()

# # # #         if not history:

# # # #             self.display_system(
# # # #                 "Welcome to YuiBot.\n"
# # # #                 "I am a rule-based chatbot and do not use an AI model."
# # # #             )

# # # #             self.display_bot(
# # # #                 "Hello! I'm YuiBot. "
# # # #                 "Type 'help' to see what I can do."
# # # #             )

# # # #             return

# # # #         for item in history:

# # # #             role = item.get("role")
# # # #             message = item.get("content", "")

# # # #             if role == "user":

# # # #                 self.display_user(
# # # #                     message
# # # #                 )

# # # #             elif role == "assistant":

# # # #                 self.display_bot(
# # # #                     message
# # # #                 )

# # # #     # =========================================================
# # # #     # DISPLAY USER
# # # #     # =========================================================

# # # #     def display_user(self, message):

# # # #         self.chat_text.configure(
# # # #             state="normal"
# # # #         )

# # # #         self.chat_text.insert(
# # # #             "end",
# # # #             "You\n",
# # # #             "user_name"
# # # #         )

# # # #         self.chat_text.insert(
# # # #             "end",
# # # #             message + "\n",
# # # #             "message"
# # # #         )

# # # #         self.chat_text.configure(
# # # #             state="disabled"
# # # #         )

# # # #         self.chat_text.see(
# # # #             "end"
# # # #         )

# # # #     # =========================================================
# # # #     # DISPLAY BOT
# # # #     # =========================================================

# # # #     def display_bot(self, message):

# # # #         self.chat_text.configure(
# # # #             state="normal"
# # # #         )

# # # #         self.chat_text.insert(
# # # #             "end",
# # # #             "YuiBot\n",
# # # #             "bot_name"
# # # #         )

# # # #         self.chat_text.insert(
# # # #             "end",
# # # #             message + "\n",
# # # #             "message"
# # # #         )

# # # #         self.chat_text.configure(
# # # #             state="disabled"
# # # #         )

# # # #         self.chat_text.see(
# # # #             "end"
# # # #         )

# # # #     # =========================================================
# # # #     # DISPLAY SYSTEM
# # # #     # =========================================================

# # # #     def display_system(self, message):

# # # #         self.chat_text.configure(
# # # #             state="normal"
# # # #         )

# # # #         self.chat_text.insert(
# # # #             "end",
# # # #             message + "\n\n",
# # # #             "system"
# # # #         )

# # # #         self.chat_text.configure(
# # # #             state="disabled"
# # # #         )

# # # #         self.chat_text.see(
# # # #             "end"
# # # #         )

# # # #     # =========================================================
# # # #     # SEND MESSAGE
# # # #     # =========================================================

# # # #     def send_message(self, event=None):

# # # #         message = self.input_box.get(
# # # #             "1.0",
# # # #             "end"
# # # #         ).strip()

# # # #         if not message:
# # # #             return "break"

# # # #         # Clear input
# # # #         self.input_box.delete(
# # # #             "1.0",
# # # #             "end"
# # # #         )

# # # #         # Display user
# # # #         self.display_user(
# # # #             message
# # # #         )

# # # #         # Process chatbot
# # # #         response = self.bot.respond(
# # # #             message
# # # #         )

# # # #         # Display response
# # # #         self.display_bot(
# # # #             response
# # # #         )

# # # #         # Save
# # # #         self.bot.memory.add_user_message(
# # # #             message
# # # #         )

# # # #         self.bot.memory.add_assistant_message(
# # # #             response
# # # #         )

# # # #         self.input_box.focus()

# # # #         return "break"

# # # #     # =========================================================
# # # #     # NEW CHAT
# # # #     # =========================================================

# # # #     def new_chat(self):

# # # #         answer = messagebox.askyesno(
# # # #             "New Chat",
# # # #             "Start a new conversation?"
# # # #         )

# # # #         if not answer:
# # # #             return

# # # #         self.bot.memory.clear()

# # # #         self.chat_text.configure(
# # # #             state="normal"
# # # #         )

# # # #         self.chat_text.delete(
# # # #             "1.0",
# # # #             "end"
# # # #         )

# # # #         self.chat_text.configure(
# # # #             state="disabled"
# # # #         )

# # # #         self.display_system(
# # # #             "New conversation started."
# # # #         )

# # # #         self.display_bot(
# # # #             "Hello! I'm YuiBot. "
# # # #             "How can I help you?"
# # # #         )

# # # #     # =========================================================
# # # #     # CLEAR CHAT
# # # #     # =========================================================

# # # #     def clear_chat(self):

# # # #         answer = messagebox.askyesno(
# # # #             "Clear Conversation",
# # # #             "Delete the saved conversation?"
# # # #         )

# # # #         if not answer:
# # # #             return

# # # #         self.bot.memory.clear()

# # # #         self.chat_text.configure(
# # # #             state="normal"
# # # #         )

# # # #         self.chat_text.delete(
# # # #             "1.0",
# # # #             "end"
# # # #         )

# # # #         self.chat_text.configure(
# # # #             state="disabled"
# # # #         )

# # # #         self.display_system(
# # # #             "Conversation cleared."
# # # #         )

# # # #     # =========================================================
# # # #     # HELP
# # # #     # =========================================================

# # # #     def show_help(self):

# # # #         help_text = """
# # # # YuiBot Commands
# # # # ================

# # # # help
# # # # Show this help message.

# # # # hello
# # # # Say hello to YuiBot.

# # # # time
# # # # Show the current time.

# # # # date
# # # # Show today's date.

# # # # calculate 10 + 5
# # # # Perform a calculation.

# # # # remember my name is John
# # # # Save your name.

# # # # what is my name
# # # # Ask YuiBot what it remembers.

# # # # teach: question = answer
# # # # Teach YuiBot a new response.

# # # # forget everything
# # # # Clear learned knowledge.

# # # # clear
# # # # Clear the conversation.

# # # # about
# # # # Show information about YuiBot.

# # # # exit
# # # # Close YuiBot.

# # # # You can also simply chat using normal
# # # # sentences containing supported keywords.
# # # # """

# # # #         messagebox.showinfo(
# # # #             "YuiBot Help",
# # # #             help_text
# # # #         )

# # # #     # =========================================================
# # # #     # ABOUT
# # # #     # =========================================================

# # # #     def show_about(self):

# # # #         messagebox.showinfo(
# # # #             "About YuiBot",
# # # #             "YuiBot v1.0\n\n"
# # # #             "A Python rule-based chatbot.\n\n"
# # # #             "No OpenAI\n"
# # # #             "No Ollama\n"
# # # #             "No Llama\n"
# # # #             "No Qwen\n"
# # # #             "No external AI model\n"
# # # #             "No API key\n\n"
# # # #             "Everything runs locally."
# # # #         )

# # # #     # =========================================================
# # # #     # CLOSE
# # # #     # =========================================================

# # # #     def close_application(self):

# # # #         self.bot.memory.save()

# # # #         self.root.destroy()


# # # # # =============================================================
# # # # # START
# # # # # =============================================================

# # # # def main():

# # # #     root = tk.Tk()

# # # #     app = YuiBotApp(
# # # #         root
# # # #     )

# # # #     root.mainloop()


# # # # if __name__ == "__main__":
# # # #     main()



# # # import tkinter as tk
# # # from tkinter import messagebox

# # # from chatbot import YuiBot


# # # class YuiBotApp:

# # #     def __init__(self, root):

# # #         self.root = root

# # #         # =====================================================
# # #         # WINDOW
# # #         # =====================================================

# # #         self.root.title(
# # #             "YuiBot v2"
# # #         )

# # #         self.root.geometry(
# # #             "1100x720"
# # #         )

# # #         self.root.minsize(
# # #             850,
# # #             600
# # #         )

# # #         # =====================================================
# # #         # COLORS
# # #         # =====================================================

# # #         self.bg = "#171717"
# # #         self.sidebar = "#202020"
# # #         self.chat = "#1e1e1e"
# # #         self.input_bg = "#292929"

# # #         self.text = "#ffffff"
# # #         self.secondary = "#999999"

# # #         self.accent = "#8b3d5c"
# # #         self.accent_hover = "#a84b6e"

# # #         self.user_name_color = "#7fb0ff"
# # #         self.bot_name_color = "#75d89a"

# # #         # =====================================================
# # #         # ROOT
# # #         # =====================================================

# # #         self.root.configure(
# # #             bg=self.bg
# # #         )

# # #         self.root.grid_columnconfigure(
# # #             1,
# # #             weight=1
# # #         )

# # #         self.root.grid_rowconfigure(
# # #             0,
# # #             weight=1
# # #         )

# # #         # =====================================================
# # #         # BOT
# # #         # =====================================================

# # #         self.bot = YuiBot()

# # #         # =====================================================
# # #         # UI
# # #         # =====================================================

# # #         self.create_sidebar()

# # #         self.create_chat()

# # #         # =====================================================
# # #         # LOAD HISTORY
# # #         # =====================================================

# # #         self.load_history()

# # #         # =====================================================
# # #         # CLOSE
# # #         # =====================================================

# # #         self.root.protocol(
# # #             "WM_DELETE_WINDOW",
# # #             self.close
# # #         )

# # #     # =========================================================
# # #     # SIDEBAR
# # #     # =========================================================

# # #     def create_sidebar(self):

# # #         self.sidebar_frame = tk.Frame(
# # #             self.root,
# # #             bg=self.sidebar,
# # #             width=240
# # #         )

# # #         self.sidebar_frame.grid(
# # #             row=0,
# # #             column=0,
# # #             sticky="nsew"
# # #         )

# # #         self.sidebar_frame.grid_propagate(
# # #             False
# # #         )

# # #         # -----------------------------------------------------
# # #         # LOGO
# # #         # -----------------------------------------------------

# # #         tk.Label(
# # #             self.sidebar_frame,
# # #             text="YuiBot",
# # #             bg=self.sidebar,
# # #             fg=self.text,
# # #             font=(
# # #                 "Segoe UI",
# # #                 27,
# # #                 "bold"
# # #             )
# # #         ).pack(
# # #             pady=(35, 0)
# # #         )

# # #         tk.Label(
# # #             self.sidebar_frame,
# # #             text="Version 2.0",
# # #             bg=self.sidebar,
# # #             fg=self.secondary,
# # #             font=(
# # #                 "Segoe UI",
# # #                 9
# # #             )
# # #         ).pack(
# # #             pady=(0, 30)
# # #         )

# # #         # -----------------------------------------------------
# # #         # NEW CHAT
# # #         # -----------------------------------------------------

# # #         self.create_button(
# # #             self.sidebar_frame,
# # #             "+  New Chat",
# # #             self.new_chat
# # #         ).pack(
# # #             padx=20,
# # #             fill="x",
# # #             ipady=10
# # #         )

# # #         # -----------------------------------------------------
# # #         # HELP
# # #         # -----------------------------------------------------

# # #         self.create_button(
# # #             self.sidebar_frame,
# # #             "Help",
# # #             self.show_help,
# # #             secondary=True
# # #         ).pack(
# # #             padx=20,
# # #             pady=(15, 5),
# # #             fill="x",
# # #             ipady=7
# # #         )

# # #         # -----------------------------------------------------
# # #         # ABOUT
# # #         # -----------------------------------------------------

# # #         self.create_button(
# # #             self.sidebar_frame,
# # #             "About",
# # #             self.show_about,
# # #             secondary=True
# # #         ).pack(
# # #             padx=20,
# # #             pady=5,
# # #             fill="x",
# # #             ipady=7
# # #         )

# # #         # -----------------------------------------------------
# # #         # STATUS
# # #         # -----------------------------------------------------

# # #         status_frame = tk.Frame(
# # #             self.sidebar_frame,
# # #             bg=self.sidebar
# # #         )

# # #         status_frame.pack(
# # #             side="bottom",
# # #             padx=20,
# # #             pady=(0, 20),
# # #             fill="x"
# # #         )

# # #         tk.Label(
# # #             status_frame,
# # #             text="CHATBOT ENGINE",
# # #             bg=self.sidebar,
# # #             fg="#666666",
# # #             font=(
# # #                 "Segoe UI",
# # #                 8,
# # #                 "bold"
# # #             )
# # #         ).pack(
# # #             anchor="w"
# # #         )

# # #         tk.Label(
# # #             status_frame,
# # #             text="● Rule-based / Offline",
# # #             bg=self.sidebar,
# # #             fg="#6bd17e",
# # #             font=(
# # #                 "Segoe UI",
# # #                 10
# # #             )
# # #         ).pack(
# # #             anchor="w",
# # #             pady=(3, 0)
# # #         )

# # #         # -----------------------------------------------------
# # #         # CLEAR
# # #         # -----------------------------------------------------

# # #         self.create_button(
# # #             self.sidebar_frame,
# # #             "Clear Conversation",
# # #             self.clear_chat,
# # #             danger=True
# # #         ).pack(
# # #             side="bottom",
# # #             padx=20,
# # #             pady=(0, 10),
# # #             fill="x",
# # #             ipady=8
# # #         )

# # #     # =========================================================
# # #     # BUTTON
# # #     # =========================================================

# # #     def create_button(
# # #         self,
# # #         parent,
# # #         text,
# # #         command,
# # #         secondary=False,
# # #         danger=False
# # #     ):

# # #         if danger:

# # #             bg = "#632c2c"
# # #             hover = "#803838"

# # #         elif secondary:

# # #             bg = self.sidebar
# # #             hover = "#303030"

# # #         else:

# # #             bg = self.accent
# # #             hover = self.accent_hover

# # #         button = tk.Button(
# # #             parent,
# # #             text=text,
# # #             command=command,
# # #             bg=bg,
# # #             fg="white",
# # #             activebackground=hover,
# # #             activeforeground="white",
# # #             relief="flat",
# # #             bd=0,
# # #             cursor="hand2",
# # #             font=(
# # #                 "Segoe UI",
# # #                 10,
# # #                 "bold" if not secondary else "normal"
# # #             )
# # #         )

# # #         return button

# # #     # =========================================================
# # #     # CHAT
# # #     # =========================================================

# # #     def create_chat(self):

# # #         self.chat_frame = tk.Frame(
# # #             self.root,
# # #             bg=self.chat
# # #         )

# # #         self.chat_frame.grid(
# # #             row=0,
# # #             column=1,
# # #             sticky="nsew"
# # #         )

# # #         self.chat_frame.grid_columnconfigure(
# # #             0,
# # #             weight=1
# # #         )

# # #         self.chat_frame.grid_rowconfigure(
# # #             1,
# # #             weight=1
# # #         )

# # #         # =====================================================
# # #         # HEADER
# # #         # =====================================================

# # #         header = tk.Frame(
# # #             self.chat_frame,
# # #             bg=self.chat,
# # #             height=70
# # #         )

# # #         header.grid(
# # #             row=0,
# # #             column=0,
# # #             sticky="ew"
# # #         )

# # #         tk.Label(
# # #             header,
# # #             text="YuiBot",
# # #             bg=self.chat,
# # #             fg=self.text,
# # #             font=(
# # #                 "Segoe UI",
# # #                 21,
# # #                 "bold"
# # #             )
# # #         ).pack(
# # #             side="left",
# # #             padx=(25, 10),
# # #             pady=20
# # #         )

# # #         tk.Label(
# # #             header,
# # #             text="Offline chatbot",
# # #             bg=self.chat,
# # #             fg=self.secondary,
# # #             font=(
# # #                 "Segoe UI",
# # #                 9
# # #             )
# # #         ).pack(
# # #             side="left"
# # #         )

# # #         # =====================================================
# # #         # CHAT BOX
# # #         # =====================================================

# # #         chat_container = tk.Frame(
# # #             self.chat_frame,
# # #             bg=self.chat
# # #         )

# # #         chat_container.grid(
# # #             row=1,
# # #             column=0,
# # #             sticky="nsew",
# # #             padx=15
# # #         )

# # #         chat_container.grid_columnconfigure(
# # #             0,
# # #             weight=1
# # #         )

# # #         chat_container.grid_rowconfigure(
# # #             0,
# # #             weight=1
# # #         )

# # #         self.chat_box = tk.Text(
# # #             chat_container,
# # #             bg=self.chat,
# # #             fg=self.text,
# # #             insertbackground="white",
# # #             selectbackground="#555555",
# # #             relief="flat",
# # #             bd=0,
# # #             wrap="word",
# # #             font=(
# # #                 "Segoe UI",
# # #                 11
# # #             ),
# # #             padx=20,
# # #             pady=15,
# # #             state="disabled"
# # #         )

# # #         self.chat_box.grid(
# # #             row=0,
# # #             column=0,
# # #             sticky="nsew"
# # #         )

# # #         scrollbar = tk.Scrollbar(
# # #             chat_container,
# # #             command=self.chat_box.yview
# # #         )

# # #         scrollbar.grid(
# # #             row=0,
# # #             column=1,
# # #             sticky="ns"
# # #         )

# # #         self.chat_box.configure(
# # #             yscrollcommand=scrollbar.set
# # #         )

# # #         # Tags

# # #         self.chat_box.tag_configure(
# # #             "user",
# # #             foreground=self.user_name_color,
# # #             font=(
# # #                 "Segoe UI",
# # #                 10,
# # #                 "bold"
# # #             ),
# # #             spacing1=15
# # #         )

# # #         self.chat_box.tag_configure(
# # #             "bot",
# # #             foreground=self.bot_name_color,
# # #             font=(
# # #                 "Segoe UI",
# # #                 10,
# # #                 "bold"
# # #             ),
# # #             spacing1=15
# # #         )

# # #         self.chat_box.tag_configure(
# # #             "message",
# # #             foreground=self.text,
# # #             font=(
# # #                 "Segoe UI",
# # #                 11
# # #             ),
# # #             spacing3=12
# # #         )

# # #         self.chat_box.tag_configure(
# # #             "system",
# # #             foreground=self.secondary,
# # #             font=(
# # #                 "Segoe UI",
# # #                 9,
# # #                 "italic"
# # #             ),
# # #             justify="center",
# # #             spacing3=15
# # #         )

# # #         # =====================================================
# # #         # INPUT
# # #         # =====================================================

# # #         input_container = tk.Frame(
# # #             self.chat_frame,
# # #             bg=self.chat
# # #         )

# # #         input_container.grid(
# # #             row=2,
# # #             column=0,
# # #             sticky="ew",
# # #             padx=20,
# # #             pady=(10, 3)
# # #         )

# # #         input_container.grid_columnconfigure(
# # #             0,
# # #             weight=1
# # #         )

# # #         self.input_box = tk.Text(
# # #             input_container,
# # #             height=3,
# # #             bg=self.input_bg,
# # #             fg=self.text,
# # #             insertbackground="white",
# # #             relief="flat",
# # #             bd=0,
# # #             wrap="word",
# # #             font=(
# # #                 "Segoe UI",
# # #                 11
# # #             ),
# # #             padx=15,
# # #             pady=12
# # #         )

# # #         self.input_box.grid(
# # #             row=0,
# # #             column=0,
# # #             sticky="ew",
# # #             padx=(0, 10)
# # #         )

# # #         self.input_box.bind(
# # #             "<Control-Return>",
# # #             self.send
# # #         )

# # #         self.send_button = tk.Button(
# # #             input_container,
# # #             text="Send",
# # #             command=self.send,
# # #             bg=self.accent,
# # #             fg="white",
# # #             activebackground=self.accent_hover,
# # #             activeforeground="white",
# # #             relief="flat",
# # #             bd=0,
# # #             cursor="hand2",
# # #             font=(
# # #                 "Segoe UI",
# # #                 10,
# # #                 "bold"
# # #             ),
# # #             width=10
# # #         )

# # #         self.send_button.grid(
# # #             row=0,
# # #             column=1,
# # #             sticky="ns"
# # #         )

# # #         tk.Label(
# # #             self.chat_frame,
# # #             text="Ctrl + Enter to send",
# # #             bg=self.chat,
# # #             fg="#666666",
# # #             font=(
# # #                 "Segoe UI",
# # #                 8
# # #             )
# # #         ).grid(
# # #             row=3,
# # #             column=0,
# # #             pady=(0, 8)
# # #         )

# # #     # =========================================================
# # #     # LOAD HISTORY
# # #     # =========================================================

# # #     def load_history(self):

# # #         history = self.bot.memory.get_messages()

# # #         if not history:

# # #             self.display_system(
# # #                 "Welcome to YuiBot v2.\n"
# # #                 "No AI model is being used."
# # #             )

# # #             self.display_bot(
# # #                 "Hello! I'm YuiBot. "
# # #                 "Type 'help' to see what I can do."
# # #             )

# # #             return

# # #         for item in history:

# # #             if item["role"] == "user":

# # #                 self.display_user(
# # #                     item["content"]
# # #                 )

# # #             elif item["role"] == "assistant":

# # #                 self.display_bot(
# # #                     item["content"]
# # #                 )

# # #     # =========================================================
# # #     # DISPLAY USER
# # #     # =========================================================

# # #     def display_user(self, message):

# # #         self.chat_box.configure(
# # #             state="normal"
# # #         )

# # #         self.chat_box.insert(
# # #             "end",
# # #             "You\n",
# # #             "user"
# # #         )

# # #         self.chat_box.insert(
# # #             "end",
# # #             message + "\n\n",
# # #             "message"
# # #         )

# # #         self.chat_box.configure(
# # #             state="disabled"
# # #         )

# # #         self.chat_box.see(
# # #             "end"
# # #         )

# # #     # =========================================================
# # #     # DISPLAY BOT
# # #     # =========================================================

# # #     def display_bot(self, message):

# # #         self.chat_box.configure(
# # #             state="normal"
# # #         )

# # #         self.chat_box.insert(
# # #             "end",
# # #             "YuiBot\n",
# # #             "bot"
# # #         )

# # #         self.chat_box.insert(
# # #             "end",
# # #             message + "\n\n",
# # #             "message"
# # #         )

# # #         self.chat_box.configure(
# # #             state="disabled"
# # #         )

# # #         self.chat_box.see(
# # #             "end"
# # #         )

# # #     # =========================================================
# # #     # DISPLAY SYSTEM
# # #     # =========================================================

# # #     def display_system(self, message):

# # #         self.chat_box.configure(
# # #             state="normal"
# # #         )

# # #         self.chat_box.insert(
# # #             "end",
# # #             message + "\n\n",
# # #             "system"
# # #         )

# # #         self.chat_box.configure(
# # #             state="disabled"
# # #         )

# # #         self.chat_box.see(
# # #             "end"
# # #         )

# # #     # =========================================================
# # #     # SEND
# # #     # =========================================================

# # #     def send(self, event=None):

# # #         message = self.input_box.get(
# # #             "1.0",
# # #             "end"
# # #         ).strip()

# # #         if not message:

# # #             return "break"

# # #         self.input_box.delete(
# # #             "1.0",
# # #             "end"
# # #         )

# # #         self.display_user(
# # #             message
# # #         )

# # #         response = self.bot.respond(
# # #             message
# # #         )

# # #         self.display_bot(
# # #             response
# # #         )

# # #         self.bot.memory.add_user_message(
# # #             message
# # #         )

# # #         self.bot.memory.add_assistant_message(
# # #             response
# # #         )

# # #         self.input_box.focus()

# # #         return "break"

# # #     # =========================================================
# # #     # NEW CHAT
# # #     # =========================================================

# # #     def new_chat(self):

# # #         answer = messagebox.askyesno(
# # #             "New Chat",
# # #             "Start a new conversation?"
# # #         )

# # #         if not answer:

# # #             return

# # #         self.bot.memory.clear()

# # #         self.chat_box.configure(
# # #             state="normal"
# # #         )

# # #         self.chat_box.delete(
# # #             "1.0",
# # #             "end"
# # #         )

# # #         self.chat_box.configure(
# # #             state="disabled"
# # #         )

# # #         self.bot.last_intent = None

# # #         self.display_system(
# # #             "New conversation started."
# # #         )

# # #         self.display_bot(
# # #             "Hello! How can I help you?"
# # #         )

# # #     # =========================================================
# # #     # CLEAR
# # #     # =========================================================

# # #     def clear_chat(self):

# # #         answer = messagebox.askyesno(
# # #             "Clear Conversation",
# # #             "Delete the current conversation?"
# # #         )

# # #         if not answer:

# # #             return

# # #         self.bot.memory.clear()

# # #         self.chat_box.configure(
# # #             state="normal"
# # #         )

# # #         self.chat_box.delete(
# # #             "1.0",
# # #             "end"
# # #         )

# # #         self.chat_box.configure(
# # #             state="disabled"
# # #         )

# # #         self.display_system(
# # #             "Conversation cleared."
# # #         )

# # #     # =========================================================
# # #     # HELP
# # #     # =========================================================

# # #     def show_help(self):

# # #         messagebox.showinfo(
# # #             "YuiBot Help",
# # #             "YuiBot v2\n\n"

# # #             "Examples:\n\n"

# # #             "hello\n"
# # #             "helo\n"
# # #             "what is your name?\n"
# # #             "who are you?\n"
# # #             "what can you do?\n\n"

# # #             "Memory:\n"
# # #             "my name is Alex\n"
# # #             "what is my name?\n\n"

# # #             "Utilities:\n"
# # #             "what time is it?\n"
# # #             "what is today's date?\n"
# # #             "calculate 25 + 50\n\n"

# # #             "Teaching:\n"
# # #             "teach: what is pizza = Pizza is food.\n\n"

# # #             "Commands:\n"
# # #             "help\n"
# # #             "about\n"
# # #             "forget everything"
# # #         )

# # #     # =========================================================
# # #     # ABOUT
# # #     # =========================================================

# # #     def show_about(self):

# # #         messagebox.showinfo(
# # #             "About YuiBot",
# # #             "YuiBot v2.0\n\n"

# # #             "A custom rule-based chatbot "
# # #             "written completely in Python.\n\n"

# # #             "No OpenAI\n"
# # #             "No Ollama\n"
# # #             "No Llama\n"
# # #             "No Qwen\n"
# # #             "No AI model\n"
# # #             "No API\n"
# # #             "No internet required"
# # #         )

# # #     # =========================================================
# # #     # CLOSE
# # #     # =========================================================

# # #     def close(self):

# # #         self.bot.memory.save()

# # #         self.root.destroy()


# # # # =============================================================
# # # # MAIN
# # # # =============================================================

# # # def main():

# # #     root = tk.Tk()

# # #     YuiBotApp(
# # #         root
# # #     )

# # #     root.mainloop()


# # # if __name__ == "__main__":

# # #     main()


# # import tkinter as tk
# # from tkinter import messagebox
# # from datetime import datetime

# # from chatbot import YuiBot


# # class YuiBotApp:

# #     def __init__(self, root):

# #         self.root = root

# #         self.root.title(
# #             "YuiBot"
# #         )

# #         self.root.geometry(
# #             "1100x720"
# #         )

# #         self.root.minsize(
# #             850,
# #             600
# #         )

# #         # ======================================================
# #         # COLORS
# #         # ======================================================

# #         self.bg_color = "#171717"
# #         self.sidebar_color = "#202020"
# #         self.chat_color = "#1e1e1e"
# #         self.input_color = "#292929"

# #         self.accent_color = "#8b3d5c"

# #         self.text_color = "#f0f0f0"
# #         self.secondary_color = "#aaaaaa"
# #         self.border_color = "#333333"

# #         # ======================================================
# #         # BOT
# #         # ======================================================

# #         self.bot = YuiBot()

# #         # ======================================================
# #         # WINDOW
# #         # ======================================================

# #         self.root.configure(
# #             bg=self.bg_color
# #         )

# #         self.root.protocol(
# #             "WM_DELETE_WINDOW",
# #             self.close
# #         )

# #         self.build_ui()

# #         self.load_chat()

# #     # ==========================================================
# #     # UI
# #     # ==========================================================

# #     def build_ui(self):

# #         # ======================================================
# #         # SIDEBAR
# #         # ======================================================

# #         self.sidebar = tk.Frame(
# #             self.root,
# #             bg=self.sidebar_color,
# #             width=220
# #         )

# #         self.sidebar.pack(
# #             side="left",
# #             fill="y"
# #         )

# #         self.sidebar.pack_propagate(
# #             False
# #         )

# #         # ------------------------------------------------------
# #         # LOGO
# #         # ------------------------------------------------------

# #         title = tk.Label(
# #             self.sidebar,
# #             text="YuiBot",
# #             font=("Segoe UI", 24, "bold"),
# #             fg=self.text_color,
# #             bg=self.sidebar_color
# #         )

# #         title.pack(
# #             pady=(28, 2)
# #         )

# #         version = tk.Label(
# #             self.sidebar,
# #             text="Version 3.0",
# #             font=("Segoe UI", 9),
# #             fg=self.secondary_color,
# #             bg=self.sidebar_color
# #         )

# #         version.pack(
# #             pady=(0, 25)
# #         )

# #         # ------------------------------------------------------
# #         # BUTTON HELPER
# #         # ------------------------------------------------------

# #         def sidebar_button(
# #             text,
# #             command
# #         ):

# #             button = tk.Button(
# #                 self.sidebar,
# #                 text=text,
# #                 command=command,
# #                 font=("Segoe UI", 10),
# #                 fg=self.text_color,
# #                 bg=self.sidebar_color,
# #                 activebackground=self.accent_color,
# #                 activeforeground="white",
# #                 relief="flat",
# #                 bd=0,
# #                 anchor="w",
# #                 padx=22,
# #                 pady=12,
# #                 cursor="hand2"
# #             )

# #             button.pack(
# #                 fill="x"
# #             )

# #             return button

# #         # ------------------------------------------------------
# #         # SIDEBAR BUTTONS
# #         # ------------------------------------------------------

# #         sidebar_button(
# #             "＋  New Chat",
# #             self.new_chat
# #         )

# #         sidebar_button(
# #             "⌕  Memories",
# #             self.show_memories
# #         )

# #         sidebar_button(
# #             "?  Help",
# #             self.show_help
# #         )

# #         sidebar_button(
# #             "ⓘ  About",
# #             self.show_about
# #         )

# #         # ------------------------------------------------------
# #         # BOTTOM
# #         # ------------------------------------------------------

# #         bottom = tk.Frame(
# #             self.sidebar,
# #             bg=self.sidebar_color
# #         )

# #         bottom.pack(
# #             side="bottom",
# #             fill="x",
# #             pady=15
# #         )

# #         status = tk.Label(
# #             bottom,
# #             text="●  Rule-based / Offline",
# #             font=("Segoe UI", 9),
# #             fg="#6fcf97",
# #             bg=self.sidebar_color
# #         )

# #         status.pack(
# #             pady=(0, 10)
# #         )

# #         clear_button = tk.Button(
# #             bottom,
# #             text="Clear Conversation",
# #             command=self.clear_chat,
# #             font=("Segoe UI", 9),
# #             fg="#dddddd",
# #             bg="#292929",
# #             activebackground="#3a3a3a",
# #             activeforeground="white",
# #             relief="flat",
# #             bd=0,
# #             padx=10,
# #             pady=8,
# #             cursor="hand2"
# #         )

# #         clear_button.pack(
# #             padx=15,
# #             fill="x"
# #         )

# #         # ======================================================
# #         # MAIN AREA
# #         # ======================================================

# #         self.main_frame = tk.Frame(
# #             self.root,
# #             bg=self.chat_color
# #         )

# #         self.main_frame.pack(
# #             side="right",
# #             fill="both",
# #             expand=True
# #         )

# #         # ======================================================
# #         # HEADER
# #         # ======================================================

# #         header = tk.Frame(
# #             self.main_frame,
# #             bg=self.chat_color,
# #             height=65
# #         )

# #         header.pack(
# #             fill="x"
# #         )

# #         header.pack_propagate(
# #             False
# #         )

# #         header_title = tk.Label(
# #             header,
# #             text="YuiBot",
# #             font=("Segoe UI", 16, "bold"),
# #             fg=self.text_color,
# #             bg=self.chat_color
# #         )

# #         header_title.pack(
# #             side="left",
# #             padx=25,
# #             pady=(15, 0)
# #         )

# #         header_status = tk.Label(
# #             header,
# #             text="Offline chatbot • Python rules",
# #             font=("Segoe UI", 9),
# #             fg=self.secondary_color,
# #             bg=self.chat_color
# #         )

# #         header_status.pack(
# #             side="left",
# #             padx=(8, 0),
# #             pady=(17, 0)
# #         )

# #         # ======================================================
# #         # CHAT AREA
# #         # ======================================================

# #         chat_container = tk.Frame(
# #             self.main_frame,
# #             bg=self.chat_color
# #         )

# #         chat_container.pack(
# #             fill="both",
# #             expand=True,
# #             padx=20,
# #             pady=(0, 10)
# #         )

# #         self.chat_box = tk.Text(
# #             chat_container,
# #             wrap="word",
# #             font=("Segoe UI", 11),
# #             bg=self.chat_color,
# #             fg=self.text_color,
# #             insertbackground="white",
# #             selectbackground=self.accent_color,
# #             relief="flat",
# #             bd=0,
# #             padx=15,
# #             pady=15,
# #             state="disabled"
# #         )

# #         self.chat_box.pack(
# #             side="left",
# #             fill="both",
# #             expand=True
# #         )

# #         scrollbar = tk.Scrollbar(
# #             chat_container,
# #             command=self.chat_box.yview
# #         )

# #         scrollbar.pack(
# #             side="right",
# #             fill="y"
# #         )

# #         self.chat_box.configure(
# #             yscrollcommand=scrollbar.set
# #         )

# #         # ======================================================
# #         # CHAT TAGS
# #         # ======================================================

# #         self.chat_box.tag_configure(
# #             "user_name",
# #             foreground="#d98ca8",
# #             font=("Segoe UI", 10, "bold")
# #         )

# #         self.chat_box.tag_configure(
# #             "bot_name",
# #             foreground="#ffffff",
# #             font=("Segoe UI", 10, "bold")
# #         )

# #         self.chat_box.tag_configure(
# #             "message",
# #             foreground=self.text_color,
# #             font=("Segoe UI", 11),
# #             spacing3=8
# #         )

# #         self.chat_box.tag_configure(
# #             "system",
# #             foreground=self.secondary_color,
# #             font=("Segoe UI", 9, "italic")
# #         )

# #         # ======================================================
# #         # INPUT AREA
# #         # ======================================================

# #         input_container = tk.Frame(
# #             self.main_frame,
# #             bg=self.chat_color
# #         )

# #         input_container.pack(
# #             fill="x",
# #             padx=20,
# #             pady=(0, 20)
# #         )

# #         self.input_box = tk.Text(
# #             input_container,
# #             height=3,
# #             wrap="word",
# #             font=("Segoe UI", 11),
# #             bg=self.input_color,
# #             fg=self.text_color,
# #             insertbackground="white",
# #             relief="flat",
# #             bd=0,
# #             padx=12,
# #             pady=10
# #         )

# #         self.input_box.pack(
# #             side="left",
# #             fill="both",
# #             expand=True
# #         )

# #         self.send_button = tk.Button(
# #             input_container,
# #             text="Send",
# #             command=self.send,
# #             font=("Segoe UI", 10, "bold"),
# #             fg="white",
# #             bg=self.accent_color,
# #             activebackground="#a64b6d",
# #             activeforeground="white",
# #             relief="flat",
# #             bd=0,
# #             width=9,
# #             cursor="hand2"
# #         )

# #         self.send_button.pack(
# #             side="right",
# #             padx=(10, 0),
# #             fill="y"
# #         )

# #         # ======================================================
# #         # KEYBOARD
# #         # ======================================================

# #         self.input_box.bind(
# #             "<Control-Return>",
# #             self.send_event
# #         )

# #         self.root.bind(
# #             "<Control-l>",
# #             lambda event: self.clear_chat()
# #         )

# #         self.input_box.focus_set()

# #     # ==========================================================
# #     # CHAT DISPLAY
# #     # ==========================================================

# #     def add_message(
# #         self,
# #         sender,
# #         message,
# #         tag
# #     ):

# #         self.chat_box.configure(
# #             state="normal"
# #         )

# #         self.chat_box.insert(
# #             "end",
# #             sender + "\n",
# #             tag
# #         )

# #         self.chat_box.insert(
# #             "end",
# #             message + "\n\n",
# #             "message"
# #         )

# #         self.chat_box.configure(
# #             state="disabled"
# #         )

# #         self.chat_box.see(
# #             "end"
# #         )

# #     def add_system_message(
# #         self,
# #         message
# #     ):

# #         self.chat_box.configure(
# #             state="normal"
# #         )

# #         self.chat_box.insert(
# #             "end",
# #             message + "\n\n",
# #             "system"
# #         )

# #         self.chat_box.configure(
# #             state="disabled"
# #         )

# #         self.chat_box.see(
# #             "end"
# #         )

# #     # ==========================================================
# #     # SEND
# #     # ==========================================================

# #     def send_event(self, event):

# #         self.send()

# #         return "break"

# #     def send(self):

# #         message = self.input_box.get(
# #             "1.0",
# #             "end"
# #         ).strip()

# #         if not message:
# #             return

# #         self.input_box.delete(
# #             "1.0",
# #             "end"
# #         )

# #         self.add_message(
# #             "You",
# #             message,
# #             "user_name"
# #         )

# #         self.bot.memory.add_user_message(
# #             message
# #         )

# #         response = self.bot.respond(
# #             message
# #         )

# #         self.add_message(
# #             "YuiBot",
# #             response,
# #             "bot_name"
# #         )

# #         self.bot.memory.add_assistant_message(
# #             response
# #         )

# #     # ==========================================================
# #     # LOAD CHAT
# #     # ==========================================================

# #     def load_chat(self):

# #         messages = self.bot.memory.get_messages()

# #         if not messages:

# #             self.add_system_message(
# #                 "Welcome to YuiBot v3.\n"
# #                 "I am an offline rule-based chatbot "
# #                 "written in Python.\n\n"
# #                 "Try: hello, what is Python?, "
# #                 "remember my favorite color is blue"
# #             )

# #             return

# #         for message in messages:

# #             role = message.get(
# #                 "role",
# #                 ""
# #             )

# #             content = message.get(
# #                 "content",
# #                 ""
# #             )

# #             if role == "user":

# #                 self.add_message(
# #                     "You",
# #                     content,
# #                     "user_name"
# #                 )

# #             elif role == "assistant":

# #                 self.add_message(
# #                     "YuiBot",
# #                     content,
# #                     "bot_name"
# #                 )

# #     # ==========================================================
# #     # NEW CHAT
# #     # ==========================================================

# #     def new_chat(self):

# #         self.bot.memory.clear()

# #         self.bot.last_intent = None
# #         self.bot.last_topic = None
# #         self.bot.last_user_message = ""

# #         self.chat_box.configure(
# #             state="normal"
# #         )

# #         self.chat_box.delete(
# #             "1.0",
# #             "end"
# #         )

# #         self.chat_box.configure(
# #             state="disabled"
# #         )

# #         self.add_system_message(
# #             "New conversation started."
# #         )

# #         self.input_box.focus_set()

# #     # ==========================================================
# #     # CLEAR CONVERSATION
# #     # ==========================================================

# #     def clear_chat(self):

# #         result = messagebox.askyesno(
# #             "Clear Conversation",
# #             "Are you sure you want to clear the conversation?"
# #         )

# #         if not result:
# #             return

# #         self.bot.memory.clear()

# #         self.chat_box.configure(
# #             state="normal"
# #         )

# #         self.chat_box.delete(
# #             "1.0",
# #             "end"
# #         )

# #         self.chat_box.configure(
# #             state="disabled"
# #         )

# #         self.add_system_message(
# #             "Conversation cleared."
# #         )

# #     # ==========================================================
# #     # MEMORIES
# #     # ==========================================================

# #     def show_memories(self):

# #         memories = self.bot.show_memories()

# #         messagebox.showinfo(
# #             "YuiBot Memories",
# #             memories
# #         )

# #     # ==========================================================
# #     # HELP
# #     # ==========================================================

# #     def show_help(self):

# #         messagebox.showinfo(
# #             "YuiBot Help",
# #             self.bot.help_text()
# #         )

# #     # ==========================================================
# #     # ABOUT
# #     # ==========================================================

# #     def show_about(self):

# #         messagebox.showinfo(
# #             "About YuiBot",
# #             """YuiBot v3

# # An offline rule-based chatbot
# # built entirely with Python.

# # Features:

# # • Personal memory
# # • Custom knowledge
# # • Fuzzy matching
# # • Context handling
# # • Calculator
# # • Date and time
# # • Tkinter GUI

# # No AI model.
# # No OpenAI.
# # No API.
# # No internet required."""
# #         )

# #     # ==========================================================
# #     # CLOSE
# #     # ==========================================================

# #     def close(self):

# #         self.bot.memory.save()

# #         self.root.destroy()


# # # ==============================================================
# # # MAIN
# # # ==============================================================

# # def main():

# #     root = tk.Tk()

# #     app = YuiBotApp(
# #         root
# #     )

# #     root.mainloop()


# # if __name__ == "__main__":

# #     main()


# import tkinter as tk
# from tkinter import messagebox

# from chatbot import YuiBot
# from knowledge_manager import KnowledgeManager


# class YuiBotApp:

#     def __init__(
#         self,
#         root
#     ):

#         self.root = root

#         self.root.title(
#             "YuiBot"
#         )

#         self.root.geometry(
#             "1150x750"
#         )

#         self.root.minsize(
#             850,
#             600
#         )

#         # ======================================================
#         # COLORS
#         # ======================================================

#         self.bg_color = "#171717"
#         self.sidebar_color = "#202020"
#         self.chat_color = "#1e1e1e"
#         self.input_color = "#292929"

#         self.accent_color = "#8b3d5c"

#         self.text_color = "#f0f0f0"
#         self.secondary_color = "#aaaaaa"

#         # ======================================================
#         # BOT
#         # ======================================================

#         self.bot = YuiBot()

#         self.build_ui()

#         self.load_chat()

#         self.root.protocol(
#             "WM_DELETE_WINDOW",
#             self.close
#         )

#     # ==========================================================
#     # BUILD UI
#     # ==========================================================

#     def build_ui(self):

#         # ======================================================
#         # SIDEBAR
#         # ======================================================

#         self.sidebar = tk.Frame(
#             self.root,
#             bg=self.sidebar_color,
#             width=230
#         )

#         self.sidebar.pack(
#             side="left",
#             fill="y"
#         )

#         self.sidebar.pack_propagate(
#             False
#         )

#         # ------------------------------------------------------
#         # TITLE
#         # ------------------------------------------------------

#         tk.Label(
#             self.sidebar,
#             text="YuiBot",
#             font=(
#                 "Segoe UI",
#                 24,
#                 "bold"
#             ),
#             fg=self.text_color,
#             bg=self.sidebar_color
#         ).pack(
#             pady=(25, 0)
#         )

#         tk.Label(
#             self.sidebar,
#             text="Version 4.0",
#             font=(
#                 "Segoe UI",
#                 9
#             ),
#             fg=self.secondary_color,
#             bg=self.sidebar_color
#         ).pack(
#             pady=(0, 25)
#         )

#         # ------------------------------------------------------
#         # BUTTON HELPER
#         # ------------------------------------------------------

#         def add_sidebar_button(
#             text,
#             command
#         ):

#             button = tk.Button(
#                 self.sidebar,
#                 text=text,
#                 command=command,
#                 font=(
#                     "Segoe UI",
#                     10
#                 ),
#                 fg=self.text_color,
#                 bg=self.sidebar_color,
#                 activebackground=self.accent_color,
#                 activeforeground="white",
#                 relief="flat",
#                 bd=0,
#                 anchor="w",
#                 padx=22,
#                 pady=12,
#                 cursor="hand2"
#             )

#             button.pack(
#                 fill="x"
#             )

#         # ------------------------------------------------------
#         # SIDEBAR MENU
#         # ------------------------------------------------------

#         add_sidebar_button(
#             "＋  New Chat",
#             self.new_chat
#         )

#         add_sidebar_button(
#             "▣  Knowledge Manager",
#             self.open_knowledge_manager
#         )

#         add_sidebar_button(
#             "⌕  Search Conversation",
#             self.search_conversation_dialog
#         )

#         add_sidebar_button(
#             "♡  Memories",
#             self.show_memories
#         )

#         add_sidebar_button(
#             "?  Help",
#             self.show_help
#         )

#         add_sidebar_button(
#             "ⓘ  About",
#             self.show_about
#         )

#         # ------------------------------------------------------
#         # STATUS
#         # ------------------------------------------------------

#         bottom = tk.Frame(
#             self.sidebar,
#             bg=self.sidebar_color
#         )

#         bottom.pack(
#             side="bottom",
#             fill="x",
#             pady=15
#         )

#         tk.Label(
#             bottom,
#             text="●  Rule-based / Offline",
#             font=(
#                 "Segoe UI",
#                 9
#             ),
#             fg="#6fcf97",
#             bg=self.sidebar_color
#         ).pack(
#             pady=(0, 10)
#         )

#         tk.Button(
#             bottom,
#             text="Clear Conversation",
#             command=self.clear_chat,
#             font=(
#                 "Segoe UI",
#                 9
#             ),
#             fg="#dddddd",
#             bg="#292929",
#             activebackground="#3a3a3a",
#             activeforeground="white",
#             relief="flat",
#             bd=0,
#             padx=10,
#             pady=8
#         ).pack(
#             padx=15,
#             fill="x"
#         )

#         # ======================================================
#         # MAIN
#         # ======================================================

#         self.main_frame = tk.Frame(
#             self.root,
#             bg=self.chat_color
#         )

#         self.main_frame.pack(
#             side="right",
#             fill="both",
#             expand=True
#         )

#         # ======================================================
#         # HEADER
#         # ======================================================

#         header = tk.Frame(
#             self.main_frame,
#             bg=self.chat_color,
#             height=65
#         )

#         header.pack(
#             fill="x"
#         )

#         header.pack_propagate(
#             False
#         )

#         tk.Label(
#             header,
#             text="YuiBot",
#             font=(
#                 "Segoe UI",
#                 16,
#                 "bold"
#             ),
#             fg=self.text_color,
#             bg=self.chat_color
#         ).pack(
#             side="left",
#             padx=25,
#             pady=(15, 0)
#         )

#         tk.Label(
#             header,
#             text="Offline chatbot • Python rules",
#             font=(
#                 "Segoe UI",
#                 9
#             ),
#             fg=self.secondary_color,
#             bg=self.chat_color
#         ).pack(
#             side="left",
#             pady=(17, 0)
#         )

#         # ======================================================
#         # CHAT
#         # ======================================================

#         chat_container = tk.Frame(
#             self.main_frame,
#             bg=self.chat_color
#         )

#         chat_container.pack(
#             fill="both",
#             expand=True,
#             padx=20,
#             pady=(0, 10)
#         )

#         self.chat_box = tk.Text(
#             chat_container,
#             wrap="word",
#             font=(
#                 "Segoe UI",
#                 11
#             ),
#             bg=self.chat_color,
#             fg=self.text_color,
#             insertbackground="white",
#             selectbackground=self.accent_color,
#             relief="flat",
#             bd=0,
#             padx=15,
#             pady=15,
#             state="disabled"
#         )

#         self.chat_box.pack(
#             side="left",
#             fill="both",
#             expand=True
#         )

#         scrollbar = tk.Scrollbar(
#             chat_container,
#             command=self.chat_box.yview
#         )

#         scrollbar.pack(
#             side="right",
#             fill="y"
#         )

#         self.chat_box.configure(
#             yscrollcommand=scrollbar.set
#         )

#         # ------------------------------------------------------
#         # TAGS
#         # ------------------------------------------------------

#         self.chat_box.tag_configure(
#             "user_name",
#             foreground="#d98ca8",
#             font=(
#                 "Segoe UI",
#                 10,
#                 "bold"
#             )
#         )

#         self.chat_box.tag_configure(
#             "bot_name",
#             foreground="#ffffff",
#             font=(
#                 "Segoe UI",
#                 10,
#                 "bold"
#             )
#         )

#         self.chat_box.tag_configure(
#             "message",
#             foreground=self.text_color,
#             font=(
#                 "Segoe UI",
#                 11
#             ),
#             spacing3=8
#         )

#         self.chat_box.tag_configure(
#             "system",
#             foreground=self.secondary_color,
#             font=(
#                 "Segoe UI",
#                 9,
#                 "italic"
#             )
#         )

#         # ======================================================
#         # INPUT
#         # ======================================================

#         input_container = tk.Frame(
#             self.main_frame,
#             bg=self.chat_color
#         )

#         input_container.pack(
#             fill="x",
#             padx=20,
#             pady=(0, 20)
#         )

#         self.input_box = tk.Text(
#             input_container,
#             height=3,
#             wrap="word",
#             font=(
#                 "Segoe UI",
#                 11
#             ),
#             bg=self.input_color,
#             fg=self.text_color,
#             insertbackground="white",
#             relief="flat",
#             bd=0,
#             padx=12,
#             pady=10
#         )

#         self.input_box.pack(
#             side="left",
#             fill="both",
#             expand=True
#         )

#         tk.Button(
#             input_container,
#             text="Send",
#             command=self.send,
#             font=(
#                 "Segoe UI",
#                 10,
#                 "bold"
#             ),
#             fg="white",
#             bg=self.accent_color,
#             activebackground="#a64b6d",
#             activeforeground="white",
#             relief="flat",
#             bd=0,
#             width=9,
#             cursor="hand2"
#         ).pack(
#             side="right",
#             padx=(10, 0),
#             fill="y"
#         )

#         self.input_box.bind(
#             "<Control-Return>",
#             self.send_event
#         )

#         self.root.bind(
#             "<Control-l>",
#             lambda event: self.clear_chat()
#         )

#         self.input_box.focus_set()

#     # ==========================================================
#     # DISPLAY
#     # ==========================================================

#     def add_message(
#         self,
#         sender,
#         message,
#         tag
#     ):

#         self.chat_box.configure(
#             state="normal"
#         )

#         self.chat_box.insert(
#             "end",
#             sender + "\n",
#             tag
#         )

#         self.chat_box.insert(
#             "end",
#             message + "\n\n",
#             "message"
#         )

#         self.chat_box.configure(
#             state="disabled"
#         )

#         self.chat_box.see(
#             "end"
#         )

#     def add_system_message(
#         self,
#         message
#     ):

#         self.chat_box.configure(
#             state="normal"
#         )

#         self.chat_box.insert(
#             "end",
#             message + "\n\n",
#             "system"
#         )

#         self.chat_box.configure(
#             state="disabled"
#         )

#         self.chat_box.see(
#             "end"
#         )

#     # ==========================================================
#     # SEND
#     # ==========================================================

#     def send_event(
#         self,
#         event
#     ):

#         self.send()

#         return "break"

#     def send(self):

#         message = (
#             self.input_box
#             .get(
#                 "1.0",
#                 "end"
#             )
#             .strip()
#         )

#         if not message:
#             return

#         self.input_box.delete(
#             "1.0",
#             "end"
#         )

#         self.add_message(
#             "You",
#             message,
#             "user_name"
#         )

#         self.bot.memory.add_user_message(
#             message
#         )

#         response = self.bot.respond(
#             message
#         )

#         self.add_message(
#             "YuiBot",
#             response,
#             "bot_name"
#         )

#         self.bot.memory.add_assistant_message(
#             response
#         )

#     # ==========================================================
#     # LOAD HISTORY
#     # ==========================================================

#     def load_chat(self):

#         messages = (
#             self.bot.memory.get_messages()
#         )

#         if not messages:

#             self.add_system_message(
#                 "Welcome to YuiBot v4.\n\n"
#                 "I am an offline rule-based "
#                 "chatbot written in Python.\n\n"
#                 "New in v4:\n"
#                 "• Knowledge Manager\n"
#                 "• Conversation Search\n"
#                 "• Better context\n"
#                 "• Personal memory\n"
#                 "• Import / Export knowledge"
#             )

#             return

#         for item in messages:

#             role = item.get(
#                 "role",
#                 ""
#             )

#             content = item.get(
#                 "content",
#                 ""
#             )

#             if role == "user":

#                 self.add_message(
#                     "You",
#                     content,
#                     "user_name"
#                 )

#             elif role == "assistant":

#                 self.add_message(
#                     "YuiBot",
#                     content,
#                     "bot_name"
#                 )

#     # ==========================================================
#     # NEW CHAT
#     # ==========================================================

#     def new_chat(self):

#         result = messagebox.askyesno(
#             "New Chat",
#             "Start a new conversation?\n\n"
#             "Your personal memories and knowledge "
#             "will not be deleted."
#         )

#         if not result:
#             return

#         self.bot.memory.clear_messages()

#         self.bot.last_intent = None
#         self.bot.last_topic = None
#         self.bot.last_question = None

#         self.chat_box.configure(
#             state="normal"
#         )

#         self.chat_box.delete(
#             "1.0",
#             "end"
#         )

#         self.chat_box.configure(
#             state="disabled"
#         )

#         self.add_system_message(
#             "New conversation started."
#         )

#         self.input_box.focus_set()

#     # ==========================================================
#     # CLEAR CHAT
#     # ==========================================================

#     def clear_chat(self):

#         result = messagebox.askyesno(
#             "Clear Conversation",
#             "Clear the current conversation?\n\n"
#             "Personal memories and learned knowledge "
#             "will remain."
#         )

#         if not result:
#             return

#         self.bot.memory.clear_messages()

#         self.chat_box.configure(
#             state="normal"
#         )

#         self.chat_box.delete(
#             "1.0",
#             "end"
#         )

#         self.chat_box.configure(
#             state="disabled"
#         )

#         self.add_system_message(
#             "Conversation cleared."
#         )

#     # ==========================================================
#     # KNOWLEDGE MANAGER
#     # ==========================================================

#     def open_knowledge_manager(self):

#         KnowledgeManager(
#             self.root,
#             self.bot.memory
#         )

#     # ==========================================================
#     # SEARCH CONVERSATION
#     # ==========================================================

#     def search_conversation_dialog(self):

#         window = tk.Toplevel(
#             self.root
#         )

#         window.title(
#             "Search Conversation"
#         )

#         window.geometry(
#             "700x500"
#         )

#         window.configure(
#             bg="#171717"
#         )

#         tk.Label(
#             window,
#             text="Search previous messages",
#             font=(
#                 "Segoe UI",
#                 16,
#                 "bold"
#             ),
#             fg="white",
#             bg="#171717"
#         ).pack(
#             pady=(20, 10)
#         )

#         entry = tk.Entry(
#             window,
#             font=(
#                 "Segoe UI",
#                 11
#             ),
#             bg="#292929",
#             fg="white",
#             insertbackground="white",
#             relief="flat"
#         )

#         entry.pack(
#             fill="x",
#             padx=20,
#             ipady=8
#         )

#         result_box = tk.Text(
#             window,
#             wrap="word",
#             font=(
#                 "Segoe UI",
#                 10
#             ),
#             bg="#202020",
#             fg="#eeeeee",
#             relief="flat"
#         )

#         result_box.pack(
#             fill="both",
#             expand=True,
#             padx=20,
#             pady=15
#         )

#         def perform_search():

#             query = (
#                 entry.get()
#                 .strip()
#             )

#             if not query:
#                 return

#             results = (
#                 self.bot.memory
#                 .search_messages(
#                     query
#                 )
#             )

#             result_box.delete(
#                 "1.0",
#                 "end"
#             )

#             if not results:

#                 result_box.insert(
#                     "end",
#                     "No matching messages found."
#                 )

#                 return

#             for item in results:

#                 role = item.get(
#                     "role",
#                     "unknown"
#                 )

#                 content = item.get(
#                     "content",
#                     ""
#                 )

#                 timestamp = item.get(
#                     "timestamp",
#                     ""
#                 )

#                 label = (
#                     "You"
#                     if role == "user"
#                     else "YuiBot"
#                 )

#                 result_box.insert(
#                     "end",
#                     f"[{timestamp}] {label}\n",
#                     "header"
#                 )

#                 result_box.insert(
#                     "end",
#                     content
#                     + "\n\n"
#                 )

#         tk.Button(
#             window,
#             text="Search",
#             command=perform_search,
#             bg="#8b3d5c",
#             fg="white",
#             activebackground="#a64b6d",
#             relief="flat",
#             bd=0,
#             padx=20,
#             pady=8
#         ).pack(
#             pady=(0, 15)
#         )

#         result_box.tag_configure(
#             "header",
#             foreground="#d98ca8",
#             font=(
#                 "Segoe UI",
#                 9,
#                 "bold"
#             )
#         )

#         entry.bind(
#             "<Return>",
#             lambda event: perform_search()
#         )

#         entry.focus_set()

#     # ==========================================================
#     # MEMORIES
#     # ==========================================================

#     def show_memories(self):

#         memories = (
#             self.bot.show_memories()
#         )

#         messagebox.showinfo(
#             "YuiBot Memories",
#             memories
#         )

#     # ==========================================================
#     # HELP
#     # ==========================================================

#     def show_help(self):

#         messagebox.showinfo(
#             "YuiBot Help",
#             self.bot.help_text()
#         )

#     # ==========================================================
#     # ABOUT
#     # ==========================================================

#     def show_about(self):

#         messagebox.showinfo(
#             "About YuiBot",
#             """YuiBot v4

# Offline Python chatbot.

# Features:

# • Rule-based conversation
# • Fuzzy matching
# • Conversation context
# • Personal memory
# • Custom knowledge
# • Knowledge Manager
# • Conversation Search
# • Import / Export
# • Calculator
# • Date / Time

# No AI model.
# No OpenAI.
# No Ollama.
# No Llama.
# No Qwen.
# No API.
# No internet required."""
#         )

#     # ==========================================================
#     # CLOSE
#     # ==========================================================

#     def close(self):

#         self.bot.memory.save()

#         self.root.destroy()


# # ==============================================================
# # MAIN
# # ==============================================================

# def main():

#     root = tk.Tk()

#     YuiBotApp(
#         root
#     )

#     root.mainloop()


# if __name__ == "__main__":

#     main()



import tkinter as tk
from tkinter import messagebox

from chatbot import YuiBot
from knowledge_manager import KnowledgeManager
from settings_manager import SettingsManager


class YuiBotApp:

    def __init__(
        self,
        root
    ):

        self.root = root

        self.root.title(
            "YuiBot"
        )

        self.root.geometry(
            "1150x750"
        )

        self.root.minsize(
            850,
            600
        )

        # ======================================================
        # COLORS
        # ======================================================

        self.bg = "#171717"
        self.sidebar = "#202020"
        self.chat = "#1e1e1e"
        self.input = "#292929"
        self.accent = "#8b3d5c"

        self.text = "#f0f0f0"
        self.secondary = "#aaaaaa"

        # ======================================================
        # BOT
        # ======================================================

        self.bot = YuiBot()

        self.build_ui()

        self.load_chat()

        self.update_header()

        self.root.protocol(
            "WM_DELETE_WINDOW",
            self.close
        )

    # ==========================================================
    # UI
    # ==========================================================

    def build_ui(self):

        # ======================================================
        # SIDEBAR
        # ======================================================

        self.sidebar_frame = tk.Frame(
            self.root,
            bg=self.sidebar,
            width=240
        )

        self.sidebar_frame.pack(
            side="left",
            fill="y"
        )

        self.sidebar_frame.pack_propagate(
            False
        )

        self.title_label = tk.Label(
            self.sidebar_frame,
            text="YuiBot",
            font=(
                "Segoe UI",
                24,
                "bold"
            ),
            fg=self.text,
            bg=self.sidebar
        )

        self.title_label.pack(
            pady=(25, 0)
        )

        tk.Label(
            self.sidebar_frame,
            text="Version 5.0",
            font=(
                "Segoe UI",
                9
            ),
            fg=self.secondary,
            bg=self.sidebar
        ).pack(
            pady=(0, 25)
        )

        self.add_sidebar_button(
            "＋  New Chat",
            self.new_chat
        )

        self.add_sidebar_button(
            "⚙  Settings",
            self.open_settings
        )

        self.add_sidebar_button(
            "▣  Knowledge Manager",
            self.open_knowledge
        )

        self.add_sidebar_button(
            "⌕  Search Conversation",
            self.search_dialog
        )

        self.add_sidebar_button(
            "♡  Memories",
            self.show_memories
        )

        self.add_sidebar_button(
            "▥  Statistics",
            self.show_statistics
        )

        self.add_sidebar_button(
            "?  Help",
            self.show_help
        )

        self.add_sidebar_button(
            "ⓘ  About",
            self.show_about
        )

        # ======================================================
        # BOTTOM
        # ======================================================

        bottom = tk.Frame(
            self.sidebar_frame,
            bg=self.sidebar
        )

        bottom.pack(
            side="bottom",
            fill="x",
            pady=15
        )

        self.status_label = tk.Label(
            bottom,
            text="●  Offline",
            font=(
                "Segoe UI",
                9
            ),
            fg="#6fcf97",
            bg=self.sidebar
        )

        self.status_label.pack(
            pady=(0, 10)
        )

        tk.Button(
            bottom,
            text="Clear Conversation",
            command=self.clear_chat,
            bg="#292929",
            fg="#dddddd",
            activebackground="#3a3a3a",
            relief="flat",
            bd=0,
            pady=8
        ).pack(
            padx=15,
            fill="x"
        )

        # ======================================================
        # MAIN
        # ======================================================

        self.main_frame = tk.Frame(
            self.root,
            bg=self.chat
        )

        self.main_frame.pack(
            side="right",
            fill="both",
            expand=True
        )

        # ======================================================
        # HEADER
        # ======================================================

        header = tk.Frame(
            self.main_frame,
            bg=self.chat,
            height=70
        )

        header.pack(
            fill="x"
        )

        header.pack_propagate(
            False
        )

        self.header_name = tk.Label(
            header,
            text="YuiBot",
            font=(
                "Segoe UI",
                17,
                "bold"
            ),
            fg=self.text,
            bg=self.chat
        )

        self.header_name.pack(
            side="left",
            padx=25,
            pady=15
        )

        self.header_info = tk.Label(
            header,
            text="Offline chatbot",
            font=(
                "Segoe UI",
                9
            ),
            fg=self.secondary,
            bg=self.chat
        )

        self.header_info.pack(
            side="left",
            pady=15
        )

        # ======================================================
        # CHAT
        # ======================================================

        container = tk.Frame(
            self.main_frame,
            bg=self.chat
        )

        container.pack(
            fill="both",
            expand=True,
            padx=20
        )

        self.chat_box = tk.Text(
            container,
            wrap="word",
            font=(
                "Segoe UI",
                11
            ),
            bg=self.chat,
            fg=self.text,
            insertbackground="white",
            relief="flat",
            bd=0,
            padx=15,
            pady=15,
            state="disabled"
        )

        self.chat_box.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar = tk.Scrollbar(
            container,
            command=self.chat_box.yview
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.chat_box.configure(
            yscrollcommand=scrollbar.set
        )

        self.chat_box.tag_configure(
            "user",
            foreground="#d98ca8",
            font=(
                "Segoe UI",
                10,
                "bold"
            )
        )

        self.chat_box.tag_configure(
            "bot",
            foreground="#ffffff",
            font=(
                "Segoe UI",
                10,
                "bold"
            )
        )

        self.chat_box.tag_configure(
            "message",
            foreground=self.text,
            font=(
                "Segoe UI",
                11
            ),
            spacing3=8
        )

        self.chat_box.tag_configure(
            "system",
            foreground=self.secondary,
            font=(
                "Segoe UI",
                9,
                "italic"
            )
        )

        # ======================================================
        # INPUT
        # ======================================================

        input_frame = tk.Frame(
            self.main_frame,
            bg=self.chat
        )

        input_frame.pack(
            fill="x",
            padx=20,
            pady=20
        )

        self.input_box = tk.Text(
            input_frame,
            height=3,
            wrap="word",
            font=(
                "Segoe UI",
                11
            ),
            bg=self.input,
            fg=self.text,
            insertbackground="white",
            relief="flat",
            bd=0,
            padx=12,
            pady=10
        )

        self.input_box.pack(
            side="left",
            fill="both",
            expand=True
        )

        tk.Button(
            input_frame,
            text="Send",
            command=self.send,
            font=(
                "Segoe UI",
                10,
                "bold"
            ),
            bg=self.accent,
            fg="white",
            activebackground="#a64b6d",
            relief="flat",
            bd=0,
            width=9
        ).pack(
            side="right",
            padx=(10, 0),
            fill="y"
        )

        self.input_box.bind(
            "<Control-Return>",
            self.send_event
        )

        self.root.bind(
            "<Control-l>",
            lambda event: self.clear_chat()
        )

        self.input_box.focus_set()

    # ==========================================================
    # SIDEBAR BUTTON
    # ==========================================================

    def add_sidebar_button(
        self,
        text,
        command
    ):

        tk.Button(
            self.sidebar_frame,
            text=text,
            command=command,
            font=(
                "Segoe UI",
                10
            ),
            fg=self.text,
            bg=self.sidebar,
            activebackground=self.accent,
            activeforeground="white",
            relief="flat",
            bd=0,
            anchor="w",
            padx=22,
            pady=12,
            cursor="hand2"
        ).pack(
            fill="x"
        )

    # ==========================================================
    # HEADER
    # ==========================================================

    def update_header(self):

        name = self.bot.settings.get(
            "bot_name",
            "YuiBot"
        )

        personality = self.bot.settings.get(
            "personality",
            "Friendly"
        )

        self.header_name.config(
            text=name
        )

        self.title_label.config(
            text=name
        )

        self.header_info.config(
            text=(
                f"Offline • {personality} personality"
            )
        )

    # ==========================================================
    # SEND
    # ==========================================================

    def send_event(
        self,
        event
    ):

        self.send()

        return "break"

    def send(self):

        message = (
            self.input_box
            .get(
                "1.0",
                "end"
            )
            .strip()
        )

        if not message:
            return

        self.input_box.delete(
            "1.0",
            "end"
        )

        self.add_message(
            "You",
            message,
            "user"
        )

        if self.bot.settings.get(
            "memory_enabled",
            True
        ):

            self.bot.memory.add_user_message(
                message
            )

        response = self.bot.respond(
            message
        )

        # ======================================================
        # SPECIAL CLEAR COMMAND
        # ======================================================

        if response == "__CLEAR_CHAT__":

            self.clear_chat(
                confirm=False
            )

            return

        bot_name = self.bot.settings.get(
            "bot_name",
            "YuiBot"
        )

        self.add_message(
            bot_name,
            response,
            "bot"
        )

        if self.bot.settings.get(
            "memory_enabled",
            True
        ):

            self.bot.memory.add_assistant_message(
                response
            )

    # ==========================================================
    # DISPLAY
    # ==========================================================

    def add_message(
        self,
        sender,
        message,
        tag
    ):

        self.chat_box.configure(
            state="normal"
        )

        self.chat_box.insert(
            "end",
            sender + "\n",
            tag
        )

        self.chat_box.insert(
            "end",
            message + "\n\n",
            "message"
        )

        self.chat_box.configure(
            state="disabled"
        )

        self.chat_box.see(
            "end"
        )

    def system_message(
        self,
        message
    ):

        self.chat_box.configure(
            state="normal"
        )

        self.chat_box.insert(
            "end",
            message + "\n\n",
            "system"
        )

        self.chat_box.configure(
            state="disabled"
        )

        self.chat_box.see(
            "end"
        )

    # ==========================================================
    # LOAD CHAT
    # ==========================================================

    def load_chat(self):

        messages = (
            self.bot.memory.get_messages()
        )

        if not messages:

            self.system_message(
                "Welcome to YuiBot v5.\n\n"
                "This chatbot is completely "
                "offline and uses Python rules.\n\n"
                "New in v5:\n"
                "• Settings\n"
                "• Personality modes\n"
                "• Custom commands\n"
                "• Statistics\n"
                "• Better context"
            )

            return

        for item in messages:

            role = item.get(
                "role",
                ""
            )

            content = item.get(
                "content",
                ""
            )

            if role == "user":

                self.add_message(
                    "You",
                    content,
                    "user"
                )

            elif role == "assistant":

                name = self.bot.settings.get(
                    "bot_name",
                    "YuiBot"
                )

                self.add_message(
                    name,
                    content,
                    "bot"
                )

    # ==========================================================
    # NEW CHAT
    # ==========================================================

    def new_chat(self):

        result = messagebox.askyesno(
            "New Chat",
            "Start a new conversation?\n\n"
            "Your memories and knowledge will remain."
        )

        if not result:
            return

        self.bot.memory.clear_messages()

        self.bot.last_intent = None
        self.bot.last_topic = None
        self.bot.last_question = None

        self.chat_box.configure(
            state="normal"
        )

        self.chat_box.delete(
            "1.0",
            "end"
        )

        self.chat_box.configure(
            state="disabled"
        )

        self.system_message(
            "New conversation started."
        )

    # ==========================================================
    # CLEAR CHAT
    # ==========================================================

    def clear_chat(
        self,
        confirm=True
    ):

        if confirm:

            result = messagebox.askyesno(
                "Clear Conversation",
                "Clear the current conversation?"
            )

            if not result:
                return

        self.bot.memory.clear_messages()

        self.chat_box.configure(
            state="normal"
        )

        self.chat_box.delete(
            "1.0",
            "end"
        )

        self.chat_box.configure(
            state="disabled"
        )

        self.system_message(
            "Conversation cleared."
        )

    # ==========================================================
    # SETTINGS
    # ==========================================================

    def open_settings(self):

        SettingsManager(
            self.root,
            self.bot.settings,
            self.settings_changed
        )

    def settings_changed(self):

        self.bot.reload_settings()

        self.update_header()

        self.system_message(
            "Settings updated."
        )

    # ==========================================================
    # KNOWLEDGE
    # ==========================================================

    def open_knowledge(self):

        KnowledgeManager(
            self.root,
            self.bot.memory
        )

    # ==========================================================
    # SEARCH
    # ==========================================================

    def search_dialog(self):

        window = tk.Toplevel(
            self.root
        )

        window.title(
            "Search Conversation"
        )

        window.geometry(
            "700x500"
        )

        window.configure(
            bg=self.bg
        )

        tk.Label(
            window,
            text="Search Conversation",
            font=(
                "Segoe UI",
                18,
                "bold"
            ),
            fg="white",
            bg=self.bg
        ).pack(
            pady=20
        )

        entry = tk.Entry(
            window,
            bg=self.input,
            fg="white",
            insertbackground="white",
            relief="flat",
            font=(
                "Segoe UI",
                11
            )
        )

        entry.pack(
            fill="x",
            padx=20,
            ipady=8
        )

        results = tk.Text(
            window,
            wrap="word",
            bg=self.sidebar,
            fg="#eeeeee",
            relief="flat",
            font=(
                "Segoe UI",
                10
            )
        )

        results.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=15
        )

        def search():

            query = entry.get().strip()

            if not query:
                return

            found = (
                self.bot.memory.search_messages(
                    query
                )
            )

            results.delete(
                "1.0",
                "end"
            )

            if not found:

                results.insert(
                    "end",
                    "No matching messages found."
                )

                return

            for item in found:

                role = item.get(
                    "role",
                    ""
                )

                content = item.get(
                    "content",
                    ""
                )

                timestamp = item.get(
                    "timestamp",
                    ""
                )

                label = (
                    "You"
                    if role == "user"
                    else self.bot.settings.get(
                        "bot_name",
                        "YuiBot"
                    )
                )

                results.insert(
                    "end",
                    f"[{timestamp}] {label}\n",
                )

                results.insert(
                    "end",
                    content
                    + "\n\n"
                )

        tk.Button(
            window,
            text="Search",
            command=search,
            bg=self.accent,
            fg="white",
            relief="flat",
            bd=0,
            padx=20,
            pady=8
        ).pack(
            pady=(0, 15)
        )

        entry.bind(
            "<Return>",
            lambda event: search()
        )

        entry.focus_set()

    # ==========================================================
    # MEMORIES
    # ==========================================================

    def show_memories(self):

        messagebox.showinfo(
            "Memories",
            self.bot.show_memories()
        )

    # ==========================================================
    # STATISTICS
    # ==========================================================

    def show_statistics(self):

        if not self.bot.settings.get(
            "show_statistics",
            True
        ):

            messagebox.showinfo(
                "Statistics",
                "Statistics are disabled in Settings."
            )

            return

        messagebox.showinfo(
            "YuiBot Statistics",
            self.bot.statistics_text()
        )

    # ==========================================================
    # HELP
    # ==========================================================

    def show_help(self):

        messagebox.showinfo(
            "YuiBot Help",
            self.bot.help_text()
        )

    # ==========================================================
    # ABOUT
    # ==========================================================

    def show_about(self):

        messagebox.showinfo(
            "About YuiBot",
            self.bot.about_text()
        )

    # ==========================================================
    # CLOSE
    # ==========================================================

    def close(self):

        self.bot.memory.save()

        self.root.destroy()


def main():

    root = tk.Tk()

    YuiBotApp(
        root
    )

    root.mainloop()


if __name__ == "__main__":

    main()