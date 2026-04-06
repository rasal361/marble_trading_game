#Import random module
#Create a bag with 10 marbles, 6 green and 4 red
#Starting amount of money
#Current money amount
#Result of last round
#How many rounds?
#Last marble
#Welcome user to game
#Loop drawing marbles
    #How much was bet
    #Draw marble
    #Win or loss
    #Calc win or loss/ result and new amount/purse
    #Lose game if lose half of money
#Print final results    


import random

bag=('green','green','green','green','green','black','red','red','red','white')
start_purse=1000
purse=start_purse
result=0
rounds=10
marble='none'
print(f'You start the game with {start_purse} gold pieces in your purse. You have {rounds} rounds to play. Good luck!')
for draw in range(1,rounds+1):
    bet=int(input(f'Current purse: {purse} last draw: {marble}\nRound {draw} - How much do you bet? '))
    marble=random.choice(bag)
    if marble=='green':
        result=bet
    elif marble=='black':
        result= 10 * bet
    elif marble=='white':
        result= -5 * bet
    else:
        result=-bet
    purse+=result
    if purse< 0.5*start_purse:
        print(f'Game over! You lost half of your money.')
        break
    print(f'purse: {purse} last result: {marble} : {result}')    
    print('')
print('starting/ ending purse: ', start_purse, '/',purse)
print('gain/loss: ', ((purse-start_purse)/start_purse *100),'%')

