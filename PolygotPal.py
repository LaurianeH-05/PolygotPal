import tkinter as tk
from tkinter import messagebox, ttk
from googletrans import Translator

# Create main window
root = tk.Tk()
root.title("PolyglotPal")
root.geometry("900x500")
root.minsize(600, 400)

translator = Translator()

# Define colors
main_bg_color = "#ffd3e6"
header_bg_color = "#ebb9ce"
tip_bg_color = "#fff4f9"
user_bubble_color = "#ffffff"
bot_bubble_color = "#fff5e1"
input_bg_color = "#ffffff" 

# 1/10 Header section
header_frame = tk.Frame(root, bg=header_bg_color, height=50)
header_frame.pack(fill=tk.X)
header_label = tk.Label(header_frame, text="PolyglotPal", font=("Arial", 12, "bold"), bg=header_bg_color)
header_label.pack(pady=10)

# 3/10 Tips Banner
tips_frame = tk.Frame(root, bg=tip_bg_color, height=150)
tips_frame.pack(fill=tk.X)
tips_label = tk.Label(tips_frame, text="Tips: Select a language and I'll translate the input!", bg=tip_bg_color)
tips_label.pack(pady=20)

# 6/10 Chat area
chat_frame = tk.Frame(root, bg=main_bg_color)
chat_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Create chat display area (Text widget)
chat_display = tk.Text(chat_frame, bg=main_bg_color, wrap=tk.WORD, state=tk.DISABLED)
chat_display.pack(fill=tk.BOTH, expand=True)

# User input section (Fixed at the bottom)
input_frame = tk.Frame(root, bg=input_bg_color, height=50)
input_frame.pack(fill=tk.X, side=tk.BOTTOM)

# Dropdown for selecting language
languages = {
    "English": "en", "Spanish": "es", "French": "fr",
    "Korean": "ko", "Japanese": "ja", "German": "de", "Italian": "it"
}
lang_label = tk.Label(input_frame, text="Select language:")
lang_label.pack(side=tk.LEFT, padx=10)

lang_dropdown = ttk.Combobox(input_frame, values=list(languages.keys()), state="readonly")
lang_dropdown.set("Select Language")  # Set default text
lang_dropdown.pack(side=tk.LEFT, padx=10)

# User input entry
user_input = tk.Entry(input_frame, width=50, bg="white")
user_input.pack(side=tk.LEFT, padx=10, pady=10)

# Send button
send_button = tk.Button(input_frame, text="Send", bg="#fff0d2", command=lambda: send_message())
send_button.pack(side=tk.RIGHT, padx=10, pady=10)

# Function to handle sending the message
def send_message():
    user_message = user_input.get()
    target_language = lang_dropdown.get()

    if not user_message.strip():
        messagebox.showerror("Error", "Please enter some text to translate.")
        return

    if target_language == "Select Language":
        messagebox.showerror("Error", "Please select a target language.")
        return

    lang_code = languages[target_language]

    # Display user message
    chat_display.config(state=tk.NORMAL)
    chat_display.insert(tk.END, "You: " + user_message + "\n", "user")
    chat_display.config(state=tk.DISABLED)

    user_input.delete(0, tk.END)
    
    # Translate and display bot's response
    translate_message(user_message, lang_code)

def translate_message(user_message, lang_code):
    try:
        translation = translator.translate(user_message, dest=lang_code)
        bot_reply = translation.text

        chat_display.config(state=tk.NORMAL)
        chat_display.insert(tk.END, "Bot: " + bot_reply + "\n", "bot")
        chat_display.config(state=tk.DISABLED)

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Tag configurations for user and bot messages
chat_display.tag_config("user", foreground="black", background=user_bubble_color)
chat_display.tag_config("bot", foreground="black", background=bot_bubble_color)

root.mainloop()
