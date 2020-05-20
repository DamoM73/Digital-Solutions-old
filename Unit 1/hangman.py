import random
import words
import stages

def get_word():
    # return a random variable from the word list
    word = random.choice(words.word_list)
    return word.upper()

def display_hangman(tries):
    # return the gallow for the number of tries left
    return stages.stages[tries]

def reveal_letter(word_completion, word, guess):
    # iterate over the word and identify each instance of the guessed letter
    indices = []        # a list to store the index number of each instance
    for index in range(len(word)):
        if word[index] == guess:
            indices.append(index)
        
    word_as_list = list(word_completion) # convert the completion word to list so it can be manipulated
    
    # for each instance of the guessed letter, replace corresponding "_"
    for index in indices:
        word_as_list[index] = guess
    
    word_completion = "".join(word_as_list)     # convert the list back to a string
    return word_completion      # return new word_completion with revealed letters

def play(word):
    # play a round of the game for the word provided

    # initialise the round
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print("\n")
   
    # Guessing word loop
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        # user enters letter
        if len(guess) == 1 and guess.isalpha():
            # letter has already been guessed
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            # letter not in word
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            # letter is in word
            else:
                print("Good job,", guess, "is in the word!")
                # record that the letter has been guessed
                guessed_letters.append(guess)
                # reveal letter on screen
                word_completion = reveal_letter(word_completion,word,guess)
                # check if word is complete
                if "_" not in word_completion:
                    guessed = True
        # user enters a word of the right length
        elif len(guess) == len(word) and guess.isalpha():
             # guessed word has already been guessed 
            if guess in guessed_words:
                print("You already guessed the word", guess)
            # guessed word in not correct
            elif guess != word:
                print(guess,"is not the word.")
                tries -= 1
                guessed_words.append(guess)
            # guessed word is correct
            else:
                guessed = True
                word_completion = word
        # user has entered something other than a letter or word of the correct length
        else:
            print("Not a valid guess.")
        
        # update display
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    # round has ended, check if player won
    if guessed:
        print("Congratz, you guessed the word. You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time")


# ***** MAIN PROGRAM ****
word = get_word()
play(word)
while input("Play Again (Y/N)? ").upper() == "Y":
    word = get_word()
    play(word)