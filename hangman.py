import random

words = ["python", "javascript", "java", "react", "android", "ios", "html"]

words_index = random.randint(0,6)

selected_word = words[words_index]

total_letters = len(selected_word)

mystery_word = list("_" * len(selected_word))

number_of_tries = 6

while (number_of_tries > 0):

    print("\nMystery word: " + "".join(mystery_word))

    user_input = input("\nGuess a letter: ")

    if user_input in selected_word:

        print("\nLetter correct!") 

        count = selected_word.count(user_input)

        index = 0

        while count == 1 or count > 1:

            index = selected_word.find(user_input, index)

            mystery_word[index] = user_input

            index += 1

            count -= 1

            total_letters = total_letters - 1
          
        if (total_letters == 0): 

            print("\nMystery word: " + "".join(mystery_word))

            print("\nYou guessed the word: " + selected_word + "!")

            break
    
    else:

        print("\nLetter incorrect!\n")

        number_of_tries = number_of_tries - 1

        print(str(number_of_tries) + " tries left")

else:

    print("\nToo many wrong guesses, You lose!")


