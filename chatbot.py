# Import necessary libraries

from dotenv import load_dotenv # To load your secret API key safely

from openai import OpenAI    # To talk to OpenAI's AI models

import os            # To access environment variables


# Load the API key from the .env file

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# This list keeps track of the conversation between you and the AI

conversation_history = [

  {"role": "system", "content": "You are a helpful, friendly AI chatbot."}

]


# Greet the user

print("Welcome to AI Chatbox! Type 'bye' to exit.\n")


# We use a flag instead of break to make the loop easier to follow

running = True


while running:

  # Get what the user types

  user_input = input("You: ")


  # Check if the user wants to leave

  if user_input.lower() == "bye":

    print("Chatbot: Goodbye! Have a great day!")

    running = False # Stop the loop

  else:

    # Add what the user said to the conversation

    conversation_history.append({

      "role": "user",

      "content": user_input

    })


    # Ask OpenAI to respond to the conversation so far

    response = client.responses.create(

      model="gpt-4.1-mini",   # This is the AI model

      input=conversation_history # Send the conversation history

    )


    # Get the AI's reply text

    reply = response.output_text

    print("Chatbot:", reply)


    # Add AI's reply to the conversation history

    conversation_history.append({

      "role": "assistant",

      "content": reply

    })


