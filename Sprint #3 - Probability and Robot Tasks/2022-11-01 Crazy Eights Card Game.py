#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Game import *
from Game.cards import *


# https://www.pagat.com/eights/crazy8s.html

# In[52]:


def initial_state():
    # state = stock (face down),discard (face up), hand1, hand2,
    # observation = discard, own hand
    
    make_a_small_deck=True  # use this for  agents, for debugging
    
    
    deck=makedeck()
    
    
    if make_a_small_deck:
        # to keep things a litter easier
        # make a small deck
        for card in deck:
            if card.rank in [8,9,10]:
                continue

            deck.remove(card)
        cards_per_hand=3  # small game
    else:
        cards_per_hand=7  # typical game
    
    
    hand1=deck.deal(cards_per_hand)
    hand2=deck.deal(cards_per_hand)
        
    while True:  # keep pulling from the discard until no eights
        discard=deck.deal(1)
        if not discard[0].rank==8:
            break
            
        deck+=discard   # put the card back and reshuffle
        random.shuffle(deck)
    
    stock=deck
    
    state=stock,discard,hand1,hand2

    return state


# In[53]:


def state_to_observation(state,player):
    stock,discard,hand1,hand2=state
    
    if player==1:
        observation=discard,hand1
        
    else:
        observation=discard,hand2
        
    
    return observation


# In[54]:


a=[3,5,3,2,5,56,6,7,7,4,3,3]


# In[55]:


a[-1:-5:-1]


# In[56]:


def show_state(observation):
    discard,hand=observation
    print("My hand:","(%d cards)" % len(hand),str(hand))
    print("Top card:",discard[-1])
    
    
    print("Top 10 cards from the discard: ",str(CardList(discard[-1:-11:-1])))
    print()


# In[57]:


state=initial_state()
show_state(state_to_observation(state,1))


# In[58]:


show_state(state_to_observation(state,2))


# In[59]:


def valid_moves(observation,player):
    discard,hand=observation
    top_card=discard[-1]

    moves=['draw']
    
    for card in hand:
        if card.rank==8:
            for suit in ['h','s','d','c']:
                moves.append( [card,suit] )
        elif card.rank == top_card.rank:
            moves.append(card)
        elif card.suit==top_card.suit:
            moves.append(card)
    
    return moves


# In[60]:


state=initial_state()
observation=state_to_observation(state,1)
show_state(observation)

valid_moves(observation,1)


# In[61]:


def update_state(state,player,move):
    stock,discard,hand1,hand2=state
    
    if move=='draw':
        cards=stock.deal(1)
        if player==1:
            hand1+=cards
        else:
            hand2+=cards
    
        if not stock:  # stock is empty, reuse the discard pile other than the last card
            stock=CardList(discard[:-1])
            discard=CardList([discard[-1]])
            
        
    elif isinstance(move,Card):
        card=move
        discard+=[move]
        
        if player==1:
            hand1.remove(card)
        else:
            hand2.remove(card)
        
    elif isinstance(move[0],Card):  # should be an eight
        card=move[0]
        
        if player==1:
            hand1.remove(card)
        else:
            hand2.remove(card)
                
        
        card.suit=move[1]
        discard+=[card]
    else:
        raise ValueError("Can't get there from here.")
    

    new_state=stock,discard,hand1,hand2
    return new_state


# In[62]:


def repeat_move(state,player,move):
    if move=='draw':
        return True
    else:
        return False


# In[63]:


def win_status(state,player):
    stock,discard,hand1,hand2=state
    
    if player==1 and not hand1:
        return 'win'
    if player==2 and not hand2:
        return 'win'
    


# In[64]:


def random_move(state,player):

    moves=valid_moves(state,player)
    return random.choice(moves)

random_agent=Agent(random_move)


# In[65]:


def human_move(observation,player):
    discard,hand=observation
    
    moves=valid_moves(observation,player)
    print( "Player ", player)
    print("Moves:")
    for i, move in enumerate(moves):
        print(f"\t{i}: {move}")
        
    valid_move=False
    while not valid_move:
        move_number=int(input('Which move do you want (enter a number)?'))

        if move_number in range(len(moves)):
            valid_move=True
        else:
            print( "Illegal move.")

    
    return moves[move_number]

human_agent=Agent(human_move)


# In[50]:


g=Game()
wins=g.run(human_agent,human_agent)


# In[51]:


g=Game()
wins=g.run(random_agent,random_agent)


# In[ ]:




