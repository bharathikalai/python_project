import tkinter as tk
from tkinter import Scrollbar, Text, Entry, Button

def simple_chatbot(user_input):
    user_input = user_input.lower()

    if 'hello' in user_input:
        return "Hi there! How can I help you?"
    elif 'how are you' in user_input:
        return "I'm just a computer program, but thanks for asking!"
    elif 'bye' in user_input:
        return "Goodbye! Have a great day."
    else:
        return "I'm sorry, I don't understand. Can you please rephrase?"

def send_message():
    user_input = entry.get()
    entry.delete(0, tk.END)
    
    response = simple_chatbot(user_input)

    chat_history.config(state=tk.NORMAL)
    chat_history.insert(tk.END, f"You: {user_input}\n")
    chat_history.insert(tk.END, f"Bot: {response}\n\n")
    chat_history.config(state=tk.DISABLED)
    chat_history.see(tk.END)

# Create the main window
root = tk.Tk()
root.title("Simple Chatbot")

# Create a text widget for the chat history
chat_history = Text(root, wrap=tk.WORD, state=tk.DISABLED)
chat_history.pack(expand=True, fill=tk.BOTH)

# Create a scrollbar for the chat history
scrollbar = Scrollbar(root, command=chat_history.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
chat_history.config(yscrollcommand=scrollbar.set)

# Create an entry widget for user input
entry = Entry(root, width=50)
entry.pack(pady=10)

# Create a button to send messages
send_button = Button(root, text="Send", command=send_message)
send_button.pack()

# Run the main loop
root.mainloop()
