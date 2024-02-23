import random

def hangman():
    list_of_words=['hangman','python','india','language','apple']
    word=random.choice(list_of_words)
    turns=10
    guess_word=''
    valid_word=set('abcdefghijklmnopqrstuvwxyz')
    while len(word)>0:
        main_word=''
        for i in word:
            if i in guess_word:
                main_word+=i
            else:
                main_word+='_'

        if main_word==word:
            print(main_word)
            print("---You won---")
            break

        print("guess the words",main_word)
        guess=input()
        if guess in valid_word:
            guess_word+=guess
        else:
            print("Enter Valid Character")
            guess=input()

        if guess not in word:
            turns=turns-1

            if turns==9:
                print("9 turns left")
                print("-----------------")
            if turns==8:
                print("8 turns left")
                print("------------------")
                print("         O        ")
            if turns==7:
                print("7 turns left")
                print("------------------")
                print("         O        ")
                print("         |        ")
            if turns==6:
                print("6 turns left")
                print("------------------")
                print("         O        ")
                print("         |        ")
                print("        /         ")
            if turns==5:
                print("5 turns left")
                print("------------------")
                print("         O        ")
                print("         |        ")
                print("        / \       ")
            if turns==4:
                print("4 turns left")
                print("------------------")
                print("        \O        ")
                print("         |        ")
                print("        / \       ")
            if turns==3:
                print("3 turns left")
                print("------------------")
                print("        \O/       ")
                print("         |        ")
                print("        / \       ")
            if turns==2:
                print("2 turns left")
                print("------------------")
                print("        \O/--     ")
                print("         |        ")
                print("        / \       ")
            if turns==1:
                print("1 turns left")
                print("------------------")
                print("             |    ")
                print("        \O/--     ")
                print("         |        ")
                print("        / \       ")
            if turns==0:
                print("You loose the game...!!!! and Try Again")
                print("------------------")
                print("              |    ")
                print("         O----     ")
                print("        /|\        ")
                print("        / \        ")
                break


name=input("Enter your name")
print("---Welcome to Hangman Game ---")
print(name)
hangman()