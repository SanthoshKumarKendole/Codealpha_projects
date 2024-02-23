import nltk
from nltk.chat.util import reflections, Chat


chatbox=[(r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you', ['I am good, thank you.']),
    (r'(.*) your name?', ['I am a chatbot created by ChatGPT.', 'You can call me Chatbot.']),
    (r'What are you doing',['Nothing']),
    (r'Had lunch|Had tiffin | Had dinner',['Yahhh done!!']),
    (r'What plans today',['I am going to movie']),
    (r'bye', ['Bye!', 'Goodbye!', 'Take care.']),]


chat=Chat(chatbox,reflections)
print("Welcome to chat box, If you want to quit please enter bye")
while True:
    user=input("Type Text : ")
    if user.lower()=='bye':
        print("Meet you again!! Take Care Byee!!!!")
        break
    else:
        response=chat.respond(user)
        print("chat :", response)