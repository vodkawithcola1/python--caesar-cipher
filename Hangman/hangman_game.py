import words
import art
import random

is_guessed = False

random_word = random.choice(words.word_list)
word_new_list = []

for rw_len in random_word:
    word_new_list.append("_")

print(art.logo)
print(random_word)

life = 6

while not is_guessed:
    print(f"Word to guess: {''.join(word_new_list)}")
    guessed_letter = input("Guess a letter: ")
    if len(guessed_letter) > 1:
        print("Sorry... please enter just one character!\n")
    if guessed_letter in random_word:
        for i, char in enumerate(random_word):
            if char == guessed_letter:
                word_new_list[i] = guessed_letter

    else:
        life -= 1
        if life > 0:
            print(f"You guessed {guessed_letter}, that's not in the word. You lose a life.")
            print(art.stages[life-1])
            print(f"************************{life}/6 LIVES LEFT ************************")
        else:
            is_guessed = True
            print(f"Sorry... your word was {random_word}... you can try again if you want!")

    if "".join(word_new_list) == random_word:
        is_guessed = True
        print(f"Congratulations! Your word was {random_word}... Thanks for playing and you can try again if you want!")
