def reveal_letter(word_completion, word, guess):
    # iterate over the word and identify each instance of the guessed letter
    indices = []        # list to store the index nubmer of each instance
    for index in range(len(word)):
        if word[index] == guess:
            indices.append(index)
    
    # convert the completion word to list so it can be manipulated
    word_as_list = list(word_completion)
    
    # for each instance of the guessed letter, replace corresponding "_"
    for index in indices:
        word_as_list[index] = guess
    
    # convert the list back to a string, and return to main program
    return "".join(word_as_list)

    

print(reveal_letter("_____","DODGE", "D"))