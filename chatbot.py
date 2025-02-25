def chatbot():
    print("Hello! I'm a simple chatbot. How can I help you today?")
    
    while True:
        user_input = input("You: ").lower()

        # Exit condition
        if user_input == "bye" or user_input == "exit":
            print("Chatbot: Goodbye! Have a nice day.")
            break
        
        # Responding to different queries using if-else statements
        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How can I assist you today?")
        
        elif "how are you" in user_input:
            print("Chatbot: I'm just a bot, but I'm doing fine. How about you?")
        
        elif "your name" in user_input:
            print("Chatbot: I am a simple rule-based chatbot.")
        
        elif "weather" in user_input:
            print("Chatbot: I don't have access to live data, but I hope it's nice where you are!")
        
        elif "thanks" in user_input or "thank you" in user_input:
            print("Chatbot: You're welcome! Let me know if you need anything else.")
        
        elif "help" in user_input:
            print("Chatbot: I'm here to help! You can ask me about greetings, weather, or just chat.")
        
        else:
            print("Chatbot: Sorry, I didn't understand that. Could you ask something else?")
        
# Call the chatbot function to start interacting
chatbot()
