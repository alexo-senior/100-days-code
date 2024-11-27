#Step 1 
import random

word_list = ["mouse", "horse", "bird"]
choosen_word = random.choice(word_list)
word_lenght =len(choosen_word)

#testing code 
print(f"pssst, the soluction is: {choosen_word}.")
#create blanks

display = []
for _ in  range(word_lenght):
    display += "_"
print(display)

end_of_game = False

while not end_of_game:
    guess = input("guess a letter: ").lower()

    for position in range(word_lenght):
        letter = choosen_word[position]
        #print(f"current position: {position}\n current letter: {letter}\n guessed letter:{guess}")
        if letter == guess:
            display[position] = letter
            
    print(display)
    #Check if there are no more "_" left in 'display'. Then all letters have been guessed.
    if "_" not in display:
        end_of_game = True
        print("you win!")
        

        

