sentence = input("Type in a sentence to check the number of words\n\n")
numberofwords = len(sentence.split())
print("\nYou gave the sentence: " + sentence + "\nThere are " + str(numberofwords) + " words in the sentence.")