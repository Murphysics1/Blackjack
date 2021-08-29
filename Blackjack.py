#!/usr/bin/env python
# coding: utf-8

# ### Classes

# In[1]:


#global variables:
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}


# In[2]:


#card

class Card():
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__ (self):
        return self.rank + ' of '+self.suit


# In[3]:


#deck

class Deck():
    
    def __init__(self):
        
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
    
    def shuffle(self):
        
        random.shuffle(self.all_cards)
        
    def deal_card(self,player):
        
        card = self.all_cards.pop()
        player.total += card.value
        if card.rank == "Ace":
            player.aces += 1
        
        return card
        
    def initial_deal(self,player,dealer):
        
        player.hand.append(self.deal_card(player))
        dealer.hand.append(self.deal_card(dealer))
        player.hand.append(self.deal_card(player))
        dealer.hand.append(self.deal_card(dealer))


# In[4]:


#player

class Player():
    
    def __init__(self,name,balance = 100):
        
        self.balance = balance
        self.name = name
        self.hand =[]
        self.total = 0
        self.aces = 0
        
    def hit(self,delt_card):
        
        self.hand.append(delt_card)
        self.total += delt_card.value
        if delt_card.rank == "Ace":
            self.aces += 1
        
    def bet(self):
        
        while True:
            try:
                bet_size = int(input("Place your bet: $"))
                
                if self.balance < bet_size:
                    print("\nInsufficient Funds!")
                else:
                    break
            except:
                print("\nSorry, that is not a value")
        
        return bet_size
                
    def info(self,player):
        
        print(f'\n{player.name}:')
        print(f'Current Value: {player.total}')
        print(f'Current Hand:')
        for item in player.hand:
            print(f'               {item}')
    
    def __str__ (self):
        
        return f'\n{self.name}, you currently have a balance of ${self.balance}'


# In[5]:


#Dealer

class Dealer():
    
    def __init__(self):
        
        self.hand =[]
        self.total = 0
        self.aces = 0
        
    def hit(self,delt_card):

        self.hand.append(delt_card)
        self.total += delt_card.value
        if delt_card.rank == "Ace":
            self.aces += 1
    
    def info(self,dealer,case):
        #This version hides the total and first card
        if case == 'initial':
            print(f'\nDealer:')
            print(f'Current Value: #######')
            print(f'Current Hand:')
            print(f'               #######')
            for item in dealer.hand[1:]:
                print(f'               {item}')
                
        #this version shows all info
        elif case == 'final':
            print(f'\nDealer:')
            print(f'Current Value: {dealer.total}')
            print(f'Current Hand:')
            for item in dealer.hand:
                print(f'               {item}')


# In[6]:


def Display(bet,player,dealer,state):
    
    print(f"{player.name}'s balance: ${player.balance}")
    print(f'Current Bet: ${bet}')
    player.info(player)
    dealer.info(dealer,state)


# In[7]:


def Results(bet,player,dealer):
    
    if player.total > 21:
        return (f'\nDealer wins! New balance is ${player.balance-bet}',player.balance - bet)
    elif dealer.total > 21:
        return (f'\n{player.name} wins! New balance is ${player.balance+bet}',player.balance + bet)
    elif player.total == dealer.total:
        return (f'\nDealer wins! New balance is ${player.balance-bet}',player.balance - bet)
    elif player.total > dealer.total:
        return (f'\n{player.name} wins! New balance is ${player.balance+bet}',player.balance + bet)
    else:
        return (f'\nDealer wins! New balance is ${player.balance-bet}',player.balance - bet)


# In[8]:


def Ending(player):
    
    if player.balance > 100:
        print(f'\nCongrats! You finished with a balance of ${player.balance}.\nAwesome Job!')
    elif player.balance > 0:
        print(f'\nYou lost some, but not all! You finished with a balance of ${player.balance}.')
    else:
        print("\nBetter luck next time")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ### Game Logic

# In[9]:


#create a shuffled deck of cards
    #create card
    #create a deck
    #shuffle deck

#take a bet from the player
    #if bet cannot be taken the game ends

#from the top deal two cards to the player (both visible), and two to the dealer (one visible)

#Player can hit or stand
    #if hit:
        #deal one card to player
        #repeat questioning until player stands or busts
            #If bust and hand contains an Ace, reduce by 10
            
            #BUST is an automatic player loss
    #else: (stand)
        #return the value and move to the dealers turn

