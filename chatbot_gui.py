import tkinter as tk

from tkinter import scrolledtext

from dotenv import load_dotenv

from openai import OpenAI

import os


load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


conversation_history = [

 {"role": "system", "content": "You are a helpful, friendly AI chatbot."}

]


def send_message():

 user_input = user_entry.get()

 if not user_input.strip():

  return


 chat_area.config(state=tk.NORMAL)

 chat_area.insert(tk.END, f"You: {user_input}\n")

 chat_area.config(state=tk.DISABLED)


 conversation_history.append({"role": "user", "content": user_input})


 response = client.responses.create(

  model="gpt-4.1-mini",

  input=conversation_history

 )


 reply = response.output_text


 chat_area.config(state=tk.NORMAL)

 chat_area.insert(tk.END, f"Chatbot: {reply}\n\n")

 chat_area.config(state=tk.DISABLED)

 chat_area.yview(tk.END)


 conversation_history.append({"role": "assistant", "content": reply})

 user_entry.delete(0, tk.END)


# Create GUI window

window = tk.Tk()

window.title("AI Chatbox")


chat_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=60, height=20, state=tk.DISABLED)

chat_area.pack(padx=10, pady=10)


user_entry = tk.Entry(window, width=50)

user_entry.pack(side=tk.LEFT, padx=(10,0), pady=(0,10))

user_entry.bind("<Return>", lambda event: send_message())


send_button = tk.Button(window, text="Send", command=send_message)

send_button.pack(side=tk.LEFT, padx=10, pady=(0,10))


window.mainloop()

