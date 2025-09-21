import random
from hangman_function import words,Hangman_Drawing

hangman_drawing = Hangman_Drawing()

chosen_word = random.choice(words)
chosen_word_list = [char for char in chosen_word]
chosen_word_list_unique = list(set(chosen_word_list))

word_to_guess = ['_' for _ in range(len(chosen_word_list))]

l = 0
i = 0
parts = [hangman_drawing.draw_head, hangman_drawing.draw_body, hangman_drawing.draw_left_arm, hangman_drawing.draw_right_arm, hangman_drawing.draw_left_leg, hangman_drawing.draw_right_leg]
hangman_drawing.draw_gallows()
while i < (len(chosen_word_list_unique)) and l<6:
    print("Word to Guess: "+' '.join(word_to_guess))
    guessed_letter = input("Guess a letter: ").lower()

    if guessed_letter not in chosen_word_list:
        print(f"Sorry, you guessed a wrong word!")
        parts[l]()
        l += 1
        # print(hangman_ascii[l])

    elif guessed_letter in word_to_guess:
        print(f"Letter already chosen!")

    elif guessed_letter in chosen_word_list and guessed_letter not in word_to_guess:
        positions = [i for i, chars in enumerate(chosen_word_list) if chars == guessed_letter]
        for position in positions:
            word_to_guess[int(position)] = guessed_letter
        i+=1
        # print(hangman_ascii[l])
        print(f"Congrats, you guessed the right word!")

if i == len(chosen_word_list_unique):
    print("congrats you win")
elif l == 6:
    print("You are dead. The word was "+ chosen_word.upper())