#Dealer's turn
    #Dealer reveals hidden card
    #Dealer must hit until bust or 16 or greater
        #BUST is an automatic player win

#if BUST, Player loses
#if no bust, compare values. Closest to 21 wins
#if player wins
    #bet size is added to balance
    #Congratulate player and display balance
#if dealer wins
    #bet size is taken from balance
    #Encourage player and display balance
    
#ask if player would like to play another hand
    #if yes:
        #extend playing_deck to include player.hand and dealer.hand
    #if no:
        #game = False
        

#OUTSIDE OF WHILE LOOP: END OF GAME


#if balance > 100
    #player.name, you won $(balance - 100). Great work!
#elif balance > 0 and < 100:
    #player.name, you'll get em next time. Good game!
#else:
    #Better luck next time
    


# In[10]:


def Blackjack():
    

    spaces = 15
    #from IPython.display import clear_output
    #Making a Deck
    
    playing_deck = Deck()

    print('Welcome to BlackJack!')
    
    #Set some initial parameters
    player = Player(input("Player, what is your name?: "))
    dealer = Dealer()
    
    game_on = True

    while game_on:
        
        #Shuffle the deck
        playing_deck.shuffle()
        
        #Give the player info about their current balance
        print('\n'*spaces)
        print(player)
      
        #Take the player's bet
        bet = player.bet()
        
        #Deal two cards to player and dealer
        playing_deck.initial_deal(player,dealer)
        
        #Start the round
        input("Press Enter:")
    
        #Player's Turn
        player_turn = True
        while player_turn:
            
            #Display Current Gamestate
            print('\n'*spaces)
            Display(bet,player,dealer,'initial')
            
            #Check for Blackjack or BUST!
            if player.total == 21:
                print(f'{player.name}, you have a 21 !!!')
                player_turn = False
            elif player.total > 21:
                print(f'{player.name} BUSTS!')
                player_turn = False
            
            #Hit or Stand Decisions
            else:
                choice =''
                
                #Select hit or stand with verification
                while choice.lower() not in ['h','s']:
                    print(f'\n{player.name}, would you like to hit or stand?')
                    choice = input("h or s?: ")
                
                if choice.lower() == 'h':
                    player.hit(playing_deck.all_cards.pop())
                    
                    #Check for whether an Ace should be played as a 1 or 11
                    while (player.total > 21) and (player.aces > 0):
                        player.total -= 10
                        player.aces -= 1
                
                else:
                    player_turn = False
        
        #Does the Dealer get a turn?
        if player.total <= 21:  
            dealer_turn = True
        else:
            dealer_turn = False
        
        #Dealer's Turn
        while dealer_turn:
            print('\n'*spaces)
            Display(bet,player,dealer,'final')
            
            #The dealer must hit on any total below 17
            if dealer.total < 17:
                dealer.hit(playing_deck.all_cards.pop())
                
                while (dealer.total > 21) and (dealer.aces > 0):
                        dealer.total -= 10
                        dealer.aces -= 1
            
            #The dealer must stand on any value between 17 and 21
            elif (dealer.total >= 17) and (dealer.total < 21):
                dealer_turn = False
            
            #The dealer's turn ends on 21 or more
            elif dealer.total == 21:
                print("Dealer has a 21 !!!")
                dealer_turn = False
            else:
                print("Dealer BUSTS!")
                dealer_turn = False
                    
        #End of Game Results
        
        message,player.balance = Results(bet,player,dealer)
        print(message)
        
        #Continue Game?
        #Game ends if balance is zero
        cont = ''
        if player.balance == 0:
            print("Game Over")
            game_on = False
            break
        
        while cont.lower() not in ['y','n']:
            cont = input('\nWould you like to continue the game?: (Y or N): ')
        
        if cont.lower() == 'y':
            #recombine the player and dealer hands into the deck
            playing_deck.all_cards = playing_deck.all_cards + player.hand + dealer.hand
            
            #recast the player and dealer classes
            player = Player(player.name,player.balance)
            dealer = Dealer()
            continue
        else:
            game_on = False
        
        #game_on = False   #Prevent Infinite Loop for now

    #Ending Message
    Ending(player)


# In[ ]:


Blackjack()


# In[ ]:





# In[ ]:





# In[ ]:




