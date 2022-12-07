#!/usr/bin/env python
# coding: utf-8

# Let's work backward from the answer we need to how we get there.  We'll write the entire robot playing a board game.  We'll make empty or partial functions first, and then fill them out.

# In[ ]:


state=read_state()     #  read the state from the world
move=get_move(state,1)   # from an agent
make_move(move)        # robot motion to move pieces, etc...


# # get_move

# In[1]:


from breakthrough import *


# there are several get_move functions one could use.  Like random....

# In[2]:


def random_move(state,player):
    moves=valid_moves(state,player)
    return random.choice(moves)

def get_move(state,player):
    return random_move(state,player)


# or minimax the same way.

# In[3]:


def get_move(state,player):
    return minimax_move(state,player)


# Q or skittles, the move comes from the table.

# In[4]:


def get_move(state,player):
    if player==1:
        Q=LoadTable("Q1_breakthrough_table.json")
    else:
        Q=LoadTable("Q2_breakthrough_table.json")
        
    
    if state not in Q:
        return random_move(state,player)
    else:
        return top_choice(Q[state])


# In[5]:


state=initial_state()


# In[6]:


state


# In[7]:


state.show_locations()


# In[6]:


get_move(state,1)


# ## make_move

# the minimal one just prints the move

# In[7]:


def make_move(move):
    print("If I could move, I would do move: ",move)


# everything else will be specific to your robot, but it might do something like this.

# In[8]:


move=[12,8]
move=[9,6]


# In[9]:


def move_forward(distance):
    print("forward ",distance)
    
def move_backward(distance):
    print("backward ",distance)    
    
def turn_robot_left_90():
    print("left 90")
    
def turn_robot_right_90():
    print("right 90")    
    
def turn_robot_left_45():
    print("left 45")    
    
def turn_robot_right_45():
    print("right 45")     
    
def arm_up():
    print("arm up")
def arm_down():
    print("arm down")


# In[10]:


def make_move(move):
    print("Making move ",move)
    
    board=Board(4,4)  # just to get the conversion functions for free
    
    start,end=move
    rs,cs=board.rc_from_index(start)  # convert to row, column
    re,ce=board.rc_from_index(end)
    
    distance_to_board=10
    length_column=4
    length_row=4

    type_of_move=ce-cs  # 0 for a forward move, +1 for a right-hand diagonal, -1 for left-hand diagonal
    distance_to_column=distance_to_board+length_column*cs
    distance_to_row=(4-rs)*length_row

    if type_of_move==0:  # forward

        move_forward(distance_to_column)
        turn_robot_left_90()
        move_forward(distance_to_row)
        arm_down()  # to push the piece
        move_forward( 1*length_row )
        arm_up()

        # go back
        move_backward(distance_to_row + 1*length_row)
        turn_robot_right_90()
        move_backward(distance_to_column)

    elif type_of_move==1:  # right-hand diagonal

        move_forward(distance_to_column)
        turn_robot_left_90()
        move_forward(distance_to_row)


        arm_down()  # to push the piece
        turn_robot_right_45()
        move_forward( 1*length_row )

        # go back
        move_backward(1*length_row)
        turn_robot_left_45()    
        move_backward(distance_to_row )
        turn_robot_right_90()
        move_backward(distance_to_column)

    elif type_of_move==-1:  # right-hand diagonal
        move_forward(distance_to_column)
        turn_robot_left_90()
        move_forward(distance_to_row)


        arm_down()  # to push the piece
        turn_robot_left_45()
        move_forward( 1*length_row )

        # go back
        move_backward(1*length_row)
        turn_robot_right_45()    
        move_backward(distance_to_row )
        turn_robot_right_90()
        move_backward(distance_to_column)

    else:
        raise ValueError("You can't get there from here.")

    


# In[11]:


state=initial_state()
show_state(state)
state.show_locations()


# In[12]:


make_move([13,8])


# ## read_state

# a nice fall-back is to read the state from a file

# In[13]:


def read_state_from_file(filename='current_board.txt'):
    with open(filename) as fid:
        text=fid.read()

    text2=text.strip().split('\n')
    number_of_rows=len(text2)
    number_of_cols=len(text2[0].split())
    
    b=Board(number_of_rows,number_of_cols)
        
    board=[int(v) for v in text.split()]
    b.board=board
    return b


# In[1]:


from Game import Board
state=Board(3,3,3)


# In[6]:


def read_3dttt_state_from_file(filename='current_board_3dttt.txt'):
    with open(filename) as fid:
        text=fid.read()

    b=Board(3,3,3)
        
    board=[int(v) for v in text.strip().split()]
    b.board=board
    return b


# In[7]:


read_3dttt_state_from_file('current_board_3dttt.txt')


# In[ ]:





# In[14]:


def read_state():
    state=read_state_from_file()
    return state


# In[15]:


with open("current_board.txt","w") as fid:
    fid.write("""
2 0 2 0 
0 2 0 0
1 0 1 1
0 1 0 0
    """)


# In[16]:


state=read_state()
show_state(state)


# now we can do the reading from the world

# ## Now the full game

# In[17]:


state=read_state()     #  read the state from the world
move=get_move(state,1)   # from an agent
make_move(move)        # robot motion to move pieces, etc...


# In[ ]:




