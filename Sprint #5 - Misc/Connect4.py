from Game import *

def initial_state():
    state=Board(6,7)
    return state

def valid_moves(state,player):
    
    moves=[]
    for location in range(7):
        if state[location]==0:
            moves.append(location)
          
    return moves

def update_state(state,player,move):
    
    new_state=state
    
    for c in range(5,-1,-1):
        if state[c,move]==0:    
            new_state[c,move]=player
            break
            
    return new_state

def four_in_a_row(a,b,c,d,player):
    
    if a==player and b==player and c==player and d==player:
        return True
    else:
        return False
    
    
    
def win_status(state,player):
    
    # 0  1  2  3  4  5  6
    # 7  8  9  10 11 12 13
    # 14 15 16 17 18 19 20
    # 21 22 23 24 25 26 27
    # 28 29 30 31 32 33 34
    # 35 36 37 38 39 40 41
    
    if player==1:
        other_player=2
    else:
        other_player=1
        
    for four in [state.diags(4),state.rows(4),state.cols(4)]:
        for d in four:
            if d.count(player)==4:
                return 'win'

    
    if not valid_moves(state,other_player):
        return 'stalemate'
    

def show_state(state):
    print(state)
    
    
from termcolor import colored
def show_state(state):
    
    for i in range(42):
        if state[i]==1:
            print(colored(" (r) ",'red'),end="")
        elif state[i]==2: 
            print(colored(" (y) ",'yellow'),end="")
        else:
            print("  .  ",end="")
            
        if i==6 or i==13 or i==20 or i==27 or i==34 or i==41:
            print()
            
def random_move(state,player):    
    moves=valid_moves(state,player)
    return random.choice(moves)
 
random_agent=Agent(random_move) 

def human_move(state,player):    
    print("""
  0    1    2    3    4    5    6
  7    8    9    10   11   12   13
  14   15   16   17   18   19   20
  21   22   23   24   25   26   27
  28   29   30   31   32   33   34
  35   36   37   38   39   40   41
    ""","\n","Your valid moves are: ",valid_moves(state,1))
    for i in range(5):
        if player == 1:
            move=int(input("\n Where do you want to put your piece? You are red!"))
            if move in valid_moves(state,player):
                return move
            else:
                print("Illegal move.")
        else: 
            move=int(input("\n Where do you want to put your piece? You are yellow!"))
            if move in valid_moves(state,player):
                return move
            else:
                print("Illegal move.")
    return move
 
human_agent=Agent(human_move) 

from Game.minimax import *
def minimax_move(state,player):
    values,moves=minimax_values(state,player,maxdepth=5,display=True)
    return top_choice(moves,values)
    
    
minimax_agent=Agent(minimax_move)

def easy_win(state,player):
    from copy import deepcopy
    moves=valid_moves(state,player)
    for move in moves:
        new_state=update_state(deepcopy(state),player,move)
        if win_status(new_state,player)=='win':
            return move
    
    return None

def Q_move(state,player,info):
    if player==1:
        other_player=2
    else:
        other_player=1
        
    Q=info.Q
    last_state=info.last_state
    last_action=info.last_action
    learning=info.learning
    
    α=info.α  # learning rate
    ϵ=info.ϵ  # how often to take a random move
    γ=info.γ  # memory constant -- how quickly does the table update back in time (earlier in the game)
    
    # \alpha <hit tab>    α
    # \epsilon <hit tab>  ϵ
    # \gamma <hit tab>    γ
    
    if state not in Q:
        actions=valid_moves(state,player)
        Q[state]=Table()
        for action in actions:
            Q[state][action]=0  # initial value of table
    
    if learning:
        if random.random()<ϵ:  # take a random move occasionally to explore the environment
            move=random_move(state,player)
        else:
            move=top_choice(Q[state])
    else:
        move=top_choice(Q[state])
        
    # check for easy win, which should get rewarded later
    winning_move=easy_win(state,player)
    if not winning_move is None:
        move=winning_move
    else:
        # for TTT and connect4 the moves are symmetrical between the players
        # so you can look to block easy wins for the other player
        # this wont work for any other game.
        blocking_move=easy_win(state,other_player)
        if not blocking_move is None:
            move=blocking_move
        
        
    
    if not last_action is None:  # not the first move
        reward=0
        
        # learn
        if learning:
            Q[last_state][last_action]+=α*(reward +
                        γ*max([Q[state][a] for a in Q[state]]) - Q[last_state][last_action])
    
    return move

def Q_after(status,player,info):
    Q=info.Q
    last_state=info.last_state
    last_action=info.last_action
    learning=info.learning
    
    α=info.α  # learning rate
    ϵ=info.ϵ  # how often to take a random move
    γ=info.γ  # memory constant -- how quickly does the table update back in time (earlier in the game)
    
    # \alpha <hit tab>    α
    # \epsilon <hit tab>  ϵ
    # \gamma <hit tab>    γ

    if status=='lose':
        reward=-1
    elif status=='win':
        reward=1
    elif status=='stalemate':
        reward=.5 # value stalemate a little closer to a win
    else:
        reward=0
    
    
    if learning:
        Q[last_state][last_action]+=α*(reward - Q[last_state][last_action])
        