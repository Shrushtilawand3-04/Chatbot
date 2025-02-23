import nltk
from nltk.chat.util import Chat, reflections

# Define chatbot patterns and responses
patterns = [
    (r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]),
    (r"how are you", ["I'm doing well, thank you!", "I'm great! How about you?"]),
    (r"(.*) your name", ["I'm a simple chatbot.", "Call me ChatBot!"]),
    (r"what can you do", ["I can chat with you! Ask me anything."]),
    (r"bye|goodbye", ["Goodbye! Have a great day!", "Bye! Talk to you later!"]),
    (r"where are you from", ["I exist in the digital world!", "I'm from the cloud."]),
    (r"who created you", ["I was created by a programmer using Python!", "A developer wrote my code!"]),
    (r"what is your purpose", ["I'm here to chat and assist you!", "I exist to talk with you!"]),
    (r"tell me a joke", ["Why did the computer catch a cold? Because it left its Windows open!", "I told my laptop I needed a break, and now it won’t stop sending me vacation ads!"]),
    (r"what is AI", ["AI stands for Artificial Intelligence, which enables machines to learn and make decisions.", "Artificial Intelligence is the simulation of human intelligence in machines."])
]

# Create chatbot instance
chatbot = Chat(patterns, reflections)

def chat():
    print("Hello! I'm a chatbot. Type 'bye' to exit.")
    while True:
        user_input = input(">> ")
        if user_input.lower() == "bye":
            print("Goodbye!")
            break
        response = chatbot.respond(user_input)
        print(response)

if __name__ == "__main__":
    chat()
