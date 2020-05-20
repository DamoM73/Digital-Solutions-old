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
   
   # Guessing letter loop
   while not guessed and tries > 0:
      guess = input("Please guess a letter or word: ").upper()
      if len(guess) == 1 and guess.isalpha():
         if guess in guessed_letters:
            print("You already guessed the letter", guess)
         elif guess not in word:
            print(guess, "is not in the word.")
            tries -= 1
            guessed_letters.append(guess)
         else:
            print("Good job,", guess, "is in the word!")
            guessed_letters.append(guess)
            word_as_a_list = list(word_completion)
            indices = [i for i, letter in enumerate(word) if letter == guess]
            for index in indices:
               word_as_a_list[index] = guess
            word_completion = "".join(word_as_a_list)
            if "_" not in word_completion:
               guessed = True

      elif len(guess) == len(word) and guess.isalpha():
         if guess in guessed_words:
            print("You already guessed the word", guess)
         elif guess != word:
            print(guess,"is not the word.")
            tries -= 1
            guessed_words.append(guess)
         else:
            guessed = True
            word_completion = word
      else:
         print("Not a valid guess.")
      print(display_hangman(tries))
      print(word_completion)
      print("\n")
   if guessed:
      print("Congratz, you guessed the word. You win!")
   else:
      print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time")




def main():
   word = get_word()
   play(word)
   while input("Play Again").upper() == "Y":
      word = get_word()
      play(word)

if __name__ == "__main__":
   main()