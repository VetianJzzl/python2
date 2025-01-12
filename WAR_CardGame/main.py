import random
import time

cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'X', 'J', 'Q', 'K', 'A']

suits = ['C', 'D', 'H', 'S']

deck_of_cards = []

for kk in range(len(suits)):
  for jj in range(len(cards)):
    deck_of_cards.append(suits[kk]+cards[jj])

for kk in range(len(deck_of_cards)):
  print(deck_of_cards[kk] , end = ' ')
print()

random.shuffle(deck_of_cards)

for kk in range(len(deck_of_cards)):
  print(deck_of_cards[kk], end = ' ')


toss = random.randint(1,4)

if toss == 1 or toss == 4 :
  first_mover = 'player'
  print()
  print('You won the toss, you will play first')

else:
  first_mover = 'computer'
  print()
  print('Computer won the toss, it will play first')


player_cards = deck_of_cards[0:52:2] 
comput_cards = deck_of_cards[1:53:2] 
discard_pile = []


move_complete = False
game_complete = False
move_played = 0


while not(game_complete):

  if len(player_cards)<1 or len(comput_cards)<1:
    move_complete = True
    game_complete = True

  move_complete = False

  while not(move_complete):
    card_p = player_cards.pop(0)
    card_c = comput_cards.pop(0)

    print('Player card is ...', card_p)
    print('Computer card is ...', card_c)

    time.sleep(1.5)

    discard_pile.append(card_p)
    discard_pile.append(card_c)

    if cards.index(card_p[1])>cards.index(card_c[1]):
      print()
      print('Player wins...')
      time.sleep(1)
      player_cards.extend(discard_pile)
      discard_pile.clear()
      move_complete = True
      move_played = move_played + 1

    elif cards.index(card_p[1])<cards.index(card_c[1]):
      print()
      print('Computer wins!')
      time.sleep(1)
      comput_cards.extend(discard_pile)
      discard_pile.clear()
      move_complete = True
      move_played = move_played + 1

    else:
      #WAR begins
      print('War begins...')
      #Checking for enough cards

      if len(player_cards)<4 or len(comput_cards)<4:
        move_complete = True

      else:
        discard_pile.extend(player_cards[0:3])
        discard_pile.extend(comput_cards[0:3])

        del player_cards[0:3]
        del comput_cards[0:3]


    if move_played == 14:
      game_complete = True

    print("Player Cards: ", len(player_cards), "Computer Cards: ", len(comput_cards), "Discard Pile: ", len(discard_pile))  


print()
print()

if len(player_cards) > len(comput_cards):
  print('Player is the Winner (Nice one!).')
elif len(player_cards) < len(comput_cards):
  print('Computer is the winner (oof!).')
else:
  print('MATCH DRAWN') 
