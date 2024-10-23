import re
import time

def get_chatbot_response(user_input):
    # Normalize the user input to lower case
    user_input = user_input.lower()
    
    # Respond based on specific keywords using if-else statements
    if "hello" in user_input or "hi" in user_input:
        return "Hi there! How can I help you today?"
    
    elif "what is your name" in user_input or "your name" in user_input:
        return "I’m a simple rule-based chatbot."
    
    elif "time" in user_input:
        current_time = time.strftime("%H:%M:%S", time.localtime())
        return f"The current time is {current_time}."
    
    elif re.search(r"bye|goodbye|see you", user_input):
        return "Goodbye! Have a wonderful day!"
    
    else:
        return "I'm not sure how to respond to that. Could you please rephrase your question?"

# Start a conversation with the user
while True:
    user_input = input("You: ")
    if "bye" in user_input.lower() or "exit" in user_input.lower():
        print("Chatbot: Goodbye! Have a wonderful day!")
        break
    response = get_chatbot_response(user_input)
    print(f"Chatbot: {response}")
