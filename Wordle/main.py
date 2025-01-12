import random
import tkinter as tk

guessNum = 0


def revealHint():
  random_index = random.randint(0, word_length - 1)
  hint_word = list('_' * word_length)
  hint_word[random_index] = chosenWord[random_index]
  clue_label.config(text=f"Hint: {' '.join(hint_word)}")
  HintButton.config(state='disabled')



def getWord():
  guessedWord = EntryBox.get()
  global guessNum
  cnt = []
  rpt_ltr = []
  correct = 0



  if guessedWord in wordlist:
    for kk in range(5):
      label = tk.Label(text = guessedWord[kk].upper(), font = 12, pady = 5, borderwidth = 1, relief= 'solid')
      label.grid(row = guessNum, column = kk, sticky = tk.NSEW)

      if guessedWord in wordlist and len(guessedWord) == word_length:
              for kk in range(word_length):
                  label = tk.Label(text=guessedWord[kk].upper(), font=('Arial', 12), pady=5, borderwidth=1, relief='solid')
                  label.grid(row=guessNum, column=kk, sticky=tk.NSEW)

                  if guessedWord[kk] in chosenWord:
                      if guessedWord[kk] == chosenWord[kk]:
                          label.config(bg='green', fg='white')
                          correct += 1
                      else:
                          label.config(bg='gold', fg='white')


                          M = guessedWord.count(guessedWord[kk]) - chosenWord.count(guessedWord[kk])
                          if guessedWord[kk] not in rpt_ltr:
                              cnt.append(0)
                              rpt_ltr.append(guessedWord[kk])
                          if cnt[rpt_ltr.index(guessedWord[kk])] < M:
                              label.config(bg='grey', fg='white')
                              cnt[rpt_ltr.index(guessedWord[kk])] += 1




      else:
        label.config(bg = 'grey')
        label.config(fg = 'white')

    if correct == word_length:
      GuessButton.config(state = 'disabled')
      ResultLabel.configure(text = 'You win!')
    elif guessNum == 6:
      GuessButton.config(state = 'disabled')
      ResultLabel.configure(text = 'You lose!')
    else:
      guessNum = guessNum + 1
  else:
    print('Invalid word, try again')

  guessNum = guessNum + 1


print(f'Welcome to Wordle! You have 6 guesses to guess the -letter word. Good')

wordlist = []
chosenWord = 'Wordle'

with open('Wordle/Wordlist.txt') as f:
  print("Reading WordList")
  wordlist = f.read().splitlines()
  chosenWord = random.choice(wordlist)

if chosenWord == 'Wordle':
  print("Problem reading the worldlist file")

word_length = len(chosenWord)
print(f"chosenWord: {chosenWord} has {word_length} characters")

window = tk.Tk()
window.title("Vihaan's Worlde")
window.geometry('600x800')

HintLabel = tk.Label(text=f'The word has {len(chosenWord)} letters.',
                     font=('Arial', 12))
HintLabel.grid(row=0, column=0, columnspan=len(chosenWord))

clue_label = tk.Label(text=f'Hint: {"_ " * word_length}', font=('Arial', 12))
clue_label.grid(row=1, column=0, columnspan=word_length)

HintButton = tk.Button(text='Get Hint', command=revealHint)
HintButton.grid(row=2, column=0, columnspan=word_length)

ResultLabel = tk.Label(text='')
ResultLabel.grid(row=101, column=0, columnspan=word_length)

EntryBox = tk.Entry()
EntryBox.grid(row=99, column=0, columnspan=word_length)

GuessButton = tk.Button(text='Guess', command=getWord)

